"""
Belgian Government-issued IDs:
  - NN (Rijksregisternummer / Numéro de registre national)
"""

import re

from typing import Iterable


from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for NN
_NN_PATTERN = r"\b\d{2}[\. ](0\d|1[012])[\. ]([0-2]\d|3[01])-?\d{3}[\. ]\d{2}\b"


class BelgianNN(BasePiiTask):
    """
    Belgian Government-issued NN numbers, recognize & validate
    """

    pii_name = "Belgian NN"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.nn_pattern = re.compile(_NN_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # NN
        for item in self.nn_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.GOV_ID,
                item.start(),
                item_value,
                country=self.country,
                name=" Belgian NN",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, BelgianNN)]