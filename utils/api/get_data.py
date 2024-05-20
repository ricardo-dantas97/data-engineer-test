import requests


def get_api_data(url):
  try:
    r = requests.get(url)
    data = r.json()
    return data
  except requests.exceptions.RequestException as e: 
    print(f'Request error: {e}')