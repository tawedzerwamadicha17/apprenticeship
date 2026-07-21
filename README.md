# Apprenticeship

A Frappe app that sits **on top of** the Education app to turn it into an
apprenticeship training and workplace-assessment system, without modifying
Education's own code (so future `bench update` on Education stays safe).

## What this gives you

**Rebranding (via Translation fixtures, no code touched in Education):**
- Student → Apprentice
- Instructor → Trainer / Assessor
- Program → Apprenticeship Programme
- Course → Training Module
- Student Group → Cohort

**New doctypes:**
- **Workplace** — the employer/site where an apprentice trains
- **Trainer Assignment** — links an Apprentice ↔ Trainer/Assessor ↔ Workplace, with start/end dates
- **Competency** — a skill/task tied to a Training Module (Course) that an apprentice must be signed off on
- **Practical Assessment** (submittable) — the on-the-job assessment record:
  - Apprentice, Competency, Workplace, Assessor, date, outcome (Competent / Not Yet Competent / Competent with Gaps)
  - Assessor comments + apprentice reflection
  - **Evidence table** for uploading photos, videos, or documents as proof of competent performance
  - Assessor sign-off checkbox (auto-stamps date/time) + apprentice acknowledgement checkbox
  - Won't let you submit until the assessor has signed off

Everything from Education still works as-is: Program, Course, Student, Instructor,
Student Group, Assessment Plan / Assessment Criteria / Assessment Result, Quiz —
this app just adds the workplace layer on top and relabels what's shown.

## Installation (on your existing bench)

```bash
# 1. Copy this app into your bench's apps folder, e.g.:
cp -r apprenticeship /path/to/frappe-bench/apps/

# 2. From your bench root:
bench setup requirements
bench --site your-site.local install-app apprenticeship

# 3. This also runs fixtures automatically, but if you add/edit translations later:
bench --site your-site.local migrate
```

If your bench uses git apps normally, push this folder to its own git repo first
and use `bench get-app <repo-url>` instead of copying — that's the more
maintainable route long-term.

## Apprentice self-login (built)

Apprentices log in themselves through the **portal**, not the desk (no
`desk_access`, so they never see the full backend).

How it's wired:
1. Each **Student** record has a **User ID** field (already in Education).
   Set it to the apprentice's login/User.
2. The moment that Student record is saved, this app automatically:
   - adds the **Apprentice** role to that user
   - creates a **User Permission** scoping that user to their own Student
     record — which Frappe then applies automatically to anything linking
     back to Student (Practical Assessment, Trainer Assignment), so an
     apprentice only ever sees their own records.
3. The apprentice logs in and visits `/my-practical-assessments` — a portal
   page (Web Form) listing their assessments. There they can:
   - read the assessor's comments and outcome (read-only)
   - add their own **evidence** (photos/videos of the work, e.g. taken on
     site) — these permlevel-1 fields are the only fields they can edit
   - add their own reflection comments
   - tick **"I acknowledge this assessment"** once they've read it

## Approval workflow (built)

`Practical Assessment` now has a workflow instead of a single submit button:

```
Draft --(Submit for Review)--> Awaiting Review --(Review)--> Reviewed --(Sign Off)--> Signed Off
                                       |
                                  (Send Back)
                                       v
                                    Draft
```

- **Draft / Awaiting Review**: editable by the **Instructor** (Trainer/Assessor)
  who did the on-the-job observation.
- **Reviewed to Signed Off**: actioned by an **Education Manager**, who has the
  final say. Only the "Sign Off" transition actually submits the document
  (`docstatus = 1`) - the existing rule that the assessor must have ticked
  "Assessor Confirms Outcome" still applies before that can happen.
- The apprentice's own acknowledgement (`apprentice_signed`) is separate from
  this workflow - they can tick it any time via the portal, independent of
  where the record sits in Draft to Signed Off.

If your process needs different roles at each step (e.g. a dedicated
"Quality Assessor" role rather than reusing Education Manager), tell me and
I'll adjust the workflow fixture - it's a straightforward JSON edit.

## New in this update

- **Apprentice Competency Progress report** (Reports > Apprenticeship) — one
  row per apprentice: how many mandatory Competencies are signed off with a
  "Competent" outcome vs outstanding, with a % complete column. Filter by
  apprentice or Training Module.
- **Print Format: "Practical Assessment Sign-off"** — a clean printable/PDF
  record of a single assessment (outcome, comments, evidence list, both
  sign-off timestamps) for paper files or emailing to an employer.
- **Email notifications** on the workflow: the Education Manager is notified
  when something reaches "Awaiting Review"; the assessor is notified if it's
  "Sent Back"; both the assessor and the apprentice (via their portal login)
  are notified — with the print format attached — once it's "Signed Off".
- **Trainer Assignment Tool** (bulk tool, under the Apprenticeship module) —
  pick a Cohort (Student Group) or an Apprenticeship Programme, pick a
  Trainer/Assessor and Workplace, and create Trainer Assignment records for
  every apprentice in one go instead of one at a time. It flags anyone who
  already has an active assignment with that trainer/workplace so you don't
  duplicate.

## Suggested next steps (not yet built, happy to add)

1. **Bulk-create Practical Assessments** — pre-populate a batch of assessments
   for a cohort against a set of Competencies (e.g. at the start of a training block).
2. **Dashboard/workspace** — a home page with charts (outcomes this month,
   apprentices nearing completion, overdue assessments).
3. **Reminder emails** for apprentices who haven't acknowledged a Signed Off
   assessment after some days.
4. **Split the workflow's reviewer role** — right now "Reviewed → Signed Off"
   both use Education Manager; say the word if you want a distinct
   "Quality Assessor" role instead.

Tell me which of these matter most and I'll build them next.
