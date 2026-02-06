"""
German Social Insurance number So­zi­a­l­ver­si­che­rungs­num­mer 
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for German Social Insurance
_SI_PATTERN = r"\b\d{2}\s?([012]\d|3[01])(0\d|1[0-2])\d{2}\s?[A-Z]\s?\d{3}\b"


class GermanSocialInsurance(BasePiiTask):
    """
    German Social Insurance numbers Sozialversicherungsnummer recognize
    """

    pii_name = "German Social Insurance"
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
                name="German Social Insurance",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, GermanSocialInsurance)]