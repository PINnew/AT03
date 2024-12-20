import requests

def get_cat_image() -> str:
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list) and len(data) > 0:
            return data[0]['url']
    return None

def get_cat_image_error() -> str:
    response = requests.get("https://api.thecatapi.com/v1/images/search/invalid")
    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list) and len(data) > 0:
            return data[0]['url']
    return None
