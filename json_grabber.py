import json
import requests
import re


def get_json():
    """
    stupidly parse the source and encode json
    :return: json dictionary
    """
    resp = requests.get("http://offthegridsf.com/markets").content
    for line in resp.splitlines():
        if "OTGMarketsJson" in line:
            json_data = re.search(r".*OTGMarketsJson = '(?P<dat>.*)';</script>", line).groupdict()
            return json.loads(json_data['dat'].replace('\\', ''))
    return None