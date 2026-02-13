from sqlalchemy.orm import Column, Integer, String #импорт
from sqlalchemy.orm import relationship #импорт
from ..database import Base #импорт


class Category(Base): #класс который наследуется от Base который мы писали в database
    __tablename__ = "category" #__tablename__ в переводе имя таблицы

    id = Column(Integer, primary_key=True, index=True) #даем определение нашему продукту (id)
    name = Column(String, unique=True, nullable=False, index=True) #даем определение нашему продукту (имя)
    slug = Column(String, unique=True, nullable=False, index=True) #даем определение нашему продукту (слаг)


    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category (id = {self.id}, name= '{self.name}')>"