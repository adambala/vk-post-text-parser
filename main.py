from vk_api.exceptions import VkApiError
from typing import List, Dict
import vk_api
import json

API_VERSION = "5.131"
POSTS_AT_A_TIME = 100  # VK API post count limit


def is_appropriate_post(post_data) -> bool:
    post_text = post_data["text"]
    return any((
        not post_text,
        not any(restricted_word in post_text for restricted_word in RESTRICTED_WORDS),
        not AD_ALLOWED and post_data["ad"],
        not REPOST_ALLOWED and post_data["repost"],
    ))


def get_max_offset() -> int:
    try:
        return api.method(
            method="wall.get",
            values={"domain": DOMAIN, "count": POSTS_AT_A_TIME}
        )["count"]
    except VkApiError:
        raise VkApiError("Invalid access token. How to get your own token: "
                         "https://dev.vk.com/api/access-token/getting-started")


def parse_wall_data(post_offset) -> List[Dict]:
    data = api.method(
        method="wall.get",
        values={"domain": DOMAIN, "offset": post_offset, "count": POSTS_AT_A_TIME}
    )["items"]

    return [{
        "text": post["text"],
        "ad": post["marked_as_ads"],
        "repost": "copy_history" in post,
    } for post in data]


if __name__ == "__main__":
    with open("config.json", "r", encoding="utf-8") as file:
        f_data = json.load(file)

        ACCESS_TOKEN = f_data["access_token"]
        DOMAIN = f_data["domain"]

        RESTRICTED_WORDS = tuple(f_data["post_filter"]["restricted_words"])
        AD_ALLOWED = f_data["post_filter"]["ad_allowed"]
        REPOST_ALLOWED = f_data["post_filter"]["repost_allowed"]

        post_number = f_data["post_number"]

        del f_data

    api = vk_api.VkApi(token=ACCESS_TOKEN, api_version=API_VERSION)
    max_offset = get_max_offset()

    if not post_number:
        post_number = max_offset

    post_offset = 1
    with open("output.txt", "w", encoding="utf-8") as file:
        while (post_offset <= post_number) and (post_offset <= max_offset):
            posts = parse_wall_data(post_offset)
            post_offset += POSTS_AT_A_TIME

            for post_data in posts:
                if is_appropriate_post(post_data):
                    file.write(post_data["text"] + "\n")
