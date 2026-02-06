"""
Greek Social Insurance number AMKA (Αριθμός Μητρώου Κοινωνικής Ασφάλισης)
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for Greek Social Insurance
_SI_PATTERN = r"\b([012]\d|3[01])(0\d|1[0-2])\d{2}\s?\d{4}\s?\d\b"


class GreekSocialInsurance(BasePiiTask):
    """
    Greek Social Insurance numbers AMKA
    """

    pii_name = "Greek Social Insurance"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.si_pattern = re.compile(_SI_PATTERN, flags=re.X)

    def validate(self, amka_number):
        """
        Validates a Greek Social Security Number (AMKA) using the Luhn algorithm.
        
        The AMKA consists of 11 digits:
        - First 6: Date of birth (DDMMYY)
        - Next 4: Sequential registration number
        - Last 1: Check digit (Luhn)
        """
        # Convert to string and remove any whitespace
        amka_str = str(amka_number).strip()

        # AMKA must be exactly 11 numeric digits
        if not amka_str.isdigit() or len(amka_str) != 11:
            return False

        total_sum = 0
        # Reverse the string to process digits from right to left
        digits = [int(d) for d in amka_str[::-1]]

        for index, digit in enumerate(digits):
            # Every second digit (starting from the one after the check digit) is doubled
            if index % 2 == 1:
                doubled_value = digit * 2
                # If doubling results in a number > 9, subtract 9 (sum the digits)
                if doubled_value > 9:
                    doubled_value -= 9
                total_sum += doubled_value
            else:
                total_sum += digit

        # If the total sum is a multiple of 10, the number is valid
        return total_sum % 10 == 0

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
                    name="Greek Social Insurance",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, GreekSocialInsurance)]