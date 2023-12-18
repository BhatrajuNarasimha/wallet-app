from ._anvil_designer import report_analysisTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
import re  # Import the regular expression module
from anvil.tables import app_tables

class report_analysis(report_analysisTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.refresh_data()

    def refresh_data(self):
        # Call the server function to get transactions data
        transactions = anvil.server.call('get_transactions')

        # Organize data for plotting (example: aggregate by date and type)
        data_for_plot = {}
        for transaction in transactions:
            date = transaction['date']
            trans_type = transaction['transaction_type']

            if date not in data_for_plot:
                data_for_plot[date] = {'Deposit': 0, 'Account to E-wallet': 0}

            # Extract numeric value from the 'money' field using regular expressions
            money_match = re.search(r'[-€$]?([\d,.]+)', transaction['money'])
            if money_match:
                money_amount = float(money_match.group(1).replace(',', ''))
            else:
                # Handle cases where no numeric value is found
                money_amount = 0

            if trans_type == 'Deposit':
                data_for_plot[date]['Deposit'] += money_amount
            elif trans_type == 'Account to E-wallet':
                data_for_plot[date]['Account to E-wallet'] += money_amount

        # Plot the data
        categories = list(data_for_plot.keys())
        deposit_values = [data['Deposit'] for data in data_for_plot.values()]
        e_wallet_values = [data['Account to E-wallet'] for data in data_for_plot.values()]

        self.plot_1.data = [
            {'x': categories, 'y': deposit_values, 'type': 'bar', 'name': 'Deposit'},
            {'x': categories, 'y': e_wallet_values, 'type': 'bar', 'name': 'Account to E-wallet'}
        ]
