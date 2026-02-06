"""
Australian license plate
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for license plate
_LICENSE_PLATE_PATTERN = r"\b[A-Z0-9-· ]{5,11}\b"
_REGIONAL_PLATE_PATTERN = r"\b(" \
                        r"\b[A-Z]{3}\d{2}[A-Z]|" \
                        r"\b[A-Z]{3}[-· ]?\d{3}|" \
                        r"\b\d{3}[-· ]?[A-Z]{3}|" \
                        r"\bS\d{3}[A-Z]{3}|" \
                        r"\b\d[A-Z]{3}\d{3}|" \
                        r"\b[A-Z]\d{2}[A-Z]{2}|" \
                        r"\b[A-Z]{2,3}[-· ]?\d{2}[A-Z]|" \
                        r"\b[A-Z]{2}[-· ]?\d{3}" \
                        r")\b"



class AustralianLicensePlate(BasePiiTask):
    """
    Australian license plate numbers recognize
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.license_plate_pattern = re.compile(_LICENSE_PLATE_PATTERN, flags=re.X)

    def find(self, doc: str) -> Iterable[PiiEntity]:
        # license plate
        for item in self.license_plate_pattern.finditer(doc):
            item_value = item.group()
            if not re.match(_REGIONAL_PLATE_PATTERN, item_value):
                continue
            yield PiiEntity(
                PiiEnum.LICENSE_PLATE,
                item.start(),
                item_value,
                country=self.country,
                name=" Australian license plate",
            )
# Task descriptor
PII_TASKS = [(PiiEnum.LICENSE_PLATE, AustralianLicensePlate)]