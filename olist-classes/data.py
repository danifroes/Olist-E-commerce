import os
import pandas as pd

class Olist:

    #csv_path = os.path.join('/Users/daniellefroes/code/danifroes/03-Olist-Ecommerce/data/csv')

    def get_data(self):

        """
        This function returns a Python dict.
        Its keys are 'sellers', 'orders', 'order_items' etc...
        Its values are pandas.DataFrame loaded from csv files
        """
        root_dir = os.path.dirname(os.path.dirname(__file__))
        csv_path = os.path.join(root_dir, "data", "csv")

        file_names = [file_name for file_name in os.listdir(csv_path) if '.csv' in file_name]

        key_names = [key_names
                     .replace("olist_", " ")
                     .replace(".csv", " ")
                     .replace('_dataset', " ")
                     .strip()
                     for key_names in file_names]

        #dict keys
        data = {}
        for k, f in zip(key_names, file_names):
            data[k] = pd.read_csv(os.path.join(csv_path, f))
            data.keys()
        return data


    def get_matching_table(self):

        data = self.get_data()
        """
        This function returns a matching table between columns
        [ "order_id", "review_id", "customer_id", "product_id", "seller_id"]
        """
        orders = data['orders'][['customer_id', 'order_id']]
        reviews = data['order_reviews'][['order_id', 'review_id']]
        items = data['order_items'][['order_id', 'product_id','seller_id']]

        matching_table = orders\
        .merge(reviews, on = 'order_id', how = 'outer')\
        .merge(items, on = 'order_id', how = 'outer')
        return matching_table

    def ping(self):
        """
        You call ping I print pong.
        """
        print('pong')
