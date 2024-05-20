import pandas as pd
from utils.api.get_data import get_api_data


def extract(url_carts, url_products):
  carts_data = get_api_data(url=url_carts)
  products_data = get_api_data(url=url_products)

  carts_df = pd.DataFrame(data=carts_data)
  products_df = pd.DataFrame(data=products_data)
  
  return carts_df, products_df
