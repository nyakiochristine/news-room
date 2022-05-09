from app  import create_app
from flask_script  import Manager,Server


app = create_app('development')
manager = Manager(app)

@manager.command
def test():
    """Function that runs all the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()