from DefaultClient import *


class DatabaseInterface:
    def __init__(self):
        self.client = DefaultClient()

    def fetch_all_stocks_for_company_in_last_five_minutes(self, query_map):
        self.client.fetch_all_stocks_for_company_in_last_five_minutes(query_map)
