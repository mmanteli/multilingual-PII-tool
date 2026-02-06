"""
Detection of phone numbers written with local notation (with or without country code), for Bulgarian format.
"""


from pii_manager import PiiEnum

PATTERN_BG_PHONE = r'\b\+359\s?\d{8,9}\b'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_BG_PHONE,
        "name": "Bulgarian phone number",
        "doc": "detect phone numbers that use Bulgarian format.",
    }
]