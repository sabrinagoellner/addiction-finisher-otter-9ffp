import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import get_asset_url

dash.register_page(
    __name__,
    path='/',
    redirect_from=['/home'],
    title='Home'
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Alert("LIVE DEMO will be available soon on this page.", color="light"),
                dbc.Card([
                    dbc.CardHeader("VERIFAI Lifecycle"),
                    dbc.CardImg(src=get_asset_url('verifai_lifecycle.png '))
                ],
                    class_name="my-2",
                ),

                dbc.Col(
                    [
                        dbc.Row([
                            dbc.Col(
                                html.I(className="fa fa-2x fa-lock"),
                                width=2
                            ),
                            dbc.Col(
                                html.H2(
                                    "Privacy",
                                    className="card-title"),
                                width=10
                            ),
                        ]),
                        html.P(
                            "Privacy Leakage belongs to the big issues in the AI Landscape. Therefore we check if our model values privacy."
                        ),
                    ],
                    md=4,
                ),

                dbc.Col(
                    [
                        dbc.Row([
                            dbc.Col(
                                html.I(className="fa fa-2x fa-scale-balanced"),
                                width=2
                            ),
                            dbc.Col(
                                html.H2(
                                    "Fairness",
                                    className="card-title"),
                                width=10
                            ),
                        ]),
                        html.P(
                            "A fair model is the baseline for a responsible AI System. Fairness is defined as: non-biased and non-discriminating in any way."
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        dbc.Row([
                            dbc.Col(
                                html.I(className="fa fa-2x fa-shield"),
                                width=2
                            ),
                            dbc.Col(
                                html.H2(
                                    "Security",
                                    className="card-title"),
                                width=10
                            ),
                        ]),
                        html.P(
                            "Secure is defined as robust against any kind of adversarial attacks."
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        dbc.Row([
                            dbc.Col(
                                html.I(className="fa fa-2x fa-lightbulb"),
                                width=2
                            ),
                            dbc.Col(
                                html.H2(
                                    "Explainability",
                                    className="card-title"),
                                width=10
                            ),
                        ]),
                        html.P(
                            "Explainability is the most important feature for users trust in your AI System."
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        dbc.Row([
                            dbc.Col(
                                html.I(className="fa fa-2x fa-handshake"),
                                width=2
                            ),
                            dbc.Col(
                                html.H2(
                                    "Trust",
                                    className="card-title"),
                                width=10
                            ),
                        ]),
                        html.P(
                            "Trustworthy AI for the user."
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        dbc.Row([
                            dbc.Col(
                                html.I(className="fa fa-2x fa-user-circle"),
                                width=2
                            ),
                            dbc.Col(
                                html.H2(
                                    "Human Centered",
                                    className="card-title"),
                                width=10
                            ),
                        ]),
                        html.P(
                            "AI built to support humans and maintained by humans."
                        ),
                    ],
                    md=4,
                ),
                html.Hr(className="my-2"),

            ]
        )
    ],
    className="mt-4",
)