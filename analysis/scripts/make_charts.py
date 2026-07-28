#!/usr/bin/env python3
"""Regenerate every derived chart in figures/charts/ from analysis/data/.

    python analysis/scripts/make_charts.py

Requires: matplotlib, numpy. No other dependencies; run from the repo root or
anywhere -- paths are resolved relative to this file.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "analysis" / "data"
OUT = ROOT / "figures" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- palette ---
# Slots 1-3 of the validated reference categorical palette, used in fixed order.
# Never cycled; no chart here carries more than three series.
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
CRITICAL = "#d03b3b"          # reserved status colour, always paired with a label
SURFACE = "#fcfcfb"
INK, INK_2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, BASELINE = "#e1e0d9", "#c3c2b7"

plt.rcParams.update({
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "DejaVu Sans", "Arial"],
    "font.size": 10,
    "text.color": INK,
    "axes.labelcolor": INK_2,
    "axes.edgecolor": BASELINE,
    "axes.titlesize": 12.5,
    "axes.titleweight": "semibold",
    "axes.titlecolor": INK,
    "axes.titlepad": 12,
    "axes.labelpad": 8,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "xtick.labelcolor": INK_2,
    "ytick.labelcolor": INK_2,
    "legend.frameon": False,
    "legend.fontsize": 9.5,
    "grid.color": GRID,
    "grid.linewidth": 0.8,
    "figure.dpi": 160,
})


def dress(ax, *, grid_axis="y"):
    """Recessive chrome: no top/right spine, hairline grid behind the marks."""
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_linewidth(0.9)
    ax.grid(True, axis=grid_axis, zorder=0)
    ax.set_axisbelow(True)
    ax.tick_params(length=0)


def caption(ax, text, dy=-0.30):
    """Source/interpretation note, anchored below the axes so it can never
    collide with the x-axis label."""
    ax.annotate(text, xy=(0, dy), xycoords="axes fraction", fontsize=7.8,
                color=MUTED, ha="left", va="top", annotation_clip=False,
                linespacing=1.5)


def save(fig, name):
    fig.savefig(OUT / name, bbox_inches="tight", pad_inches=0.28)
    plt.close(fig)
    print(f"  figures/charts/{name}")


def read_csv(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        rows = [r for r in f if not r.lstrip().startswith("#")]
    return list(csv.DictReader(rows))


# ------------------------------------------------------- 1. load-deflection ---
def chart_load_deflection():
    rows = read_csv("load_deflection.csv")
    P = np.array([float(r["load_N"]) for r in rows])
    centre = np.array([float(r["centre_deflection_mm"]) for r in rows])
    emp = np.array([float(r["empennage_deflection_mm"]) for r in rows])

    fig, ax = plt.subplots(figsize=(7.4, 4.5))
    dress(ax, grid_axis="both")

    stiff = {}
    for y, colour, label in ((centre, BLUE, "Centre"), (emp, ORANGE, "Empennage")):
        # least-squares through the origin: the rig reads zero at zero load
        k = float(P @ y / (P @ P))          # mm/N
        stiff[label] = 1.0 / k              # N/mm
        ax.plot(P, np.polyval([k, 0], P), color=colour, lw=1.2, alpha=0.45, zorder=2)
        ax.plot(P, y, color=colour, lw=2.0, marker="o", ms=4.5,
                mec=SURFACE, mew=1.2, label=label, zorder=3)

    ax.set_xlabel("Applied load  (N)")
    ax.set_ylabel("Deflection  (mm)")
    ax.set_title("Airframe stiffness under the ultimate load test")
    ax.set_xlim(0, 600)
    ax.set_ylim(0, 8)
    ax.legend(loc="upper left", handlelength=1.6)

    # selective direct labels: the fitted stiffness, not a number on every point
    for label, colour, dy in (("Centre", BLUE, 0.30), ("Empennage", ORANGE, -0.62)):
        ax.annotate(f"{stiff[label]:.0f} N/mm", xy=(P[-1], (centre if label == "Centre" else emp)[-1]),
                    xytext=(P[-1] + 14, (centre if label == "Centre" else emp)[-1] + dy),
                    color=colour, fontsize=9.5, fontweight="semibold", va="center")

    caption(ax, "Response is linear to the ultimate load case; no stiffness knee before failure.\n"
                 "Digitised from the original test plot — see analysis/data/load_deflection.csv.")
    save(fig, "load-deflection.png")
    return stiff


# ------------------------------------------------------- 2. reserve factors ---
def chart_reserve_factors():
    rows = read_csv("reserve_factors.csv")
    rows.sort(key=lambda r: float(r["reserve_factor"]))
    labels = [f"{r['part']} — {r['check'].lower()}" for r in rows]
    rf = np.array([float(r["reserve_factor"]) for r in rows])

    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    dress(ax, grid_axis="x")

    # Dot plot, not bars: the spread runs 1.95 -> 39, which needs a log axis, and
    # bar length on a log axis no longer encodes value from zero. Position does.
    y = np.arange(len(rf))
    for yi, v in zip(y, rf):
        colour = CRITICAL if v == rf.min() else BLUE
        ax.plot([1.0, v], [yi, yi], color=colour, lw=1.4, alpha=0.30, zorder=2,
                solid_capstyle="round")
        ax.plot(v, yi, "o", ms=10, color=colour, mec=SURFACE, mew=1.6, zorder=4)

    ax.set_yticks(y, labels)
    ax.invert_yaxis()

    ax.axvline(1.0, color=MUTED, lw=1.1, ls=(0, (4, 3)), zorder=1)

    ax.set_xscale("log")
    ax.set_xlim(0.86, 62)
    ax.set_xticks([1, 2, 5, 10, 20, 40], ["1", "2", "5", "10", "20", "40"])
    ax.set_ylim(len(rf) - 0.4, -1.15)
    ax.set_xlabel("Reserve factor  (log scale)")
    ax.set_title("Reserve factors at the 9g ultimate load case")

    for yi, v in zip(y, rf):
        crit = v == rf.min()
        ax.text(v * 1.13, yi, f"{v:g}", va="center", fontsize=9,
                color=CRITICAL if crit else INK_2,
                fontweight="semibold" if crit else "normal")

    ax.text(1.0, -1.0, "RF = 1  ·  failure", color=MUTED, fontsize=8.6,
            va="center", ha="left")
    ax.annotate("critical member", xy=(rf.min(), 0), xytext=(rf.min() * 1.9, -0.72),
                color=CRITICAL, fontsize=8.8, fontweight="semibold", va="center",
                arrowprops=dict(arrowstyle="->", color=CRITICAL, lw=1.0,
                                connectionstyle="arc3,rad=0.25"))

    caption(ax, "6g manoeuvre × 1.5 statutory safety factor. The 22.2 mm centre bar governs the design at RF 1.95;\n"
                "in test the airframe instead failed by bolt shear-out in the PLA main wing clamp — an unmodelled path.",
            dy=-0.20)
    save(fig, "reserve-factors.png")


# ------------------------------------------------------ 3. aerofoil vs test ---
def chart_aerofoil():
    rows = read_csv("aerofoil_performance.csv")
    configs = ["Clean (0 deg flap)", "Flap 30 deg"]
    nice = ["Clean\n(0° flap)", "Flap\ndeployed 30°"]
    sources = ["XFoil", "Wind tunnel"]

    def get(cfg, src, key):
        return next(float(r[key]) for r in rows if r["configuration"] == cfg and r["source"] == src)

    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.3))
    x = np.arange(len(configs))
    w = 0.33

    for ax, key, title, unit in ((axes[0], "cl_max", "Maximum lift coefficient", "$C_{L,max}$"),
                                 (axes[1], "cd_min", "Minimum drag coefficient", "$C_{D,min}$")):
        dress(ax, grid_axis="y")
        for i, (src, colour) in enumerate(zip(sources, (BLUE, ORANGE))):
            vals = [get(c, src, key) for c in configs]
            # 2px surface gap between adjacent bars
            ax.bar(x + (i - 0.5) * (w + 0.02), vals, w, color=colour,
                   label=src if ax is axes[0] else None, zorder=3)
            for xi, v in zip(x + (i - 0.5) * (w + 0.02), vals):
                ax.text(xi, v, f"{v:g}", ha="center", va="bottom", fontsize=8.8,
                        color=INK_2, zorder=4, clip_on=False)
        ax.set_xticks(x, nice)
        ax.set_title(title, fontsize=11)
        ax.set_ylabel(unit)
        ax.margins(y=0.18)

    axes[0].legend(loc="upper left", handlelength=1.4)
    fig.suptitle("NACA 2414 section: 2D prediction against wind tunnel measurement",
                 fontsize=12.5, fontweight="semibold", y=1.015)
    caption(axes[0], "Re = 4.11×10⁵, M = 0.058, chord 0.30 m. The tunnel loses lift and gains drag in both "
                 "configurations — finite span,\nwall blockage and a real transition point that the 2D panel "
                 "method does not carry. Separate axes, never a shared one.")
    fig.tight_layout()
    save(fig, "aerofoil-prediction-vs-test.png")


# ---------------------------------------------------------- 4. mass budget ---
def chart_mass():
    rows = read_csv("subassembly_mass.csv")
    rows.sort(key=lambda r: float(r["total_mass_g"]), reverse=True)
    rows = [r for r in rows if float(r["total_mass_g"]) >= 4.0]
    labels = [r["part"] for r in rows]
    mass = np.array([float(r["total_mass_g"]) for r in rows])
    cat = [r["category"] for r in rows]

    palette = {"fairing": ORANGE, "joint": BLUE, "fastener": AQUA}
    fig, ax = plt.subplots(figsize=(7.8, 4.8))
    dress(ax, grid_axis="x")

    y = np.arange(len(mass))
    ax.barh(y, mass, height=0.64, color=[palette[c] for c in cat], zorder=3)
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlabel("Mass  (g)")
    ax.set_title("Where the 1,011 g of joints and fairings went")

    for yi, v in zip(y, mass):
        ax.text(v + 8, yi, f"{v:g}", va="center", fontsize=9, color=INK_2)

    handles = [plt.Rectangle((0, 0), 1, 1, color=palette[k]) for k in ("fairing", "joint", "fastener")]
    ax.legend(handles, ["Fairings", "Joints", "Fasteners"], loc="lower right", handlelength=1.2)
    ax.margins(x=0.12)

    structural = sum(float(r["total_mass_g"]) for r in read_csv("subassembly_mass.csv")
                     if r["category"] in ("joint", "fastener"))
    caption(ax, f"The two main-wing fairing halves alone are 600 g — 59% of the subassembly. Everything that "
                f"actually carries load\n(joints, clamps, the aluminium strap and all fasteners) comes to "
                f"{structural:.0f} g. Aerodynamic shell mass dominates the budget.")
    save(fig, "mass-budget.png")


# ------------------------------------------------------ 5. company benchmark ---
def chart_benchmark():
    rows = read_csv("company_mass_benchmark.csv")
    r = next(x for x in rows if x["assembly"] == "Fairings")
    names = ["Albatross Aviation\n(this team)", "Bluebird", "Cropheed Martin"]
    vals = np.array([float(r["albatross_kg"]), float(r["bluebird_kg"]), float(r["cropheed_martin_kg"])]) * 1000

    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    dress(ax, grid_axis="y")
    colours = [CRITICAL, BLUE, BLUE]
    ax.bar(np.arange(3), vals, 0.5, color=colours, zorder=3)
    ax.set_xticks(np.arange(3), names)
    ax.set_ylabel("Fairing mass  (g)")
    ax.set_title("Fairing mass against the other two companies")
    ax.margins(y=0.2)

    for i, v in enumerate(vals):
        ax.text(i, v + 14, f"{v:.0f} g", ha="center", fontsize=10, color=INK_2,
                fontweight="semibold" if i == 0 else "normal")
    ax.annotate("3.1× the lightest", xy=(0, vals[0]), xytext=(0.55, vals[0] * 0.86),
                color=CRITICAL, fontsize=9.5, fontweight="semibold",
                arrowprops=dict(arrowstyle="-", color=CRITICAL, lw=1.1))

    caption(ax, "Same requirement set, same envelope. Committing early to 100% PLA additive manufacture bought "
                 "iteration speed\nand cost mass — the clearest quantified trade of the project.")
    save(fig, "fairing-mass-benchmark.png")


# ------------------------------------------------------- 6. tunnel drag/AoA ---
def chart_tunnel():
    rows = read_csv("tunnel_runs_fairings_on.csv")
    aoa = np.array([float(r["aoa_deg"]) for r in rows])
    drag = np.array([float(r["drag_fx_norm_N"]) for r in rows])
    lift = np.array([float(r["lift_fz_norm_N"]) for r in rows])

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    dress(ax, grid_axis="both")

    # One point per attitude: 0 deg was run seven times, so the sweep line must
    # follow the mean at each angle rather than zig-zag through the repeats.
    angles = np.array(sorted(set(aoa)))
    means = np.array([drag[aoa == a].mean() for a in angles])
    zero = drag[aoa == 0]
    sigma = zero.std(ddof=1)

    ax.plot(angles, means, color=BLUE, lw=2.0, marker="o", ms=7,
            mec=SURFACE, mew=1.5, zorder=3, label="Mean drag at each attitude")

    ax.errorbar(0, zero.mean(), yerr=sigma, color=ORANGE, lw=0,
                elinewidth=1.8, capsize=5, capthick=1.8, zorder=4)
    ax.plot(np.zeros_like(zero) + 0.0, zero, "o", color=ORANGE, ms=4.5, alpha=0.65,
            mec="none", zorder=5,
            label=f"0° repeat runs  (n={len(zero)}, σ = {sigma:.2f} N)")

    ax.set_xlabel("Angle of attack  (deg)")
    ax.set_ylabel("Drag  (N)")
    ax.set_title("Fuselage drag with fairings fitted, 20 m/s")
    ax.set_xlim(-13, 19)
    ax.set_ylim(4.2, 9.0)
    ax.legend(loc="upper center", handlelength=1.6, ncol=1)

    ax.annotate("minimum-drag attitude sits\nnear 0–5°; drag climbs either side",
                xy=(2.5, 5.03), xytext=(3.2, 4.45),
                color=MUTED, fontsize=8.8, ha="left",
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.9,
                                connectionstyle="arc3,rad=0.25"))

    caption(ax, f"Seven repeats at 0° bound run-to-run scatter at σ = {sigma:.2f} N. The fairing-on minus "
                "fairing-off difference measured across the\nwhole campaign was 0.09 N — well inside that "
                "scatter, so the tunnel result is honestly inconclusive rather than a drag penalty.")
    save(fig, "tunnel-drag-vs-aoa.png")


if __name__ == "__main__":
    print("Regenerating charts ->")
    stiff = chart_load_deflection()
    chart_reserve_factors()
    chart_aerofoil()
    chart_mass()
    chart_benchmark()
    chart_tunnel()
    print(f"\nFitted stiffness: centre {stiff['Centre']:.1f} N/mm, "
          f"empennage {stiff['Empennage']:.1f} N/mm")
