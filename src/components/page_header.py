# package imports
import dash_bootstrap_components as dbc
from dash import html

# notes
"""
This creates a header box, which shows information about what happens in the current step.
"""


def create_page_header_box(icon=None, title='Title', description='Desc', prev_step="", next_step="", extension=None):
    header_box = dbc.Card(
        dbc.CardBody(
            [dbc.CardHeader(
                [
                    dbc.Row([
                        dbc.Col(
                            html.I(className=icon),
                            width=1
                        ),
                        dbc.Col(
                            html.H4(
                                title,
                                className="card-title"),
                            width=11
                        ),
                    ]),
                ]
            ),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col([
                                    html.P(
                                        description
                                    ),
                                ],
                                    width=10
                                ),
                                dbc.Col(
                                    dbc.ButtonGroup(
                                        [
                                            prev_step,
                                            next_step,
                                        ]
                                    ),
                                    width=2
                                ),
                            ]
                        ),

                    ]

                ),

                dbc.CardFooter(extension),
            ]
        ),
        className='mb-2'
    )
    return header_box
