"""
Detection of phone numbers written with local notation (with or without country code), for Bulgarian format.
"""


from pii_manager import PiiEnum

PATTERN_BG_PHONE = r'((\(\+359[ ]\d{1,3}\)[ ])|(\(\+359\)[ ]?)|(\+359[ ]\(0\)[ ]?\d{1,3}[ \/]?)|(\+359[ ]?\d{1,3}[\/]?[ ]?)|(0\d{1,2}[\/]?[ ]?))((\d{5,9})|(\d{2,3}[ ]\d{2,3}[ ]\d{2,3})|(\d{1,4}[ ]\d{3,4}))'
# updated based on false negatives
#PATTERN_BG_PHONE = r'(((\+359[ ]?\d{1,3}[ ]?)|(0\d[ \/][ ]?))\d{1,3}[ ]?\d{3,4})|(\+359[ ]\(0\)\d\/\d[ ]\d{4,6})' 


PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_BG_PHONE,
        "name": "Bulgarian phone number",
        "doc": "detect phone numbers that use Bulgarian format.",
    }
]