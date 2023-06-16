# notes
"""
This file creates a model card.
"""
import dash
# package imports
import dash_bootstrap_components as dbc
from dash import html, get_asset_url

def create_model_card(data_id, image_src, title, task, data_type, framework, model_kind, template=""):
    card = dbc.Card(
        dbc.CardBody(
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(src=get_asset_url(image_src)),
                        width=3,
                        className="mt-4"
                    ),
                    dbc.Col(
                        [
                            html.H5(title, className="card-title"),
                            html.B("Machine Learning task:"),
                            html.P(task),
                            html.B("Data type:"),
                            html.P(data_type),
                            html.B("Machine Learning Framework:"),
                            html.P(framework),
                            html.B("Model:"),
                            html.P(model_kind),
                        ],
                        width=9,
                        className="mt-4"
                    ),
                ],
            )
        ), color=template
    )
    return card
