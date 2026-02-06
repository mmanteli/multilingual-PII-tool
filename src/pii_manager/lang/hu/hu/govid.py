"""
Hungarian Government-issued IDs:
  - TAJ (Társadalombiztosítási Azonosító Jel)
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for TAJ
_TAJ_PATTERN = r"\b\d{3}\s?\d{3}\s?\d{3}\b"


class HungarianTAJ(BasePiiTask):
    """
    Hungarian Government-issued TAJ numbers, recognize & validate
    """

    pii_name = "Hungarian TAJ"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.taj_pattern = re.compile(_TAJ_PATTERN, flags=re.X)

    def validate(self, taj: str) -> bool:
        if len(taj) != 9 or not taj.isdigit():
            return False

        digits = [int(d) for d in taj]
        suma = 0
        for i in range(8):
            if i % 2 == 0:
                suma += digits[i] * 3
            else:
                suma += digits[i] * 7
        control = suma % 10
        return control == digits[-1]


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # TAJ
        for item in self.taj_pattern.finditer(doc):
            item_value = item.group()
            if self.validate(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Hungarian TAJ",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, HungarianTAJ)]