# from typing import Union
from fastapi import FastAPI, Response
# from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn

# from pydantic import BaseModel

app = FastAPI()

# if __name__ == "__main__":
#     app.run(port=5000)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["Content-Type", 'application/html'],
)

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# if __name__ == '__main__':
#     uvicorn.run('main:app', server_header=False)

# if __name__ == "__main__":
#     uvicorn.run("main:app", headers=[("server", "firstproject")])


@app.get("/")
async def root():
    return {"message": "Hello Vivek"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {'item_id': item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
