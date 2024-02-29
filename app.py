from flask import Flask, render_template, flash, request
from blueprints.entities.blueprint import blueprint as entities_blueprint
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.register_blueprint(entities_blueprint, url_prefix='/entities')

# Set the configuration data in the app.config dictionary
app.config.update(
    DASHBOARD_TITLE=os.getenv("DASHBOARD_TITLE")
)

# Define a context processor to send configuration to all templates
@app.context_processor
def inject_config():
    return dict(config=app.config)

@app.route("/dashboard", methods=["GET"])
def dashboard():
    print(dir(request))
    flash("Info flash example", "info")
    flash("Warning flash example", "warning")
    flash("Danger flash example", "danger")
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)