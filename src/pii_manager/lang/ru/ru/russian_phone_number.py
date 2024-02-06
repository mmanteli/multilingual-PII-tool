"""
Detection of phone numbers written with local notation (with or without country code), for Russian format.
"""


from pii_manager import PiiEnum

PATTERN_RU_PHONE = r'((\+7[ ])|(8[ ])|(00[ ]?7[ ])|(8-\d{1,3}[ ]))\d{2,3}[ ]((\d{3}-\d{2}-\d{2})|(\d{3}-\d{3}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_RU_PHONE,
        "name": "Russian phone number",
        "doc": "detect phone numbers that use Russian format.",
    }
]