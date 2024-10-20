from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import plotly.express as px
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "graph": None})

@app.post("/", response_class=HTMLResponse)
async def generate_map(request: Request, country: str = Form(...)):
    data = pd.DataFrame({
        'Country': [country],
        'Values': [100]
    })
    fig = px.choropleth(
        data,
        locationmode='country names',
        locations='Country',
        color='Values',
        color_continuous_scale='Inferno',
        title=f'Country Map Highlighting {country}'
    )
    fig.update_layout(
        autosize=True,
        width=1000,  
        height=500  
    )
    graph_html = fig.to_html(full_html=False)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "graph": graph_html,
        "country": country
    })
