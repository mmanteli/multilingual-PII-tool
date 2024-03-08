"""
Detection of phone numbers written with local notation (with or without country code), for Hungarian format.
"""


from pii_manager import PiiEnum

PATTERN_HU_PHONE = r'((\(\+36[ -]\d{1,2}\))|(\+36[ -]\(\d{1,2}\))|(\+36([ -/]|[ ]-[ ])\d{1,2})|(0\d[ \/]\d{2}))[- \/]?((\d{1}[ -]\d{3}[ -]\d{3,4})|(\d{3}[ -]\d{2}[ -]\d{2})|(\d{3}[- ]\d{3,4})|(\d{3,4}[- ]\d{3}))|((\+36[ ])|(00[ ]?36[ ])|(\d{2}[ -\/]))(\d{1,2}[ -]\d{3}[ -]\d{3,4})'
# updated based on false negatives
#PATTERN_HU_PHONE = r'((\+36[ ])|(00[ ]36[ ])|(\d{2}[ ]))(\d{1,2}[ ]\d{3}[ ]\d{3,4})'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_HU_PHONE,
        "name": "Hungarian phone number",
        "doc": "detect phone numbers that use Hungarian format.",
    }
]