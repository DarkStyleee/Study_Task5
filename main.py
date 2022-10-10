from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn


c = 1
name = "Felix Ussaev"
app = FastAPI()


@app.get("/")
async def root():
    return {"Counter": c}


@app.get("/stat")
async def stat():
    global c
    c += 1
    return {"Counter": c - 1}


@app.get("/about")
async def about():
    return HTMLResponse(f"<h3> Hello , { name }</h3>")


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
