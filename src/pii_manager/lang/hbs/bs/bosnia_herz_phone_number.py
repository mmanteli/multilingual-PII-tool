"""
Detection of phone numbers written with local notation (with or without country code), for Bosnian-Herzegovinian format.
Imported from the central definition in pii_manager.lang.bs.ba.bosnia_herz_phone_number
"""

from pii_manager.lang.bs.ba.bosnia_herz_phone_number import PII_TASKS, PATTERN_BA_PHONE

__all__ = ['PII_TASKS', 'PATTERN_BA_PHONE']
