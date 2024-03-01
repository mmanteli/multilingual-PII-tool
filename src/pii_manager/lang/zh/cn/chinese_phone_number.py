"""
Detection of phone numbers written with local phone number format for China
This is last minute implementation and thus taken from 
https://regex101.com/library/dnOlNH?filterFlavors=javascript&filterFlavors=python&orderBy=RELEVANCE&page=5&search=phone
I also define separate for exceptions, like 
+ 86-24-31523801
which are found in our data.
"""


from pii_manager import PiiEnum

PATTERN_ZH_PHONE = r'(13[4-9]|14[7-8]|15[0-27-9]|178|18[2-47-8]|198|13[0-2]|14[5-6]|15[5-6]|166|17[5-6]|18[5-6]|133|149|153|17[37]|18[0-19]|199|17[0-1])[0-9]{8}'



PII_TASKS = [
    {
        "pii": PiiEnum.PHONE_NUMBER,
        "type": "regex",
        "task": PATTERN_ZH_PHONE,
        "name": "Chinese phone number",
        "doc": "detect phone numbers that use Chinese format. ",
    }
]
