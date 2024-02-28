"""
Detection of phone numbers written with local notation (with or without country code), for Greek format.
"""


from pii_manager import PiiEnum

PATTERN_GR_PHONE = r'(\+30[ -])?[269]\d{1,4}[ -]((\d{2,4}[ -]\d{2,4}[ -]\d{2,4})|(\d{2,4}[ -]\d{2,4})|(\d{5,8}))'
# updating to catch numbers with - and loosening the rules slightly
#PATTERN_GR_PHONE = r'(\+30[ ])?[26]\d{1,3}[ ]((\d{5,7})|(\d[ ]\d{3}[ ]\d{4})|(\d{3,4}[ ]\d{4}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_GR_PHONE,
        "name": "Greek phone number",
        "doc": "detect phone numbers that use Greek format.",
    }
]