from flask import Blueprint, render_template, request

call = Blueprint(
    "call",
    __name__,
    template_folder = "templates",
    static_folder = "static"
)

@call.route("/", methods = ["GET", "POST"])
def caller():
    return render_template("call_center.html")
