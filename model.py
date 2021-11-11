from datetime import datetime, date
from typing import Optional
from uuid import uuid4, UUID

from pynamodb.models import Model
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute,
)


class Baby(Model):
    class Meta:
        table_name = 'Baby'
        region = 'us-east-1'

    id: UUID = UnicodeAttribute(hash_key=True, default_for_new=uuid4)

    class FirstNameIndex(GlobalSecondaryIndex):
        class Meta:
            projection = AllProjection()
            first_name = UnicodeAttribute(hash_key=True)

    first_name: str = UnicodeAttribute()
    first_name_index = FirstNameIndex()
    birthdate: Optional[date] = UTCDateTimeAttribute(null=True)

    def __str__(self):
        return self.first_name


class FeedingEvent(Model):
    class Meta:
        table_name = 'BabyEvent'
        region = 'us-east-1'

    baby_id: int = UnicodeAttribute(hash_key=True, attr_name='BabyId')
    start_datetime: datetime = UTCDateTimeAttribute(
        range_key=True, default_for_new=datetime.utcnow, attr_name='StartDateTime',
    )
    type = UnicodeAttribute(default='feeding')

    meal_type: str = UnicodeAttribute(null=True)
    end_datetime: datetime = UTCDateTimeAttribute(null=True)
    quantity: Optional[str] = UnicodeAttribute(null=True)
    notes: Optional[str] = UnicodeAttribute(null=True)

    def __str__(self):
        return f'{self.start_datetime} - {self.type}'


