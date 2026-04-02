"""
Irish Government-issued IDs:
  - PPS (Personal Public Service Number)
"""

import re

from typing import Iterable

from stdnum.ie import pps

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for PPS
_PPS_PATTERN = r"\b\d{7}[A-Z]\b"


class IrishPPS(BasePiiTask):
    """
    Irish Government-issued PPS numbers, recognize & validate
    """

    pii_name = "Irish PPS"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.pps_pattern = re.compile(_PPS_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # PPS
        for item in self.pps_pattern.finditer(doc):
            item_value = item.group()
            if pps.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name=" Irish PPS",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, IrishPPS)]