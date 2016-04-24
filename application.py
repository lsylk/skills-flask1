from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show the application form."""

    return render_template("application-form.html")


@app.route("/application")
def application():
    """Fill out the application form."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.args.get("salary")
    title = request.form.get("select")

    return render_template("application-form.html", first_name=first_name, last_name=last_name, salary=salary, title=title)

if __name__ == "__main__":
    app.run(debug=True)
