"""
Detection and validation of Finnish Personal ID.

Since it contains a check digit, it can be validated.
"""



check_digit = {0 :"0", 
               1 : "1", 
               2 : "2",
               3 : "3",
               4 : "4",
               5 : "5",
               6 : "6",
               7 : "7",
               8 : "8",
               9 : "9",
               10 : "A",
               11 : "B",
               12 : "C",
               13 : "D",
               14 : "E",
               15 : "F",
               16 : "H",
               17 : "J",
               18 : "K",
               19 : "L",
               20 : "M",
               21 : "N",
               22 : "P",
               23 : "R",
               24 : "S",
               25 : "T",
               26 : "U",
               27 : "V",
               28 : "W",
               29 : "X",
               30 : "Y"
              }

import re


from typing import Iterable

from pii_manager import PiiEnum


def is_valid_hetu(candidate):
    number_as_string = str(candidate)[0:6]+str(candidate)[7:10]
    check = check_digit[int(number_as_string)%31]
    if check == str(candidate[-1]):
        return True
    else:
        return False

_HETU_REGEX = re.compile(r"[0123]\d(0\d|11|12)\d{2}[\-\+ ]\d{3}.", flags=re.X)


def hetu(doc: str) -> Iterable[str]:
    """
    Finnish personal ID (detect and validate)
    """
    for candidate in _HETU_REGEX.findall(doc):
        if is_valid_hetu(candidate):
            yield candidate


PII_TASKS = [(PiiEnum.GOV_ID, social_insurance_number)]
