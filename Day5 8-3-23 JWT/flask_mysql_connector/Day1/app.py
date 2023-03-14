from flask import Flask, session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:8282@localhost/flask1'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base = declarative_base()


class MyTable(Base):
   __tablename__ = 'mytable'
   id = Column(Integer, primary_key=True)
   name = Column(String(50))
   age = Column(Integer)
   Session = sessionmaker(bind=engine)
   session = Session()
   


   @app.route('/')
   def index(self):
     
     rows = session.query(MyTable).all()
     return str(rows)

if __name__ == '__main__':
 
 app.run()