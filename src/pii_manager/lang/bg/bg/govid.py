"""
Bulgarian Goverment-issued IDs:
  - EGN (Единен граждански номер)
  - PNF (Личен номер на чужденец)
  - VAT (Данъчен номер)
"""

import re

from typing import Iterable

from stdnum.bg import egn, pnf, vat

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for EGN
_EGN_PATTERN = r"\b\d{2}(?:0[1-9]|1[0-2]|2[1-9]|3[0-2]|4[1-9]|5[0-2])(?:0[1-9]|[12]\d|3[01])\d{4}\b"
# _PNF_PATTERN = r"\b\d{10}\b" I couldn't find a clear non ambiguous pattern of PNF
_VAT_PATTERN = r"\bBG *\d{9,10}\b"


class BulgarianEgnVat(BasePiiTask):
    """
    Bulgarian Government-issued EGN numbers, recognize & validate
    """

    pii_name = "Bulgarian EGN"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.egn_pattern = re.compile(_EGN_PATTERN, flags=re.X)
        # self.pnf_pattern = re.compile(_PNF_PATTERN, flags=re.X)
        self.vat_pattern = re.compile(_VAT_PATTERN, flags=re.X | re.IGNORECASE)

    def find(self, doc: str) -> Iterable[PiiEntity]:
        # EGN
        for item in self.egn_pattern.finditer(doc):
            item_value = item.group()
            if egn.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name=" Bulgarian EGN",
                )
        # PNF
        # for item in self.pnf_pattern.finditer(doc):
        #     item_value = item.group()
        #     if pnf.is_valid(item_value):
        #         yield PiiEntity(
        #             PiiEnum.GOV_ID,
        #             item.start(),
        #             item_value,
        #             country=self.country,
        #             name="Bulgarian PNF",
        #         )

        # VAT
        for item in self.vat_pattern.finditer(doc):
            item_value = item.group()
            if vat.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name=" Bulgarian VAT",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, BulgarianEgnVat)]
