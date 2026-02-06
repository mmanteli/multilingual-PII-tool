"""
German Government-issued IDs:
  - IDNR (Steuerliche Identifikationsnummer)
  - PWN (Personalausweisnummer)
"""

import re

from typing import Iterable

from stdnum.de import idnr

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for IDNR
_IDNR_PATTERN = r"\b\d{11}\b"
# regex for PWN
_PWN_PATTERN = r"\b[A-Z]{9,10}\b"



class GermanIDNRPWD(BasePiiTask):
    """
    German Government-issued IDNR and PWN numbers, recognize & validate
    """

    pii_name = "German IDNRPWD"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.idnr_pattern = re.compile(_IDNR_PATTERN, flags=re.X)
        self.pwn_pattern = re.compile(_PWN_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # IDNR
        for item in self.idnr_pattern.finditer(doc):
            item_value = item.group()
            if idnr.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name=" German IDNR",
                )
        # PWN
        for item in self.pwn_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.GOV_ID,
                item.start(),
                item_value,
                country=self.country,
                name=" German PWN",
            )
# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, GermanIDNRPWD)]