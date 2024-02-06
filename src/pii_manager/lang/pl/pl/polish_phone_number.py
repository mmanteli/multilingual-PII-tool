"""
Detection of phone numbers written with local notation (with or without country code), for Polish format.
"""


from pii_manager import PiiEnum

PATTERN_PL_PHONE = r'(\+48 )?((\d{3} \d{3} \d{3})|(\d{2} \d{3} \d{2} \d{2}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_PL_PHONE,
        "name": "Polish phone number",
        "doc": "detect phone numbers that use Polish format.",
    }
]