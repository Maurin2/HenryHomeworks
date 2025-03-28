from fastapi import APIRouter, HTTPException, Path, Query
from models import Task, UpdateTaskModel, TaskList
from db import db

tasks_router = APIRouter()

"""
Delete all tasks from the database.

Returns:
    dict: A message confirming that all tasks have been deleted successfully.
"""
@tasks_router.delete("/delete_all")
async def delete_all_tasks():
    db.delete_all_tasks()
    return {"message": "All tasks deleted successfully"}

"""
Create a new task in the database.

Args:
    task (Task): The task to be added.

Returns:
    Task: The newly created task with any server-generated attributes.
"""
@tasks_router.post("/", response_model=Task)
async def create_task(task: Task):
    return db.add_task(task)


"""
Retrieve a specific task by its ID.

Args:
    task_id (int): The unique identifier of the task to retrieve.

Returns:
    Task: The task with the specified ID.

Raises:
    HTTPException: If no task is found with the given task_id (404 Not Found).
"""
@tasks_router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int = Path(..., gt=0, description="The ID of the task to retrieve")):
    task = db.get_task(task_id)
    if task is None:
        raise HTTPException(
            status_code=404,
            detail={
                "message": "Task not found",
                "task_id": task_id
            }
        )
    return task



"""
Retrieve all tasks from the database.

Returns:
    TaskList: A list containing all tasks currently stored in the database.
"""
@tasks_router.get("/", response_model=TaskList)
async def get_tasks():
    tasks = db.get_tasks()
    return TaskList(tasks=tasks)


"""
Update a specific task by its ID.

Args:
    task_id (int): The unique identifier of the task to update.
    task_update (UpdateTaskModel): The model containing the fields to update.

Returns:
    Task: The updated task with the new values.

Raises:
    HTTPException: If no task is found with the given task_id (404 Not Found).
"""
@tasks_router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: UpdateTaskModel):
    updated_task = db.update_task(task_id, task_update)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

"""
Delete a specific task by its ID.

Args:
    task_id (int): The unique identifier of the task to delete.

Returns:
    dict: A message confirming the successful deletion of the task.
"""
@tasks_router.delete("/{task_id}")
async def delete_task(task_id: int):
    db.delete_task(task_id)
    return {"message": "Task deleted successfully"}