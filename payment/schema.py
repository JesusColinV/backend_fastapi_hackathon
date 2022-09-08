

from pydantic import BaseModel

class IPayment(BaseModel):
    service:str 
    cost: float
    is_paid:bool 
    
    class Config:
        orm_mode = True
        
        
