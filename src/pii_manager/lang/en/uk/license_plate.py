"""
UK license plate
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for license plate
_LICENSE_PLATE_PATTERN = r"\b[A-HJ-PR-Y][A-HJ-NPR-Y]\d{2}[\s-]?[A-Z]{3}\b"



class UkLicensePlate(BasePiiTask):
    """
    UK license plate numbers recognize
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.license_plate_pattern = re.compile(_LICENSE_PLATE_PATTERN, flags=re.X)

    def find(self, doc: str) -> Iterable[PiiEntity]:
        # license plate
        for item in self.license_plate_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.LICENSE_PLATE,
                item.start(),
                item_value,
                country=self.country,
                name=" UK license plate",
            )
# Task descriptor
PII_TASKS = [(PiiEnum.LICENSE_PLATE, UkLicensePlate)]