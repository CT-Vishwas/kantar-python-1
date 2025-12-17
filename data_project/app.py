from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# engine = create_engine("sqlite+pysqlite:///dev.db", echo=True)
engine = create_engine("mysql+pymysql://root:root@localhost:3306/devdb")
sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class UsersORM(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100),nullable=False)
    age = Column(Integer)
    email = Column(String(100), unique=True)


Base.metadata.create_all(engine)