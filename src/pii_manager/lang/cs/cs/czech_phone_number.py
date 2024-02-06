"""
Detection of phone numbers written with local notation (with or without country code), for Czech Rep. format.
"""


from pii_manager import PiiEnum

PATTERN_CS_PHONE = r'((\+420[ ]\d{3}[ ])|(\d{3}[ ]))\d{3}[ ]\d{3}'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_CS_PHONE,
        "name": "Czech phone number",
        "doc": "detect phone numbers that use Czech Rep. format.",
    }
]