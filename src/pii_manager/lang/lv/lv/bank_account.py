"""
Latvian frequent bank account numbers
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for Latvian bank account numbers
_BA_PATTERN = r"\bLV[0-9]{2}[A-Z]{4}[A-Z0-9]{13}\b"


class LatvianBankAccount(BasePiiTask):
    """
    Latvian frequent bank account numbers recognize
    """

    pii_name = "Latvian Bank Account"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.ba_pattern = re.compile(_BA_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # Bank Account
        for item in self.ba_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.BANK_ACCOUNT,
                item.start(),
                item_value,
                country=self.country,
                name="Latvian Bank Account",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.BANK_ACCOUNT, LatvianBankAccount)]