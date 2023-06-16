# notes
'''
This file is for creating a navigation bar that will sit at the top of your application.
Much of this page is pulled directly from the Dash Bootstrap Components documentation linked below:
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
'''

# package imports
from dash import html, callback, Output, Input, State, dcc, get_asset_url
import dash_bootstrap_components as dbc

# local imports
# from utils.images import logo_encoded
# from components.login import login_info
PROJECT_NAME = 'VERIFAI'

# TODO create a All in One Component for reusing this with dynamic states -> progress steps

row_content = [
    dbc.Col(
        dbc.CardImg(
            src=('assets/logos/verifai-logo-small.png'),
            style={'height': '65px', 'width': 'auto', 'text-align': 'center', 'display': 'block'},
            className="center mx-auto",
        ),
        width=2,
        className="align-items-center justify-content-center"
    ),
]

row = html.Div(
    [
        dbc.Row(
            row_content,
            justify="center",
        ),
    ]
)

# component
navbar = dbc.CardHeader(
    row,
    className="m-0 p-0"
)

# @callback(
#     Output('progress', 'value'),
#     [Input('url', 'pathname')])
# def callback_func(pathname):
#
#     if pathname == '/start':
#         print(pathname)
#         return 10
#     return 50
