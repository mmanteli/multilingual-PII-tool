"""
Mexican Government-issued IDs:
  - CURP (Clave Única de Registro de Población)
  - RFC (Registro Federal de Contribuyentes)
"""

import re

from typing import Iterable

from stdnum.mx import curp, rfc

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for CURP & RFC
_CURP_PATTERN = r"\b[A-Z]{4}\d{6}[HM][A-Z]{2}[A-Z]{3}[0-9A-Z]\d\b"
_RFC_PATTERN = r"\b[A-ZÑ&]{3,4}\d{6}[A-Z0-9]{3}\b"


class MexicanCURPRFC(BasePiiTask):
    """
    Mexican Government-issued CURP & RFC numbers, recognize & validate
    """

    pii_name = "Mexican CURP and RFC numbers"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regexes
        self.curp = re.compile(_CURP_PATTERN, flags=re.X)
        self.rfc = re.compile(_RFC_PATTERN, flags=re.X)

    def find(self, doc: str) -> Iterable[PiiEntity]:
        # CURP
        for item in self.curp.finditer(doc):
            item_value = item.group()
            if curp.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Mexican CURP",
                )
        # RFC
        for item in self.rfc.finditer(doc):
            item_value = item.group()
            if rfc.is_valid(item_value):
                yield PiiEntity(
                    PiiEnum.GOV_ID,
                    item.start(),
                    item_value,
                    country=self.country,
                    name="Mexican RFC",
                )


# Task descriptor
PII_TASKS = [(PiiEnum.GOV_ID, MexicanCURPRFC)]