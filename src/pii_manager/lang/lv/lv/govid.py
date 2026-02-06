"""
Latvian Government-issued IDs:
  - PK (Personas kods)
"""

import re

from typing import Iterable
from datetime import datetime


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for KODS
_PK_PATTERN = r"\b(0[1-9]|[12]\d|3[01])(0[1-9]|1[0-2])\d{2}-?\d{5}\b"



class LatvianPK(BasePiiTask):
    """
    Latvian Government-issued PK numbers, recognize & validate
    """

    pii_name = "Latvian PK"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.pk_pattern = re.compile(_PK_PATTERN, flags=re.X)

    def validate(self, pk: str) -> bool:
        pk = pk.strip().replace("-", "")
        if len(pk) != 11 or not pk.isdigit():
            return False

        dd = pk[0:2]
        mm = pk[2:4]
        yy = pk[4:6]
        serial = pk[6:10]
        control = int(pk[10])
        try:
            year = int(yy)
            if year <= 49:
                year += 2000
            else:
                year += 1900

            datetime(year, int(mm), int(dd))
        except ValueError:
            return False

        digits = [int(d) for d in pk[:10]]
        weights = [1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

        total = sum(d * w for d, w in zip(digits, weights))
        remainder = total % 11

        if remainder == 10:
            return False
        return remainder == control


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # PK
        for item in self.pk_pattern.finditer(doc):
            item_value = item.group()
            if self.validate(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Latvian PK",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, LatvianPK)]