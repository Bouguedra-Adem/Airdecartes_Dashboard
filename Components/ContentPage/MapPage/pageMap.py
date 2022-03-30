import dash_bootstrap_components as dbc

from Components.ContentPage.MapPage.FilterMap.FilterMapHtml import FiltreMap
from Components.ContentPage.MapPage.MapcallbackHtml import *
from Components.ContentPage.MapPage.MapcallbackHtml.Maphtml import Map

containerpage2=dbc.Container([

     dbc.Row(
        [
             dbc.Col([FiltreMap],lg=12,className="ColFiltre"),
             dbc.Col([Map], lg=12 ),

        ],id="RowMap"

     ),
],fluid=True,style={'width': '100%', 'height': '100%'},id="containerpage2")