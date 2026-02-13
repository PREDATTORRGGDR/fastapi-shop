from sqlalchemy.orm import Coliunm, Iteger, String, Text, Float, DateTime , ForeignKey #импорт
from sqlalchemy.orm import relationship #импорт
from datetime import datetime #импорт
from ..database import Base #импорт


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True) #даем определение нашему продукту (id)
    name = Column(String, unique=True, nullable=False) #имя продукта
    description = Column(text) #описание продукта
    price = Column(Float, nullable=False) # цена
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False) #id - категории
    image_url = Coliunm(String) # колонка для хранения текстовой строки (URL картинки)
    created_at = Column(DateTime, default=datetime.utcnow) # колонка даты, автоматически сохраняет текущее время при создании записи

    category = relationship("Category", back_populates="product")


    def __repr__(self):
        return f"<Product(id = {self.id}, name = '{self.name}', price = {self.price})>"
    
