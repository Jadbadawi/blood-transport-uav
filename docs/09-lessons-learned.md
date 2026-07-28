# 09 · Lessons Learned

[← Project management & risk](08-project-management-and-risk.md) · [My contribution →](my-contribution.md)

---

The subassembly worked. The aircraft assembled, survived past its ultimate load
case, and went through a full tunnel entry. What follows is what I would do
differently, written to be useful rather than flattering.

---

## 1 · Draw the analysis boundary around the aircraft, not around the method

**What happened.** Eight reserve factors were computed, all sound, all
conservative. The airframe then failed in a mode with no reserve factor at all —
bolt shear-out through printed PLA.

**Why.** The checks were classical metallic joint checks: bearing, tension,
shear, cleavage, prying, bending. That was the taught method and it was applied
correctly. But requirement 2.5.2.a treats printed plastic as a non-structural
former, so PLA parts fell outside the analysis by definition — even after one of
them ended up in a primary load path.

**The generalisable lesson.** An analysis scope inherited from a *method* will
quietly stop matching the *artefact* as the design evolves. The question to ask
before a test is not "did I do the checks correctly" but "**is there any load
path I have not checked at all**". The second question would have found this.

## 2 · Configuration control is a real engineering deliverable

**What happened.** Two clamp variants were correctly designed for two different
test configurations. The wrong one was fitted for the load test, because
swapping it meant disassembling the pod and time had run out. The aircraft
failed at exactly that part.

**Why it matters.** This was not a design error. The design anticipated the
problem and solved it. What failed was the process that carries the right part
to the right test on the right day.

**What I would do.** A written build configuration sheet per test, checked
against fitted part numbers before loading, signed off by someone who is not the
person who fitted them. That is a ten-minute control that would have prevented
the project's only structural failure.

## 3 · Do not let one material decision become permanent

**What happened.** 100% FDM PLA, decided early. Fairings ended up at **3.1× the
mass of the lightest company** and **11.85% of all-up UAV mass**, on an aircraft
where mass drives take-off from a short rural runway.

**The nuance.** The decision was correct when it was made — fast iteration and
complex curves were genuinely needed, given how much neighbouring geometry
moved. The error was never revisiting it. Some parts, like the nose cone
fairing, were geometrically stable from early on and paid for a flexibility they
never used.

**What I would do.** Review material choice per-part at design freeze, and split
the set: keep additive for parts still moving, move stable geometry to foam or
formed sheet. A hybrid was available — a printed exoskeleton under a film
covering was discussed and never tried.

## 4 · Weighting a criterion is not the same as enforcing it

**What happened.** Weight came out of the pairwise comparison as one of the top
three criteria at **21%**. The delivered fairings were the heaviest of three
companies.

**Why.** The weighting informed concept *selection* and then stopped being used.
Nothing tracked mass against a budget during detailed design, so it drifted
without anyone noticing until the week-16 inspection preparation — by which
point rearranging other joints and fairings would have cost more time than
existed.

**What I would do.** Convert every top-weighted criterion into a **tracked
number with a budget and an owner**. A mass column reviewed weekly makes the
problem visible in week 4 rather than week 16.

## 5 · Plan the dependencies you do not control

**What happened.** The critical path predicted **48 hours**. The team clocked
**105 lab hours**, plus outside work.

**Why.** The network diagram modelled dependencies within Team 08. The dependency
that actually governed the schedule — waiting on six other teams' geometry — was
not on it.

**What I would do.** Put external dependencies on the diagram as first-class
nodes with owners and needed-by dates. For a team this far downstream, those
*are* the critical path.

## 6 · Freeze earlier, and mean it

**What happened.** I imposed a company-wide design freeze as Design Team
Manager. It was the right mechanism and it came too late — some teams finalised
after Gate 3, and the rework it was meant to prevent had largely already
happened.

**What I would do.** Freeze interfaces before geometry. Teams do not need a
finished VTP to commit to its root footprint. **Freezing the interface early
allows the part behind it to keep moving**, which is exactly the flexibility
everyone actually wanted.

## 7 · Build knowledge has to be transferred deliberately

**What happened.** A trial assembly on 3 March confirmed the FRF attachments
aligned correctly. At the structural test days later, the one team member
present was the only one who had missed that assembly. The joint could not be
fitted, cable ties were used instead, wing deflection went uneven, and Gate 4
recorded it.

**Why.** The parts were right. The knowledge of how to assemble them lived in
the heads of people who were not there.

**What I would do.** Photograph the assembly sequence during the practice build
and attach it to the part drawings. Ensure anyone attending a test has either
done the build or has the sequence in hand. The information cost nothing to
capture and its absence caused a visible failure.

## 8 · A risk register written by novices misses novel risks

**What happened.** 3D printing failures were not on the register, because nobody
had enough additive experience to know what its failure modes look like.

**What I would do.** Co-author the register with lab technicians and students
from the year above. They have seen the failures a first-time team cannot
imagine. And write mitigations specific enough to execute under pressure —
"ensure correct assembly" is not actionable; a part-number check against a
configuration sheet is.

---

## What went right, and why

Worth recording, because these were not luck:

**Structural analysis was done early, ahead of detailed design.** That gave the
design team limits to work inside rather than an audit to fail afterwards. It is
the main reason the aircraft passed its load test.

**Tolerance stack-ups were run for every printed part.** CAD nominal dimensions
do not survive contact with a printer, and this was recognised on the first
prints rather than the last. Parts generally fitted first time.

**The CAD was rebuilt when it needed rebuilding.** Abandoning a live-referenced
model mid-project and redrawing against derived sketches was expensive and felt
like lost ground. It unblocked the rest of the year.

**Interfaces were negotiated, repeatedly.** Being downstream of six teams forced
a discipline of asking rather than assuming. Integration became the
subassembly's strongest area — and when the Technical Director did not deliver
the company CAD assembly, this team was able to build it.

**The empennage joint doing double duty as its own fairing** was the best design
decision on the subassembly: it got most of the available aerodynamic benefit
for zero additional part count, on an argument about where the flow is already
turbulent rather than on aesthetics.

---

## The thing I would most want a reviewer to notice

The two most valuable findings in this project both came from the gap between
**what was analysed** and **what was built**:

- The stress analysis was correct and did not cover the aircraft.
- The design anticipated the clamp problem and the build did not carry the fix
  through.

Neither is an arithmetic mistake. Both are failures of *scope and process* — and
in my experience of this project, that is where engineering actually goes wrong.
The calculations were the easy part.

---

[← Project management & risk](08-project-management-and-risk.md) · [My contribution →](my-contribution.md)
