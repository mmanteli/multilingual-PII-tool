"""
Detection of phone numbers written with local notation (with or without country code), for ES.
Imported from the central definition in pii_manager.lang.any.spanish_phone_number
"""

from ...es.es.spanish_phone_number import PII_TASKS, PATTERN_ES_PHONE

__all__ = ['PII_TASKS', 'PATTERN_ES_PHONE']