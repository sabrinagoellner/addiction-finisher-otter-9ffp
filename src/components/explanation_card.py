# notes
"""
This file creates an exlpanation card.
"""

# package imports
import dash_bootstrap_components as dbc
from dash import html, get_asset_url


def create_explanation_card(card_title, explanation, metric_result, metric_explanation, image_name="placeholder-image"):
    card = dbc.Card(
        dbc.CardBody(
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(src=get_asset_url('images/'+image_name+'.png')),
                        width=4,
                        className="mt-4",
                        style={"display": "none"} if image_name == "placeholder-image" else {"display": "block"}
                    ),
                    dbc.Col(
                        [
                            html.H5(card_title, className="card-title"),
                            html.B("Metric Result:"),
                            html.H4(id=metric_result),
                            html.H5(id=metric_explanation),
                            html.B("Explanation:"),
                            html.P(explanation),
                        ],
                        width=8,
                        className="mt-4",

                    ),
                ],
            )
        )
    )
    return card


