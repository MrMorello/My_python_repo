from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/promptdb', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)

Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname="ednickname")
session.add(ed_user)
#our_user = session.query(User).filter_by(name='ed').first()
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Marry Poppins', nickname='mary'),
    User(name='fred', fullname='Fred Flint stone', nickname='freddie')
])

ed_user.nickname = 'eddie'


session.commit()

for i in session.query(User).order_by(User.id):
    print(i.name, i.fullname)

session.close()
