from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer, Float, Boolean
from database.base_class import Base
from fastapi_utils.guid_type import GUID

class EcommerceModel(Base):
    __tablename__ = 'ecommerce_table'
    id = Column(GUID, primary_key=True, index = True)
    people_shared = Column(String(16), nullable = False)
    people_matched = Column(String(16), nullable = False)
    photo = Column(String(16), nullable = False)
    title = Column(String(16), nullable = False)
    cost = Column(Float)
    category = Column(String(16), nullable = False)
    state = Column(String(16), nullable = False)
    description = Column(String(16), nullable = False)
    is_dollar = Column(Boolean, nullable = False)
    is_sold = Column(Boolean, nullable = False)

#SqlAlchemyBase.metadata.create_all(engine)

