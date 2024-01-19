"""
Detection of phone numbers written with local phone number format (with our without country code), for DE
"""


from pii_manager import PiiEnum

PATTERN_DE_PHONE = r'((\+49[ ])|(0049 )|((0[ ]?))|(\+49 \(0\)))(\d{2,4}[ ])(\d{6,7})'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_DE_PHONE,
        "name": "German phone number",
        "doc": "detect phone numbers that use German format. Uses language context",
        "context": {
            "value": ["Tel", "Telefon", "Telefonnummer", "Rufen", "Tel.Nr."],
            "width": [22, 0],
            "type": "word",
        },
    }
]
