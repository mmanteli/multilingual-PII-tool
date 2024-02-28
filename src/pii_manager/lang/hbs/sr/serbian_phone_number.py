"""
Detection of phone numbers written with Serbian notation.
"""


from pii_manager import PiiEnum

from ...sr.sr.serbian_phone_number import PATTERN_SR_PHONE


PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_SR_PHONE,
        "name": "Serbian phone number",
        "doc": "detect phone numbers that use Serbian notation.",
    }
]
