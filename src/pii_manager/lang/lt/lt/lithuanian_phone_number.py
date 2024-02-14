"""
Detection of phone numbers written with local notation (with or without country code), for Lithuanian format.
"""


from pii_manager import PiiEnum

PATTERN_LT_PHONE = r'((\+370[ ]\d{1,2}[ ])|(\+370[ ])|(\(\d{2,4}\)[ ]))((\d{2,3}[ ]\d{4})|(\d{3}[ ]\d{2}[ ]\d{2}))|(\(370[ ]\d\)[ ]\d{3}[ ]\d{4})'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_LT_PHONE,
        "name": "Lithuanian phone number",
        "doc": "detect phone numbers that use Lithuanian format.",
    }
]