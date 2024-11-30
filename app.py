from flask import Flask
from routes.home import home_bp
from routes.contact import contact_bp
from routes.about import about_bp
from routes.times_tables import times_tables_bp
from routes.math_problem import math_problem_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a unique secret key here

app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(contact_bp, url_prefix='/contact')
app.register_blueprint(about_bp, url_prefix='/about')
app.register_blueprint(times_tables_bp, url_prefix='/times-tables')
app.register_blueprint(math_problem_bp, url_prefix='/math-problem')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
