from typing import Optional

from pydantic import BaseModel, Field
from enum import Enum

class Rating(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"

class Chapters(BaseModel):
    name: str = Field(...)
    text: str = Field(...)
    rating: Rating = Field(...)

class CourseSchema(BaseModel):
    name: str = Field(...)
    date: int = Field(...)
    description: str = Field(...)
    domain: list[str] = Field(...)
    chapters: list[Chapters] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name":"Highlights of Calculus",
                "date":1530133200,
                "description":"Highlights of Calculus is a series of short videos that introduces the basic ideas of calculus \u2014 how it works and why it is important. The intended audience is high school students, college students, or anyone who might need help understanding the subject.\nIn addition to the videos, there are summary slides and practice problems complete with an audio narration by Professor Strang. You can find these resources to the right of each video.",
                "domain":[
                    "mathematics"
                ],
                "chapters":[
                    {
                        "name":"Gil Strang's Introduction to Calculus for Highlights for High School",
                        "text":"Highlights of Calculus"
                    },
                    {
                        "name":"Big Picture of Calculus",
                        "text":"Highlights of Calculus"
                    }
                ]
            }
        }

class UpdateCourseSchema(BaseModel):
    name: Optional[str]
    date: Optional[int]
    description: Optional[str]
    domain: Optional[list[str]]
    chapters: Optional[list[Chapters]]

    class Config:
        schema_extra = {
            "example": {
                "name":"Highlights of Calculus",
                "date":1530133200,
                "description":"Highlights of Calculus is a series of short videos that introduces the basic ideas of calculus \u2014 how it works and why it is important. The intended audience is high school students, college students, or anyone who might need help understanding the subject.\nIn addition to the videos, there are summary slides and practice problems complete with an audio narration by Professor Strang. You can find these resources to the right of each video.",
                "domain":[
                    "mathematics"
                ],
                "chapters":[
                    {
                        "name":"Gil Strang's Introduction to Calculus for Highlights for High School",
                        "text":"Highlights of Calculus"
                    },
                    {
                        "name":"Big Picture of Calculus",
                        "text":"Highlights of Calculus"
                    }
                ]
            }
        }

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
