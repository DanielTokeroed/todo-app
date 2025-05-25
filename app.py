import os
from flask import Flask
from models import db
from models.tasks import Task
from models.test import User
from sqlalchemy.sql import text
from routes.todo import todo_bp
""" Integrates SQLAlchemy with Flask. 
This handles setting up one or more engines, associating tables and models with specific engines, and cleaning up connections and sessions after each request.
Only the engine configuration is specific to each application, other things like the model, table, metadata, 
and session are shared for all applications using that extension instance. Call init_app to configure the extension on an application."""

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# initialize the app with the extension
db.init_app(app)
print(app)

app.register_blueprint(todo_bp)
print(todo_bp)


def test_db_connection():
    """Check if the database connection is working."""
    try:
        with app.app_context():
            try:
                db.create_all()
                print('models created')
            except:
                print('Could not create models')
            db.session.execute(text("SELECT 1"))
        print("✅ Connected to the database successfully!")
    except Exception as e:
        print(f"❌ Failed to connect to the database: {e}")

test_db_connection()


if __name__ == "__main__":
    test_db_connection()
    app.run(debug=True)
