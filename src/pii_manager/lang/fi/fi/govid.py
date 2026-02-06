"""
Finnish Government-issued IDs:
  - HETU (Henkilötunnus)
"""

import re
import datetime

from typing import Iterable

from stdnum.fi import hetu

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for HETU
_HETU_PATTERN = r"\b(0[1-9]|[12]\d|3[01])(0[1-9]|1[0-2])([5-9]\d\+|\d\d-|[01]\dA)\d{3}[\dABCDEFHJKLMNPRSTUVWXY]\b"


class FinnishHETU(BasePiiTask):
    """
    Finnish Government-issued HETU numbers, recognize & validate
    """

    pii_name = "Finnish HETU"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.hetu_pattern = re.compile(_HETU_PATTERN, flags=re.X)

    def validate_hetu(self, hetu: str) -> bool:
        """
        Validate Finnish HETU (Henkilötunnus)
        Returns True if valid, False otherwise
        """
        CHECKSUM_TABLE = "0123456789ABCDEFHJKLMNPRSTUVWXY"
        # Basic format check
        if not re.fullmatch(r"\d{6}[+\-A]\d{3}[0-9A-Z]", hetu):
            return False

        dd = int(hetu[0:2])
        mm = int(hetu[2:4])
        yy = int(hetu[4:6])
        century_sign = hetu[6]
        individual = int(hetu[7:10])
        checksum_char = hetu[10]

        # Century resolution
        if century_sign == "+":
            year = 1800 + yy
        elif century_sign == "-":
            year = 1900 + yy
        elif century_sign == "A":
            year = 2000 + yy
        else:
            return False

        # Date validation
        try:
            datetime.date(year, mm, dd)
        except ValueError:
            return False

        # Individual number range
        if not (2 <= individual <= 899):
            return False

        # Checksum calculation
        number = int(hetu[0:6] + hetu[7:10])
        expected_checksum = CHECKSUM_TABLE[number % 31]

        return checksum_char == expected_checksum

    def find(self, doc: str) -> Iterable[PiiEntity]:
        # HETU
        for item in self.hetu_pattern.finditer(doc):
            item_value = item.group()
            if self.validate_hetu(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name=" Finnish HETU",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, FinnishHETU)]