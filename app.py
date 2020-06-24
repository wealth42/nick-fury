from flask import Flask, make_response

from db_conection import fetch_data

app = Flask(__name__)

@app.route('/')
def view():
    response = fetch_data()

    return {
        "response" : response
    }

if __name__ == "__main__":
    app.run()
