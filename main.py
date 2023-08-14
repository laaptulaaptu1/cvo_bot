#Import statements
from fastapi import FastAPI
from cvbot import cvbot_router
from fastapi.middleware.cors import CORSMiddleware

client_apps = ['*']#Our REACT app will be running on this IP and PORT

#Create app
app = FastAPI(debug=True)
#register your router
app.include_router(cvbot_router)

#Register App with CORS middleware to allow resourse sharing between different domains/origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=client_apps,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)