"""
Maltese Government-issued IDs:
  - IDN (Identity Card Number)
"""

import re

from typing import Iterable
from datetime import datetime


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for IDN
_IDN_PATTERN = r"\b\d{6,7}\s?[A-Z]\b"


class MalteseIDN(BasePiiTask):
    """
    Maltese Government-issued IDN numbers, recognize & validate
    """

    pii_name = "Maltese IDN"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.idn_pattern = re.compile(_IDN_PATTERN, flags=re.X)

    def validate(self, malta_id: str) -> bool:
        malta_id = malta_id.strip().upper()

        if not malta_id[0].isalpha() or not malta_id[-1].isalpha():
            return False

        middle = malta_id[1:-1]
        if not middle.isdigit() or len(middle) not in (6, 7):
            return False

        number = int(middle)
        expected_letter = chr((number % 26) + ord('A'))

        return malta_id[-1] == expected_letter


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # IDN
        for item in self.idn_pattern.finditer(doc):
            item_value = item.group()
            if self.validate(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Maltese IDN",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, MalteseIDN)]