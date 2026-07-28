# 04 · Structural Analysis

[← Detailed design](03-detailed-design.md) · [Next: Aerodynamics →](05-aerodynamics.md)

---

## The design case

All checks were run at **6g** (gust or manoeuvre) with the standard aerospace
**1.5** safety factor applied on top:

```
F_design = 6 × 1.5 × F_1g = 9 × F_1g
```

The analysis was completed in **teaching block 1**, deliberately ahead of
detailed design, so that the design team had structural limits to work inside
rather than a structural audit to fail afterwards. That sequencing was correct
and is the main reason the aircraft passed its load test.

## Analysis chain

Each step feeds the next; every step carries an assumption.

**1 · Mass and centre of mass.** A mass table was compiled across all
subassemblies and cross-checked with the other teams, giving

```
CoM = Σ(mᵢzᵢ) / Σmᵢ = 3.69 / 10 = 0.369 m
```

![Centre of mass calculation](../figures/structures/centre-of-mass-calculation.png)

**2 · Lift.** With the CG located, lift in steady level flight was resolved as a
statics problem to find the force at the main wing joint and around the
empennage joint.

**3 · Wing bending and shear.** The wing spar was modelled as a **cantilever
with uniform lift and weight** across the half-span, giving shear force and
bending moment at the wing root.

**4 · Torsion.** Weight was taken to act **120 mm** from the leading edge and
lift at the **rear of the wing spar**, giving root torsion:

```
T_R = 375 N·mm at 1g  →  3375 N·mm at 9g
```

![Wing spar torsion calculation](../figures/structures/torsion-calculation.png)

**5 · Reserve factors.** Root shear, bending and torsion were combined and
carried into the individual joint checks.

## Reserve factors

![Reserve factors by check](../figures/charts/reserve-factors.png)

| Part | Check | RF |
|---|---|---|
| **Centre bar** | **Bending** | **1.95** |
| Spar | Bearing | 2.4 |
| Flange | Prying | 3.4 |
| Spar | Tension | 4.4 |
| Spar | Shear | 5.1 |
| Pin | Shear | 7.4 |
| Spar | Cleavage | 8.9 |
| Lug | Prying | 39.0 |

Data: [`analysis/data/reserve_factors.csv`](../analysis/data/reserve_factors.csv)

**Centre bar sizing.** A **22.2 mm diameter solid bar** gives RF 1.95 — the
lowest value in the set, and therefore the predicted first point of failure.
Retaining it was justified rather than merely accepted: the checks are
conservative by construction (9g, plus simplifying assumptions that all err
toward higher predicted stress), so a reserve factor near 2 on the governing
member is a sound design point, not a marginal one.

**The lug at RF 39 is the other signal in this table.** A reserve factor of 39
is not a triumph, it is 39× more material than the load requires. On a vehicle
where mass drives take-off performance, an outlier that high is an unclaimed
mass saving. It went unclaimed.

---

## Comparing prediction against test

The airframe was loaded to **813 N**, past the ultimate load case.

![Load versus deflection](../figures/charts/load-deflection.png)

The response is **linear throughout** — no knee, no progressive softening. Least
squares through the origin gives:

| Station | Stiffness |
|---|---|
| Centre | **74 N/mm** |
| Empennage | **102 N/mm** |

Linearity to ultimate load is the strongest single piece of evidence in the
project. It says the structure behaved as a well-understood elastic system right
up to the design case, which is precisely what requirement 3.2.5.a asks for.

> **On this chart's provenance.** The raw acquisition log stayed with the unit,
> so these points are digitised from the original test plot at roughly ±0.1 mm.
> They are more than good enough for a stiffness fit and should not be quoted as
> primary measurements. The original figure is at
> [`figures/structures/load-deflection-original.png`](../figures/structures/load-deflection-original.png)
> and the digitised values, with this caveat in the file header, are in
> [`analysis/data/load_deflection.csv`](../analysis/data/load_deflection.csv).

### Then it failed somewhere else

Past 813 N the measured load fell to 804 N, then abruptly to 764 N. A load drop
without an audible or visible event means something has yielded. The aircraft
was stripped and inspected.

The centre bar — the predicted failure point, RF 1.95 — showed **no deformation
whatsoever**. The failure was **bolt shear-out through the PLA main wing joint
clamp**.

![Damage to the main wing joint clamp](../figures/testing/clamp-shear-damage-1.png)
![Damage to the main wing joint clamp, second view](../figures/testing/clamp-shear-damage-2.png)

Full physical narrative in [Test campaign](07-test-campaign.md).

### Why the prediction missed

**No reserve factor was ever computed for any 3D-printed part.** Every check in
the table above is a check on a metallic member — the aluminium centre bar, the
CFRP spar, the aluminium strap and its fasteners. The printed PLA components
were treated, per requirement 2.5.2.a, as non-structural formers. So the
analysis had no term for the mode that actually occurred.

This is not really an arithmetic failure. It is a **scoping** failure, and a
common one in real practice: the analysis boundary was drawn around the parts
the method knew how to handle, and the boundary was never revisited when a
printed part ended up in a primary load path.

Two things follow, and both were true:

- The predictions that *were* made were sound. Linear response to ultimate load
  and an undamaged centre bar confirm the whole analysis chain.
- The predictions did not cover the aircraft. Correct answers to the wrong
  question.

---

## Structural review of the delivered design

### Load path asymmetry — the direct cause

The **upper** half of the Fus-MWP joint is protected: load passes into the
formed 2014A-T3 strap and away from the PLA. The **lower** clamp has no such
protection, and bolt forces bear directly on printed plastic.

