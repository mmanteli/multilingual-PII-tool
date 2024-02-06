"""
Detection of phone numbers written with local notation (with or without country code), for Portuguese format.
"""


from pii_manager import PiiEnum

PATTERN_PT_PHONE = r'((\+351 (\d{2,3})|(\d{2}\(\d\))|(\+351 \d{2,3}\(\d\))) \d{3} \d{3,4})|(00351 ((\d{3} \d{4,6})|(\d{7,10})))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_PT_PHONE,
        "name": "Portuguese phone number",
        "doc": "detect phone numbers that use Portuguese format.",
    }
]
