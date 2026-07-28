# 03 · Detailed Design

[← Concept selection](02-concept-selection.md) · [Next: Structural analysis →](04-structural-analysis.md)

---

Ten parts went onto the flying article: five structural, five aerodynamic.

![All ten delivered parts](../figures/cad/parts-catalogue.png)

*The delivered part set. Joints and clamps on the left, fairings on the right.*

---

# Part 1 — Joints

The joints exist to attach the wings, HTP and VTP to the **CFRP fuselage spar**
which forms the aircraft's backbone.

## 1.1 Fus-MWP joint (wing to fuselage)

Secures the port and starboard wings to the aluminium centre bar that passes
through the fuselage.

**Fit.** The bore holding the centre bar was sized from a tolerance stack so the
bar would be a **friction fit** — tight enough to satisfy 2.5.1.a (spars held
horizontal, no unwanted pitch angle) without needing a secondary clamping
feature that would add mass and assembly time.

**Anti-rotation.** A cylindrical centre bar has infinite rotational symmetry
and will roll inside its bore. This was solved with a **through-bolt** locking
the bar to the joint. The assessors singled this out as the strongest feature of
the design at Gate 3 — *"good innovation in the centre-spar locating screw."*

It was not free. Drilling the bar reduced the load-bearing section, complicated
manufacture, and — as [Structural analysis](04-structural-analysis.md) argues —
a **cuboid centre bar** would have removed the need for the feature entirely by
being unable to roll in the first place.

**Load path.** PLA is a poor load-bearing material, and 2.5.2.a is explicit
about it. A **formed 2014A-T3 aluminium strap** sits over the joint so that bolt
bearing loads pass through aluminium rather than through printed plastic.

![The formed 2014A-T3 aluminium bearing strap](../figures/cad/aluminium-strap.png)

The strap has a known weakness: because it was formed to a shape that does not
perfectly follow the joint's surface, there are **small regions where it does
not contact the joint** and therefore is not carrying load locally. A joint
profile designed for ease of sheet forming would have fixed this at no
aerodynamic cost — the entire joint is hidden under the main fairing, so its
external shape is unconstrained. This was a missed opportunity.

## 1.2 Fus-MWP joint clamps

Two clamps attach the joint to the CFRP fuselage spar via **M4 bolts at 100 mm
spacing**, and are **locally tapered** to follow the spar's own taper and sit
flush.

Clamp thickness was a genuine two-sided compromise: too thin and the clamp fails
in service; too thick and it fouls the payload. 

**Two variants were drawn** because the two test campaigns need different
things:

| Variant | Feature | Reason |
|---|---|---|
| Wind tunnel | 8 mm counterbore | Accepts a flanged bronze bush for the tunnel mounting |
| Structural test | No counterbore | Solid material under the wing nut |

![The 8 mm counterbore in the wind tunnel clamp](../figures/cad/mwp-clamp-counterbore.png)

**This distinction is the single most consequential detail in the project.** The
wind-tunnel clamp was left fitted for the structural test, because disassembling
the pod to swap it would have cost time the team did not have. The counterbore
left a cavity directly under the wing nut, the nut dropped into it, and the bolt
began working through the remaining thin section. The full failure analysis is
in [Test campaign](07-test-campaign.md).

The parts were right. The configuration control was not.

## 1.3 Emp-Fus joint (empennage to fuselage)

Attaches the VTP and HTP to the rear of the fuselage spar — and, unusually, is
**shaped to act as its own fairing**.

That decision is worth defending, because it looks like scope creep and isn't.
By the time flow reaches the empennage it has already crossed the main fairing
and the payload pod, so it is thoroughly disturbed. Adding a *separate* fairing
back there would add wetted area, mass and frontal footprint to smooth flow that
is already turbulent — paying a certain cost for an uncertain benefit.
Aerodynamically shaping the joint itself gets most of the available benefit for
no additional part count.

![Exploded view of the empennage joint](../figures/cad/emp-fus-joint-exploded.png)

**Construction.** Split horizontally into two halves to give access for the VTP
and HTP fittings. The VTP is bonded to the upper half; the HTP main and false
rear spars are friction-fitted per 2.5.1.b.

**Brass inserts.** The two halves are bolted together into **heat-set brass
inserts** melted into the lower half. The original intent was to recess bolt
heads and washers inside the adaptor, but there was not enough internal volume.
Inserts were the fallback.

Honest assessment: it worked here, and it would not always. Heat-setting inserts
locally degrades the PLA around them, and under significant **lateral** load the
inserts could pull free. The structural test applied no lateral loading, so this
was never exercised. The correct fix is to enlarge the joint and return to the
original recessed-bolt scheme — constrained only by the top face, which had to
match the VTP; there was room to grow both taller and wider.

