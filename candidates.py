import json


def candidates_json():
    with open("candidates.json", "r", encoding="utf-8") as read_file:
      candidates = json.load(read_file)
    return candidates

