"""
Spanish Goverment-issued IDs:
  - DNI (Documento Nacional de Identidad)
  - NIE (Número de Identificación de Extranjero)
Imported from the central definition in pii_manager.lang.es.es.govid
"""

from pii_manager.lang.es.es.govid import PII_TASKS, SpanishDniNie, _DNI_PATTERN, _NIE_PATTERN

__all__ = ['PII_TASKS', 'SpanishDniNie', '_DNI_PATTERN', '_NIE_PATTERN']
