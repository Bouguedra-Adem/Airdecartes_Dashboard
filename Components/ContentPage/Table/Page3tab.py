import dash_core_components as dcc
import dash_bootstrap_components as dbc
from .TableHt.table import tabhtml

containerpage3=dbc.Container([

     dbc.Row(
        [
             dbc.Col([tabhtml],lg=12,className="ColFiltre",id="ad"),

        ],
       id="Rowtabb"
     )],

    id="containerTab2",
fluid=True
)