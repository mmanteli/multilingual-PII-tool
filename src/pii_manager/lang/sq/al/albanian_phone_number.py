"""
Detection of phone numbers written with local notation (with or without country code), for Albanian format.
"""


from pii_manager import PiiEnum

PATTERN_AL_PHONE = r'((00355[ ]\d{1,3}[ \/])|(\+355[ ]\d{1,3}[ ])|(\+355[ ]\(\d{2}\)[ ]\d{1,3}[ ])|(0[ ]\d{1,3} ))((\d{7,8})|(\d{3,4}[ ]\d{3,4}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_AL_PHONE,
        "name": "Albanian phone number",
        "doc": "detect phone numbers that use Albanian format.",
    }
]