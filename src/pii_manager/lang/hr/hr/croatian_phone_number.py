"""
Detection of phone numbers written with local notation (with or without country code), for Croatian format.
"""


from pii_manager import PiiEnum

PATTERN_HR_PHONE = r'((\+385[ ])|(0)|(0[ ]))\d{1,2}[ ]\d{3,4}[ ]\d{3,4}'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_HR_PHONE,
        "name": "Croatian phone number",
        "doc": "detect phone numbers that use Croatian format.",
    }
]