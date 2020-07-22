from app import create_app
from app.models import Sources,Articles
from flask_script import Manager,Server


# Creatig app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)





if __name__ == '__main__':
    manager.run()