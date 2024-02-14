"""
Detection of phone numbers written with French notation.
"""


from pii_manager import PiiEnum

# The pattern for the regex is the same as for English
from ...fr.fr.french_phone_number import PATTERN_FR_PHONE


PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_FR_PHONE,
        "name": "French phone number",
        "doc": "detect phone numbers that use French notation.",
    }
]
