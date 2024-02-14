"""
Detection of phone numbers written with local notation (with or without country code), for Maltese format.
"""


from pii_manager import PiiEnum

PATTERN_MT_PHONE = r'((\+?356[ ]\d{4}[ ])|(2\d{3}[ ]))\d{4}'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_MT_PHONE,
        "name": "Maltese phone number",
        "doc": "detect phone numbers that use Maltese format.",
    }
]