"""
Detection of phone numbers written with local notation (with or without country code), for Brazilian format.
"""


from pii_manager import PiiEnum

PATTERN_BR_PHONE = r'((\+55[ ]\d{2})[ ]|(\d{2}[ ])|(\(\d{2}\)[ ]))(\d{4,5}-\d{4})'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_BR_PHONE,
        "name": "Brazilian phone number",
        "doc": "detect phone numbers that use Brazilian format.",
    }
]
