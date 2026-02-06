"""
Costa Rican Government-issued IDs:
  - CPF (Cédula de Persona Física)
"""

import re

from typing import Iterable

from stdnum.cr import cpf

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for CPF
_CPF_PATTERN = r"\b\d[\.\- ]\d{4}[\.\- ]\d{4}\b"


class CostaRicanCPF(BasePiiTask):
    """
    Costa Rican Government-issued CPF numbers, recognize & validate
    """

    pii_name = "Costa Rican CPF"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.cpf_pattern = re.compile(_CPF_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # CPF
        for item in self.cpf_pattern.finditer(doc):
            item_value = item.group()
            if cpf.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Costa Rican CPF",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, CostaRicanCPF)]