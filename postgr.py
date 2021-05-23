
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
#from sqlalchemy.orm.session import Session

#engine = create_engine("mysql+mysqlconnector://root:root@localhost/test",echo = True)
engine = create_engine("postgresql+psycopg2://postgres:root@localhost/test",echo = True)

Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    tg_id = Column(Integer)
    time = Column(String(5))
    wcards = relationship("Card", back_populates="user")
        
    def __init__(self, name, lastname, tg_id, time):
        self.name = name
        self.lastname = lastname
        self.tg_id = tg_id
        self.time = time
   
class Card(Base):
    __tablename__ = 'cards'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    eng_word = Column(String(50))
    rus_word = Column(String(50))
    repeat_num = Column(Integer)
    user = relationship("User", back_populates="wcards")
    
    def __init__(self, user_id, eng_word, rus_word, repeat_num):
        self.user_id = user_id
        self.eng_word = eng_word
        self.rus_word = rus_word
        self.repeat_num = repeat_num

#User.cards = relationship("Card", order_by = Card.id, back_populates = "user")
                              
#newUser = User('Max', 'Durov', 7777999)
#session.add(newUser)
#session.commit()

Base.metadata.create_all(engine)
