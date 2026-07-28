# Figure Index

## `charts/` — generated

Produced by [`analysis/scripts/make_charts.py`](../analysis/scripts/make_charts.py)
from the CSVs in [`analysis/data/`](../analysis/data/). Regenerate with
`python analysis/scripts/make_charts.py`. Do not edit these by hand — change the
data or the script.

| File | Shows |
|---|---|
| `reserve-factors.png` | All eight reserve factors, critical member highlighted |
| `load-deflection.png` | Load vs deflection with fitted stiffness (74 / 102 N/mm) |
| `aerofoil-prediction-vs-test.png` | XFoil vs wind tunnel, C<sub>L,max</sub> and C<sub>D,min</sub> |
| `tunnel-drag-vs-aoa.png` | Fuselage drag vs angle of attack, with 0° repeat scatter |
| `mass-budget.png` | Subassembly mass by part, split structural vs aerodynamic |
| `fairing-mass-benchmark.png` | Fairing mass against the two competing companies |

## `cad/` — model renders and part views

`uav-assembly-iso/side/front.png` are Inventor renders of the full vehicle,
autocropped. `parts-catalogue.png` is the delivered part set. The remainder are
individual parts, assembly sequences and downselection material.

## `testing/` — test campaign photography

`ultimate-load-test-station.png` is the load test station on 5 March 2025.
`clamp-shear-damage-*.png` are the post-test inspection photographs of the
failed main wing joint clamp. `tunnel-*.png` are wind tunnel configuration
photographs. `trial-assembly-airframe.png` is the practice build.

## `structures/`, `aero/`, `pm/` — figures from the technical report

Original figures as they appeared in Team 08's A2 technical report:
hand-derived calculations, the original drag polars, mass tables, and the
project management artefacts (WBS, Gantt charts, network diagrams, risk
register and rating matrix).

`structures/load-deflection-original.png` is the original test plot that
`charts/load-deflection.png` was digitised from — kept so the derived chart can
be checked against its source.

---

## Editorial notes

Two figures were altered before publishing, both for privacy. This repository is
public and the people in these photographs did not consent to appearing in it:

- **`testing/ultimate-load-test-station.png`** — a small reflected face in the
  top-left rig panel has been irreversibly blurred.
- **`testing/trial-assembly-airframe.png`** — cropped from a wider photograph to
  remove two identifiable people, keeping the airframe on the bench.

One figure from the technical report was **excluded**: a drag breakdown diagram
reproduced from university teaching material. It was used in the report under
academic fair dealing, which does not extend to republication here. The concept
it illustrates is set out in words in
[`docs/05-aerodynamics.md`](../docs/05-aerodynamics.md).
