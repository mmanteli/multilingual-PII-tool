"""
Detection of phone numbers written with local notation (with or without country code), for Ukranian format.
"""


from pii_manager import PiiEnum

PATTERN_UK_PHONE = r'((\+380 )|(0)|(00[ ]?380 ))\d{2,3} ((\d{3}-\d{2}-\d{2})|(\d{3}-\d{3}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_UK_PHONE,
        "name": "Ukrainian phone number",
        "doc": "detect phone numbers that use Ukrainian format.",
    }
]