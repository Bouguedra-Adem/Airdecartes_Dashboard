from datetime import date
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import re

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

FiltreMap= html.Div([
    dbc.Row(
        [
        dbc.Col(
               [dcc.DatePickerRange(
                    id='my-date-picker-rangeMap',
                    min_date_allowed=date(1995, 8, 5),
                    max_date_allowed=date(2050, 9, 19),
                    initial_visible_month=date(2021, 1, 1),
                    start_date=date(2023, 1, 1),
                    end_date=date(2023, 12, 1)
                )],lg=12
                ),
         ]
    ),

    html.Div(id='output-container-date-picker-rangeMap')
])