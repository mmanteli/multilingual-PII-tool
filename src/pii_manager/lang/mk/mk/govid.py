"""
North Macedonian Government-issued IDs:
  - EMBG (Единствен матичен број на граѓанинот)
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for EMBG
_EMBG_PATTERN = r"\b\d{13}\b"


class NorthMacedonianEMBG(BasePiiTask):
    """
    North Macedonian Government-issued EMBG numbers, recognize & validate
    """

    pii_name = "North Macedonian EMBG"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.embg_pattern = re.compile(_EMBG_PATTERN, flags=re.X)

    def validate(self, embg: str) -> bool:
        embg = embg.strip()
        if not embg.isdigit() or len(embg) != 13:
            return False

        digits = [int(d) for d in embg]
        a = sum((7-i) * (digits[i] + digits[i+6]) for i in range(6))
        k_calc = 11 - (a % 11)
        if k_calc > 9:
            k_calc = 0

        return k_calc == digits[12]


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # EMBG
        for item in self.embg_pattern.finditer(doc):
            item_value = item.group()
            if self.validate(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="North Macedonian EMBG",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, NorthMacedonianEMBG)]