"""
Detection and validation of Canadian Social Insurance Number
Imported from the central definition in pii_manager.lang.en.ca.social_insurance_number

Since it contains a check digit, it can be validated.
"""

from pii_manager.lang.en.ca.social_insurance_number import PII_TASKS, social_insurance_number, _SIN_REGEX

__all__ = ['PII_TASKS', 'social_insurance_number', '_SIN_REGEX']
