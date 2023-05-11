import motor.motor_asyncio
from bson.objectid import ObjectId
from .models.courses import Rating

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.kimo

course_collection = database.get_collection("courses")

def course_helper(course) -> dict:
    return {
        "name": course["name"],
        "date": course["date"],
        "description": course["description"],
        "domain": course["domain"],
        "chapters": course["chapters"],
    }

def chapter_helper(chapter) -> dict:
    return {
        "name": chapter["chapters"][0]["name"],
        "text": chapter["chapters"][0]["text"],
        "rating": chapter["chapters"][0]["rating"] if "rating" in chapter["chapters"][0] else ""
    }

# Retrieve all cources present in the database
async def retrieve_cources(sort:str=None, domain:str=None):
    cources = []
    db_fetch = course_collection.find({},{"_id": 0})
    if domain:
            db_fetch = course_collection.find(
                {
                    "domain": domain
                },
                {
                    "_id": 0
                }
            )
    if sort=='name':
        db_fetch = db_fetch.sort("name", 1)
    if sort=='date':
        db_fetch = db_fetch.sort("date", -1)
    async for cource in db_fetch:
        cources.append(course_helper(cource))
    return cources

# Retrieve a cource with a matching ID
async def retrieve_cource(id: str) -> dict:
    cource = await course_collection.find_one(
        {
            "_id": ObjectId(id)
        },
        {
            "_id": 0
        }
    )
    if cource:
        return course_helper(cource)

# Retrieve a chapter with a matching cource ID and chapter name
async def retrieve_chapter(id: str, name: str) -> dict:
    chapter = await course_collection.find_one(
        {
            "_id": ObjectId(id),
            "chapters.name": name
        },
        {
            "_id": 0,
            "chapters.$": 1
        }
    )
    if chapter:
        return chapter_helper(chapter)

# Retrieve a chapter with a matching cource ID and chapter name
async def rating_chapter(id: str, name: str, rating: Rating) -> dict:
    course = course_collection.find_one(
        {
            "_id": ObjectId(id),
            "chapters.name": name
        }
    )
    if course:
        chapter = course_collection.update_one(
            {
                "_id": ObjectId(id),
                "chapters.name": name
            },
            {
                "$set": {
                    "chapters.$.rating": rating
                }
            },
            upsert=True
        )
        if chapter:
                return True
        return False
