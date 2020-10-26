from django.conf import settings
from requests.auth import HTTPBasicAuth
from requests import get
from rest_framework import status

root_url = 'http://127.0.0.1:8000/'
products_url = 'http://127.0.0.1:8000/products/'
orders_url = 'http://127.0.0.1:8000/orders/'

auth_user = HTTPBasicAuth('Default User', 'my_store_secret')


def test_get_root_url_without_authentication_returning_401():
    
    request = get(root_url)

    assert request.status_code == status.HTTP_401_UNAUTHORIZED


def test_get_root_url_with_authentication_returning_200():
    
    request = get(root_url, auth=auth_user)

    assert request.status_code == status.HTTP_200_OK


def test_get_products_returning_200():
    
    request = get(products_url, auth=auth_user)

    assert request.status_code == status.HTTP_200_OK


def test_get_products_detail_returning_200():

    request = get(products_url + '1', auth=auth_user)

    assert request.status_code == status.HTTP_200_OK


def test_get_orders_returning_200():
    
    request = get(orders_url, auth=auth_user)

    assert request.status_code == status.HTTP_200_OK


def test_get_orders_detail_returning_200():

    request = get(orders_url + '1', auth=auth_user)

    assert request.status_code == status.HTTP_200_OK

