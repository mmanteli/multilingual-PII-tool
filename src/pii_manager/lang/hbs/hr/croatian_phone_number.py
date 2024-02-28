"""
Detection of phone numbers written with Croatian notation.
"""


from pii_manager import PiiEnum

from ...hr.hr.croatian_phone_number import PATTERN_HR_PHONE

PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_HR_PHONE,
        "name": "Croatian phone number",
        "doc": "detect phone numbers that use Croatian notation.",
    }
]
