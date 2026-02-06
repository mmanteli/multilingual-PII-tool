"""
Czech Government-issued IDs:
  - RC (Rodné číslo)
"""

import re

from typing import Iterable

from stdnum.cz import rc

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for RC
_RC_PATTERN = r"\b\d{2}(0[1-9]|1[0-2]|5[1-9]|6[0-2])(0[1-9]|[12][0-9]|3[01])\/?\d{3,4}\b"


class CzechRC(BasePiiTask):
    """
    Czech Government-issued RC numbers, recognize & validate
    """

    pii_name = "Czech RC"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.rc_pattern = re.compile(_RC_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # RC
        for item in self.rc_pattern.finditer(doc):
            item_value = item.group()
            if rc.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name=" Czech RC",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, CzechRC)]