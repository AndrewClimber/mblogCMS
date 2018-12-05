from app import mblog_app, db
from app.models import User, Post


@mblog_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
