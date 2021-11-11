from datetime import datetime, timezone
from typing import Optional

import humanize

from model import Baby, FeedingEvent


def new_feeding(
        baby_name: str = 'Charlotte',
        end_datetime: Optional[datetime] = None,
        meal_type: Optional[str] = None,
        quantity: Optional[float] = None,
        notes: Optional[str] = None,
) -> tuple[str, Optional[str]]:
    baby = Baby.first_name_index.query(baby_name).next()

    event = FeedingEvent(
        hash_key=baby.id,
        end_datetime=end_datetime,
        meal_type=meal_type,
        quantity=quantity,
        notes=notes,
    )
    event.save()
    return f"Ok, I wrote down {baby.first_name}'s feeding!", None


def last_feeding(baby_name: str = 'Charlotte') -> tuple[str, Optional[str]]:
    baby = Baby.first_name_index.query(baby_name).next()
    most_recent = FeedingEvent.query(baby.id, scan_index_forward=True).next()
    humanized_last_time = humanize.naturaltime(datetime.now(timezone.utc) - most_recent.start_datetime)
    return f"{baby.first_name} last ate {humanized_last_time}.", None
