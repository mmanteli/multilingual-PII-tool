"""
Detection of phone numbers written with local notation (with or without country code), for IT.
"""


from pii_manager import PiiEnum


PATTERN_IT_PHONE = r'((\+39[- .\/]?[03]\d{1,3}[- .\/]?)|(\(39\)[ ]?\d{1,3}[- .\/])|([03]\d{1,3}[- .\/]?))((\d{5,8})|(\d{3,4}[- .]\d{3,4}))'
# this was modified because
# 1. Italians write their phone numbers however they please (humor) (i.e. use -, or ., or /)
# 2. applying countrycode as ()? is risky
#PATTERN_IT_PHONE = r'(((\+39|0039|\(\+39\))[ ])?0\d{1,2}[ -](\d{5,8}|\d{3}[ -]\d{2,5}))|((\+39-)?0(\d{1,2}-\d{5,8}|\d{1,2}-\d{3}-\d{2,5}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_IT_PHONE,
        "name": "Italian phone number",
        "doc": "detect phone numbers that use Italian format.",
        #"context": {
        #    "value": ["numero", "chiamare", "chiamata", "chiama", "telefono", "tel", "Tel"],
        #    "width": [16, 0],
        #    "type": "word",
        #},
    }
]