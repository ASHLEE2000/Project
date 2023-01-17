import fastapi
from fastapi import Request , Form
import chain
import QR_gen
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse , FileResponse, RedirectResponse


app = fastapi.FastAPI()
templates = Jinja2Templates(directory = "htmlfiles")


# uviocorn main:app --reload
# python -m uvicorn fast_api:app --reload
# ctrl + c to stop local server


#first endpoint
@app.get('/',response_class=HTMLResponse)
def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("home.html", context) 

#second endpoint
@app.post('/scanner',response_class=HTMLResponse)
async def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("scan.html", context) 

#third endpoint
@app.post('/add_block',response_class=HTMLResponse)
async def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("chain.html", context) 

#4th endpoint
@app.post('/enter_block')
async def e_block(ID: str= Form(...),name : str = Form(...), price : float = Form(...)):
    #context = {"request": request}
    chain.block(ID,name,price)
    #file_path = "/qrcodesImgs/"
    #c= QR_gen.QR_co.block_no
    #return RedirectResponse("/enter_block/entered_block")
    return "sucessfull"

@app.get('/enter_block/entered_block', response_class=HTMLResponse)
def e_b(request: Request):
    context = {'request': request }
    return templates.TemplateResponse("blockEntered.html", context)

@app.get('/about', response_class=HTMLResponse)
def e_b(request: Request):
    context = {'request': request }
    return templates.TemplateResponse("about.html", context)