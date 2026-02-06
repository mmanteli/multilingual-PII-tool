"""
Detection of U.S. Social Security Number.
Imported from the central definition in pii_manager.lang.en.us.social_security_number

We just match on the number, it cannot be
validated using only the number since it does not carry a checksum
"""

from pii_manager.lang.en.us.social_security_number import PII_TASKS, _SSN_PATTERN

__all__ = ['PII_TASKS', '_SSN_PATTERN']
