"""
Lithuanian Government-issued IDs:
  - ASMENS (Asmens kodas)
"""

import re

from typing import Iterable

from stdnum.lt import asmens

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for ASMENS
_ASMENS_PATTERN = r"\b[1-6]\d{10}\b"

class LithuanianASMENS(BasePiiTask):
    """
    Lithuanian Government-issued ASMENS numbers, recognize & validate
    """

    pii_name = "Lithuanian ASMENS"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.asmens_pattern = re.compile(_ASMENS_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # ASMENS
        for item in self.asmens_pattern.finditer(doc):
            item_value = item.group()
            if asmens.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Lithuanian ASMENS",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, LithuanianASMENS)]