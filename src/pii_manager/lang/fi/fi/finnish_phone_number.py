"""
Detection of phone numbers written with local phone number format (with our without country code), for FI
"""


from pii_manager import PiiEnum

PATTERN_FI_PHONE = r'(((\+358[ ]\d{2}[ ])|(0\d{1,2}[ ]))((\d{7,8})|(\d{2,4}[ ]\d{3,4})))|(0\d{3}[ ](\d{3,4}[ ]\d{3,4}|\d{6,8}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_FI_PHONE,
        "name": "Finnish phone number",
        "doc": "detect phone numbers that use Finnish format.",
        #"context": {
        #    "value": ["puh.", "p.", "kotip.", "matkapuh.", "puhelin"],
        #    "width": [22, 0],
        #    "type": "word",
        #},
    }
]
