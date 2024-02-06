"""
Test German phone numbers
"""

from pii_manager import PiiEnum
from pii_manager.api import PiiManager
from pii_manager.lang import COUNTRY_ANY

TEST = [
    # German
    ("Telefonnummer: +49 (0)30 4851923", "Telefonnummer: <PHONE_NUMBER>"),
    ("Telefonnummer: 01522 3433333", "Telefonnummer: <PHONE_NUMBER>"),
    ("Tel. 0049 30 901820", "Tel. <PHONE_NUMBER>"),
    ("Telefonnummer: 030 901820", "Telefonnummer: <PHONE_NUMBER>"),
    ("internatinal number: +358442759009", "international number: <PHONE_NUMBER>"),
    ("years: 2011-2013", "years: 2011-2013"),
]


def test10_ssn():
    obj = PiiManager("de", COUNTRY_ANY, PiiEnum.PHONE_NUMBER)
    for doc, exp in TEST:
        got = obj(doc)
        assert got == exp
