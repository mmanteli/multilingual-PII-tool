"""
Detection of phone numbers written with local notation (with or without country code), for Latvian format.
"""


from pii_manager import PiiEnum

PATTERN_LA_PHONE = r'([567]\d{7})|((\+371[ ]\d{7,9})|(\+371[ ]\d{2}([ ]\d{3}){1,2})|(\+371[ ]\d{4}[ ]\d{4}))'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_LA_PHONE,
        "name": "Latvian phone number",
        "doc": "detect phone numbers that use Latvian format.",
    }
]