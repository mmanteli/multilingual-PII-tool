"""
Salvadoran Government-issued IDs:
  - DUI (Número de identificación nacional)
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for DUI
_DUI_PATTERN = r"\b\d{8}-\d\b"


class SalvadoranDUI(BasePiiTask):
    """
    Salvadoran Government-issued DUI numbers, recognize & validate
    """

    pii_name = "Salvadoran DUI"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.dui_pattern = re.compile(_DUI_PATTERN, flags=re.X)

    def validate(self, dui: str) -> bool:
        dui = dui.strip().replace("-", "")
        if not dui.isdigit() or len(dui) != 9:
            return False

        numbers = [int(d) for d in dui]
        total = sum((i+1) * numbers[i] for i in range(8)) 
        calculated_verificator = total % 10

        return calculated_verificator == numbers[8]


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # DUI
        for item in self.dui_pattern.finditer(doc):
            item_value = item.group()
            if self.validate(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Salvadoran DUI",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, SalvadoranDUI)]