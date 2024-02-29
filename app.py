import os

from dotenv import load_dotenv
from flask import Flask, flash, render_template

from blueprints.entities.blueprint import blueprint as entities_blueprint

load_dotenv()

app = Flask(__name__)
app.secret_key = "your_secret_key"


def configure_app():
    with app.app_context():
        app.config.update(
            DASHBOARD_TITLE=os.getenv("DASHBOARD_TITLE"),
            SIDEBAR_ROUTES=[{"label": "entities", "url": "/entities"}],
        )
        app.register_blueprint(entities_blueprint, url_prefix="/entities")


configure_app()


@app.context_processor
def inject_config():
    return dict(config=app.config)


@app.route("/dashboard", methods=["GET"])
def dashboard():
    flash("Info flash example", "info")
    flash("Warning flash example", "warning")
    flash("Danger flash example", "danger")
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
