"""
Norwegian Government-issued IDs:
  - Fodselsnummer
"""

import re

from typing import Iterable

from stdnum.no import fodselsnummer

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for FO
_FO_PATTERN = r"\b\d{11}\b"


class NorwegianFO(BasePiiTask):
    """
    Norwegian Government-issued FO numbers, recognize & validate
    """

    pii_name = "Norwegian FO"


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.fo_pattern = re.compile(_FO_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # FO
        for item in self.fo_pattern.finditer(doc):
            item_value = item.group()
            if fodselsnummer.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Norwegian FO",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, NorwegianFO)]