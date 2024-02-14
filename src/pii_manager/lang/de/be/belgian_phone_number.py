"""
Detection of phone numbers written with local notation for Belgium.
"""


from pii_manager import PiiEnum

PATTERN_BE_PHONE = r'((\+32[ ]\d{1,3}[ ])|(0\d{1,3}[ ]))\d{2,3}[ ]\d{2}[ ]\d{2}'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_BE_PHONE,
        "name": "Belgian phone number",
        "doc": "detect phone numbers that use Belgian format. ",
        #"context": {
        #    "value": ["appeler","numéro", "numero","appelez","téléphone","tél", "tel"],
        #    "width": [16, 0],
        #    "type": "word",
        #},
    }
]
