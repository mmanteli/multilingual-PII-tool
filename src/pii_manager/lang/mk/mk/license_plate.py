"""
North Macedonian license plate
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for license plate
_LICENSE_PLATE_PATTERN = r"\b(BE|BT|DB|DE|DH|DK|GE|GV|KA|KI|KO|KR|KP|KS|KU|MB|MK|NE|OH|PE|PP|PS|RA|RE|SK|SN|SU|SR|ST|TE|VA|VE|VI|VV)\s?\d{4}\s?[A-Z]{2}\b"



class NorthMacedonianLicensePlate(BasePiiTask):
    """
    North Macedonian license plate numbers recognize
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.license_plate_pattern = re.compile(_LICENSE_PLATE_PATTERN, flags=re.X | re.IGNORECASE)

    def find(self, doc: str) -> Iterable[PiiEntity]:
        # license plate
        for item in self.license_plate_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.LICENSE_PLATE,
                item.start(),
                item_value,
                country=self.country,
                name="North Macedonian license plate",
            )
# Task descriptor
PII_TASKS = [(PiiEnum.LICENSE_PLATE, NorthMacedonianLicensePlate)]