"""Machine Learning service.

Provides a non-blocking trigger to send submission events to an external ML microservice.
The call is fire-and-forget from the submission path and failures are logged.
"""

from __future__ import annotations

import asyncio
import httpx
import threading
from typing import Dict
from app.core import config


async def _post_ml_event(payload: Dict) -> None:
    url = getattr(config, "ML_ENDPOINT", None) or "http://localhost:9100/events"
    async with httpx.AsyncClient(timeout=5.0) as client:
        await client.post(url, json=payload)


def trigger_ml_event(payload: Dict) -> None:
    """Trigger an async ML event without blocking request flow.

    Runs the async HTTP call in a background thread.
    """

    def _runner(p: Dict):
        try:
            asyncio.run(_post_ml_event(p))
        except Exception as exc:
            # Log failure safely; do not propagate
            try:
                import logging

                logging.exception("ML event failed: %s", exc)
            except Exception:
                pass

    thread = threading.Thread(target=_runner, args=(payload,), daemon=True)
    thread.start()

