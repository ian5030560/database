from flask import Blueprint, render_template, request

custom = Blueprint(
    "custom",
    __name__,
    template_folder = "templates",
    static_folder = "static"
)

@custom.route("/", methods = ["GET", "POST"])
def customer():
    if request.method == "POST":
        city = request.form.get("city")
        store = request.form.get("store")
        product = request.form.get("product")
        
        return render_template("custom.html")
    
    return render_template("custom.html")
