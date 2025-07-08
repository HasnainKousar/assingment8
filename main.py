#####################
# main.py
#####################

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, field_validator
from fastapi.exceptions import RequestValidationError
from app.operations import add, subtract, multiply, divide
import uvicorn
import logging


# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

#setup templates directory
templates = Jinja2Templates(directory="templates")