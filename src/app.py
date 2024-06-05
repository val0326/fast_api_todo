from contextlib import asynccontextmanager

from databases import Database
from fastapi import FastAPI

import controller.todo as todo_module
from api import include_routers
from core.settings import get_settings


config = get_settings()

db = Database(config.db.dsn)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await db.connect()
    todo_module.todo_controller = todo_module.TodoController(db)
    yield
    await db.disconnect()


app = FastAPI(title="Fast API - todo list", lifespan=lifespan)
include_routers(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

# MVC - Nodel, View, Controller

# GET /lists
# POST /lists
# DELETE /lists/{list_id}


# GET /lists/{list_id}/todos
# POST /lists/{list_id}/todos
# PATCH /lists/{list_id}/todos/{todo_id}
# DELETE /lists/{list_id}/todos/{todo_id}
