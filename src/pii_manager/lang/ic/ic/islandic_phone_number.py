"""
Detection of phone numbers written with local notation (with or without country code), for Icelandic format.
"""


from pii_manager import PiiEnum

PATTERN_IS_PHONE = r'((\+354[ ]\d{3})|(\d{3})|(\(00354\)[ ]\d{3}))[ ]\d{4}|((\+354[ ]\d{3})|(\(00354\)[ ]\d{3}))[-]\d{4}'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_IS_PHONE,
        "name": "Icelandic phone number",
        "doc": "detect phone numbers that use icelandic format.",
    }
]