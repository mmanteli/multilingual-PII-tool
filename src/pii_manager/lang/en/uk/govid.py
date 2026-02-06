"""
United Kingdom Government-issued IDs:
  - NINO (National Insurance Number)
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for PPS
_NINO_PATTERN = r"\b(?!BG|GB|KN|NK|NT|TN|ZZ)[A-CEGHJ-PR-TW-Z]{2}\s?\d{2}\s?\d{2}\s?\d{2}[A-D]\b"

class BritishNINO(BasePiiTask):
    """
    British Government-issued NINO numbers, recognize & validate
    """

    pii_name = "British NINO"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.nino_pattern = re.compile(_NINO_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # NINO
        for item in self.nino_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.GOV_ID,
                item.start(),
                item_value,
                country=self.country,
                name=" British NINO",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, BritishNINO)]