"""
Detection of phone numbers written with local phone number format (with our without country code), for the US
"""


from pii_manager import PiiEnum

PATTERN_US_PHONE = r'(((\+1-)|(1-))?\d{3}[ -]\d{3}[ -]\d{4})|(\(\d{3}\)[ -]\d{3}[ -]\d{4})|((\+1)\d{10})'
# Original: (((\+1-)|(1-))?\d{3}[ -]\d{3}[ -]\d{4})|(\(\d{3}\)[ -]\d{3}[ -]\d{4})|((\+1)?\d{10})
# removed the one ? since it lead to more errors than it corrected


PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_US_PHONE,
        "name": "US phone number",
        "doc": "detect phone numbers that use US format. ",
    }
]
