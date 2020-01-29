import json


def bin_to_dict(bin):
    return json.loads(bin.decode("utf-8"))