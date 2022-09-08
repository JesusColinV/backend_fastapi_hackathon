import fastapi
from typing import List
from sqlalchemy.orm import Session
from database.services import get_db
from .schema import *
from .model import *
from .services import *

router = fastapi.APIRouter()


@router.post(
    "/ecommerce/post/",
    tags=["Ecommerce"],
    #response_model = EcommerceModel,
    description="crear una publicacion de un producto a vender",
)
async def post_ecommerce(product:IEcommerce, db:Session = fastapi.Depends(get_db)):
    product_object = await post_product(product,db)
    return product_object


@router.get(
    "/ecommerce/{category}",
    tags=["Ecommerce"],
    description="Obtener una lista de post dada una categoria",
)
async def get_category_first(category:str, db:Session = fastapi.Depends(get_db)):
    product_object = await get_1_by_category_async(category = category, db = db) #connection.execute(stmt).fetchall()
    if not product_object:
        raise fastapi.HTTPException(status_code=204, detail="no exiten registro de esa categoria")
    return product_object

@router.get(
    "/ecommerce/sold/{is_sold}",
    tags=["Ecommerce"],
    description="identificar productos vendidos o no vendidos",
)
async def get_category_first(is_sold: str, db:Session = fastapi.Depends(get_db)):
    payment_object = await get_sold_ecommerce_async(is_sold,db)
    return payment_object


@router.get(
    "/apis/payment_services/is_paid/{is_paid}",
    tags=["Payment"],
    description="Obtener la lista de servicios pagados o no pagados")
async def get_paid_services(is_paid:bool, db:Session = fastapi.Depends(get_db)):
    payment_object = await get_sold_ecommerce_async(is_paid,db)
    return payment_object
