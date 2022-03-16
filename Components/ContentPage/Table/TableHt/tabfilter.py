import dash_html_components as html
import dash
import datetime as date
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from callbacks_managers import CallbackManager
import dash_leaflet as dl
import dash_leaflet.express as dlx
from ast import literal_eval
import http.client
import json
from dash_extensions.javascript import assign

callback_managerFiltretab = CallbackManager()


@callback_managerFiltretab.callback(
    Output('datatable-interactivity1', 'style_data_conditional'),
    Input('datatable-interactivity1', 'selected_columns')
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]
