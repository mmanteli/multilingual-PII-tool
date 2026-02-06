"""
Detection of phone numbers written with local phone number format (with our without country code), for the US
Imported from the central definition in pii_manager.lang.en.us.us_phone_number
"""

from pii_manager.lang.en.us.us_phone_number import PII_TASKS, PATTERN_US_PHONE

__all__ = ['PII_TASKS', 'PATTERN_US_PHONE']
