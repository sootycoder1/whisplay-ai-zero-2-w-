# ============================================================
# WHISPLAY ASSISTANT FAULTS
# STAGE 530 — DIAGNOSTIC FAULT CLASSIFICATION CANDIDATE
# ============================================================

from copy import deepcopy
from time import time

import assistant_diagnostics_STAGE520_LOCKED as diagnostics


ENGINE_NAME = "assistant_faults"
ENGINE_STAGE = 530
ENGINE_VERSION = "530.0-candidate"


FAULT_TYPES = {
    "stage_mismatch",
    "missing_engine",
    "missing_interface",
    "runtime_failure",
    "unknown_failure",
}


STATE = {
    "classifications": 0,
    "healthy_results": 0,
    "fault_results": 0,
    "faults_found": 0,
    "last_result": "",
    "updated": 0.0,
}


def now():
    return time()


def snapshot():
    return deepcopy(STATE)


def classify_module(module):
    name = str(module.get("name") or "")
    engine = module.get("engine")
    expected_stage = module.get("expected_stage")
    actual_stage = module.get("actual_stage")
    interface_ok = module.get("interface_ok") is True
    required_callable = str(
        module.get("required_callable") or ""
    )

    faults = []

    if not engine:
        faults.append({
            "type": "missing_engine",
            "module": name,
            "location": f"{name} module metadata",
            "expected": "ENGINE_NAME value",
            "actual": engine,
            "recovery_target": (
                f"Inspect the locked {name} module header."
            ),
            "message": (
                f"{name} has no engine metadata."
            ),
        })

    if actual_stage != expected_stage:
        faults.append({
            "type": "stage_mismatch",
            "module": name,
            "location": f"{name} module stage metadata",
            "expected": expected_stage,
            "actual": actual_stage,
            "expected_stage": expected_stage,
            "actual_stage": actual_stage,
            "recovery_target": (
                f"Check the imported {name} file and its "
                "ENGINE_STAGE value."
            ),
            "message": (
                f"{name} expected stage {expected_stage} "
                f"but reported {actual_stage}."
            ),
        })

    if not interface_ok:
        faults.append({
            "type": "missing_interface",
            "module": name,
            "location": f"{name} public interface",
            "expected": required_callable,
            "actual": "missing or not callable",
            "required_callable": required_callable,
            "recovery_target": (
                f"Inspect the {name} module for the required "
                f"{required_callable} function."
            ),
            "message": (
                f"{name} is missing required callable "
                f"{required_callable}."
            ),
        })

    if not faults and module.get("ok") is not True:
        faults.append({
            "type": "unknown_failure",
            "module": name,
            "location": f"{name} health result",
            "expected": "module health PASS",
            "actual": "module health FAIL",
            "recovery_target": (
                f"Inspect Stage 510 health output for {name}."
            ),
            "message": (
                f"{name} failed for an unknown reason."
            ),
        })

    return faults


def classify_report(report=None):
    STATE["classifications"] += 1
    STATE["updated"] = now()

    source = (
        deepcopy(report)
        if isinstance(report, dict)
        else diagnostics.build_report()
    )

    faults = []

    for module in source.get("modules", []):
        faults.extend(classify_module(module))

    runtime_state = source.get("runtime_state") or {}

    if source.get("ok") is not True and not faults:
        faults.append({
            "type": "runtime_failure",
            "module": "runtime",
            "last_operation": runtime_state.get(
                "last_operation",
                "",
            ),
            "last_result": runtime_state.get(
                "last_result",
                "",
            ),
            "location": "Stage 500 runtime active state",
            "expected": "valid active actor and healthy runtime",
            "actual": {
                "last_operation": runtime_state.get(
                    "last_operation",
                    "",
                ),
                "last_result": runtime_state.get(
                    "last_result",
                    "",
                ),
            },
            "recovery_target": (
                "Inspect Stage 500 runtime, active actor, "
                "and Stage 510 runtime health result."
            ),
            "message": "Runtime health failed.",
        })

    valid_faults = all(
        fault.get("type") in FAULT_TYPES
        for fault in faults
    )

    healthy = (
        source.get("ok") is True
        and not faults
        and valid_faults
    )

    if healthy:
        STATE["healthy_results"] += 1
        STATE["last_result"] = "healthy"
    else:
        STATE["fault_results"] += 1
        STATE["faults_found"] += len(faults)
        STATE["last_result"] = "faults_classified"

    return {
        "ok": healthy,
        "source_ok": source.get("ok") is True,
        "fault_count": len(faults),
        "faults": faults,
        "failed_modules": deepcopy(
            source.get("failed_modules", [])
        ),
        "active_actor": deepcopy(
            source.get("active_actor", {})
        ),
        "state": snapshot(),
    }


def readable_faults(report=None):
    result = classify_report(report)

    if result["ok"]:
        return "No multi-actor runtime faults detected."

    lines = [
        "WHISPLAY MULTI-ACTOR FAULTS",
        f"Fault count: {result['fault_count']}",
    ]

    for fault in result["faults"]:
        lines.append(
            f"- {fault['type']}: {fault['message']}"
        )
        lines.append(
            f"  Location: {fault.get('location', 'unknown')}"
        )
        lines.append(
            f"  Expected: {fault.get('expected', 'unknown')}"
        )
        lines.append(
            f"  Actual: {fault.get('actual', 'unknown')}"
        )
        lines.append(
            "  Recovery target: "
            f"{fault.get('recovery_target', 'manual inspection')}"
        )

    return "\n".join(lines)


def status():
    return {
        "engine": ENGINE_NAME,
        "stage": ENGINE_STAGE,
        "version": ENGINE_VERSION,
        "fault_types": sorted(FAULT_TYPES),
        "state": snapshot(),
    }
