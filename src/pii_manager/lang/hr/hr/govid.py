"""
Croatian Government-issued IDs:
  - OIB (Osobni identifikacijski broj)
"""

import re

from typing import Iterable

from stdnum.hr import oib

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for OIB
_OIB_PATTERN = r"\b\d{11}\b"


class CroatianOIB(BasePiiTask):
    """
    Croatian Government-issued OIB numbers, recognize & validate
    """

    pii_name = "Croatian OIB"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.oib_pattern = re.compile(_OIB_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # OIB
        for item in self.oib_pattern.finditer(doc):
            item_value = item.group()
            if oib.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Croatian OIB",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, CroatianOIB)]