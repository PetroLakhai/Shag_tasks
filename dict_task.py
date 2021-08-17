import requests

data = {
    "data": [
        {"name": "name_1"},
        {"name": "name_2"},
        {"name": "name_3"},
        {"name": "name_4", "data": [
            {"name": "name_5"},
            {"name": "name_7"},
            {"name": "name_8", "data": [
                {"name": "name_9"},
                {"name": "name_10", "data": [
                    {"name": "name_11"},
                    {"name": "name_12"},
                    {"name": "name_13"},
                    {"name": "name_14", "data": {
                        "res": "ok"
                    }}
                ]}
            ]}
        ]}
    ],
    "name": "name"
}

request = requests.get('https://6112b7a489c6d00017ac0505.mockapi.io/test_dict')
print(request.text)

data = data.get('data')
list_of_values = []


def _func_(data):
    for obj in data:
        for value in obj.values():
            if type(value) == dict:
                for value in value.values():
                    list_of_values.append(value)
            elif type(value) == str:
                list_of_values.append(value)
            elif type(value) == list:
                _func_(value)


def contains_ok(list_of_values):
    if 'ok' in list_of_values:
        print("Yes")
    else:
        print("No")


_func_(data)

print(f"All values in data: {list_of_values}.")
print("Does the date contain the word ok in the values?")
filter(contains_ok(list_of_values), list_of_values)


