import pandas as pd


def transform_products_df(df):
  colums_to_delete = ['description', 'image', 'rating', 'title']
  df = df.drop(columns=colums_to_delete)
  
  return df


def transform_carts_df(df):
  df = df.explode('products')
  df = pd.concat([df, df['products'].apply(pd.Series)], axis=1)
  df['date'] = pd.to_datetime(df['date']).dt.date
  df = df.drop(columns=['products', '__v'])

  rename_columns = {
    'id': 'cart_id',
    'productId': 'product_id',
    'userId': 'user_id'
  }

  df = df.rename(columns=rename_columns)

  return df


def transform(carts_df, products_df):
  carts_df = transform_carts_df(carts_df)
  products_df = transform_products_df(products_df)

  df = carts_df.merge(
    products_df[['price', 'category', 'id']],
    left_on='product_id',
    right_on='id'
  ).drop(columns=['id'])

  df['total_price'] = df['quantity'] * df['price']

  aggregations = {
    'quantity': 'sum',
    'total_price': 'sum',
    'category': lambda x: x.value_counts().idxmax()
}

  df = df.groupby(['cart_id', 'user_id', 'date']).agg(aggregations).reset_index()

  rename_columns = {
    'category': 'top_category',
    'quantity': 'total_products'
  }

  df = df.rename(columns=rename_columns)

  return df
