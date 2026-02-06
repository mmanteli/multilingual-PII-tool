"""
French Government-issued IDs:
  - NIR (Numéro de Sécurité Sociale)
"""

import re

from typing import Iterable

from stdnum.fr import nir

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for NIR
_NIR_PATTERN = r"\b[12]\d{2}(0[1-9]|1[0-2]|[2-9]\d)\d{6}\d{2}\b"


class FrenchNIR(BasePiiTask):
    """
    French Government-issued NIR numbers, recognize & validate
    """

    pii_name = "French NIR"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.nir_pattern = re.compile(_NIR_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # NIR
        for item in self.nir_pattern.finditer(doc):
            item_value = item.group()
            if nir.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name=" French NIR",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, FrenchNIR)]