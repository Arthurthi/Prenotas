from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///prenotas.db')

base = declarative_base()

Session = sessionmaker(bind=engine)

class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    vendedores = Column(String, nullable=False)









base.metadata.create_all(bind=engine)
