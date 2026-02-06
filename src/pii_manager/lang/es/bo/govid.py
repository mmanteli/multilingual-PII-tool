"""
Bolivian Government-issued IDs:
  - CI (Cédula de Identidad)
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for CI
_CI_PATTERN = r"\b((BE|CB|CH|LP|OR|PD|PT|SC|TJ)[ -]?\d{7}|\d{7}[ -]?(BE|CB|CH|LP|OR|PD|PT|SC|TJ))\b"


class BolivianCI(BasePiiTask):
    """
    Bolivian Government-issued CI numbers, recognize & validate
    """

    pii_name = "Bolivian CI"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.ci_pattern = re.compile(_CI_PATTERN, flags=re.X | re.IGNORECASE)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # CI
        for item in self.ci_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.GOV_ID,
                item.start(),
                item_value,
                country=self.country,
                name="Bolivian CI",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, BolivianCI)]