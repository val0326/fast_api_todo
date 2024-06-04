from fastapi import FastAPI

from api import include_routers


app = FastAPI(title="Fast API - todo list")
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
