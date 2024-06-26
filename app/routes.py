from flask import Flask

app = Flask(__name__)

@app.get("/")
def about():
    me = {
        "first_name": "Daisha",
        "last_name": "McCutcheon",
        "hobbies": "All things art",
        "is_online": True
    }
    return me