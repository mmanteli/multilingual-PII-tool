"""
Detection of phone numbers written with local notation (with or without country code), for Turkish format.
"""


from pii_manager import PiiEnum

PATTERN_TR_PHONE = r'\b(?:\+90[ -]?)?(?:0?\d{3}[ -]?)\d{3}[ -]?\d{4}\b'


PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_TR_PHONE,
        "name": "Turkish phone number",
        "doc": "detect phone numbers that use Turkish format.",
    }
]