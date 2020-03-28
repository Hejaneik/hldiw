from app import db, create_app
from app.models import Delay, User
from datetime import datetime

app = create_app()

with app.app_context():
    # NOTE if the database URI points to a directory, this diretory has to exist. SQLAlchemy only creates the db file, not paths
    db.create_all()

    delay1 = Delay(1, 2, 12, datetime.utcnow(), 'no excuse')
    delay2 = Delay(1, 2, 13, datetime.utcnow(), 'excuse one')
    delay3 = Delay(1, 2, 14, datetime.utcnow(), 'excusez moi')

    user1 = User('admin', 'Hendrik', 'Höfert', 'admin', 'admin@example.com')

    db.session.add(delay1)
    db.session.add(delay2)
    db.session.add(delay3)

    db.session.add(user1)

    db.session.commit()
