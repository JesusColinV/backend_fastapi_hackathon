from sqlalchemy.orm import Session
from .schema import *
from .model import PaymentModel as P
from uuid import uuid1
async def register_new_service_async(payment:IPayment, db:Session ):
    payment_object = P(
                        id = uuid1(),
                        service = payment.service, 
                        cost = payment.cost,
                        is_paid = payment.is_paid, 
                        )
    db.add(payment_object)
    db.commit()
    db.refresh(payment_object)
    return payment_object

async def get_paid_service_async(is_paid:bool, db:Session ):
    return db.query(P).filter(P.is_paid == is_paid).all()


async def get_services_async(db:Session):
    return db.query(P).all()

async def get_1_services_async(service:str,db:Session):
    return db.query(P).filter(P.service == service).first()

async def update_services_async(payment:IPayment, db:Session ):
    payment.is_paid = not payment.is_paid
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment