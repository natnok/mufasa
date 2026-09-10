from typing import ClassVar

from src.config import settings


class CeleryConfig:
    broker_url = settings.REDIS_URL.unicode_string()
    imports = "src.tasks.tasks"
    timezone = "UTC"
    enable_utc = True

    beat_schedule: ClassVar = {
        "luboe_nazvanie": {
            "task": "beat_task",
            "schedule": 5,
        },
    }
