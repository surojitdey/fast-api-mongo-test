import os
import sys
from fastapi.testclient import TestClient
from .server.app import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
# Declaring test client
client = TestClient(app)

def test_get_courses():
    "asserting status code"
    response = client.get("/course")
    assert response.json()["code"] == 200