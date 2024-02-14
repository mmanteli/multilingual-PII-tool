"""
Detection of phone numbers written with local notation (with or without country code), for Belarusian format.
"""


from pii_manager import PiiEnum

PATTERN_BE_PHONE = r'((\+375[ ]\d{1,3}[- ])|(\(\+375[ ]\d{1,3}\)[ ])|(\d{1,3}[ -]))((\d{3,4}[- ]\d{3,4})|(\d{2,3}[- ]\d{2,3}[- ]\d{2,3}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_BE_PHONE,
        "name": "Belarusian phone number",
        "doc": "detect phone numbers that use Belarusian format.",
    }
]