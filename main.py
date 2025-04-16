from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Create directories if they don't exist
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Home page (login)
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Task boards list
@app.get("/boards", response_class=HTMLResponse)
async def get_boards(request: Request):
    return templates.TemplateResponse("boards.html", {"request": request})

# Task board detail
@app.get("/board/{board_id}", response_class=HTMLResponse)
async def get_board(request: Request, board_id: str):
    return templates.TemplateResponse("board.html", {"request": request, "board_id": board_id})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)