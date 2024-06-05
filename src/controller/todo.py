import uuid

from databases import Database
from sqlalchemy import delete, insert, select

from db.models import TodoList
from schemas.todo import TodoListResponse


class TodoController:
    def __init__(self, db: Database):
        self.db = db

    async def get_lists(self) -> list[TodoListResponse]:
        query = select(TodoList)
        rows = await self.db.fetch_all(query)
        result = [dict(row) for row in rows]
        return [
            TodoListResponse(id=row.get("id"), title=row.get("title"))
            for row in result
        ]

    async def create_lists(self, title: str) -> TodoListResponse:
        list_id = uuid.uuid4()
        await self.db.execute(insert(TodoList).values(id=list_id, title=title))
        return TodoListResponse(id=list_id, title=title)

    # def update_todos(self):
    #     return

    async def delete_list(self, list_id: uuid.UUID) -> None:
        query = delete(TodoList).where(TodoList.id == list_id)
        await self.db.execute(query)


todo_controller: TodoController = None


def get_todo_controller():
    if todo_controller is None:
        raise RuntimeWarning("TodoController is not initialized")
    return todo_controller
