"""
Detection of phone numbers written with local phone number format (with our without country code), for UK
"""


from pii_manager import PiiEnum

PATTERN_UK_PHONE = r'((\+49[ ])|(0049 )|((0[ ]?))|(\+49 \(0\)))(\d{2,4}[ ])(\d{6,7})'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_UK_PHONE,
        "name": "UK phone number",
        "doc": "detect phone numbers that use UK format. ",
    }
]
