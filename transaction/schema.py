from pydantic import BaseModel



class ITransaction(BaseModel):
    cost:float 
    start:float 
    
    class Config:
        orm_mode = True

class ITransactionResponse(ITransaction):
    end:float 
    done:bool 
    
    class Config:
        orm_mode = True
