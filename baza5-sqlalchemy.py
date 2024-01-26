from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"


engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='Jan kowalski', age=30)
session.add(new_user)
session.commit()
session.close()

users = session.query(User).all()
for user in users:
    print(user)
# <User(name=Jan kowalski, age=30)>
# <User(name=Jan kowalski, age=30)>
