
from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
db_string = "postgres://pkwiromdzmgkzs:434ae4bf64675314facf74d1adb2ca6813abe2c7a7bf4b4486dff9b5afe60223@ec2-50-17-225-140.compute-1.amazonaws.com:5432/d3dp5vc7dfors7"
db = create_engine(db_string)
base = declarative_base()
class Fruit(base):  
    __tablename__ = 'fruits'

    name = Column(String, primary_key=True)
    color = Column(String)

 
Session = sessionmaker(db)  
session = Session()
base.metadata.create_all(db)
firstfruit = Fruit(name="apple",color="red")
session.add(firstfruit)
session.commit()
fruits = session.query(Fruit)
for fruit in fruits:
         print(fruit.name)
	 session.delete(fruit)
	 session.commit()

Fruit.__table__.drop(db)
session.commit()
session.close()
