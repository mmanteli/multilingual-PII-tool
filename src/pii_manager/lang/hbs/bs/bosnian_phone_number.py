"""
Detection of phone numbers written with Bosnian-Herzegovinian notation.
"""


from pii_manager import PiiEnum

from ...bs.ba.bosnia_herz_phone_number import PATTERN_BA_PHONE

PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_BA_PHONE,
        "name": "Bosnian-Herzegovinian phone number",
        "doc": "detect phone numbers that use Bosnian-Herzegovinian notation.",
    }
]
