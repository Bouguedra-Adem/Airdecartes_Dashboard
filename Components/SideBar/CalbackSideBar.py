import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from Components.ContentPage.MapPage.pageMap import containerpage2
from Components.ContentPage.TablePage.Page3tab import containerpage3
from callbacks_managers import CallbackManager
from Components.ContentPage.GraphePage.Page1ContentHTML import *
callback_manager = CallbackManager()



#**********************************************************************************************************

@callback_manager.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return containerpage1
    elif pathname == "/page-2":
        return containerpage2
    elif pathname == "/page-3":
        return containerpage3
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
