import dash
import base64
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


#from Components.NavBar.StyleNavBar import NAV_Style, Img_Style



image_filename = "./Assets/images/téléchargement (2).png"
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')

navbar = dbc.NavbarSimple(
    children=[

        dbc.Button("Full Screen", outline=False, color="secondary", className="mr-1", id="btn_sidebar" )


    ],


    color="rgb(45 44 42)",
    dark=True,
    fluid=True,
    className="NAV_Style"

)




