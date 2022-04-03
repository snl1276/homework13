from sqlalchemy import insert, select
from db import Base, engine, execute
from models import User, Address

Base.metadata.create_all(engine)

