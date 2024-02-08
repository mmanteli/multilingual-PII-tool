# multilingual PII tool

Extension of BigScience PII-manager data-tool (https://github.com/bigscience-workshop/data_tooling/tree/master/pii-manager).
Contains new phone number recognition tasks for over 20 languages.
Test done using a different scripts than the unit testing feature, unit tests to be implemented.

See *Building* below for installation.

New mode also implemented: ``convert``, which converts the detected PII to a placeholder, e.g. ``example@email.com``. 
``convert`` implemented for ``PHONE_NUMBER``, ``EMAIL_ADDRESS``, and ``IP_ADDRESS``. See ``src/api/manager.py`` row 36->

Example usage:

```
from pii_manager import PiiEnum
from pii_manager.api import PiiManager
from pii_manager.lang import COUNTRY_ANY #, LANG_ANY

lang = "en" # or any other implemented one
country = COUNTRY_ANY  # this uses all rules for English: US, UK, CA, AU, IN
tasklist = (PiiEnum.IP_ADDRESS, PiiEnum.EMAIL_ADDRESS, PiiEnum.PHONE_NUMBER)   # Define here which tasks are to be used

# Define the detector:
proc = PiiManager(lang, country, tasks=tasklist, mode="convert")  # mode can be "tag", "replace" (default) or "convert"
# or debug (all_tasks=True needed for this)
#proc = PiiManager(lang, country, all_tasks=True, debug=True)

# get info of tasks, if you so desire:
print(proc.task_info())

text = "..."
redacted = proc(text)
print(redacted)
```
***

bigscience-workshop/data-tooling/pii-manager

This repository builds a Python package that performs PII processing for text
data i.e. replacement/tagging/extraction of PII (Personally Identifiable
Information aka [Personal Data]) items existing in the text.

The PII Tasks in the package are structured by language & country, since many
of the PII elements are language- and/or -country dependent.

## Requirements

The package needs at least Python 3.8, and uses the [python-stdnum] package to
validate identifiers.

## Usage

The package can be used:
 * As an API, in two flavors: function-based API and object-based API
 * As a command-line tool **NOTE**: Command-line tool has no "convert" mode implemented.

For details, see the [usage document].


## Building

The provided [Makefile] can be used to process the package:
 * `make pkg` will build the Python package, creating a file that can be
   installed with `pip`
 * `make unit` will launch all unit tests (using [pytest], so pytest must be
   available)
 * `make install` will install the package in a Python virtualenv. The
   virtualenv will be chosen as, in this order:
     - the one defined in the `VENV` environment variable, if it is defined
     - if there is a virtualenv activated in the shell, it will be used
     - otherwise, a default is chosen as `/opt/venv/bigscience` (it will be
       created if it does not exist)


## Contributing

To add a new PII processing task, please see the [contributing instructions].


[python-stdnum]: https://github.com/arthurdejong/python-stdnum
[Makefile]: Makefile
[pytest]: https://docs.pytest.org
[contributing instructions]: doc/contributing.md
[usage document]: doc/usage.md
[Personal Data]: https://en.wikipedia.org/wiki/Personal_data
