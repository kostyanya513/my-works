import json
from pprint import pprint

if __name__ == '__main__':

    def find_key(new: dict, old: dict, desired_list: list, differences={}) -> dict:
        for key, value in new.items():
            if isinstance(value, dict):
                find_key(new[key], old[key], desired_list)
            elif new[key] != old[key] and key in desired_list:
                differences[key] = old[key]
        return differences


    with open('json_old.json', 'r', encoding='utf-8') as json_old:
        old_file = json.load(json_old)
    with open('json_new.json', 'r', encoding='utf-8') as json_new:
        new_file = json.load(json_new)
    diff_list = ["services", "staff", "datetime"]

    result = find_key(new_file, old_file, diff_list)
    pprint(result)
    with open('result.json', 'w') as result_json:
        json.dump(result, result_json, indent=4)
