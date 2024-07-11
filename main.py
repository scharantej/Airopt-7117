
from flask import Flask, render_template, request

app = Flask(__name__)

destinations = ["Japan", "Taiwan", "Singapore", "Korea"]
prices = {"Japan": 100, "Taiwan": 120, "Singapore": 150, "Korea": 180}

@app.route('/')
def index():
    return render_template('index.html', destinations=destinations, prices=prices)

@app.route('/refresh', methods=['POST'])
def refresh():
    for destination in destinations:
        prices[destination] = get_price(destination)
    return render_template('index.html', destinations=destinations, prices=prices)

def get_price(destination):
    # Replace this with an actual API call to retrieve the latest price
    return prices[destination]

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
