# 07 · Test Campaign

[← Manufacturing & integration](06-manufacturing-and-integration.md) · [Next: Project management & risk →](08-project-management-and-risk.md)

---

Three test events, each answering a different question.

| Test | When | Question | Result |
|---|---|---|---|
| Graphite Goose | TB-1 | Do the joints work as predicted at limit load? | Pass — behaved as analysed |
| Ultimate load test | 5 Mar 2025 | Does the airframe survive past ultimate load? | Pass to **813 N**, then failed in an unpredicted mode |
| Wind tunnel | TB-2 | Do the fairings reduce drag? | **Inconclusive** — the configuration could not answer it |

---

## 1 · Graphite Goose

A representative prototype assembly loaded to limit, with reactions applied at
the forward fuselage CG and empennage spar positions to reproduce Load Case 1
(requirement 3.2.6.a).

Everything fitted, and the structure behaved as the TB-1 analysis predicted.
This is worth flagging for a reason that only becomes clear later: **in this
test all parts assembled properly and the structure was correctly restrained.**
In the ultimate load test neither was true — and the two tests gave different
failure behaviour partly because of it.

---

## 2 · Ultimate load test

![The ultimate load test station](../figures/testing/ultimate-load-test-station.png)

*Load test station, 5 March 2025. Clockwise from top left: the loaded airframe
in the rig; the LabVIEW acquisition showing deflection channels at port wing,
starboard wing, centre and empennage; the aircraft viewed from the front.*

### Load response

The airframe was loaded past the ultimate load case to **813 N**.

![Load versus deflection](../figures/charts/load-deflection.png)

The relationship is **linear all the way to the ultimate load case** — no knee,
no progressive softening, no sign of anything yielding early. Fitted stiffness:
**74 N/mm** at the centre and **102 N/mm** at the empennage.

This directly satisfies requirement 3.2.5.a and validates the whole TB-1
analysis chain. Whatever went wrong afterwards, the aircraft was correctly
analysed for the modes that were analysed.

### The failure

Sensors were removed after the ultimate load was reached, to protect them.
Loading continued.

The recorded load then went **813 N → 804 N → 764 N**. A load drop with no
visible or audible event means something has yielded, but nothing was obvious
from outside. The aircraft was disassembled and inspected.

**The centre bar — RF 1.95, the predicted failure point — was undamaged.** It
was inspected specifically because it was expected to be the failure, and showed
no deformation at all.

The failure was **bolt shear-out through the PLA main wing joint clamp**:

![Damage to the main wing joint clamp](../figures/testing/clamp-shear-damage-1.png)
![Second view of the damage](../figures/testing/clamp-shear-damage-2.png)
![Detail of the shear damage](../figures/testing/clamp-shear-damage-detail.png)

*The wing nut has pulled down into the counterbore cavity and the bolt has begun
working through the remaining thin section of printed plastic.*

### Root cause: the wrong clamp was fitted

Two clamp variants existed, deliberately
([Detailed design](03-detailed-design.md)):

- **Wind tunnel clamp** — 8 mm counterbore for a flanged bronze bush
- **Structural test clamp** — no counterbore, solid material under the wing nut

**The wind tunnel clamp was fitted for the structural test.** Swapping it would
have meant disassembling the pod, and there was not enough time. So the aircraft
was loaded with a cavity directly beneath the wing nut. Under load the nut
dropped into that cavity and the bolt sheared down through the thin plastic
left below it.

The design anticipated this problem and solved it. The **build configuration
control** did not carry the solution through to the day. The correct part
existed and was not fitted.

### A second contributing factor

The structure had to be **cable-tied closed** for the test, because the FRF
attachment could not be assembled (see
[Manufacturing & integration](06-manufacturing-and-integration.md)). This
produced **uneven deflection between the two wings**. An asymmetrically
restrained structure does not distribute load into its joints the way the
analysis assumed, and plausibly contributed to the clamp failing when and where
it did. Gate 4 recorded the cable ties explicitly.

### Also inspected

The rest of the airframe was checked for further damage. The only other finding
was rough bores in the empennage joint — **left by the printing process, not by
the applied loads**, and initially mistaken for a failure. Everything else was
sound, confirming the TB-1 predictions.

