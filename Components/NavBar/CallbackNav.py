import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


from callbacks_managers import CallbackManager

callback_manager1 = CallbackManager()




#**********************************************************************************************************
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
def set_navitem_class(is_open):
    if is_open:
        return "open"
    return ""

#**********************************************************************************************************
@callback_manager1.callback(
    [
        Output("sidebar", "className"),
        Output("page-content", "className"),
        Output("side_click", "data"),
    ],
    [Input("btn_sidebar", "n_clicks"),],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            x= "SIDEBAR_HIDEN"
            content_style = "CONTENT_STYLE_2"
            cur_nclick = "HIDDEN"
        else:
            x = "SIDEBAR_STYLE"
            content_style = "CONTENT_STYLE"
            cur_nclick = "SHOW"
    else:
        x = "SIDEBAR_STYLE"
        content_style = "CONTENT_STYLE"
        cur_nclick = 'SHOW'

    return x, content_style, cur_nclick

#**********************************************************************************************************
@callback_manager1.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 5)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False,False
    return [pathname == f"/page-{i}" for i in range(1, 5)]

for i in [1, 2]:
    callback_manager1.callback(
        Output(f"submenu-{i}-collapse", "is_open"),
        [Input(f"submenu-{i}", "n_clicks")],
        [State(f"submenu-{i}-collapse", "is_open")],
    )(toggle_collapse)

    callback_manager1.callback(
        Output(f"submenu-{i}", "className"),
        [Input(f"submenu-{i}-collapse", "is_open")],
    )(set_navitem_class)
