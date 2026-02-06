"""
Panamanian Government-issued IDs:
  - CIP (Cédula de Identidad Personal)
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for CIP
_CIP_PATTERN = r"\b\d-\d{3}-\d{3,4}\b"


class PanamanianCIP(BasePiiTask):
    """
    Panamanian Government-issued CIP numbers, recognize & validate
    """

    pii_name = "Panamanian CIP"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.cip_pattern = re.compile(_CIP_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # CIP
        for item in self.cip_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.GOV_ID,
                item.start(),
                item_value,
                country=self.country,
                name="Panamanian CIP",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, PanamanianCIP)]