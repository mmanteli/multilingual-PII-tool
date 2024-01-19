"""
Detection of phone numbers written with local notation (with or without country code), for FR.
"""


from pii_manager import PiiEnum

PATTERN_FR_PHONE = r'(\+33[ ]\d([ ]\d{2}){4})|(0\d(([ ]\d{2}){4}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_FR_PHONE,
        "name": "French phone number",
        "doc": "detect phone numbers that use French format. Uses language context",
        "context": {
            "value": ["appeler","numéro", "numero","appelez","téléphone","tél", "tel"],
            "width": [16, 0],
            "type": "word",
        },
    }
]
