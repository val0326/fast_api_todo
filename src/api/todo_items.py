from fastapi import APIRouter

from controller.todo import get_todo_controller


router = APIRouter()


@router.get("/lists/{list_id}/todos")
async def get_todos():
    return


@router.post("/lists/{list_id}/todos")
async def create_todo():
    return


@router.patch("/lists/{list_id}/todos/{todo_id}")
async def update_todo():
    return


@router.delete("/lists/{list_id}/todos/{todo_id}")
async def gelete_todo():
    return
