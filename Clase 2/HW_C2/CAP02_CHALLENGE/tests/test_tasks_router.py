import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from models import Task, UpdateTaskModel, TaskList
from routers.tasks_router import tasks_router
from db import db

app = FastAPI()
app.include_router(tasks_router)
client = TestClient(app)

@pytest.fixture
def mock_db(monkeypatch):
    class MockDB:
        def __init__(self):
            self.tasks = {}
            self.next_id = 1

        def add_task(self, task):
            task.id = self.next_id
            self.tasks[self.next_id] = task
            self.next_id += 1
            return task

        def get_task(self, task_id):
            return self.tasks.get(task_id)

        def get_tasks(self):
            return list(self.tasks.values())

        def update_task(self, task_id, task_update):
            if task_id not in self.tasks:
                return None
            task = self.tasks[task_id]
            task.title = task_update.title or task.title
            task.description = task_update.description or task.description
            task.completed = task_update.completed if task_update.completed is not None else task.completed
            return task

        def delete_task(self, task_id):
            if task_id in self.tasks:
                del self.tasks[task_id]

        def delete_all_tasks(self):
            self.tasks.clear()

    mock_db_instance = MockDB()
    monkeypatch.setattr("routers.tasks_router.db", mock_db_instance)
    return mock_db_instance

def test_create_task(mock_db):
    task_data = {"id": 0, "title": "Test Task", "description": "Test Description", "completed": False}
    response = client.post("/", json=task_data)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Test Task"

def test_get_task_not_found(mock_db):
    response = client.get("/999")
    assert response.status_code == 404
    assert "Task not found" in response.json()["detail"]["message"]

def test_get_tasks_empty(mock_db):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["tasks"] == []

def test_update_task_not_found(mock_db):
    update_data = {"title": "Updated Title", "description": "Updated Description", "completed": True}
    response = client.put("/999", json=update_data)
    assert response.status_code == 404

def test_delete_all_tasks(mock_db):
    # Add some tasks first
    task1 = {"id": 0, "title": "Task 1", "description": "Description 1", "completed": False}
    task2 = {"id": 0, "title": "Task 2", "description": "Description 2", "completed": False}
    client.post("/", json=task1)
    client.post("/", json=task2)
    
    response = client.delete("/delete_all")
    assert response.status_code == 200
    assert response.json()["message"] == "All tasks deleted successfully"
    
    # Verify tasks are deleted
    response = client.get("/")
    assert response.json()["tasks"] == []

def test_update_task_partial(mock_db):
    # Create a task first
    task_data = {"id": 0, "title": "Original Title", "description": "Original Description", "completed": False}
    create_response = client.post("/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Update only the title
    update_data = {"title": "Updated Title", "description": None, "completed": None}
    response = client.put(f"/{task_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"
    assert response.json()["description"] == "Original Description"
    assert response.json()["completed"] == False

def test_delete_task_success(mock_db):
    # Create a task first
    task_data = {"id": 0, "title": "Test Task", "description": "Test Description", "completed": False}
    create_response = client.post("/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Delete the task
    response = client.delete(f"/{task_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"
    
    # Verify task is deleted
    get_response = client.get(f"/{task_id}")
    assert get_response.status_code == 404
