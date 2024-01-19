"""
Detection of phone numbers written with local notation (with or without country code), for ES.
"""


from pii_manager import PiiEnum

PATTERN_ES_PHONE = r'((\+34[ ]|0034[ ])?\d{2,3}[ ]\d{3}[ ]\d{3,4})|((\+34[ ]|0034[ ])?\d{2,3}([ ]\d{2}){3})'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_ES_PHONE,
        "name": "Spanish phone number",
        "doc": "detect phone numbers that use Spanish format. Uses language context",
        "context": {
            "value": ["teléfono", "telefono", "telf", "teléf.", "tel.", "tlf", "tfno", "numero","llama"],
            "width": [16, 0],
            "type": "word",
        },
    }
]