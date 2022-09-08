from typing import Any
from sqlalchemy.ext.declarative import declarative_base

#@as_declarative
#class Base:
#    id : Any
#    __name__ : str
#    
#    def  __tablename__(cls) -> str:
#        return cls.__name__.lower()

Base = declarative_base()