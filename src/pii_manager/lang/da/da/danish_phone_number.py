"""
Detection of phone numbers written with local notation (with or without country code), for Danish format.
"""


from pii_manager import PiiEnum

PATTERN_DA_PHONE = r'((\(\+45\)[ ]\d{2}[ ])|(\+45[ ]\d{2}[ ])|(\d{2}[ ]))\d{2}[ ]\d{2}[ ]\d{2}'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_DA_PHONE,
        "name": "Danish phone number",
        "doc": "detect phone numbers that use Danish format.",
    }
]