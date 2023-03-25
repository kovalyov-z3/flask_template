from app import create_app
from flask_alembic import Alembic

app = create_app()
with app.app_context():
    alembic = Alembic()
    alembic.init_app(app) 
    alembic.revision('initial changes')
    # run all available upgrades
    # same as ./manage.py db upgrade
    alembic.upgrade()

if __name__ == "__main__":
    app.run()





