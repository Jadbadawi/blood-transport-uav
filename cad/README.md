# CAD Repository

Autodesk Inventor 2024 native files for the complete Albatross Aviation UAV, as
frozen at the end-of-project data repository freeze.

> **Opening the model.** Open `Full Assembly (1)/FullAssembly (1).iam`. The
> assembly resolves its children by *relative* path, so the folder structure
> below must be kept intact — moving or renaming subfolders will break the
> references. If Inventor asks to resolve a missing link, point it at the
> `Full Assembly (1)` directory.

---

## What is in here, and who drew it

This was a 60-student company split into subassembly teams. **Team 08 (Joints &
Fairings) authored the `JointsAndFairings` tree** — that is the work this
portfolio documents. The remaining trees are the other teams' subassemblies,
included because the top-level assembly will not open without them and because
integrating them into a single resolvable model was itself one of Team 08's
contributions.

| Path | Subassembly | Authored by |
|---|---|---|
| `Full Assembly (1)/JointsAndFairings/` | **Joints, clamps, fairings** | **Team 08 — this team** |
| `Full Assembly (1)/FullAssembly (1).iam` | Top-level integration assembly | Team 08 (assembled) |
| `Full Assembly (1)/P Wing/` | Port wing, flap, aileron | Port wing team |
| `Full Assembly (1)/S Wing/` | Starboard wing | Starboard wing team |
| `Full Assembly (1)/S Flap and Aileron/` | Starboard control surfaces | Starboard wing team |
| `Full Assembly (1)/HTP&elevator/` | Horizontal tailplane, elevator | Empennage team |
| `Full Assembly (1)/VTP/` | Vertical tailplane | Empennage team |
| `Full Assembly (1)/Pod/` | Payload pod, rings, nose/rear cones | Pod team |

`A-Fus Wind Tunnel Test Plan.pdf` and `Full Assembly (1)/VTP/Drawings/` are the
issued test plan and a sample of the formal 2D drawing set.

---

## Team 08 part index

Ten parts went onto the flying article. Files live under
`Full Assembly (1)/JointsAndFairings/`.

### Joints and clamps

| Part | File | Material | Mass |
|---|---|---|---|
| Fus-MWP joint | `Joints/8P - MainWing Joint.ipt` | PLA + 2014A-T3 strap | 68.2 g |
| Fus-MWP joint clamp (×2) | `Joints/8P-MainWingJoint Clamp.ipt` | PLA | 25.3 g ea. |
| Aluminium bearing strap | `Aluminum Sheet.ipt` | 2014A-T3 sheet | 12.3 g |
| Emp-Fus joint, top + bottom | `Joints/Final emp joint.ipt` | PLA + brass inserts | 43.7 / 42.9 g |
| Emp-Fus clamp (servo housing) | `Joints/updated emp clamp for servo.ipt` | PLA | 32.9 g |

### Fairings

| Part | File | Material | Mass |
|---|---|---|---|
| Fus-MWP fairing (2 halves, printed in 4) | `Port/8P_PortFairing.ipt`, `StarBoard/8P_001_StarboardFairingFinal.ipt` | PLA | 300 g ea. |
| Hemispherical nose cone fairing | `NoseCone Fairing/noseconefairing.ipt` | PLA | 38.6 g |
| Shell fairings (×2) — front payload ring and fuselage | `FrontRingFairing.ipt`, `Fuselage JF.ipt` | PLA | 51.6 g ea. |
| FRF (false rear spar) attachment | integrated into the main fairing | PLA | — |

The published mass table records the two shell fairings as a single line item at
51.6 g each; it does not distinguish which is which, so they are grouped here.

Full mass breakdown, including fasteners:
[`analysis/data/subassembly_mass.csv`](../analysis/data/subassembly_mass.csv).

---

## Part numbering convention

The company used a positional scheme. Team 08's parts carry the `8` prefix:

```
8P - MainWing Joint          8  P    - <descriptive name>
                             │  └── P = part, A = assembly, D = drawing, JF = joints/fairings
                             └───── originating team number (08)
```

Other teams used a fuller dotted form, e.g.
`1P.01.01.01-HB-Rib1` → team 01, part, assembly 01, sub 01, item 01, author
initials `HB`. The inconsistency between the two schemes is one of the
configuration-management lessons recorded in
[`docs/09-lessons-learned.md`](../docs/09-lessons-learned.md).

---

## What was removed before publishing

- **`OldVersions/` directories** (26 folders, 207 files) — Inventor's automatic
  backup copies. No design intent lives in them.
- **A duplicated nested `JointsAndFairinsg (1)/` tree** — an artefact of the
  mid-project CAD rebuild described in
  [`docs/06-manufacturing-and-integration.md`](../docs/06-manufacturing-and-integration.md),
  where the same parts appeared three levels deep.

535 files and 178 MB remain. Nothing that the top-level assembly references was
removed.
