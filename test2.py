import pytest
import requests
from main2 import get_cat_image, get_cat_image_error

def test_get_cat_image():
    url = get_cat_image()
    assert url is not None, "URL should not be None"
    assert isinstance(url, str), "URL should be a string"
    assert url.startswith("https://"), "URL should start with 'https://'"
    response = requests.get(url)
    assert response.status_code == 200, "URL should return a 200 status code"

def test_get_cat_image_error():
    url = get_cat_image_error()
    assert url is None, "URL should be None for an invalid request"

if __name__ == "__main__":
    pytest.main()
