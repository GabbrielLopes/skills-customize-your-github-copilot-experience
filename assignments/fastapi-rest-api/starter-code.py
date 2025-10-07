from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items: List[Item] = []

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items", response_model=List[Item])
def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            del items[i]
            return {"ok": True}
    raise HTTPException(status_code=404, detail="Item not found")
