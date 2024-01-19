"""
Detection of phone numbers written with international notation (i.e. with
prefix and country code), for DE
"""


from pii_manager import PiiEnum

# The pattern for the regex is the same as for English
from ...en.any.international_phone_number import PATTERN_INT_PHONE


PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_INT_PHONE,
        "name": "international phone number",
        "doc": "detect phone numbers that use international notation. Uses language context",
        "context": {
            "value": ["Tel", "Telefon", "Telefonnummer", "Rufen", "Tel.Nr."],
            "width": [25, 0],
            "type": "word",
        },
    }
]
