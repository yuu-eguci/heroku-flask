
import main.models;
main.models.init()

from main.models import Entry
from main import db

entry1 = Entry(title='title1', text='text1')
db.session.add(entry1)
db.session.commit()

entry2 = Entry(title='title2', text='text2')
db.session.add(entry2)
db.session.commit()
db.session.commit()
entries = Entry.query.all()
print(entries)
