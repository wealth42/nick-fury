from flask import Flask, make_response, request

from db_conection import fetch_data

app = Flask(__name__)

@app.route('/', methods=['POST'])
def view():
    common_name = request.get_json(silent=True).get('common_name')

    response = fetch_data(common_name)

    return {
        "response" : response
    }

if __name__ == "__main__":
    app.run()
