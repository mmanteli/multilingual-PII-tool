"""
Argentine Government-issued IDs:
  - DNI (Documento Nacional de Identidad)
"""

import re

from typing import Iterable

from stdnum.ar import dni

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for DNI
_DNI_PATTERN = r"\b\d{2}\.\d{3}\.\d{3}\b"


class ArgentineDNI(BasePiiTask):
    """
    Argentine Government-issued DNI numbers, recognize & validate
    """

    pii_name = "Argentine DNI"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.dni_pattern = re.compile(_DNI_PATTERN, flags=re.X)

    def find(self, doc: str) -> Iterable[PiiEntity]:
        # DNI
        for item in self.dni_pattern.finditer(doc):
            item_value = item.group()
            if dni.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Argentine DNI",
                )

# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, ArgentineDNI)]