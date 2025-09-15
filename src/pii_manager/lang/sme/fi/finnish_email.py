"""
Detection of finnish email addresses
"""

from pii_manager import PiiEnum


PATTERN_FI_EMAIL = r"[\w\.=-]+ (at) [\w\.-]+ \. [\w]{2,3}"


PII_TASKS = [
    {
        "pii":PiiEnum.EMAIL_ADDRESS,
        "type": "regex",
        "task":PATTERN_FI_EMAIL, 
        "name":"Finnish email address",
        "doc": "detect emails that use Finnish format."
    }
]