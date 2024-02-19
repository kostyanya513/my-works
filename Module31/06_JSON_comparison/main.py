import json
from pprint import pprint

if __name__ == '__main__':

    def find_key(new: dict, old: dict, desired_list: list, differences=None) -> dict:
        if differences is None:
            differences = {}
        for key, value in new.items():
            if key in desired_list and new[key] != old[key]:
                differences[key] = new[key]
            elif isinstance(value, dict):
                res = find_key(new[key], old[key], desired_list)
                if res:
                    differences[key] = res
            elif isinstance(value, list):
                for index, j_index in enumerate(value):
                    if isinstance(j_index, dict):
                        result_list = find_key(new[key][index], old[key][index], desired_list)
                        if result_list:
                            differences[key] = result_list
        return differences

    with open('json_old.json', 'r', encoding='utf-8') as json_old:
        old_file = json.load(json_old)
    with open('json_new.json', 'r', encoding='utf-8') as json_new:
        new_file = json.load(json_new)
    diff_list = ["cost", "id"]

    result = find_key(new_file, old_file, diff_list)
    pprint(result)

    with open('result.json', 'w') as result_json:
        json.dump(result, result_json, indent=4)
