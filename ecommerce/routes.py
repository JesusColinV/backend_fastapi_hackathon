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
    #description="post a ecommerce post",
)
async def post_ecommerce(product:IEcommerce, db:Session = fastapi.Depends(get_db)):
    product_object = await post_product(product,db)
    return product_object


@router.get(
    "/ecommerce/{category}",
    tags=["Ecommerce"],
    description="Get a list of pharmacies by keyword",
)
async def get_category_first(category:str, db:Session = fastapi.Depends(get_db)):
    product_object = await get_1_by_category_async(category = category, db = db) #connection.execute(stmt).fetchall()
    if not product_object:
        raise fastapi.HTTPException(status_code=204, detail="no exiten registro de esa categoria")
    return product_object

@router.get(
    "/ecommerce/sold/{is_sold}",
    tags=["Ecommerce"],
    description="Get a list of pharmacies by keyword",
)
async def get_category_first(category: str, db:Session = fastapi.Depends(get_db)):
    product_object = await get_by_category_async(category = category, db = db) #connection.execute(stmt).fetchall()
    if not product_object:
        raise fastapi.HTTPException(status_code=204, detail="no exiten registro de esa categoria")
    return product_object

