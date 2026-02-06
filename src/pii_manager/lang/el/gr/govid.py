"""
Greek Goverment-issued IDs:
  - ADT (Αριθμός Ταυτότητας)
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for ADT
_ADT_PATTERN = r"\b([Α-Ω]|[A-Z]){1,2}\s?\d{6}\b"



class GreekAdt(BasePiiTask):
    """
    Greek Government-issued ADT numbers, recognize & validate
    """

    pii_name = "Greek ADT"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.adt_pattern = re.compile(_ADT_PATTERN, flags=re.X)

    def find(self, doc: str) -> Iterable[PiiEntity]:
        # ADT
        for item in self.adt_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.GOV_ID,
                item.start(),
                item_value,
                country=self.country,
                name=" Greek ADT",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, GreekAdt)]