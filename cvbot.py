#import statements
from fastapi import APIRouter
from ud_cvna_render import scrapper
from ud_cvna_wp_render import scrapper

cvbot_router = APIRouter()

@cvbot_router.get('/trigger-cv')
async def trigger_cv():
    return scrapper()

@cvbot_router.get('/trigger-wp-cv')
async def trigger_wp_cv():
    return scrapper()

@cvbot_router.get('/hello')
async def hello_world():
    return "Hello world"