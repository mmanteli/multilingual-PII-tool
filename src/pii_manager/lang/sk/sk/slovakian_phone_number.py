"""
Detection of phone numbers written with local notation (with or without country code), for Slovakian format.
"""


from pii_manager import PiiEnum

PATTERN_SK_PHONE = r'((\+421[ ]\d{1,3}[\/ ])|(\d{1,4}[\/ ]))(\d{3}[ ]\d{3}[ ]\d{2}|\d{2}[ ]\d{2}[ ]\d{2}[ ]\d{2}|\d{3}[ ]\d{3})'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_SK_PHONE,
        "name": "Slovakian phone number",
        "doc": "detect phone numbers that use Slovakian format.",
    }
]