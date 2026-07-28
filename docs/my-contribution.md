# My Contribution

**Jad El Badaoui** — MEng Aerospace Engineering, University of Bristol

[← Lessons learned](09-lessons-learned.md) · [Back to overview](../README.md)

---

I held **four roles** on this project. That was a deliberate choice rather than
an accident of allocation: I wanted to find out which parts of engineering I was
actually good at, and the only way to do that was to take on more than one and
find out by doing.

| Role | Scope |
|---|---|
| **Fuselage Division Design Team Manager** | Cross-team design authority across the whole fuselage division |
| **Project Manager, Team 08** | Planning, scheduling, and inter-divisional coordination |
| **Aero Specialist** | Aerodynamic design rationale and wind tunnel analysis |
| **Design Specialist** | CAD design of joints and fairings |

In the team's technical report I authored the **Project Management** section in
full, the **Aerodynamics** section in full, and the **Design and Manufacturing**
downselection and subassembly design sections (3.1–3.2).

---

## Design Team Manager — fuselage division

The DTM role sits above individual teams and owns design coherence across a
division. In practice this meant three things.

**Enforcing a design freeze.** Several teams — VTP in particular — were still
finalising geometry after Gate 3, which meant Team 08 was continually redesigning
interfaces to parts that were supposed to be settled. I imposed a company-wide
design freeze to stop it. It was the right mechanism, and my clear judgement in
hindsight is that I applied it too late: most of the rework it was designed to
prevent had already happened. → [Lessons learned §6](09-lessons-learned.md)

**Building divisional network diagrams.** Working with the other DTMs, I
produced network diagrams at *divisional* level, capturing dependencies and
critical paths across teams rather than within them. These were the documents
that connected team objectives to company objectives, and they were the layer
that had otherwise been missing entirely.

![Company fuselage division network diagram](../figures/pm/network-diagram-company.png)

**Hands-on manufacturing and build.** The DTM role carried an expectation of
being in the lab. I took it up deliberately — engineers in industry need
hands-on prototype experience, and it is the fastest way to learn what a design
actually costs to make. Printing, post-processing, fitting brass inserts and
trial assembly all sat within this.

---

## Project Manager

I built and maintained the three planning documents that governed Team 08's
year, and I made them **congruent** with one another — a WBS, a Gantt and a
network diagram are three views of one project, and if they disagree, the team
stops trusting all three.

![Design and build phase Gantt](../figures/pm/gantt-design-build-phase.png)

The change I would point to as most effective was in the design and build phase
(weeks 7–17): breaking work down to a genuinely feasible task granularity,
building in explicit slack, and **assigning each task to a named individual**
rather than to the team. Accountability at the level of a person rather than a
group changed how the plan was used.

I also introduced a **mandatory 5–10 minute reflection after every meeting**.
This came from a team self-assessment against Lencioni's five dysfunctions model
partway through teaching block 1, which showed our weakest areas were
commitment (3.00) and attention to results (3.13) — and which matched our
performance at the preliminary design review, where we were not confident in our
own designs and calculations. Alongside closer follow-up and specific individual
accountability before each milestone, the second self-assessment in teaching
block 2 showed a marked improvement.

**The honest assessment of my planning work** is in
[Project management & risk](08-project-management-and-risk.md): my critical path
predicted 48 hours and the team clocked 105. The estimates were not the problem
— the model was. I planned the dependencies inside my team and not the ones I
did not control, which for a team sitting downstream of six others were the only
ones that mattered.

---

## Aero Specialist

I owned the aerodynamic argument for the fairings and the wing section analysis,
and I attended the wind tunnel test.

I joined this specialism expecting to learn new equations and CFD. Neither was
available — there was no closed-form method for the drag benefit of an arbitrary
3D fairing, and CFD at the fidelity needed was beyond what the team could set up
and defend. A CFD result nobody can justify is worse than none.

So the work became something harder and more useful: **building an argument from
drag decomposition**. Establishing that at M = 0.058 wave and normal pressure
drag are negligible, so form and skin friction drag are the only levers;
recognising that a fairing necessarily *adds* wetted area and can only pay for
itself by removing more form drag than the friction it introduces; identifying
the exposed cylindrical wing spar as the dominant form-drag source via Cayley's
minimum-drag shape; and shaping the fairing to the NACA 2414 section accordingly.

I also did the XFoil-versus-tunnel comparison for the port wing and worked
through why they disagree — finite span, wall interference, Reynolds mismatch,
surface finish.

The result I am most willing to defend is the one that says **the experiment
could not answer the question**. The measured fairings-on penalty was 0.09 N
against a run-to-run scatter of 0.34 N, and the test configuration — fuselage
only, no wings — removed the fairing's primary benefit while leaving its cost
fully present. Reporting that as inconclusive, rather than dressing it up in
either direction, is the correct engineering answer.
→ [Aerodynamics](05-aerodynamics.md)

---

## Design Specialist

CAD design of the joints and fairings in Autodesk Inventor, including the
downselection process and subassembly design that I wrote up in the technical
report.

This is where the project pushed me hardest, because fairings were **new to the
unit that year**. There was no reference geometry and no guidance on what one is
even supposed to look like on this airframe — just a requirement and a blank
sketch. Making that tractable meant building the selection process explicitly:
seven criteria, weighted by pairwise comparison so the weights came out of the
comparison rather than out of whoever argued hardest, then scored in an MCDA
matrix. → [Concept selection](02-concept-selection.md)

I also designed the **spar plugs** for the wing attachment, which went through
the starboard wing PM for approval — a clean example of the design cycle working
as intended.

### Taking over the company CAD assembly

The company's Technical Director was responsible for assembling the entire UAV
in CAD and did not complete it. With the data repository deadline approaching,
my design team stepped outside our remit and **assembled the whole aircraft for
the company**.

That model is what is published in [`cad/`](../cad/), and it is the reason other
teams' subassemblies appear in this repository at all. Of everything I did this
year it is the piece I am most pleased with — not for the CAD, which was
laborious rather than difficult, but because a small team chose to absorb
someone else's failure rather than let the company miss its deadline.

---

## What I learned about how I work

A structured self-evaluation, cross-checked against how my teammates rated me,
identified me as a **shaper** in the Belbin model. That reading was accurate and
it cuts both ways.

The upside is real: I brought energy and drive at points where the project
needed it, and I was willing to take on work outside my remit — the design
freeze, the divisional diagrams, the company CAD assembly — rather than watch
things fail.

The downside is equally real, and I would rather record it than hide it. A
competitive, low-tolerance-for-error approach led me to **give instructions
rather than assign responsibility**, and that created friction. I eventually
understood that I was addressing the problem the wrong way: each teammate worked
differently, and my communication should have adapted to the person rather than
expecting the person to adapt to me. Handled better, it would have produced a
more collaborative and inclusive team rather than a more compliant one.

That is the single most useful thing this project taught me, and it is not a
technical lesson.

---

## Where this took me

Working across four roles made me a more rounded engineer than any one of them
would have — technically, administratively, and in leading people. It also
settled a question I had been circling: I want to work in aerospace, and I want
to get to a **technical director** position, where the job is combining deep
technical knowledge with everything the other specialisms do.

The moment that settled it was not a calculation. It was my design team stepping
up to take over the full CAD assembly when someone else had fallen behind, and
delivering it — because we had built the kind of working environment where that
was possible.

---

[← Lessons learned](09-lessons-learned.md) · [Back to overview](../README.md)
