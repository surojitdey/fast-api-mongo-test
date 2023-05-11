from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import retrieve_cources, retrieve_cource, retrieve_chapter, rating_chapter
from ..models.courses import CourseSchema, UpdateCourseSchema, ResponseModel, ErrorResponseModel, Rating
from typing import List, Dict

router = APIRouter()

@router.get("/", response_description="Courses retrieved")
async def get_cources(sort:str=None, domain:str=None):
    cources = await retrieve_cources(sort=sort, domain=domain)
    if cources:
        return ResponseModel(cources, "Courses data retrieved successfully")
    return ResponseModel(cources, "Empty list returned")


@router.get("/{id}", response_description="Courses overview")
async def get_cource(id:str):
    cource = await retrieve_cource(id=id)
    if cource:
        return ResponseModel(cource, "Course overview data retrieved successfully")
    return ResponseModel(cource, "Empty list returned")


@router.get("/{id}/chapters/{name}", response_description="Chapter information")
async def get_chapter_information(id:str, name:str):
    chapter = await retrieve_chapter(id=id, name=name)
    if chapter:
        return ResponseModel(chapter, "Chapter information retrieved successfully")
    return ResponseModel(chapter, "Empty list returned")


@router.put("/{id}/chapters/{name}", response_description="Chapter rating")
async def rate_chapter(id:str, name:str, rating: Rating):
    chapter = await rating_chapter(id=id, name=name, rating=rating)
    if chapter:
        return ResponseModel(chapter, "Chapter rated successfully")
    return ResponseModel(chapter, "Invalid chapter information")


