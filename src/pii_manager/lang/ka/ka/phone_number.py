"""
Detection of phone numbers written with local notation (with or without country code), for Georgian format.
"""


from pii_manager import PiiEnum

PATTERN_KA_PHONE = r'(?:\+995[ -]?)?(?:\(?0?\d{2,3}\)?[ -]?)?\d{3}[ -]?\d{3,4}'
# updating to catch numbers with - and loosening the rules slightly
#PATTERN_GR_PHONE = r'(\+30[ ])?[26]\d{1,3}[ ]((\d{5,7})|(\d[ ]\d{3}[ ]\d{4})|(\d{3,4}[ ]\d{4}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_KA_PHONE,
        "name": "Georgian phone number",
        "doc": "detect phone numbers that use Georgian format.",
    }
]