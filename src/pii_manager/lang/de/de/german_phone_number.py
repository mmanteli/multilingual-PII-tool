"""
Detection of phone numbers written with local phone number format (with our without country code), for DE
"""


from pii_manager import PiiEnum

PATTERN_DE_PHONE = r'((\+49[ ]\(0\)[ ]?\d{2,4})|(\+49[ ]?\d{2,4})|(0049[ ]?\d{2,4})|((0[ ]?\d{3,4})))(([ ]-[ ])|([ -]))((\d{2,3}[ -]\d{2,3}[ -]\d{2,3})|(\d{2,5}[ -]\d{3,5})|(\d{4,7}))'
# added [ ]-[ ] as one of the separators and a different way of grouping the digits
#PATTERN_DE_PHONE = r'((\+49[ ])|(0049[ ])|((0[ ]?))|(\+49[ ]\(0\)[ ]?))(\d{2,4}[ ])(\d{4,7})'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_DE_PHONE,
        "name": "German phone number",
        "doc": "detect phone numbers that use German format. ",
        #"context": {
        #    "value": ["Tel", "Telefon", "Telefonnummer", "Rufen", "Tel.Nr."],
        #    "width": [22, 0],
        #    "type": "word",
        #},
    }
]
