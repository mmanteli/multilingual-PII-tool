"""
Detection of phone numbers written with non-standard format for China
Defined for exceptions such as
+ 86-24-31523801
which are found in our data.
"""


from pii_manager import PiiEnum

PATTERN_ZH_PHONE = r'((\+86[ -])|(\+[ ]86[ -]))\d{2,3}-\d{7,9}'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_ZH_PHONE,
        "name": "Non-standard Chinese phone number",
        "doc": "detect phone numbers that use non-standard Chinese format. ",
    }
]
