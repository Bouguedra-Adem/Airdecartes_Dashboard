import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import Components.NavBar.NavBar as styleNav
from Components.ContentPage.MapPage.FilterMap.FilterMapCallback import callback_managerFiltreMap
from Components.ContentPage.GraphePage.Filtre_Hist_MoM.FiltreCallback import callback_managerFiltreHisto
from Components.ContentPage.TablePage.TableHt.tabfilter import callback_managerFiltretab
from Components.SideBar import SideBar
from Components.ContentPage import  Content
from Components.ContentPage.GraphePage.Histogram.Histogram import *
from Components.SideBar.CalbackSideBar import callback_manager
from Components.NavBar.CallbackNav import callback_manager1
suppress_callback_exceptions=True

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
chroma = "https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.1.0/chroma.min.js"

app = dash.Dash(external_scripts=[chroma], prevent_initial_callbacks=True,external_stylesheets=[dbc.themes.BOOTSTRAP, FA])
callback_manager.attach_to_app(app)
callback_manager1.attach_to_app(app)
callback_managerFiltreHisto.attach_to_app(app)
callback_managerFiltreMap.attach_to_app(app)
callback_managerFiltretab.attach_to_app(app)
navbar=styleNav.navbar
content=Content.content
sidebar = SideBar.sidebar
app.layout = html.Div(
    [
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar,
        sidebar,
        content,
    ],
)
if __name__ == "__main__":
    app.run_server(debug=False, port=8086 ,dev_tools_hot_reload=False)