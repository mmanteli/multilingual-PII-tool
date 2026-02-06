"""
Russian Social Insurance number СНИЛС (Страховой номер индивидуального лицевого счёта)
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for Russian Social Insurance
_SI_PATTERN = r"\b\d{3}-\d{3}-\d{3}\s\d{2}\b"


class RussianSocialInsurance(BasePiiTask):
    """
    Russian Social Insurance numbers СНИЛС
    """
    pii_name = "Russian Social Insurance"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.si_pattern = re.compile(_SI_PATTERN, flags=re.X)

    def validate(self, snils_number):
        """
        Validates a Russian SNILS (Insurance Number of Individual Personal Account).
        Format: 11 digits (9 main digits + 2 check digits).
        Standard string format is often: '123-456-789 01'
        """
         # Remove separators (hyphens, spaces) and ensure it's 11 digits
        snils_digits = "".join(filter(str.isdigit, str(snils_number)))

        if len(snils_digits) != 11:
            return False

        # SNILS numbers smaller than 001-001-998 are not validated by checksum
        if int(snils_digits[:9]) <= 1001998:
            return True
        main_part = snils_digits[:9]
        check_digits = int(snils_digits[9:])

        # 1. Calculate weighted sum
        # Each digit is multiplied by its inverse position (9 down to 1)
        weighted_sum = 0
        for i in range(9):
            weighted_sum += int(main_part[i]) * (9 - i)

        # 2. Apply SNILS Checksum Rules (Modulo 101)
        calculated_check = 0
        
        if weighted_sum < 100:
            calculated_check = weighted_sum
        elif weighted_sum == 100 or weighted_sum == 101:
            calculated_check = 0
        else: # weighted_sum > 101
            remainder = weighted_sum % 101
            if remainder < 100:
                calculated_check = remainder
            elif remainder == 100 or remainder == 101:
                calculated_check = 0

        return calculated_check == check_digits

    def find(self, doc: str) -> Iterable[PiiEntity]:
        # Social Insurance
        for item in self.si_pattern.finditer(doc):
            item_value = item.group()
            if self.validate(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Russian Social Insurance",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, RussianSocialInsurance)]