The fix is a second bearing plate on the bottom clamp, with three real
objections to weigh:

1. **Mass.** Is this the best use of the budget, when the damage might be
   acceptable and cosmetic?
2. **Space.** The pod and payload ring attachments crowd the region; there may
   not be room.
3. **Complexity.** The clamp assembly is already fiddly. More parts make it
   worse.

The honest resolution is that these forces should have been **modelled** to
settle the question, rather than argued. That modelling was never done — which
is exactly the gap the test found.

### Centre bar: cylindrical versus cuboid

| | Cylindrical (chosen) | Cuboid |
|---|---|---|
| Sizing freedom | Good — matches the round wing spar bore, can sit close to spar OD | Poorer — side length is limited relatively harder |
| Rolling | **Rolls.** Needs a locating bolt, which removes material and complicates manufacture | Cannot roll. No feature needed |
| Second moment of area | Same about every axis; simple | Orientation-dependent; RF calculation more convoluted |

The recommendation is the **cuboid**: it removes a hole from the primary load
path and deletes a manufacturing operation, in exchange for a slightly more
involved calculation. Trading analyst effort for structural simplicity is
usually the right trade.

### Empennage joint

Loads pass predominantly into the CFRP fuselage spar, which is sized for them,
so the unreinforced PLA joint is acceptable at these load cases. Two
observations stand:

- **Brass inserts** could work loose under significant lateral load. The
  structural test applied none, so this remains untested rather than validated.
- **The empennage oscillated noticeably during tunnel running.** Not a failure —
  loads were nowhere near critical — but vibration raises fatigue loading and
  shortens life. Remedies, in increasing order of cost: stiffen the local
  components, add damping, or fit a tuned vibration absorber.

### Mass

![Where the subassembly mass went](../figures/charts/mass-budget.png)

The subassembly totals **1,011 g**. Of that, **742 g is aerodynamic shell** and
only **269 g carries load**.

The joints are defensible: they are primary structure, and their mass buys
capability. The fairings are not. The company mass report puts all fairings at
**652 g — 11.85% of all-up UAV mass**, and **3.1× the lightest** of the three
companies.

![Fairing mass against the other companies](../figures/charts/fairing-mass-benchmark.png)

The cause is a single early decision: **commit entirely to FDM PLA**. That
bought fast iteration and the ability to print complex compound curves, both of
which the project genuinely needed given how much the interfaces moved. It cost
mass, and the bill came due at the end.

What makes this a real error rather than an accepted trade is that **some parts
never changed**. The nose cone fairing was stable from early on and could have
been Styrofoam or another light material at no schedule risk. The blanket
material decision was applied to parts that did not need its flexibility.

> **A note on the source data.** The published mass table totals 1,061.5 g. That
> figure includes the M4 × 50 mm bolt line as **56 g**, where the part is 2.8 g
> and quantity 2 — i.e. **5.6 g**, an apparent factor-of-ten transcription slip.
> [`analysis/data/subassembly_mass.csv`](../analysis/data/subassembly_mass.csv)
> carries the corrected value, giving **1,011.1 g**. The difference does not
> change any conclusion, but the corrected number is the one used throughout
> this repository.

---

## Critique of the analytical method

**Conservatism was stacked.** 9g, plus a cantilever model with uniform loading,
plus assumed load application points, all err in the same direction. The result
is a safe design, but one where you cannot easily tell how much of the reserve
is real margin and how much is accumulated pessimism.

**An inconsistent lift value went unnoticed.** The lug cleavage and flange
prying checks — both relating to the aluminium strap — used a lift value
supplied by the wing teams, while every other check used the statics-case lift
derived internally. The discrepancy was found during a final review before the
data repository freeze, too late to investigate properly.

Both values were conservative and the affected reserve factors (3.4 and 39.0)
are far from critical, so no conclusion changes. But *"it didn't matter this
time"* is not the same as *"it was handled"*. The real defect is that two
different values for the same physical quantity coexisted in one stress report
for months without anyone noticing — a review process gap, not an arithmetic
one.

**Test conditions differed between the two campaigns.** In the Graphite Goose
test every part fitted as designed and the structure behaved as predicted. For
the ultimate load test the structure had to be **cable-tied closed**, which
produced uneven deflection between the two wings — Gate 4 flagged exactly this.
An asymmetrically restrained structure does not load its joints the way the
analysis assumed, and this plausibly contributed to the clamp failing when and
where it did.

---

## Recommendations

| Priority | Recommendation | Rationale |
|---|---|---|
| **High** | Compute reserve factors for printed parts in any load path, using measured anisotropic PLA properties | The failure mode that occurred was the one never checked |
| **High** | Add a bearing plate or equivalent to the bottom clamp | Removes the asymmetry that caused the failure |
| **High** | Enforce build-configuration control between test campaigns | The wrong clamp was fitted; the parts themselves were correct |
| Medium | Adopt a cuboid centre bar | Deletes the locating hole and a manufacturing step |
| Medium | Reconcile lift values across all checks before freeze | Two values for one quantity is a review gap |
| Medium | Move stable-geometry fairings to a lighter material | 652 g at 11.85% of UAV mass, 3.1× the best competitor |
| Low | Stiffen or damp the empennage | Oscillation observed in the tunnel; fatigue, not strength |
| Low | Revisit the RF 39 lug | An outlier that large is unclaimed mass |

---

[← Detailed design](03-detailed-design.md) · [Next: Aerodynamics →](05-aerodynamics.md)
