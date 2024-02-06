"""
Detection of phone numbers written with local phone number format (with our without country code), for Austria
"""


from pii_manager import PiiEnum

PATTERN_AT_PHONE = r'((\+43 )|(0043 )|(0))\d{1,3} \d{5,8}'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_AT_PHONE,
        "name": "Austrian phone number",
        "doc": "detect phone numbers that use Austrian format. ",
    }
]
