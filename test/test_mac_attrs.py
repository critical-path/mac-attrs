import constants
import pytest

@pytest.mark.parametrize("url", constants.INDEX_URLS)
def test_index_page(pickle, client, url):
  response = client.get(url)
  assert response.status_code == 200
  assert "enter 12 hexadecimal digits in plain, hyphen, colon, or dot notation." in response.data.decode()

@pytest.mark.parametrize("url", constants.ATTRIBUTES_URLS)
def test_attributes_page(pickle, client, url):
  response = client.get(url)
  assert response.status_code == 200
  assert "<table class=\"table\">" in response.data.decode()

@pytest.mark.parametrize("url", constants.ERROR_URLS)
def test_error_page(pickle, client, url):
  response = client.get(url)
  assert response.status_code == 400
  assert "error: invalid address." in response.data.decode()
