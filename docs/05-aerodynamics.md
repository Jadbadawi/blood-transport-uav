# 05 · Aerodynamics

[← Structural analysis](04-structural-analysis.md) · [Next: Manufacturing & integration →](06-manufacturing-and-integration.md)

---

Two separate aerodynamic questions were in play, and they had very different
answers available to them:

1. **The wing section.** A well-posed 2D problem with a standard tool (XFoil),
   a standard aerofoil (NACA 2414) and tunnel data to check against.
2. **The fairings.** A 3D problem, brand new to the unit, with no reference
   geometry, no closed-form method, and no usable CFD.

The first is validation work. The second required building an argument from
first principles and then admitting how much the experiment could actually
confirm.

---

# Part 1 — Wing section: prediction versus measurement

## Operating point

Sea level ISA was assumed: ρ = 1.225 kg/m³, μ = 1.789 × 10⁻⁵ Pa·s,
a = 343.54 m/s. At the tunnel speed of 20 m/s:

```
Re = ρVc/μ = (1.225 × 20 × 0.30) / 1.789×10⁻⁵ = 4.11 × 10⁵
M  = V/a   = 20 / 343.54                      = 0.0582
```

Two things follow immediately, and they frame everything below:

- **M = 0.058 — compressibility is irrelevant.** No wave drag term exists at
  this speed. Any drag measured is viscous or form drag.
- **Re = 4.1 × 10⁵ — this is low.** That is squarely in the range where the
  laminar-to-turbulent transition point is sensitive to surface finish and
  freestream turbulence, and where a small Reynolds number error moves
  transition significantly. It is the reason the XFoil and tunnel results were
  never going to coincide.

## Results

XFoil polars were generated at 0° angle of attack for 0° and 30° flap
deflection, and compared against tunnel runs at the same settings.

![XFoil versus wind tunnel](../figures/charts/aerofoil-prediction-vs-test.png)

| Configuration | Source | C<sub>L,max</sub> | C<sub>D,min</sub> |
|---|---|---|---|
| Clean, 0° flap | XFoil | 1.25 | ~0.007 |
| Clean, 0° flap | Tunnel | **1.00** | **0.030** |
| Flap 30° | XFoil | 1.80 | 0.070 |
| Flap 30° | Tunnel | **1.25** | **0.200** |

Original polars: [XFoil clean](../figures/aero/drag-polar-xfoil-clean.png) ·
[XFoil 30° flap](../figures/aero/drag-polar-xfoil-flap30.png) ·
[tunnel clean](../figures/aero/drag-polar-tunnel-clean.png) ·
[tunnel 30° flap](../figures/aero/drag-polar-tunnel-flap30.png)

The pattern is consistent and in the expected direction: **the tunnel loses lift
and gains drag in both configurations.** The theoretical curves are smoother,
reach higher peak lift, and sit at lower drag for a given lift. The experimental
curves are more rounded — flow separation begins earlier and viscous losses are
higher.

Deploying the flap to 30° increases camber, raising both C<sub>L</sub> and
effective angle of attack. The prediction says peak lift rises to 1.80 at the
cost of drag climbing from 0.07 to 0.15. The tunnel agrees on the *shape* of
that trade and disagrees on its magnitude: peak lift only reaches 1.25, and drag
starts at 0.20 — already above where XFoil's flapped polar ends.

## Why they differ

Four mechanisms, roughly in order of contribution:

**1 · Finite span.** XFoil solves a 2D section of infinite span. The tunnel
model has ends. Tip vortices generate induced drag and shed bound circulation,
which cuts lift and adds drag — a term entirely absent from the 2D solution.
This is the dominant effect and it acts in exactly the direction observed.

**2 · Wall interference.** Tunnel walls constrict the flow around the model,
locally accelerating it and altering the pressure distribution the model sees.
The measured coefficients are therefore not free-air coefficients.

**3 · Reynolds number mismatch.** The true Re depends on the actual chord,
surface condition and freestream turbulence intensity, none of which match the
idealised value fed to XFoil. At Re ≈ 4 × 10⁵ even a modest mismatch shifts
transition, and transition location sets both separation onset and skin friction.

**4 · Surface finish.** The models are not the smooth analytical surface XFoil
assumes.

**The conclusion is not that XFoil was wrong.** It answered its own question
correctly. It is that a 2D, inviscid-plus-boundary-layer, infinite-span,
smooth-surface model is a *lower bound on drag and an upper bound on lift*, and
should be read as such rather than as a prediction of what a real finite wing in
a real tunnel will do.

---

# Part 2 — Fairings

## Working without a tool

Fairings were new to AVDASI 2 this year. There was no prior geometry to
reference and no closed-form method for the drag benefit of an arbitrary 3D
fairing. CFD was considered and rejected — honestly — on two grounds: the team
lacked the technical depth to set up and validate a credible model, and the
readily available packages do not give trustworthy results at this scale without
that depth. A CFD result nobody can defend is worse than no CFD result.

So the design was argued from drag decomposition instead.

## The argument

**Step 1 — establish the objective.** The mission requires the UAV to fly to the
test centre as fast as possible. Not furthest, not longest. **Minimising total
drag is therefore the fairings' entire purpose**, and every shaping decision
follows from that one sentence.

**Step 2 — decompose the drag.** Total drag splits into normal pressure drag and
skin friction drag. At 20 m/s, with M = 0.058:

