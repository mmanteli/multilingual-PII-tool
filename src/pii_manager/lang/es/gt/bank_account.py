"""
Guatemalan frequent bank account numbers
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for Guatemalan bank account numbers
_BA_PATTERN = r"\bGT[0-9]{2}[A-Z0-9]{24}\b"


class GuatemalanBankAccount(BasePiiTask):
    """
    Guatemalan frequent bank account numbers recognize
    """

    pii_name = "Guatemalan Bank Account"

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
                name="Guatemalan Bank Account",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.BANK_ACCOUNT, GuatemalanBankAccount)]