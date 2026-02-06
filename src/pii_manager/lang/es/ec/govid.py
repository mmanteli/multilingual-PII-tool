"""
Ecuadorian Government-issued IDs:
  - CI (Cédula de Identidad)
"""

import re

from typing import Iterable

from stdnum.ec import ci

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for CI
_CI_PATTERN = r"\b([0-2]\d|30)[0-5]\d{7}\b"



class EcuadorianCI(BasePiiTask):
    """
    Ecuadorian Government-issued CI numbers, recognize & validate
    """

    pii_name = "Ecuadorian CI"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.cedula_pattern = re.compile(_CI_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # CI
        for item in self.cedula_pattern.finditer(doc):
            item_value = item.group()
            if ci.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Ecuadorian CI",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, EcuadorianCI)]