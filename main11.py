from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(accept: Annotated[str | None, Header()] = None,content_type: Annotated[str | None, Header()] = None):

    return {"Accept": accept, "content-type":content_type}