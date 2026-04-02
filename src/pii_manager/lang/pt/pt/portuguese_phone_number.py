"""
Detection of phone numbers written with local notation (with or without country code), for Portuguese format.
"""


from pii_manager import PiiEnum

PATTERN_PT_PHONE = r'\b(?:\+351\s?)[239]\d(?:[\s.-]?\d){7}\b'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_PT_PHONE,
        "name": "Portuguese phone number",
        "doc": "detect phone numbers that use Portuguese format.",
    }
]
