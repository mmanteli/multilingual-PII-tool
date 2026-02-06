"""
Bosnian Government-issued IDs:
  - JMBG (Jedinstveni matični broj građana)
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for JMBG
_JMBG_PATTERN = r"\b(0[1-9]|[12]\d|3[01])(0[1-9]|1[0-2])\d{3}\d{2}\d{3}\d\b"


class BosnianJMBG(BasePiiTask):
    """
    Bosnian Government-issued JMBG numbers, recognize & validate
    """

    pii_name = "Bosnian JMBG"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.jmbg_pattern = re.compile(_JMBG_PATTERN, flags=re.X)

    def validate(self, jmbg: str) -> bool:
        digits = [int(d) for d in jmbg]
        control = digits[-1]
        a = digits[:12]
        
        weights = [7, 6, 5, 4, 3, 2,
                7, 6, 5, 4, 3, 2]
        
        suma = sum([a[i] * weights[i] for i in range(12)])
        
        c = 11 - (suma % 11)
        
        if c > 9:
            c = 0
        
        return c == control


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # JMBG
        for item in self.jmbg_pattern.finditer(doc):
            item_value = item.group()
            if self.validate(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Bosnian JMBG",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, BosnianJMBG)]