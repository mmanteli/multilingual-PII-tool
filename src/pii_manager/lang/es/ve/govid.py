"""
Venezuelan Government-issued IDs:
  - CI (Cédula de Identidad)
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for CI
_CI_PATTERN = r"\b[VE][- \.]\d{1,2}\.\d{3}\.\d{3}\b"


class VenezuelanCI(BasePiiTask):
    """
    Venezuelan Government-issued CI numbers, recognize & validate
    """

    pii_name = "Venezuelan CI"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.ci_pattern = re.compile(_CI_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # CI
        for item in self.ci_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.GOV_ID,
                item.start(),
                item_value,
                country=self.country,
                name="Venezuelan CI",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, VenezuelanCI)]