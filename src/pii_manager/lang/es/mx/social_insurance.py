"""
Mexican Social Insurance numbers NSS
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for Mexican Social Insurance
_SI_PATTERN = r"\b\d{2}-\d{2}-\d{2}-\d{4}-\d\b"


class MexicanSocialInsurance(BasePiiTask):
    """
    Mexican Social Insurance numbers NSS recognize
    """

    pii_name = "Mexican Social Insurance"
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
                name="Mexican Social Insurance",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, MexicanSocialInsurance)]