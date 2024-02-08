"""
Detection of phone numbers written with local notation (with or without country code), for Slovenian format.
"""


from pii_manager import PiiEnum

PATTERN_SL_PHONE = r'((\+386[ ]\d{1,2}[ ]?)|(0\d{1,3}[ ]?)|(\(0\d{1,2}\)[ ]))(\d{2,3}[ ]\d{2}[ ]\d{2}|\d{6,7}|\d{3}[ ]\d{3,4})'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_SL_PHONE,
        "name": "Slovenian phone number",
        "doc": "detect phone numbers that use Slovenian format.",
    }
]