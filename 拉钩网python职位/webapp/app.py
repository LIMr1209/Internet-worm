from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    pos_list = []
    with open('position.json', 'rb') as f:
        for line in f.readlines():
            pos = json.loads(line)
            print('pos: ', pos)
            pos_list.append(pos)
    d = {}
    for pos in pos_list:
        if pos["location"] not in d:
            d[pos["location"]] = 1
        else:
            d[pos["location"]] += 1
    my_data = [{"name": k, "value": v} for k, v in d.items()]
    print(my_data)
    return render_template('index.html', my_data=my_data)


if __name__ == "__main__":
    app.run(debug=True)
