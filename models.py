from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")
    gender_agees = relationship("Gender_age", back_populates="user")

    def __repr__(self):
        return (f"User("
                f"id={self.id!r}, "
                f"name={self.name!r}, '"
                f"fullname={self.fullname!r})")

    __str__ = __repr__


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

    __str__ = __repr__


class Gender_age(Base):
    __tablename__ = 'gender_age'

    id = Column(Integer, primary_key=True)
    gender = Column(String)
    age = Column(Integer)

    user = relationship("User", back_populates="gender_agees")

    def __repr__(self):
        return f"Gender_age(id={self.id!r}, gender={self.gender!r}, age={self.age!r})"

    __str__ = __repr__
