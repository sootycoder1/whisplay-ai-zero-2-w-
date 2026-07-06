# WHISPLAY STAGE 590 — MASTER RECOVERY MAP

Status: CANDIDATE
Purpose: Authoritative recovery map for the entire Whisplay build after disaster.
Rule: This is not a runtime recovery module.
Rule: This file exists so recovery does not rely on memory.

## 1. Recovery Stack Position

Stage 500–580 created the controlled recovery stack.

- Stage 500: recovery foundation
- Stage 510: recovery state structure
- Stage 520: recovery snapshot/checkpoint logic
- Stage 530: recovery rollback/restore logic
- Stage 540: recovery execution boundary
- Stage 550: recovery guard / safe limitation layer
- Stage 560: recovery policy and anti-loop guard
- Stage 570: recovery plan lock
- Stage 580: recovery verification

Stage 590 is the Master Recovery Map.

It explains how to recover the whole Whisplay build, not just one failed AI action.

## 2. Core Principle

The recovery system is not only for recovering the assistant.

It is for recovering the entire Whisplay build after:

- broken code
- bad edits
- failed stage changes
- SD card failure
- lost files
- corrupted runtime
- incorrect recovery attempts
- forgotten architecture
- wrong startup path
- broken controller / brain / memory / display / audio integration

## 3. Authority Rule

This map is the recovery authority.

Future recovery should follow this file before relying on memory, assumptions, or chat history.

## 4. No GitHub Push Rule

No GitHub push is allowed until Stage 610 is finished and locked.

Until then:

- local commits only
- no git push
- no GitHub sync
- no remote overwrite
- no broad git add .
- hard-copy backup comes after the complete recovery stack

## 5. Recovery Order

When recovering Whisplay, restore and verify in this order:

1. Operating system boots
2. User and project path exist
3. whisplay-ai folder exists
4. Git repository exists
5. Local commits are present
6. Python virtual environment works
7. Runtime contract loads
8. Runtime bus loads
9. State core loads
10. Brain loads
11. Controller loads
12. Display layer loads
13. Audio output works
14. Speech input path works
15. Memory/context modules load
16. Recovery stack loads
17. Recovery verification passes
18. Live runtime starts only after safe checks

## 6. Protected Runtime Files

The known protected Whisplay runtime files include:

- system_controller_STAGE12010_DEV_MIC.py
- state_core.py
- runtime_contract_STAGE6000.py
- runtime_bus_STAGE7000.py
- brain/brain_cognitive_STAGE150_MERGED.py
- context_manager_STAGE6500.py
- memory_engine_STAGE7500.py
- goal_engine_STAGE8000.py
- reasoning_engine_STAGE8500.py
- adapter_manager_STAGE9000.py
- display_orchestrator_STAGE9550_RECOVERED.py
- persistent_speech_worker_STAGE10500.py
- analysis_core_STAGE11500.py
- speak.py

## 7. Recovery Stack Files

The Stage 500–580 recovery files are locally committed and must be preserved.

Stage 590 maps them.

Stage 600 and Stage 610 complete the recovery stack before hard-copy backup and GitHub push.

## 8. Disaster Recovery Rule

If the build is damaged, do not start by editing live runtime files.

Start by checking:

1. Git status
2. Recent commits
3. Locked stage files
4. Recovery map
5. Recovery verification output
6. Backups
7. Runtime compile state

## 9. Forbidden Recovery Mistakes

Do not:

- push to GitHub before Stage 610
- run git add .
- overwrite locked files casually
- delete untracked files without review
- recover from memory only
- edit the controller first without knowing the failure point
- allow recovery logic to execute hardware actions
- allow recursive recovery loops
- repeat the same failed recovery attempt endlessly

## 10. Stage 590 Verdict

Stage 590 defines the recovery architecture.

It is the master map for restoring Whisplay as a whole system.

