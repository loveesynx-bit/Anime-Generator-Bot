import requests
from json.decoder import JSONDecodeError
from requests.exceptions import RequestException
from config import URL
from modules.enums import PicCategory, PicType


def generate_pic(type: PicType, category: PicCategory) -> str:
    json_data = False
    params = {
        "IncludedTags": category.value,
        "IsNsfw": "True" if type == PicType.NSFW else "False",
    }
    response = requests.get(URL.API, params=params, headers=URL.HEARDERS)
    try:
        response.raise_for_status()
    except RequestException:
        return
    try:
        json_data = response.json()
    except JSONDecodeError:
        return
    return json_data["items"][0]["url"] if json_data and json_data.get("items") else None
