import fastapi
from fastapi import Request ,Depends, HTTPException, Form
import chain
import QR_gen
import all_user
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse , FileResponse, RedirectResponse


app = fastapi.FastAPI()
templates = Jinja2Templates(directory = "htmlfiles")
staticfiles = StaticFiles(directory="./qrcodesImgs/")
app.mount("/static", staticfiles, name="static")

# uviocorn main:app --reload
# python -m uvicorn fast_api:app --reload
# ctrl + c to stop local server


#first endpoint
@app.get('/',response_class=HTMLResponse)
def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("home.html", context) 

@app.post('/',response_class=HTMLResponse)
def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("home.html", context) 

#second endpoint
@app.post('/add_block',response_class=HTMLResponse)
async def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("log_in.html", context) 

#third endpoint
@app.post('/sign_in', response_class=HTMLResponse)
async def sign_in(request : Request):
    context = {"request": request}
    return templates.TemplateResponse("sing_up.html", context)

#fourth endpoint
@app.post('/sign_up', response_class=HTMLResponse)
async def sign_up(request :Request, Username: str= Form(...),password : str = Form(...),):
    context = {"request": request}
    a= all_user.users(Username,password,'ff5877')
    key2=all_user.users.get_key2(a)
    path : str 
    return templates.TemplateResponse("sign_up_confirm.html",{"request": request, "un":Username, "p": password,"k":key2 } )
    
#fifth endpoint
@app.post('/enter_block')
async def e_block(request :Request, name: str= Form(...),id : str = Form(...), price: float = Form(...),date: str = Form(...)):
    n1 =chain.block(name,id,price,date)
    context = {"request": request}
    b= chain.block.get_block_no(n1)
    a= ("BLOCK-"+str(b)+".jpg")
    #return FileResponse(f"./qrcodesImgs/{a}")
    return templates.TemplateResponse("blockEntered.html",context  )


#sixth endpoint
@app.post('/log_in', response_class=HTMLResponse)
async def log_in(request :Request, Username: str= Form(...),password : str = Form(...), key: str = Form(...)):
    a= all_user.list_of_users.verify_user(100,Username,password,key)
    context = {"request": request}
    if(a):
        return templates.TemplateResponse("enterblock.html",{"request": request, "n":Username} )
    else:
        raise HTTPException(status_code=404, detail="ERROR: YOU'RE NOT A VALID USER\n PLEASE SIGN UP")

#seventh endpoint     
@app.post('/verify_product',response_class=HTMLResponse)
def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("scan.html", context) 

#eigth endpoint
@app.post('/sign_up_confirm', response_class=HTMLResponse)
async def sign_up(request :Request):
    return templates.TemplateResponse("enterblock.html",{"request": request} )


@app.post('/about',response_class=HTMLResponse)
def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("about.html", context) 
  
  #chain.block(ID,name,price)
    #file_path = "/qrcodesImgs/"
    #c= QR_gen.QR_co.block_no
    #return RedirectResponse("/enter_block/entered_block")