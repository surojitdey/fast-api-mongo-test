import pymongo
import json

mongo = pymongo.MongoClient("mongodb://localhost:27017/")

kimo = mongo["kimo"]
courses = kimo["courses"]

with open('courses.json') as file:
    courses_data = json.load(file)

courses.insert_many(courses_data)

courses.create_index(
    [
        ("name", pymongo.ASCENDING),
        ("domain", pymongo.ASCENDING)
    ],
    name="title_domain_index"
)
courses.create_index('chapters.name',name="chapters_name_index")
# courses.drop_indexes()