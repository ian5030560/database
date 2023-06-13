from flask import Flask, render_template
from customer.custom import custom
from call_center.call_center import call

app = Flask(__name__)
app.register_blueprint(custom, url_prefix = "/customer")
app.register_blueprint(call, url_prefix = "/call")

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)