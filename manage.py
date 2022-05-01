from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate
from app.models import Pitch, User, Comment

app = create_app('production')
manager = Manager(app)

manager.add_command('server', Server)

migrate = Migrate(app,db)

@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, Pitch = Pitch, User = User, Comment = Comment)

if __name__=='__main__':
    manager.run()        