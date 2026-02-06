"""
Polish Government-issued IDs:
  - PESEL (Powszechny Elektroniczny System Ewidencji Ludności)
"""

import re

from typing import Iterable

from stdnum.pl import pesel

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for PESEL
_PESEL_PATTERN = r"\b\d{11}\b"



class PolishPESEL(BasePiiTask):
    """
    Polish Government-issued PESEL numbers, recognize & validate
    """

    pii_name = "Polish PESEL"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.pesel_pattern = re.compile(_PESEL_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # PESEL
        for item in self.pesel_pattern.finditer(doc):
            item_value = item.group()
            if pesel.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Polish PESEL",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, PolishPESEL)]