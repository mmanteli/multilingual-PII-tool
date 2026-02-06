"""
Brazilian frequent bank account numbers
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for Brazilian bank account numbers
_BA_PATTERN = r"\b(BR[0-9]{2}[0-9]{23}[A-Z]{1}[A-Z0-9]{1})|(\d{12}-\d)\b"


class BrazilianBankAccount(BasePiiTask):
    """
    Brazilian frequent bank account numbers recognize
    """

    pii_name = "Brazilian Bank Account"
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
                name="Brazilian Bank Account",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.BANK_ACCOUNT, BrazilianBankAccount)]