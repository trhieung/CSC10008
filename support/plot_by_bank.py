import matplotlib.pyplot as plt

data = {
    'results': [
        {'buy': 17279.0, 'currency': 'AUD', 'sell': 18348.0},
        {'buy': 18464.0, 'currency': 'CAD', 'sell': 19606.0},
        {'buy': 24911.0, 'currency': 'CHF', 'sell': 26452.0},
        {'buy': 27156.0, 'currency': 'EUR', 'sell': 28836.0},
        {'buy': 31622.0, 'currency': 'GBP', 'sell': 33577.0},
        {'buy': 204.0, 'currency': 'JPY', 'sell': 216.0},
        {'buy': 22975.0, 'currency': 'USD', 'sell': 23746.0}
    ]
}

currencies = [item['currency'] for item in data['results']]
sell_buy_diff = [item['sell'] - item['buy'] for item in data['results']]

plt.bar(currencies, sell_buy_diff)
plt.xlabel('Currency')
plt.ylabel('Sell - Buy')
plt.title('Difference between Sell and Buy Rates for Different Currencies')

# Add value labels to each column
plt.bar_label(plt.bar(currencies, sell_buy_diff), fmt='%d')

plt.show()
