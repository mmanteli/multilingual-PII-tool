"""
Dominican Government-issued IDs:
  - cedula (Cédula de Identidad y Electoral)
"""

import re

from typing import Iterable

from stdnum.do import cedula

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for CEDULA
_CEDULA_PATTERN = r"\b\d{3}-\d{7}-\d\b"



class DominicanCEDULA(BasePiiTask):
    """
    Dominican Government-issued CEDULA numbers, recognize & validate
    """

    pii_name = "Dominican CEDULA"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.cedula_pattern = re.compile(_CEDULA_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # CEDULA
        for item in self.cedula_pattern.finditer(doc):
            item_value = item.group()
            print(item_value)
            if cedula.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Dominican CEDULA",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, DominicanCEDULA)]