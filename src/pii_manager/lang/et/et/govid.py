"""
Estonian Government-issued IDs:
  - IK (Isikukood)
"""

import re

from typing import Iterable

from stdnum.ee import ik

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for RC
_IK_PATTERN = r"\b[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}\d\b"


class EstonianIK(BasePiiTask):
    """
    Estonian Government-issued IK numbers, recognize & validate
    """

    pii_name = "Estonian IK"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.ik_pattern = re.compile(_IK_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # IK
        for item in self.ik_pattern.finditer(doc):
            item_value = item.group()
            if ik.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name=" Estonian IK",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, EstonianIK)]