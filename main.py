from fastapi import FastAPI, Request
import json
from fastapi.templating import Jinja2Templates

app= FastAPI()
templates = Jinja2Templates(directory="templates")

datos = {"1":"Python","2":"Java","3":"C++","4":"PHP"}

def key(datos):
    data = datos.keys()
    con = len(data)
    con = con + 1
    return con

@app.get('/')
def inicio(request:Request):
    sin_codificar = json.dumps(datos)
    json_datos = json.loads(sin_codificar)
    return templates.TemplateResponse("inicio.html",{"request":request , "listado":json_datos})


@app.post('/agregar')
async def nuevo(request:Request):
    nuevo_dato = await request.form()
    datos[key(datos)] = nuevo_dato['nuevo']
    sin_codificar = json.dumps(datos)
    json_datos = json.loads(sin_codificar)
    return templates.TemplateResponse("inicio.html",{"request":request , "listado":json_datos})


@app.get('/eliminar/{id}')
def elimi(request:Request, id:str):
    del datos[id]
    sin_codificar = json.dumps(datos)
    json_datos = json.loads(sin_codificar)
    return templates.TemplateResponse("inicio.html",{"request":request , "listado":json_datos})