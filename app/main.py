from flask import Flask, render_template
import requests
    

app = Flask(__name__)

app.secret_key = "Stephen@123#321%"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search/')
@app.route('/search')
def search():
    search = request.args.get("Search")
    print("Search <<<< ",search)
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
