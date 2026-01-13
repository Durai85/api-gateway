from flask import Flask
import requests

app = Flask(__name__)

@app.route("/users")
def users():
    # Use the service name 'user-service' instead of 'localhost'
    return requests.get("http://localhost:5001/users").json()

@app.route("/products")
def products():
    return requests.get("http://localhost:5002/products").json()

@app.route("/orders")
def orders():
    return requests.get("http://localhost:5003/orders").json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
