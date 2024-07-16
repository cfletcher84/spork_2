# from database import db, Base
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# import datetime

# class Task(Base):
#     __tablename__ = 'tasks'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
#     task: Mapped[str] = mapped_column(db.String(255))
#     description: Mapped[str] = mapped_column(db.String(500))
#     # date: Mapped[datetime.date] = mapped_column(db.Date, nullable=False, default=lambda : datetime.datetime.date(datetime.datetime.now()))
#     spoons_needed: Mapped[int] = mapped_column(db.Integer())
#     duration: Mapped[str] = mapped_column(db.String(100))
#     time_of_day: Mapped[str] = mapped_column(db.String(100))
#     # icon: Mapped[str] = mapped_column(db.String(100), nullable=True)
#     user: Mapped['users'] = relationship(back_populates='tasks')

from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db, Base
import datetime

class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    task: Mapped[str] = mapped_column(db.String(255))
    description: Mapped[str] = mapped_column(db.String(500))
    date: Mapped[datetime.date] = mapped_column(db.DateTime, nullable=False, default=lambda: datetime.date(datetime.now()))
    spoons_needed: Mapped[int] = mapped_column(db.Integer())
    duration: Mapped[str] = mapped_column(db.String(100))
    time_of_day: Mapped[str] = mapped_column(db.String(100))
    user: Mapped['User'] = relationship('User', back_populates='tasks') 

from models.user import User
