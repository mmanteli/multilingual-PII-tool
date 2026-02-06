"""
 Government-issued IDs:
  - CPR (Det Centrale Personregister)
"""

import re

from typing import Iterable

from stdnum.dk import cpr

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for CPR
_CPR_PATTERN = r"\b(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])\d{2}-?\d{4}\b"


class DanishCPR(BasePiiTask):
    """
    Danish Government-issued CPR numbers, recognize & validate
    """

    pii_name = "Danish CPR"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.cpr_pattern = re.compile(_CPR_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # CPR
        for item in self.cpr_pattern.finditer(doc):
            item_value = item.group()
            if cpr.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name=" Danish CPR",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, DanishCPR)]