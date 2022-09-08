

from typing import Optional
from pydantic import BaseModel


class IEcommerce(BaseModel):
    people_shared: str
    people_matched: str 
    photo: str 
    title: str 
    cost: float
    category: str 
    state: str 
    description: str 
    is_dollar: bool 
    is_sold: bool 
    class Config:
        orm_mode = True
        
class ICategory(BaseModel):
    category: str 
    
        



