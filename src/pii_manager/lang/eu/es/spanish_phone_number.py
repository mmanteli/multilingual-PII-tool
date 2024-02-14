"""
Detection of phone numbers written with Spanish notation.
"""


from pii_manager import PiiEnum

# The pattern for the regex is the same as for English
from ...es.es.spanish_phone_number import PATTERN_ES_PHONE


PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_ES_PHONE,
        "name": "Spanish phone number",
        "doc": "detect phone numbers that use Spanish notation.",
    }
]
