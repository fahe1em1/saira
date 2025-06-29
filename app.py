from dataclasses import dataclass
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@dataclass
class Bid:
    title: str
    description: str

# In-memory store for bids
bids = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', bids=bids)

@app.route('/bids', methods=['POST'])
def add_bid():
    title = request.form.get('title')
    description = request.form.get('description')
    if title and description:
        bids.append(Bid(title=title, description=description))
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
