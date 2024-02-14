"""
Detection of phone numbers written with local notation (with or without country code), for N. Macedonian format.
"""


from pii_manager import PiiEnum

PATTERN_MK_PHONE = r'((\+389[ ]\d{1,3}[ ])|(0\d{1,3}[ ])|(\+389[ ]\(0\)[ ]\d{1,3}[ ]))((\d{5,8})|(\d{3,4}[ -]\d{3,4}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_MK_PHONE,
        "name": "N. Macedonian phone number",
        "doc": "detect phone numbers that use N. Macedonian format.",
    }
]