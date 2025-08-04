from fastapi.middleware.cors import CORSMiddleware
from agent.agentic_workflow import GraphBuilder
from utils.save_to_document import save_document
from starlette.responses import JSONResponse
from langchain_core.messages import HumanMessage
from utils.config_loader import load_config
import os
import datetime
import traceback
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,  # Enable CORS middleware to handle cross-origin requests
    allow_origins=["*"],  # Allow all domains (use specific domain in production)
    allow_credentials=True,  # Allow cookies, auth headers, etc.
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all custom headers (Content-Type, Authorization, etc.)
)