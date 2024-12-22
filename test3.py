import pytest
from unittest.mock import patch
from main3 import get_random_cat_image


def test_get_random_cat_image_success():
    mock_response = [
        {"id": "MTk3NDc4MQ", "url": "https://cdn2.thecatapi.com/images/MTk3NDc4MQ.jpg", "width": 500, "height": 666}]

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        url = get_random_cat_image()

        assert url == "https://cdn2.thecatapi.com/images/MTk3NDc4MQ.jpg"


def test_get_random_cat_image_not_found():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404

        url = get_random_cat_image()

        assert url is None  # Проверяем, что функция возвращает None
