"""
Icelandic Government-issued IDs:
  - Kennitala
"""

import re

from typing import Iterable

from stdnum.is_ import kennitala

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for KNT
_KNT_PATTERN = r"\b\d{6}-?\d{4}\b"


class IcelandicKNT(BasePiiTask):
    """
    Icelandic Government-issued Kennitala numbers, recognize & validate
    """

    pii_name = "Icelandic KNT"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.knt_pattern = re.compile(_KNT_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # KNT
        for item in self.knt_pattern.finditer(doc):
            item_value = item.group()
            if kennitala.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Icelandic KNT",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, IcelandicKNT)]