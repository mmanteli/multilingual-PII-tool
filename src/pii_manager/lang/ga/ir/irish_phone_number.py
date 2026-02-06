"""
Detection of phone numbers written with local notation (with or without country code), for Irish format.
"""


from pii_manager import PiiEnum

PATTERN_IR_PHONE = r'\b((\+353[ ]\d{1,4}[ ])|(\+353[ ]\(\d{1,4}\)[ ])|(0\d{1,4}[ ])|(\(\d{1,4}\)[ ]))((\d{7,8})|(\d{3,4}[ ]\d{3,4}))\b'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_IR_PHONE,
        "name": "Irish phone number",
        "doc": "detect phone numbers that use Irish format.",
    }
]