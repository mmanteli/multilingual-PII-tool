"""
Chilean Government-issued IDs:
  - RUT (Rol Único Tributario)
"""

import re

from typing import Iterable

from stdnum.cl import rut

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for RUT
_RUT_PATTERN = r"\b\d{2}[ \.]\d{3}[ \.]\d{3}-[0-9Kk]\b"


class ChileanRUT(BasePiiTask):
    """
    Chilean Government-issued RUT numbers, recognize & validate
    """

    pii_name = "Chilean RUT"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.rut_pattern = re.compile(_RUT_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # RUT
        for item in self.rut_pattern.finditer(doc):
            item_value = item.group()
            if rut.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Chilean RUT",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, ChileanRUT)]