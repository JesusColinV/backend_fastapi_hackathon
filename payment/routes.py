import fastapi
from typing import List
from sqlalchemy.orm import Session
from database.services import get_db
from .schema import *
from .model import *
from .services import *


router = fastapi.APIRouter()


@router.get(
    "/apis/payment_services/is_paid/{is_paid}",
    tags=["Payment"],
    description="Obtener la lista de servicios pagados o no pagados")
async def get_paid_services(is_paid:bool, db:Session = fastapi.Depends(get_db)):
    payment_object = await get_paid_service_async(is_paid,db)
    return payment_object

@router.get(
    "/apis/payment_services",
    tags=["Payment"],
    description="Obtener la lista de todos los servicios")
async def get_all_services(db:Session = fastapi.Depends(get_db)):
    payment_object = await get_services_async(db)
    return payment_object

@router.get(
    "/apis/payment_services/name/{service}",
    tags=["Payment"],
    description="traer servicio dado un nombre")
async def get_one_services(service:str, db:Session = fastapi.Depends(get_db)):
    service_object = await get_1_services_async(service,db)
    return service_object


@router.post(
    "/apis/payment_services",
    tags=["Payment"],
    description="Crear un nuevo servicio")
async def post_new_payment_services(payment:IPayment, db:Session = fastapi.Depends(get_db)):
    payment_object = await register_new_service_async(payment, db)
    return payment_object


@router.put(
    "/apis/payment_services/{service}",
    tags=["Payment"],
    description="cambiar estado de servicio")
async def update_payment_services(service:str, db:Session = fastapi.Depends(get_db)):
    service_object = await get_1_services_async(service,db)
    service_object = await update_services_async(service_object,db)
    return service_object



