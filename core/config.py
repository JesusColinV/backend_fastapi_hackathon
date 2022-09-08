import os
from pathlib import Path
import dotenv

env_path = Path(".")/".env"
dotenv.load_dotenv(dotenv_path =env_path)

class Settings:
    PROJECT_TITLE : str = "HACKATHON"
    PROJECT_VERSION : str = "1.0.0"
    DESCRIPTION : str = "HACKTHON proyecto de super app"
    TAGS : str = [
                    {
                        "name": "ecommerce",
                        "description": "ecommerce endpoint"
                    }
                ]
    
    USERNAME: str= "root"
    PASSWORD: str= os.getenv("PASSWORD")
    SERVER: str= os.getenv("SERVER")
    PORT: str= os.getenv("PORT")
    DATABASE: str= os.getenv("DATABASE")
    
    DATABASE_CONNECTION = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DATABASE}'
    
    
settings = Settings()