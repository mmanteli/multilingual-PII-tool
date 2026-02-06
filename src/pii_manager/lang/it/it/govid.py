"""
Italian Government-issued IDs:
  - CF (Codice Fiscale)
"""

import re

from typing import Iterable

from stdnum.it import codicefiscale

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for CF
_CF_PATTERN = r"\b[A-Za-z]{6}[0-9]{2}[A-Za-z]{1}[0-9]{2}[A-Za-z]{1}[0-9]{3}[A-Za-z]{1}\b"


class ItalianCF(BasePiiTask):
    """
    Italian Government-issued CF numbers, recognize & validate
    """

    pii_name = "Italian CF"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.cf_pattern = re.compile(_CF_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # CF
        for item in self.cf_pattern.finditer(doc):
            item_value = item.group()
            if codicefiscale.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Italian CF",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, ItalianCF)]