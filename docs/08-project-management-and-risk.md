# 08 · Project Management and Risk

[← Test campaign](07-test-campaign.md) · [Next: Lessons learned →](09-lessons-learned.md)

---

I was one of Team 08's Project Managers and the **Fuselage Division Design Team
Manager**, so this section is largely my own work. It is also the section where
the project's real difficulties live — the engineering was rarely the hard part.

---

## Planning documents

Three documents, deliberately built to be **congruent** with one another. That
word is doing real work: a WBS, a Gantt and a network diagram are three views of
the same project, and if they disagree the team gets confused about which one is
true.

### Work breakdown structure

Decomposed the year into tangible tasks and assigned responsibility across the
specialisms within the team.

![Work breakdown structure](../figures/pm/work-breakdown-structure.png)

### Gantt chart

A calendar view of durations, dependencies and deadlines, giving early sight of
bottlenecks. It was maintained as a live document across the year.

![Full year Gantt chart](../figures/pm/gantt-full-year.png)

For the design and build phase (weeks 7–17) it was refined substantially:
tasks broken down to a feasible granularity, **slack deliberately built in**,
and — importantly — **tasks assigned to named individuals** rather than to the
team collectively.

![Design and build phase Gantt](../figures/pm/gantt-design-build-phase.png)

*Phase 3–6 detail with hour estimates per task. Assigning tasks to individuals
was the single most effective change made to the plan all year.*

### Activity-on-node network diagram

Mapped the interdependencies and identified the **critical path**.

![Team network diagram](../figures/pm/network-diagram-team.png)

At company level, the Design Team Managers built **divisional** network diagrams
capturing dependencies across teams within a division.

![Company fuselage division network diagram](../figures/pm/network-diagram-company.png)

These divisional documents were the mechanism linking team objectives to company
objectives — the layer that was otherwise missing.

---

## Critical path versus reality

This is the most instructive number in the whole project management effort:

| | Hours |
|---|---|
| Critical path prediction | **48** |
| Lab hours actually clocked | **105** |
| | *plus all work done outside the lab* |

**The plan was out by more than a factor of two.** Not because the task
estimates were bad — because the network diagram modelled the *wrong
dependencies*.

The diagram captured dependencies **within Team 08**. It did not capture the
dependency that actually governed the schedule: Team 08's tasks waiting on
**other teams' designs**. A joint cannot be dimensioned until the spar it holds
is dimensioned. That dependency is invisible on a team-level AoN diagram, and it
was the binding constraint all year.

The float analysis inherited the same blind spot. Internal tasks were correctly
sorted into "can slip" and "cannot slip". Neither category anticipated an
external change forcing a completed task to be redone.

**The lesson generalises well beyond this project.** For a team sitting
downstream of six others, a plan that models only its own internal dependencies
is not a schedule — it is a best case that assumes the rest of the world holds
still.

---

## Team integration into the company

Team 08's designs depended on measurements and fittings from other teams across
the fuselage and wing divisions, which made the phase *after* the Gate 3 design
freeze unexpectedly difficult.

The pattern was sharp and consistent:

- **Main wing joint and clamps** — counterpart geometry fixed early → almost no
  revision, easy updates
- **Empennage joint** — HTP, VTP and avionics dimensions arrived late, some
  after design freeze → repeated redesign

The team's conclusion was that **proactive engagement beat passive information
acquisition**, decisively. Waiting to be told a dimension meant learning it in a
lab session, weeks after it was needed.

A structural observation also came out of this: given how many subassemblies
depended on Team 08's parts, describing the team as sitting *within* the
fuselage division understated its role. Its actual position was
**inter-divisional**.

### Design freeze

As Design Team Manager I imposed a **company-wide design freeze**. It was
necessary — some teams, notably VTP, were still finalising after Gate 3, which
meant Team 08 was still redesigning interfaces to parts that were supposed to be
settled.

It should have come earlier. By the time it was enforced, much of the rework it
was meant to prevent had already happened.

---

## Risk management

A full risk assessment was completed for Gate 1 and maintained as a **live
document** — matters more than it sounds, since a risk register written once and
filed is an artefact rather than a tool.

![Risk register](../figures/pm/risk-register.png)

*Pre- and post-mitigation risk numbers with owners and dates. Entries carry
author initials and the date raised.*

![Risk rating matrix](../figures/pm/risk-rating-matrix.png)

Risks were scored on frequency × consequence, giving a risk number used to
prioritise effort. The register drove two concrete behaviours that paid off:
mandatory attendance at lab inductions and specialist lectures, and a habit of
asking lab technicians directly when something was uncertain.

### What the register caught

Equipment damage and scheduling were correctly identified as the dominant risk
categories. Risk 3 — damage to the wind tunnel during testing — was mitigated
by emphasising secure attachment procedures, and no tunnel damage occurred.

### What it missed, and why

**3D printing failures.** Not anticipated at all, because nobody on the team had
enough experience with additive manufacture to know what its failure modes look
like. This is a structural weakness of risk assessment done by novices: **you
cannot enumerate risks in a process you have not used.**

**Poor fairing assembly during structural testing.** The register assumed
thorough familiarity with assembly procedures. In the event, the team member
present at the test was the only one who had missed the practice assembly. The
register recorded an *assumption* about team knowledge rather than a *mechanism*
for ensuring it.

**Mitigations that were too vague to act on.** Several entries lacked the
specificity to be useful under time pressure. "Ensure correct assembly" is not a
mitigation; "verify clamp part number against the test configuration sheet
before loading" is. The clamp that failed at the load test is precisely the case
a specific mitigation would have caught.

**Scheduling risk was under-weighted.** The register leaned heavily toward
damage-to-property risks. Scheduling was the risk that actually materialised,
repeatedly and expensively.

### Company-level failures

Limited cross-team communication on technical issues produced late-stage
surprises: delays finishing the full-company CAD assembly led to **mismatched
dimensions during physical assembly**, difficulty fitting payload rings to
fairings, and a **misaligned centre of mass** that forced further revision.
Continued design changes after Gate 3, combined with poorly coordinated slack
between teams, stretched the timeline directly.

---

## What I would change

**Model external dependencies explicitly.** Flag on the Gantt and the network
diagram every internal task that depends on another subassembly, and treat those
as the critical path they actually are. This alone would have closed most of the
48 vs 105 hour gap.

**Treat PM documents as team tools, not deliverables.** They were produced,
submitted, and then under-used. Discussed weekly, they would have driven
behaviour instead of documenting it.

**More milestones than just the gates.** The gates were the only formal feedback
points, so problems surfaced at intervals of months. Intermediate milestones
would have shortened that loop.

**Build the risk register with people who have done it before.** Lab technicians
and students from the year above have seen the failure modes this team could not
imagine. The 3D printing gap was entirely foreseeable by someone with printing
experience.

**Add a financial dimension.** Real engineering is driven by cost. An internal
currency — buying lab hours, paying for print time — would force the trades that
were instead made implicitly. The fairings would not have been printed in PLA if
print time had a price attached.

**Use a live collaborative platform.** A shared tracker with cross-divisional
dependency visibility, and simple traffic-light status reporting, would have made
inter-team blockages visible while they could still be acted on. A Kanban board
did serve this purpose for part of the year and worked well while it was
maintained; it lapsed when the directors stopped posting, and cross-team
communication degraded with it.

---

[← Test campaign](07-test-campaign.md) · [Next: Lessons learned →](09-lessons-learned.md)
