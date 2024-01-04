from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    # if request.user.is_authenticated:
    #     return render(request, "dashboard.html", {}, status_code=200)
    return {"hello":"world"} # json data -> REST API render(request, "home.html", {})