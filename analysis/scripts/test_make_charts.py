"""Tests for the chart pipeline.

The README claims every chart in figures/charts/ is regenerated from the CSVs in
analysis/data/ and that nothing is hand-drawn. These tests hold that claim up: the
data files must parse, carry their provenance headers, agree with the headline
numbers quoted in the write-up, and every chart function must actually produce a file.

    python -m pytest analysis/scripts/
"""

from __future__ import annotations

import csv

import pytest

matplotlib = pytest.importorskip("matplotlib")
matplotlib.use("Agg")

import make_charts as mc


# --------------------------------------------------------------------------------------
# Data files
# --------------------------------------------------------------------------------------

EXPECTED_DATA = [
    "aerofoil_performance.csv",
    "company_mass_benchmark.csv",
    "load_deflection.csv",
    "reserve_factors.csv",
    "subassembly_mass.csv",
    "tunnel_runs_fairings_on.csv",
]


@pytest.mark.parametrize("name", EXPECTED_DATA)
def test_data_file_exists(name):
    assert (mc.DATA / name).is_file(), f"missing dataset: {name}"


@pytest.mark.parametrize("name", EXPECTED_DATA)
def test_data_file_states_where_its_numbers_came_from(name):
    """Every CSV must record its own provenance.

    Two conventions are in use and both are acceptable: a leading ``#`` comment
    block, or a per-row ``source`` column naming the document each value came from.
    What matters is that no number is anonymous -- that is the difference between a
    measured value and one digitised off a plot.
    """
    text = (mc.DATA / name).read_text(encoding="utf-8").lstrip()
    has_comment = text.startswith("#")
    first_line = text.splitlines()[0]
    has_source_column = "source" in first_line.lower()
    assert has_comment or has_source_column, f"{name} records no provenance"


@pytest.mark.parametrize("name", EXPECTED_DATA)
def test_read_csv_returns_rows(name):
    rows = mc.read_csv(name)
    assert len(rows) > 0, f"{name} parsed to zero rows"
    assert all(isinstance(r, dict) for r in rows)


@pytest.mark.parametrize("name", EXPECTED_DATA)
def test_read_csv_skips_comment_lines(name):
    """Comment lines must not leak into the parsed data."""
    for row in mc.read_csv(name):
        for key in row:
            assert key is None or not str(key).startswith("#")


# --------------------------------------------------------------------------------------
# Headline numbers quoted in the README
# --------------------------------------------------------------------------------------

def test_governing_reserve_factor_is_1_95():
    """The README reports a governing reserve factor of 1.95, on the centre bar."""
    rows = mc.read_csv("reserve_factors.csv")
    values = [float(r["reserve_factor"]) for r in rows]
    assert min(values) == pytest.approx(1.95, abs=0.01)
    governing = min(rows, key=lambda r: float(r["reserve_factor"]))
    assert governing["part"] == "Centre bar"
    assert governing["check"] == "Bending"


def test_all_reserve_factors_are_above_one():
    """A reserve factor at or below 1 would mean the check was not met."""
    rows = mc.read_csv("reserve_factors.csv")
    assert all(float(r["reserve_factor"]) > 1.0 for r in rows)


def test_subassembly_mass_totals_1011_grams():
    """The README reports a 1,011 g subassembly."""
    rows = mc.read_csv("subassembly_mass.csv")
    assert sum(float(r["total_mass_g"]) for r in rows) == pytest.approx(1011.0, abs=0.5)


def test_subassembly_mass_rows_are_internally_consistent():
    """unit_mass_g * quantity must equal total_mass_g on every row."""
    for row in mc.read_csv("subassembly_mass.csv"):
        expected = float(row["unit_mass_g"]) * int(row["quantity"])
        assert float(row["total_mass_g"]) == pytest.approx(expected, abs=0.05), row["part"]


def test_load_deflection_curve_reproduces_reported_stiffness():
    """The README quotes 74 N/mm centre and 102 N/mm empennage.

    The CSV is digitised off a printed plot, so a least-squares fit through all
    points will not land exactly on the reported figures. Agreement to within 6 %
    is the point: it confirms the digitisation is faithful enough for a stiffness
    fit, which is all the README claims for it.
    """
    import numpy as np

    rows = mc.read_csv("load_deflection.csv")
    load = np.array([float(r["load_N"]) for r in rows])
    centre = np.array([float(r["centre_deflection_mm"]) for r in rows])
    emp = np.array([float(r["empennage_deflection_mm"]) for r in rows])

    assert np.polyfit(centre, load, 1)[0] == pytest.approx(74.0, rel=0.06)
    assert np.polyfit(emp, load, 1)[0] == pytest.approx(102.0, rel=0.06)


def test_load_deflection_is_monotonic_in_load():
    """The test ramped load upward; a decrease would mean the rows are out of order."""
    rows = mc.read_csv("load_deflection.csv")
    loads = [float(r["load_N"]) for r in rows]
    assert loads == sorted(loads)


def test_load_deflection_starts_from_the_origin():
    """A stiffness fit is only meaningful if the curve starts unloaded."""
    first = mc.read_csv("load_deflection.csv")[0]
    assert float(first["load_N"]) == pytest.approx(0.0)
    assert float(first["centre_deflection_mm"]) == pytest.approx(0.0)


def test_digitised_curve_does_not_claim_to_reach_failure():
    """The digitised curve stops at 540 N; the 813 N failure load is not in it.

    Guards against the digitised stiffness data being mistaken for, or quoted as,
    the ultimate load test result -- which is exactly what its provenance header
    warns against.
    """
    rows = mc.read_csv("load_deflection.csv")
    assert max(float(r["load_N"]) for r in rows) == pytest.approx(540.0)


# --------------------------------------------------------------------------------------
# Chart generation
# --------------------------------------------------------------------------------------

CHART_FUNCTIONS = [
    mc.chart_load_deflection,
    mc.chart_reserve_factors,
    mc.chart_aerofoil,
    mc.chart_mass,
    mc.chart_benchmark,
    mc.chart_tunnel,
]


@pytest.mark.parametrize("fn", CHART_FUNCTIONS, ids=lambda f: f.__name__)
def test_chart_function_writes_a_png(fn, tmp_path, monkeypatch):
    """Each chart must regenerate to a non-trivial file, into a temporary directory."""
    monkeypatch.setattr(mc, "OUT", tmp_path)
    fn()
    written = list(tmp_path.glob("*.png"))
    assert written, f"{fn.__name__} produced no PNG"
    for path in written:
        assert path.stat().st_size > 5_000, f"{path.name} looks empty"


def test_every_chart_function_is_covered():
    """Guard against a new chart being added without a test."""
    discovered = {
        name for name in dir(mc)
        if name.startswith("chart_") and callable(getattr(mc, name))
    }
    covered = {fn.__name__ for fn in CHART_FUNCTIONS}
    assert discovered == covered, f"untested chart functions: {discovered - covered}"