**Cable routing.** Channels were added to the joint to hide the avionics team's
cabling, and the empennage servo housing bonds onto the clamp. Both came from
asking the neighbouring teams what they needed early, and both worked cleanly.

## 1.4 Emp-Fus clamp

Houses the empennage servo, secures the joint, and — like the main wing clamps —
carries a local taper to sit flush against the CFRP spar.

---

# Part 2 — Fairings

Four fairings, all serving requirement 2.6.1.a: cover the gaps and sharp edges
that the joints create, so the flow does not separate over them.

## 2.1 Fus-MWP fairing — the primary part

The largest and most demanding part on the subassembly. It covers the Fus-MWP
joint, its clamps, and **three payload rings**.

![The main wing fairing](../figures/cad/fus-mwp-fairing.png)

**Sectional shape.** The fairing adopts the **NACA 2414** profile used by the
port and starboard wing teams, so the covering blends into the wing section it
meets rather than presenting a discontinuity at the join.

**Covering the exposed spar.** With wings fitted and no fairing, roughly
**100 mm of cylindrical wing spar** sits in clean air. Citing Cayley's
minimum-drag shape: in 2D, a circular section produces on the order of **ten
times** the drag of an aerofoil section of the same thickness. Covering that
spar is not a detail — it is most of the justification for the part. The reasoning
is developed in [Aerodynamics](05-aerodynamics.md).

**Structural interface.** A **pinned joint** reacts the small loads from the
false rear spar, with PLA inserts added to stiffen the FRF attachment for the
structural test.

**Testability features**, both driven by the tunnel entry:

- a **vertical split** so the aircraft could be run as a half-model
- a **vertical cutout** clearing the tunnel mounting hardware

The cutout later proved to be an aerodynamic liability — it let flow interfere
between the fairing and the fixtures. A feature added for testability degraded
the very quantity being tested. This is discussed under
[Aerodynamics](05-aerodynamics.md).

![Fairing assembly sequence, front](../figures/cad/fairing-assembly-front.png)
![Fairing assembly sequence, rear](../figures/cad/fairing-assembly-rear.png)

*Assembly sequence: two bolts pass from front and rear.*

**Assembly is the part's weakest quality.** Two bolts must pass through holes
set far apart while the fairing is simultaneously held around the fuselage and
over the payload rings. It takes practice. For a part designed to be removed and
refitted repeatedly during a test campaign, that is a real design defect, not a
cosmetic one.

## 2.2 Hemispherical nose cone fairing

Borrowed directly from launch vehicle practice: a **length-to-diameter ratio of
3**, which minimises wetted area for a given diameter while keeping the flow
attached. A worked tolerance stack for this part is in
[Manufacturing & integration](06-manufacturing-and-integration.md).

## 2.3 Front payload ring fairing

The forward payload ring sat well ahead of the main fairing and was exposed. It
was covered with a dedicated shell.

The execution was poor and the team said so: it was attached with **zip ties**
for simplicity, which made it awkward to remove and looked improvised. Making
the covering an integral feature of the ring itself, or using permanent wire
ties, would have been simpler *and* better.

## 2.4 Fuselage shell fairing

Covers the remaining exposed fuselage structure and blends the nose cone into
the main fairing.

---

## Interface control summary

Team 08 held interfaces with **six** other teams. This table is the reason the
subassembly's schedule behaved the way it did.

| Interface | Counterpart | Controlled dimension | Stability |
|---|---|---|---|
| Wing spar → Fus-MWP joint | Port & starboard wing | Spar OD, centre bar length | Stable |
| False rear spar → FRF attachment | Port & starboard wing | FRS position | **Unstable** — the two wing teams chose *different* positions, forcing an asymmetric fairing |
| HTP spars → Emp-Fus joint | Empennage | Spar OD and spacing | Late |
| VTP root → Emp-Fus joint top | Empennage | Root footprint | **Late** — finalised after the Gate 3 design freeze |
| Servo → Emp-Fus clamp | Avionics | Servo envelope, cable route | Late |
| Payload rings → main fairing | Pod | Ring OD, axial position | Changed — a ring moved for CG reasons |

Note the pattern: **every unstable interface is one where the counterpart team
finalised late.** The main wing joint and clamps, whose counterpart geometry was
fixed early, needed almost no rework. The empennage joint, whose counterparts
finalised after design freeze, was revised repeatedly.

The mitigation applied — a **company-wide design freeze**, enforced through the
Design Team Manager role — arrived later than it should have. See
[Project management & risk](08-project-management-and-risk.md).

---

[← Concept selection](02-concept-selection.md) · [Next: Structural analysis →](04-structural-analysis.md)
