"""
Romanian Government-issued IDs:
  - CNP (Cod Numeric Personal)
"""

import re

from typing import Iterable

from stdnum.ro import cnp

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for CNP
_CNP_PATTERN = r"\b[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{2}\d{3}\d\b"



class RomanianCNP(BasePiiTask):
    """
    Romanian Government-issued CNP numbers, recognize & validate
    """

    pii_name = "Romanian CNP"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.cnp_pattern = re.compile(_CNP_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # CNP
        for item in self.cnp_pattern.finditer(doc):
            item_value = item.group()
            if cnp.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Romanian CNP",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, RomanianCNP)]