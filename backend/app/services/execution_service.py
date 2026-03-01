"""Execution engine isolated from business logic.

Provides helpers to load test cases, run code with a timeout,
compare outputs and run full execution against a problem's tests.

Notes:
- This implementation supports Python execution via a temporary file.
- Execution layer performs NO DB writes. It may read test cases.
"""

from __future__ import annotations

import time
import subprocess
import tempfile
from typing import Dict, List
from app.models.test_case import TestCase


def load_test_cases(db, problem_id: int) -> List[TestCase]:
    return db.query(TestCase).filter(TestCase.problem_id == problem_id).all()


def _normalize(text: str) -> str:
    if text is None:
        return ""
    # Normalize whitespace and line endings
    lines = [ln.strip() for ln in text.strip().splitlines() if ln.strip()]
    return "\n".join(lines)


def run_code_with_timeout(code: str, input_data: str = "", timeout_seconds: int = 3, language: str = "python") -> Dict:
    start = time.time()
    if language.lower() != "python":
        # For unsupported languages, return runtime_error stub
        return {"status": "runtime_error", "stdout": "", "stderr": f"language {language} not supported", "execution_time_ms": 0}

    try:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(code)
            fname = f.name

        proc = subprocess.run(
            ["python", fname],
            input=input_data.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout_seconds,
        )

        exec_time = int((time.time() - start) * 1000)
        stdout = proc.stdout.decode("utf-8", errors="ignore")
        stderr = proc.stderr.decode("utf-8", errors="ignore")

        status = "passed" if proc.returncode == 0 else "runtime_error"

        return {"status": status, "stdout": stdout, "stderr": stderr, "execution_time_ms": exec_time}

    except subprocess.TimeoutExpired as e:
        exec_time = int((time.time() - start) * 1000)
        return {"status": "runtime_error", "stdout": "", "stderr": "timeout", "execution_time_ms": exec_time}


def compare_output(actual: str, expected: str) -> bool:
    return _normalize(actual) == _normalize(expected)


def execute_code(db, problem_id: int, code: str, language: str = "python", timeout_seconds: int = 3) -> Dict:
    """Execute `code` against all test cases for `problem_id`.

    Returns a dict with keys: status, score, execution_time_ms
    status is one of: passed, failed, runtime_error
    """
    test_cases = load_test_cases(db, problem_id)
    if not test_cases:
        return {"status": "failed", "score": 0.0, "execution_time_ms": 0, "details": []}

    total = len(test_cases)
    passed = 0
    total_time = 0
    details = []

    for tc in test_cases:
        res = run_code_with_timeout(code, tc.input_data or "", timeout_seconds, language)
        total_time += int(res.get("execution_time_ms", 0) or 0)
        if res["status"] == "runtime_error":
            details.append({"test_case_id": tc.id, "status": "runtime_error", "stderr": res.get("stderr")})
            # runtime error short-circuits: mark as runtime_error
            return {"status": "runtime_error", "score": 0.0, "execution_time_ms": total_time, "details": details}

        ok = compare_output(res.get("stdout", ""), tc.expected_output)
        if ok:
            passed += 1
            details.append({"test_case_id": tc.id, "status": "passed"})
        else:
            details.append({"test_case_id": tc.id, "status": "failed", "expected": tc.expected_output, "actual": res.get("stdout", "")})

    score = float(passed) / float(total) if total > 0 else 0.0
    status = "passed" if passed == total else "failed"

    return {"status": status, "score": score, "execution_time_ms": total_time, "details": details}
