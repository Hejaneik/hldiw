from app import db
from app.models import Delay
from datetime import datetime

db.create_all()

delay1 = Delay(1, 2, 12, datetime.utcnow(), 'no excuse')
delay2 = Delay(1, 2, 13, datetime.utcnow(), 'excuse one')
delay3 = Delay(1, 2, 14, datetime.utcnow(), 'excusez moi')

db.session.add(delay1)
db.session.add(delay2)
db.session.add(delay3)

db.session.commit()

