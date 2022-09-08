from sqlalchemy.orm import Session
from uuid import uuid1
from ecommerce.schema import IEcommerce
from .model import EcommerceModel as E


async def get_1_by_category_async(category:str, db:Session):
    return db.query(E).filter(E.category == category).first()

async def get_1_by_not_sold_async(is_sold:bool, db:Session):
    return db.query(E).filter(E.is_sold == is_sold).first()

async def get_by_category_async(category:str, db:Session):
    return db.query(E).filter(E.category == category).fetchall()

async def get_by_not_sold_async(is_sold:bool, db:Session):
    return db.query(E).filter(E.is_sold == is_sold).fetchall()


async def post_product(product:IEcommerce, db:Session):
    product_object = E(
        id = uuid1(),
        people_shared = product.people_shared,
        people_matched = product.people_matched,
        photo = product.photo,
        title = product.title,
        cost = product.cost,
        category = product.category,
        state = product.state,
        description = product.description,
        is_dollar = product.is_dollar,
        is_sold = product.is_sold
    )
    db.add(product_object)
    db.commit()
    db.refresh(product_object)
    return product_object


async def get_sold_ecommerce_async(is_sold:bool, db:Session ):
    return db.query(E).filter(E.is_sold == is_sold).all()