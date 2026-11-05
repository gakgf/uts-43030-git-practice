# UTS 43030 Git practical activities

Course practical implementations for Lectures 1-4. Existing feature HTML pages are retained.

- Lecture 1: existing Git history plus isolated `practicals/lecture1-*` branches.
- Lecture 2: `.github/workflows/main.yml` updates HTML and records the actual actor, UTC time and source SHA here.
- Lecture 3: `practicals/lecture3/` contains a Docker vowel analyzer and a reusable Docker action.
- Lecture 4: `practicals/lecture4/` contains the task manager, unit tests and HTML report generator. `.github/workflows/ci.yml` runs both Docker exercises and commits generated reports on main.
- Projects: `tracker.yml` records linked issue closure; a Projects built-in workflow moves closed issues to Done. This avoids storing a broad Projects PAT in this repository.

## Reproduction

```sh
docker build -t vowel-frequency-analyzer:latest practicals/lecture3
docker run --rm -v "$PWD:/workspace" -w /workspace -e FILE=practicals/lecture3/data.txt -e README_PATH=practicals/lecture3/README.md -e GITHUB_USER=YOUR_LOGIN vowel-frequency-analyzer:latest
docker build -t task-manager:latest practicals/lecture4
docker run --rm -v "$PWD:/workspace" -w /workspace -e REPORT_PATH=practicals/lecture4/index.html task-manager:latest
```

The container writes only its designated report in the mounted checkout. Git commits happen in the workflow after successful execution. Unit test failures propagate and prevent publishing a successful report.

## Implementation provenance and differences from slides

Code is an implementation of the supplied activity descriptions assisted by Codex. Canvas starter scripts were not supplied at initial implementation. No additional team members or reviews are represented by these files.

Both Docker exercises have separate build contexts so their Dockerfiles, entrypoints and reports coexist. Python 3.13 and checkout v6 replace the older slide examples. The Lecture 3 action builds its local Dockerfile rather than assuming an unavailable pre-published GHCR image. Publishing and testing a GHCR-hosted variant remains a separate extension if required by the assessor.

Only overlapping edits cause merge/rebase conflicts. Editing different files by different members alone does not guarantee a conflict. Reset/rebase demonstrations use isolated unpublished branches, keeping main history intact. No old feature branches are deleted.

Workflow write access is limited to report-publishing jobs. Pull-request jobs only read contents. Report commits stage explicit output paths and never force push. All report writers share one concurrency group. Built-in GITHUB_TOKEN pushes do not recursively launch the same workflows.

## Activity log

### Updated by gakgf on 2026-11-05 14:55:23 UTC [Commit: 3cbdfa13f6435ee8711f7105cb597f5209b77d73]

### Updated by gakgf on 2026-11-05 14:59:01 UTC [Commit: 594fac875abcacca28e0785c4351d1b8d4fa5239]

### Updated by gakgf on 2026-11-05 15:02:33 UTC [Commit: bebaa82a4b5ee7f798dbae24c2767bd24e35fb6f]
