"""
French Government-issued IDs:
  - NIR (Numéro de Sécurité Sociale)
Imported from the central definition in pii_manager.lang.fr.fr.govid
"""

from pii_manager.lang.fr.fr.govid import PII_TASKS, FrenchNIR, _NIR_PATTERN

__all__ = ['PII_TASKS', 'FrenchNIR', '_NIR_PATTERN']
