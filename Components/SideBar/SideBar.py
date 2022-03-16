import base64

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

image_filename = "./Assets/images/logo_yassir.png"
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')


#************************text**********************
submenu_1 = [
    html.Li(

        dbc.Row(
            [
                dbc.Col("Menu 1"),
                dbc.Col(
                    html.I(className="fas fa-chevron-right mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        style={"color": "white"},
        id="submenu-1",
    ),
   
   
    dbc.Collapse(
        [
          
            dbc.NavLink("Visualisation", href="/page-1", id="page-1-link"),
            dbc.NavLink("Map", href="/page-2", id="page-2-link"),
            dbc.NavLink("Tab", href="/page-3", id="page-3-link"),
        ],
        id="submenu-1-collapse",
    ),
]


#************************text**********************




sidebar = html.Div(
    [
     html.Div(
            [
                html.Img(src='data:image/png;base64,{}'.format(encoded_image), className="Img_Style"),
        #        html.Div(html.H3("Yassir", style={"color": "#fff"}), className="DivSpan")
            ],
                className="YassirLog"
            ),
        html.Hr(),
        html.Hr(className="hrBottom"),
        dbc.Nav(submenu_1 ,
               vertical=True,
         ),
    ],
    className="SIDEBAR_STYLE",
    id="sidebar",
)




