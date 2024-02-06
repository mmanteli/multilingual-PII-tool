"""
Detection of phone numbers written with local notation (with or without country code), for Romanian format.
"""


from pii_manager import PiiEnum

PATTERN_RO_PHONE = r'((\+40 )|(0))((\d{2,3}[ -]\d{3,4}[ -]\d{3,4})|(\d{9,10}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_RO_PHONE,
        "name": "Romanian phone number",
        "doc": "detect phone numbers that use Romanian format.",
    }
]