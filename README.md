# Prettify JSON

Outputs the contents of the json-file to the console in a convenient format (pretty print).

# Quickstart

The example of script launch on Linux, Python 3.5 and you need default.json, which can be downloaded from https://data.mos.ru/opendata/7710881420-magaziny-alkogolnye-napitki. You can specify a different file name.

```#!bash

$ python3 pprint_json.py test.json
Рабочий файл: test.json
{
    "address": {
        "city": "Ленинград",
        "postalCode": 101101,
        "streetAddress": "Московское ш., 101, кв.101"
    },
    "firstName": "Иван",
    "lastName": "Иванов",
    "phoneNumbers": [
        "812 123-1234",
        "916 123-4567"
    ]
}
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