### What this test is actually worth

It is easy to read "failed unexpectedly" as a poor result. It is not.

- The airframe **exceeded its requirement**, surviving past ultimate load.
- The analysis was **validated** for everything it covered — linear response,
  undamaged centre bar.
- The failure was **traced to a specific, correctable cause**: a known
  configuration difference that was not enforced under time pressure.

The genuinely valuable finding is the analysis gap it exposed. **No reserve
factor was ever computed for any 3D printed part** — the checks were classical
metallic joint checks, applied to an aircraft with printed plastic in a primary
load path. The test found the boundary of the analysis rather than a mistake
inside it. That is what tests are for.

---

## 3 · Wind tunnel entry

Fuselage tested at **20 m/s** (Re ≈ 4.1 × 10⁵, M = 0.058), fairings on and
fairings off, across a range of attack angles, on a six-component balance.

![Fuselage drag with fairings fitted](../figures/charts/tunnel-drag-vs-aoa.png)

**Headline number:** fairings-on averaged **+0.09 N** drag over fairings-off.

**Why that number cannot be read as a drag penalty:** seven repeat runs at 0°
give **σ = 0.34 N** run-to-run. The claimed difference is about a quarter of one
standard deviation of the noise floor — unresolvable. Consistent with that, at
some 0° trials fairings-on measured *lower* drag than fairings-off. The honest
statement is that the tunnel detected no difference in either direction.

**Why the test could not answer the question it was set:** the wings could not
be fitted (facility size), which removes the fairing's primary benefit — 100 mm
of exposed cylindrical spar — from the experiment while leaving its cost, extra
wetted area, fully present. With no wings, the fairing's sides were open and
flow crept inside. The vertical cutout needed to clear the tunnel mounts caused
further interference. And the payload pod dominated the drag signal throughout.

The full aerodynamic argument, and what the result does and does not support, is
in [Aerodynamics](05-aerodynamics.md).

**A structural observation from the same runs:** the **empennage oscillated
noticeably** throughout. Not a failure — loads were far from critical — but
oscillation drives fatigue and shortens component life. Remedies are discussed
in [Structural analysis](04-structural-analysis.md).

---

## Design review outcomes

Two formal gate reviews assessed the subassembly.

### Gate 3 — Design sign-off, 13 January 2025

**Strengths**
- Good innovation in the centre-spar locating screw

**Concerns**
- Mounting/securing of the empennage seemed unclear
- Some questions not answered strongly
- The main wing fairing profile *"seems very simplistic and the form profile
  looks to be non-optimum for aerodynamics… design appears quite unambitious
  compared to what might be possible for this new sub-assembly"*

### Gate 4 — Quality inspection, 18 February 2025

**Strengths**
- Aero profiles fit around the wing profile
- Provision made for fitting into the tunnel

**Concerns**
- Lack of integration planning with the rest of the UAV
- Design/execution somewhat ad-hoc
- Cable ties required to close structures

### Reading the reviews against what happened

The reviews were largely right, and specific enough to be actionable:

- **"Cable ties required to close structures"** — this is the FRF attachment
  problem, flagged in February, and it was still unresolved at the March load
  test where it contributed to uneven wing deflection.
- **"Mounting/securing of the empennage seemed unclear"** — the brass insert
  scheme was a fallback for insufficient internal volume, and remains untested
  under lateral load.
- **"Non-optimum for aerodynamics"** — fair, and traceable to a real cause:
  without an early full-vehicle CAD assembly, the fairing had to be drawn
  conservatively around geometry that kept moving.

One review comment deserves a partial rebuttal. **"Lack of integration planning
with the rest of the UAV"** does not match the evidence: every interface was
reviewed repeatedly, the aircraft assembled, and this team ultimately built the
company's full CAD assembly when the Technical Director did not. What the
inspection saw was the *visible residue* of one failed interface — the cable
ties — on a subassembly that was integrated more carefully than most. The
underlying failure there was late interface definition by others and lost build
knowledge within the team, not absent planning.

---

[← Manufacturing & integration](06-manufacturing-and-integration.md) · [Next: Project management & risk →](08-project-management-and-risk.md)
