"""
Detection of phone numbers written with local notation (with or without country code), for Estonian format.
"""


from pii_manager import PiiEnum

PATTERN_ET_PHONE = r'(((\+372)|(\(\+372\)))[ ])?((\d{3,4}[ ]\d{3,4})|(\d{2,3}[ ]\d{2,3}[ ]\d{2,3}))'
# Updated based on false negatives; note: ?'ing the country code leads to false positives, but this is simply due to estonian numbers being ambiguous.
#PATTERN_ET_PHONE = r'((\+372)|(\(\+372\)))[ ]((\d{3,4}[ ]\d{4})|(\d{3}[ ]\d{2}[ ]\d{2}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_ET_PHONE,
        "name": "Estonian phone number",
        "doc": "detect phone numbers that use Estonian format.",
    }
]