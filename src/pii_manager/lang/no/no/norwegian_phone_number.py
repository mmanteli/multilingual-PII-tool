"""
Detection of phone numbers written with local notation (with or without country code), for Norwegian format.
"""


from pii_manager import PiiEnum

PATTERN_NO_PHONE = r'((\+47 \d{2,3} )|(\d{2,3} ))((\d{2} \d{3})|(\d{2} \d{2} \d{2}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_NO_PHONE,
        "name": "Norwegian phone number",
        "doc": "detect phone numbers that use Norwegian format.",
    }
]