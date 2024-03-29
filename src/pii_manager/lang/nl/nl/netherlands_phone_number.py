"""
Detection of phone numbers written with local notation (with or without country code), for Netherlands format.
"""


from pii_manager import PiiEnum

PATTERN_NL_PHONE = r'((\+31[ ]?\(0\)[ ]?\d{1,3}([ -]|[ ]-[ ]))|(\+31[ ]\d{1,3}[ -])|0|(\(\d{3}\)[ ]))((\d{6,8})|(\d{2}[ ]\d{2}[ ]\d{2}[ ]\d{2})|(\d{2,4}[ -]\d{3,5})|(\d{1,3}[ ]\d{2,4}[ ]\d{2,4}))'
# updated based on false negatives
#PATTERN_NL_PHONE = r'((\+31[ ])|0|(\(\d{3}\)[ ]))\d{1,2}[ ]?((\d{5,8})|(\d{3,4}[ ]\d{3,4}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_NL_PHONE,
        "name": "Netherlands phone number",
        "doc": "detect phone numbers that use Netherlands (Dutch) format.",
    }
]