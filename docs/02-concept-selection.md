# 02 · Concept Selection

[← Brief & requirements](01-brief-and-requirements.md) · [Next: Detailed design →](03-detailed-design.md)

---

Fairings were **new to AVDASI 2 in 2024–25**. No previous cohort had built one,
there was no reference geometry, and no guidance existed on what one was even
supposed to look like on this airframe. The starting point was requirement
2.6.1.a and a blank sketch.

That absence of precedent is the reason this section exists. When there is no
obvious answer, the defensible move is to make the selection process explicit
so the choice can be argued about on its merits rather than on taste.

## Step 1 — Establishing criteria

The design and aerodynamics specialists jointly enumerated what the fairing
actually had to do. Seven criteria emerged:

| Criterion | Definition used |
|---|---|
| Cost of materials/processes | Cost of materials for the chosen design |
| Structural integrity | Ability to withstand stresses from the false rear spar and aerodynamic forces |
| Weight | Overall mass of the fairing structure |
| Ease of assembly | Ease of removal and reassembly |
| Aerodynamic performance | Ability to minimise drag and improve airflow |
| Manufacturing complexity | Difficulty of production, tooling, and lab hours required |
| Maintenance requirements | Frequency and ease of maintaining the fairings |

![The seven downselection criteria](../figures/cad/downselection-criteria.png)

## Step 2 — Weighting by pairwise comparison

Rather than assigning weights by discussion — which tends to reward whoever
argues hardest — each criterion was compared against every other in a **pairwise
numerical comparison matrix**. The weights fall out of the comparison count
rather than out of an opinion.

Three criteria tied at the top on **21% each**:

- **Aerodynamic performance**
- **Structural integrity**
- **Weight**

This result is worth pausing on, because it is a direct consequence of the
mission. A time-critical outbound leg makes drag matter; a short rural runway
makes mass matter; the false rear spar reaction makes structure matter. The
weighting was not arbitrary — it is the brief, restated as numbers.

It also, in hindsight, contains the seed of the project's clearest failure.
Weight was weighted at 21% and the final fairings came in at **3.1× the mass of
the lightest competing company**. The criterion was correctly identified and
then not enforced. That gap between *knowing* and *doing* is picked up in
[Lessons learned](09-lessons-learned.md).

## Step 3 — Scoring concepts with an MCDA matrix

Concepts were scored against the weighted criteria in a multi-criteria decision
analysis matrix, producing a comparable number per design.

![Three rejected preliminary designs](../figures/cad/downselection-rejected.png)

*Three of the preliminary designs that did not make it onto the aircraft.*

### Why each rejected design lost

**Design 2 — rectangular, low surface area.** Cheap to make and light, but the
sharp edges are a separation trigger, which defeats the entire purpose of the
part under 2.6.1.a. It also fouled the payload rings, degrading ease of
assembly. Low surface area is only a virtue if the flow stays attached over it.

**Design 5 — half aerofoil.** Did not extend over the full chord, so it left an
abrupt discontinuity partway along — creating exactly the drag and turbulence it
was meant to remove. Its trailing edges were also thin enough to be a
manufacturing and handling risk.

**Design 4 — full-chord aerofoil outline.** Scored highly and became the basis
of the final part, but needed rework. As drawn it used a rectangular extrude
clamped between the main wing joint and the top clamp — a boltless clamping
mechanism, elegant on paper. It was rejected on **testability**: removing the
fairing between wind tunnel runs with that connection would have been slow and
fiddly, and tunnel time is the scarcest resource in the project.

### From Design 4 to the final part

The delivered fairing kept Design 4's aerofoil planform and changed three
things:

1. An **additional extrude** to cover the exposed length of wing spar
2. A **relocated FRF attachment** to suit where the wing teams had actually cut
   their false rear spars
3. **Bolted** attachment to the fuselage, replacing the clamping mechanism, so
   the part could be taken off and refitted quickly during testing

## What the method was worth

Downselection did what it was supposed to: it made a genuinely novel design
problem tractable and kept the decision objective when there was no precedent to
appeal to. Three honest limitations:

- **It could not model the requirements that had not arrived yet.** The single
  largest source of redesign was other teams changing their interfaces after the
  fact. No amount of concept scoring anticipates that.
- **Even the winning concept was flawed.** It was heavy. Seven criteria in
  tension means every option is a compromise, and the matrix tells you which
  compromise scores best — not that the result is good.
- **Better initial concepts would have come from better guidance.** Concepts
  drawn from scratch with no idea what a fairing is *for* start further from the
  answer than they need to. This is a fair criticism of the exercise as much as
  of the team.

---

[← Brief & requirements](01-brief-and-requirements.md) · [Next: Detailed design →](03-detailed-design.md)
