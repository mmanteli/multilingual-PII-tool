"""
Netherlands Government-issued IDs:
  - BSN (Burgerservicenummer)
"""

import re

from typing import Iterable

from stdnum.nl import bsn

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for BSN
_BSN_PATTERN = r"\b\d{9}\b"


class DutchBSN(BasePiiTask):
    """
    Dutch Government-issued BSN numbers, recognize & validate
    """

    pii_name = "Dutch BSN"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.bsn_pattern = re.compile(_BSN_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # BSN
        for item in self.bsn_pattern.finditer(doc):
            item_value = item.group()
            if bsn.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Dutch BSN",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, DutchBSN)]