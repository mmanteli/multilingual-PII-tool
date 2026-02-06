"""
Portuguese Social Insurance number NISS (Número de Identificação da Segurança Social or Social Security Identification Number)
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for Portuguese Social Insurance
_SI_PATTERN = r"\b1\d{10}\b"


class PortugueseSocialInsurance(BasePiiTask):
    """
    Portuguese Social Insurance numbers NISS recognize
    """

    pii_name = "Portuguese Social Insurance"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.si_pattern = re.compile(_SI_PATTERN, flags=re.X)

    def validate(self, niss_str):
        """
        Validates a Portuguese Social Security Identification Number (NISS).
        The NISS consists of 11 digits. 
        The first 10 are a sequential number, and the 11th is a check digit.
        """
        # Weights for the weighted sum (for the first 10 digits)
        # The standard weights for NISS are: 29, 23, 19, 17, 13, 11, 7, 5, 3, 2
        weights = [29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
        
        total_sum = 0
        for i in range(10):
            total_sum += int(niss_str[i]) * weights[i]

        # Calculate the remainder using Modulo 11
        remainder = total_sum % 11
        
        # Calculate the check digit
        # Rule: 11 minus the remainder. If the result is 10 or more, use the last digit (0).
        expected_check_digit = 11 - remainder
        if expected_check_digit >= 10:
            expected_check_digit = 0
            
        # Get the actual check digit from the NISS string
        actual_check_digit = int(niss_str[10])

        return actual_check_digit == expected_check_digit


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
                    name="Portuguese Social Insurance",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, PortugueseSocialInsurance)]