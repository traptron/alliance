import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin

from flask_login import LoginManager

from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()

admin_site = Admin(
    name="ССК Альянс Admin"
)

login_manager = LoginManager()

csrf = CSRFProtect()

def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or os.urandom(32).hex()

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

    # Session cookie security
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["SESSION_COOKIE_SECURE"] = False  # Set True when using HTTPS

    db.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = "main.login"

    csrf.init_app(app)

    # импорт моделей
    from .models import Team, Player, Match, Sport, Tournament, TournamentSport, TournamentRegistration, SportStatDefinition, MatchPlayerStat

    # Flask-Admin

    from .admin import (
        AdminModelView,
        TeamAdminView,
        MatchAdminView,
        TournamentAdminView,
        TournamentSportAdminView,
        TournamentRegistrationAdminView,
        SportStatDefinitionAdminView,
        MatchPlayerStatAdminView
    )

    admin_site.init_app(app)

    admin_site.add_view(TeamAdminView(Team, db.session))

    admin_site.add_view(AdminModelView(Player, db.session))

    admin_site.add_view(TournamentAdminView(Tournament, db.session))

    admin_site.add_view(TournamentSportAdminView(TournamentSport, db.session))

    admin_site.add_view(TournamentRegistrationAdminView(TournamentRegistration, db.session))

    admin_site.add_view(SportStatDefinitionAdminView(SportStatDefinition, db.session))

    admin_site.add_view(MatchPlayerStatAdminView(MatchPlayerStat, db.session))

    admin_site.add_view(MatchAdminView(Match, db.session))

    admin_site.add_view(AdminModelView(Sport, db.session))
    

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Security headers
    @app.after_request
    def set_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response

    # routes
    from .routes import main

    app.register_blueprint(main)

    return app
