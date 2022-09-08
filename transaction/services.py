from uuid import uuid1
from transaction.schema import *
from sqlalchemy.orm import Session
from .model import TransactionModel as T



async def calculate_transaction_async(transaction:ITransaction):
    end_result = transaction.start - transaction.cost
    if transaction.start >= transaction.cost:

         
        transaction_object = T(
                                id = uuid1(),
                                cost = transaction.cost,
                                start = transaction.start,
                                end = end_result,
                                done = True
                                
                            )
    else:
        transaction_object = T(
                                id = uuid1(),
                                cost = transaction.cost,
                                start = transaction.start,
                                end = end_result,
                                done = False
                                
                            )
    return transaction_object

async def register_transaction(transaction:ITransactionResponse, db:Session):
    transaction_object = T(
        id = transaction.id,
        cost = transaction.cost,
        start = transaction.start,
        end = transaction.end,
        done = transaction.done
        
    )
    db.add(transaction_object)
    db.commit()
    db.refresh(transaction_object)
    return transaction_object

