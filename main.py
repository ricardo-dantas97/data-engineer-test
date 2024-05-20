from utils.etl.extract import extract
from utils.etl.transform import transform
from utils.etl.load import load


url_carts = 'https://fakestoreapi.com/carts'
url_products = 'https://fakestoreapi.com/products'
output_path = 'data/carts_data.parquet'


def main():
  carts_df, products_df = extract(url_carts, url_products)
  final_df = transform(carts_df, products_df)
  load(final_df, output_path)


if __name__ == '__main__':
  main()