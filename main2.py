from sqlalchemy import insert, select
from db import Base, engine, execute
from models import User, Address, Gender_age

Base.metadata.create_all(engine)
