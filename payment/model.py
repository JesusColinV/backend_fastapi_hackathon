from fastapi_utils.guid_type import GUID
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer, Float, Boolean
from database.base_class import Base

class PaymentModel(Base):
    __tablename__ = 'payment_table'
    id = Column(GUID, primary_key=True, index = True)
    service = Column(String(16), nullable = False)
    cost = Column(Float)
    is_paid = Column(Boolean, nullable = False)
    
