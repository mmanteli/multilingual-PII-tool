"""
Detection of phone numbers written with local notation (with or without country code), for Serbian format.
"""


from pii_manager import PiiEnum

PATTERN_SR_PHONE = r'\b((\+381[ ]\d{2}[ ]?)|(0\d{2,3}[ ]?))(\d{2,3}[ ]\d{2}[ ]\d{2}|\d{6,7})\b'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_SR_PHONE,
        "name": "Serbian phone number",
        "doc": "detect phone numbers that use Serbian format.",
    }
]