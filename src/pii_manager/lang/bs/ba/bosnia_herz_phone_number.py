"""
Detection of phone numbers written with local notation (with or without country code), for Bosnian-Herzegovinian format.
"""


from pii_manager import PiiEnum

PATTERN_BA_PHONE = r'((\+[ ]?387[ ]\d{2}[ ])|(0[ ]?\d{2}[ ]))\d{3}[ -]\d{3}'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_BA_PHONE,
        "name": "Bosnian-Herzegovinian phone number",
        "doc": "detect phone numbers that use Bosnian-Herzegovinian format.",
    }
]