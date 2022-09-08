import fastapi
from typing import List
from sqlalchemy.orm import Session
from database.services import get_db
from .schema import *
from .model import *
from .services import *


router = fastapi.APIRouter()



@router.post(
    "/apis/transaction",
    tags=["Transactions"])
async def post_new_transaction(transaction:ITransaction,db:Session = fastapi.Depends(get_db)):
    transaction_object = await calculate_transaction_async(transaction)
    if transaction_object.done:
        await register_transaction(transaction_object, db)
    return transaction_object

