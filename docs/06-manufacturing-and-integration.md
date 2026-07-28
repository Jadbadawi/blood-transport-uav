# 06 · Manufacturing and Integration

[← Aerodynamics](05-aerodynamics.md) · [Next: Test campaign →](07-test-campaign.md)

---

## The decision that shaped everything: 100% additive

Every flight part was **FDM printed in PLA**. This was decided early, on the
back of experience gained printing the main wing joint and empennage for the
Graphite Goose prototype, and it was defensible at the time:

- **Fast iteration** — essential given how much neighbouring geometry moved
- **Near-zero attended build time** — prints run overnight without a person
  present, which matters when lab hours are a hard budget
- **Complex compound curves** — the fairing shapes are difficult by any other
  available process

It cost mass and it cost strength, and by the time that was clear it was too
late to change. The full accounting is in
[Structural analysis](04-structural-analysis.md) and
[Lessons learned](09-lessons-learned.md).

The specific defect is not choosing additive manufacture — it is choosing it
**for everything, permanently, without revisiting**. Parts that never changed,
like the nose cone fairing, carried the mass penalty of a flexibility they never
used.

---

## Tolerance analysis

The first prints made something obvious: **CAD nominal dimensions do not survive
contact with a printer.** A tolerance stack was therefore run for every part
before printing.

Worked example, hemispherical nose cone fairing:

| Question | Answer (mm) |
|---|---|
| Achievable tolerance on the fairing shaft diameter? | 3D printers hold **±0.5 mm** on diameter |
| Target clearance? | **0.2 mm** minimum for compatibility |
| Minimum fuselage inner diameter (from manufacturer)? | 36.0 − 0.1 = **35.9** |
| Maximum permissible shaft size? | 35.9 − 0.2 = **35.7** |
| Nominal shaft size? | 35.7 − 0.5 = **35.2** |

The logic runs from the worst-case mating dimension inward, subtracting the
required clearance and then the process capability. Both uncertainties are
stacked — the printer's and the CFRP supplier's — rather than assuming either is
nominal.

This is straightforward, it was done consistently, and it is the reason parts
generally fitted first time. It is one of the quieter successes of the project.

---

## Process notes, part by part

### Main wing fairing — printed in four pieces

Too large for the print bed, so it was split into **four segments and bonded**.
The bonding came out well. Two problems did not:

- The printer **erred on one edge**, leaving a gap that had to be filled with a
  bonded balsa insert. Functional, visibly a repair.
- **Bolts and nuts were left exposed.** Brass inserts should have been used
  here too — the part carries no significant load, so there was no reason not
  to.

### Empennage joint — the best-executed part

- **Brass inserts** heat-set neatly, holding a flush fit between the halves
- **Servo housing** bonded cleanly onto the clamp
- **Avionics cabling** routed through channels designed into the joint

The one genuine problem was the **HTP spar bore**. FDM left support material
inside it which had to be sanded out; the sanding was untidy enough that during
the structural test the rough bore was **mistaken for a structural failure**.

The lesson is specific and useful: a larger designed-in allowance would have
avoided it, but predicting how much material a printer will leave in a blind
bore is genuinely unreliable. Where it matters, design the feature so it can be
reamed to size rather than hoping the print is clean.

### Front payload ring cover — the weakest execution

Attached with **zip ties**. Simple, inelegant, and awkward to remove. The team's
own assessment stands: making the cover integral to the ring, or using permanent
wire ties, would have been simpler *and* better. This is what a rushed solution
to a late-emerging problem looks like.

---

## Integration — the strongest area

> *"As a result of us compromising so much with other teams, integration became
> our strongest point."*

Every interface was reviewed repeatedly for fit, shape, tolerance and position
against the other teams' existing plans. Being downstream of six teams forced a
discipline of asking rather than assuming, and it paid off: the assembled
aircraft went together.

![Trial assembly of the airframe](../figures/testing/trial-assembly-airframe.png)

### The one interface that failed

The **false rear spar joint**. The wing teams cut their false rear spars before
Team 08 established the interface, and — worse — **the two wing teams chose
different FRS positions**, forcing an asymmetric fairing and a longer design
cycle.

It then failed twice over on the day. The team member present at the structural
test was **the only one who had not attended the practice assembly**, so when
the FRF attachment did not go together, a makeshift solution was improvised and
the joint was discarded entirely. Gate 4 recorded the consequence: *"cable ties
required to close structures."*

Two independent causes, both organisational:

1. **A late interface** — not asking the wing teams before they cut
2. **Lost build knowledge** — the practice assembly did not transfer to the
   person who needed it

Neither is a CAD problem. The parts were compatible: on 3 March a trial assembly
verified that the FRF attachments aligned correctly with their respective wing
spars. The knowledge of *how* to assemble them was what went missing.

---

## The CAD rebuild

Halfway through the year the model was rebuilt from scratch.

**Why.** The original assemblies were constructed by importing other teams'
parts directly and then adjusting around them. Inventor's referencing system
then propagated every upstream change into Team 08's parts — and upstream
changed constantly. The team's own description was *"Frankenstein's monster CAD
files"*: a model that could no longer be developed because its own history was
controlled by six other people.

**The fix.** Parts were redrawn against **sketches derived from** other teams'
CAD, rather than referencing their geometry live. This decouples the model: an
upstream change now requires a deliberate update to a sketch instead of silently
rippling through.

**The result.** The design process became significantly more streamlined
afterwards. Alongside it the team recorded a candid list of CAD skills actually
learned: constraining measurements, tolerancing, and — disarmingly —
using a mouse properly.

Rebuilding a model mid-project is expensive and feels like lost ground. It was
the right call, and the residue of the old approach is still visible in the raw
folder structure: a duplicated `JointsAndFairinsg` tree nested three levels
deep, removed before publishing (see [`cad/README.md`](../cad/README.md)).

### The wider integration story

The company's Technical Director was responsible for assembling the full UAV in
CAD and did not complete it. With the repository deadline approaching, **Team
08's design specialists took over and assembled the entire aircraft** — outside
their remit, for the whole company.

That assembly is the model published in [`cad/`](../cad/), and it is why other
teams' subassemblies appear in this repository at all.

---

[← Aerodynamics](05-aerodynamics.md) · [Next: Test campaign →](07-test-campaign.md)
