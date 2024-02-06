"""
Detection of phone numbers written with local notation (with or without country code), for Swedish format.
"""


from pii_manager import PiiEnum

PATTERN_SV_PHONE = r'((\+46 \(0\)\d-)|(\+46 )|(0\d-))((\d{7,9})|(\d{2} \d{3} \d{2}) \d{2}|(\d{3} \d{3} \d{2})|(\d{3,4} \d{3,5}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_SV_PHONE,
        "name": "Swedish phone number",
        "doc": "detect phone numbers that use Swedish format.",
    }
]