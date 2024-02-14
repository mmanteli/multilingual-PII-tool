"""
Detection of phone numbers written with local phone number format (with our without country code), for UK
"""


from pii_manager import PiiEnum

from ...ga.ir.irish_phone_number import PATTERN_IR_PHONE



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_IR_PHONE,
        "name": "Irish phone number",
        "doc": "detect phone numbers that use Irish format. ",
    }
]
