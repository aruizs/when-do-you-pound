from . import main


@main.route("/")
def index():
    return "<h1>When do you pound?</h1>"
