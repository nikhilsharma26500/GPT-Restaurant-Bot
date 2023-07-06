# This is the regular store database

from sqlalchemy import Column, Float, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define a class named Pizza that inherits from the Base class.
class Pizza(Base):
    # Set the name of the database table to 'pizzas'.
    __tablename__ = 'pizzas'
    # Define a column named 'id' of type Integer, with a primary key constraint.
    id = Column(Integer, primary_key=True)
    # Define a column named 'name' of type String.
    name = Column(String)
    # Define a column named 'price' of type float.
    price = Column(Float)
    # Define a relationship between the Pizza and Order tables.
    # This creates a 'orders' attribute on Pizza instances that can be used to access related Order instances.
    # The 'back_populates' argument specifies the name of the attribute on the Order class that should be used to access related Pizza instances.
    orders = relationship('Order', back_populates='pizza')
    
    # Define a method named 'to_json' that returns a dictionary representation of the Pizza instance.
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }
        
# Define a class named Order that inherits from the Base class.
class Order(Base):
    # Set the name of the database table to 'orders'.
    __tablename__ = 'orders'
    # Define a column named 'id' of type Integer, with a primary key constraint.
    id = Column(Integer, primary_key=True)
    # Define a column named 'pizza_id' of type Integer, with a foreign key constraint that references the 'id' column of the 'pizzas' table.
    pizza_id = Column(Integer, ForeignKey('pizzas.id'))
    # Define a relationship between the Order and Pizza tables.
    # This creates a 'pizza' attribute on Order instances that can be used to access the related Pizza instance.
    # The 'back_populates' argument specifies the name of the attribute on the Pizza class that should be used to access related Order instances.
    pizza = relationship('Pizza', back_populates='orders')
    
    # Define a method named 'to_json' that returns a dictionary representation of the Order instance.
    # The 'pizza' key in the dictionary is set to the result of calling the 'to_json' method on the related Pizza instance.
    def to_json(self):
        return {
            'id': self.id,
            'pizza': self.pizza.to_json()
        }
    


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    review = Column(String)
    
    def to_json(self):
        return {
            'id': self.id,
            'review': self.review
        }
        
        
# Setting up the engine and session (this stays in the local computer)
# Create a database engine that connects to a SQLite database file named 'pizza.db'.
engine = create_engine('sqlite:///pizza.db')
# Create a session factory that uses the database engine to create new sessions.
Session = sessionmaker(bind=engine)