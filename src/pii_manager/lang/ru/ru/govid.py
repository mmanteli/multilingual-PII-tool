"""
Russian Government-issued IDs:
  - INN (Идентификационный номер налогоплательщика)
"""

import re

from typing import Iterable

from stdnum.ru import inn

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for INN
_INN_PATTERN = r"\b\d{12}\b"


class RussianINN(BasePiiTask):
    """
    Russian Government-issued INN numbers, recognize & validate
    """

    pii_name = "Russian INN"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.inn_pattern = re.compile(_INN_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # INN
        for item in self.inn_pattern.finditer(doc):
            item_value = item.group()
            if inn.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Russian INN",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, RussianINN)]