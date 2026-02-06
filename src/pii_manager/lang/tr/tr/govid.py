"""
Turkish Government-issued IDs:
  - TC (T.C. Kimlik No)
"""

import re

from typing import Iterable

from stdnum.tr import tckimlik

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for TC
_TC_PATTERN = r"\b[1-9]\d{10}\b"


class TurkishTC(BasePiiTask):
    """
    Turkish Government-issued TC numbers, recognize & validate
    """

    pii_name = "Turkish TC"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.tc_pattern = re.compile(_TC_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # TC
        for item in self.tc_pattern.finditer(doc):
            item_value = item.group()
            if tckimlik.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Turkish TC",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, TurkishTC)]