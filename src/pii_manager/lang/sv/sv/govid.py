"""
Swedish Government-issued IDs:
  - personnummer (Personnummer)
"""

import re

from typing import Iterable

from stdnum.se import personnummer

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for PERSONNUMMER
_PERSONNUMMER_PATTERN = r"\b\d{2,4}\d{2}\d{2}[+-]?\d{4}\b"


class SwedishPersonnummer(BasePiiTask):
    """
    Swedish Government-issued Personnummer numbers, recognize & validate
    """

    pii_name = "Swedish Personnummer"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.personnummer_pattern = re.compile(_PERSONNUMMER_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # PERSONNUMMER
        for item in self.personnummer_pattern.finditer(doc):
            item_value = item.group()
            if personnummer.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Swedish Personnummer",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, SwedishPersonnummer)]