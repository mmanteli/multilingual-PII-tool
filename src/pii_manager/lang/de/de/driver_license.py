"""
German driver license
"""

import re

from typing import Iterable

from pii_manager import PiiEnum, PiiEntity
from pii_manager.helper import BasePiiTask

# regex for German driver license
_DL_PATTERN = r"\b[0-9A-Z][0-9]{2}[0-9A-Z]{6}[0-9][0-9A-Z]\b"


class GermanDriverLicense(BasePiiTask):
    """
    German driver license numbers recognize
    """

    pii_name = "German Driver License"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regex
        self.dl_pattern = re.compile(_DL_PATTERN, flags=re.X)


    def find(self, doc: str) -> Iterable[PiiEntity]:
        # Driver License
        for item in self.dl_pattern.finditer(doc):
            item_value = item.group()
            yield PiiEntity(
                PiiEnum.DRIVER_LICENSE,
                item.start(),
                item_value,
                country=self.country,
                name="German Driver License",
            )

# Task descriptor
PII_TASKS = [(PiiEnum.DRIVER_LICENSE, GermanDriverLicense)]