from flask import Flask

app =   Flask(__name__)

# print(type(app))

# URL - http://IP:port/

@app.route("/")
def welcome():
    return "Welcome to GenAI Web App"

@app.route("/api")
def api():
    try:
        a = 10
        b = 20
        c = a / b
    except ZeroDivisionError:
        return "Division by zero", 500
    return f"Welcome to API Invoked {a} / {b} Value - {c}", 200

@app.route("/api/json")
def api_json():
    data = {
        "name": "GenAI Web App",
        "version": "1.0",
        "status": "running"
    }
    return data, 200

if __name__ == "__main__":
    app.run(debug=True)
