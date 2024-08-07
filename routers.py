from fastapi import APIRouter
from controller.athlete import router as athletes
from controller.category import router as categories
from controller.training_center import router as trainingcenters

api_router = APIRouter()

api_router.include_router(athletes, prefix='/athletes', tags=['athletes'])
api_router.include_router(categories, prefix='/categories', tags=['categories'])
api_router.include_router(trainingcenters, prefix='/trainingcenters', tags=['training_centers'])