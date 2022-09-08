import fastapi
import uvicorn
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from ecommerce.routes import router as ecommerce
from payment.routes import router as payment
from transaction.routes import router as transaction 
from database.services import create_database

def start_application():
    
    app = fastapi.FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.DESCRIPTION,
        version=settings.PROJECT_VERSION,
        openapi_tags=settings.TAGS,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    return app

try:
    create_database()
except Exception as ex:
    print(ex)

app = start_application()
app.include_router(ecommerce)
app.include_router(payment)
app.include_router(transaction)

if __name__ == "__main__":
    uvicorn.run(app)