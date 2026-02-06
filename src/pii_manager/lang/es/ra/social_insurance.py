"""
Argentine Social Insurance numbers CUIL
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for Argentine Social Insurance
_SI_PATTERN = r"\b\d{2}-\d{8}-\d\b"


class ArgentineSocialInsurance(BasePiiTask):
    """
    Argentine Social Insurance numbers CUIL recognize
    """

    pii_name = "Argentine Social Insurance"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.si_pattern = re.compile(_SI_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # Social Insurance
        for item in self.si_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.GOV_ID,
                item.start(),
                item_value,
                country=self.country,
                name="Argentine Social Insurance",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, ArgentineSocialInsurance)]