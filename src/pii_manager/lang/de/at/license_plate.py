"""
Austrian license plate
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for license plate
_LICENSE_PLATE_PATTERN = r"\b[A-Z]{1,2}[-\s]\d{1,5}[-\s][A-Z]{1,3}\b"



class AustrianLicensePlate(BasePiiTask):
    """
    Austrian license plate numbers recognize
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
                name=" Austrian license plate",
            )
# Task descriptor
PII_TASKS = [(PiiEnum.LICENSE_PLATE, AustrianLicensePlate)]