- **Wave drag: zero.** Not transonic.
- **Induced drag:** a wing term, not a fuselage-fairing term.
- **Normal pressure drag: negligible at this speed.**
- **Which leaves form drag and skin friction drag** as the only levers.

**Step 3 — recognise the trade.** Low skin friction drag and low form drag pull
in opposite directions. A fairing *adds wetted area*, which adds skin friction —
so it can only be worth fitting if it removes more form drag than the friction it
introduces. This is the central design tension of the whole part, and it is why
"just cover everything" is not automatically right.

**Step 4 — find where form drag is worst.** The exposed items are the payload
rings, the main wing joint, and roughly **100 mm of cylindrical wing spar**.
Using Cayley's minimum-drag shape (1810): in 2D, a circular section produces on
the order of **ten times** the drag of an aerofoil section of the same
thickness. A bluff cylinder in clean air is about the worst thing that can be
left on an aircraft.

**Step 5 — shape accordingly.** The fairing takes the **NACA 2414** section used
by the wing teams, so the covering is continuous with the wing it meets. It
maintains laminar flow as far aft as possible, thins the boundary layer, and
minimises abrupt contour changes.

The empennage joint was shaped as its own fairing on the same reasoning, argued
in [Detailed design](03-detailed-design.md).

## What the tunnel actually showed

![Fuselage drag with fairings fitted](../figures/charts/tunnel-drag-vs-aoa.png)

Averaged over the campaign, **fairings-on recorded 0.09 N more drag than
fairings-off.**

Before interpreting that: seven repeat runs at 0° give a run-to-run standard
deviation of **σ = 0.34 N**. The measured difference is roughly a quarter of one
standard deviation of the measurement noise. **It is not a resolvable
difference.** The correct statement is that the tunnel could not detect any
effect, in either direction — and indeed at some 0° trials, fairings-on recorded
*lower* drag than fairings-off.

Data: [`analysis/data/tunnel_runs_fairings_on.csv`](../analysis/data/tunnel_runs_fairings_on.csv)

### Four reasons the test could not answer the question

**1 · The wings were not fitted.** The tunnel could only accommodate the
fuselage. This removes the single largest justification for the fairing — the
100 mm of exposed spar — from the experiment entirely. The main benefit was
untestable in the available facility, while the fairing's cost (extra wetted
area) was fully present. **The test was structurally biased against the part.**

**2 · Open sides.** With no wings attached, the fairing's flanks were open. Flow
crept inside and raised drag substantially — a condition that cannot occur on the
assembled aircraft.

![The fairing in the tunnel showing the vertical cutout](../figures/testing/tunnel-fairing-cutout.png)

**3 · The vertical cutout.** Added so the fairing would clear the tunnel
mounting hardware, it let flow interfere between the fairing and the fixtures.
A feature added purely for testability degraded the quantity being tested.

![Exposed spar section in the tunnel](../figures/testing/tunnel-exposed-spar.png)

**4 · The pod dominated.** The payload pod and rings are physically large and
were by far the biggest drag source present. Whatever the fairing contributed
was buried under a much larger signal.

There is also a **blockage** effect: the fairing increases the model's frontal
area relative to the test section, and with wall interference already
constricting the flow, this shifts the measured pressure distribution.

### The honest conclusion

**Experimentally: inconclusive.** The measured difference is inside the noise,
and the configuration prevented the primary benefit from appearing at all.

**Theoretically: the fairing should reduce drag in real operation.** The
argument does not depend on the tunnel. Covering a bluff cylinder with an
aerofoil section removes form drag that is present in flight regardless of what
a fuselage-only tunnel model can measure. That drag reduction, and the fact that
the measured skin friction penalty was too small to detect, is the actual
result: **a large form-drag benefit was traded for a friction penalty that
proved unmeasurable.**

What would be needed to close this properly is a test with wings fitted, or
validated CFD. Neither was available.

## Mass, and an argument that does not survive

The fairings account for **11.85% of all-up UAV mass**.

There is a superficially appealing counter-argument: the aircraft has no
propulsion in test, so as a pure glider a heavier airframe flies *faster* for
the same L/D — the reason competition sailplanes carry water ballast.

That argument does not survive contact with the mission. The UAV is not a
glider. Every gram of fairing is a gram of thrust not spent carrying blood
samples, and take-off is limited by a short rural runway. **Lighter is
unambiguously better here.** The ballast analogy is a real effect applied to the
wrong vehicle.

Better options existed: formed aluminium sheet, or foam in selected areas —
foam carrying its own penalty of moisture sensitivity in real weather.

## Design defects worth recording

- **The tunnel fixture has no counterbore.** Bolt heads and nuts sit proud in
  the airflow. On a real vehicle that is both a drag source and a hazard. It
  should have been counterbored; it was not.
- **Surface finish.** FDM leaves a rough outer surface, made worse in places by
  post-processing. At Re ≈ 4 × 10⁵ surface roughness moves transition — so the
  manufacturing method partly undermined the laminar-flow intent of the shape.
- **Blunt profile at the wing root.** Gate 3 judged the main fairing profile
  *"very simplistic and… non-optimum for aerodynamics"*. Fair. Earlier access to
  a complete CAD assembly would have allowed a slimmer, better-integrated shape,
  and smaller payload rings would have let the whole fairing sit lower.

---

[← Structural analysis](04-structural-analysis.md) · [Next: Manufacturing & integration →](06-manufacturing-and-integration.md)
