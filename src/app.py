import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import get_asset_url

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, dbc.icons.FONT_AWESOME])
server = app.server

header = html.Div(
    dbc.Container(
        [   
            html.H2("VERIFAI - A Step towards Evaluating the Responsibility of AI-Systems."),            
            html.P([
                    "A first step towards a unified framework for RESPONSIBLE AI."                    
                ],
                className="lead",
                ),
            html.Hr(className="my-2"),            
            dbc.Button("Research Paper", color="primary", size="lg", href="https://dl.gi.de/handle/20.500.12116/40372"), 
                    
        ],
        fluid=True,
        className="py-3 my-2",
    ),
    className="h-100 p-5 text-white bg-success",
)

body = dbc.Container(
    [
        dbc.Row(
            [   
                dbc.Alert("A demo off the app will be available soon on this page.", color="light"),
                dbc.Card([
                    dbc.CardHeader("VERIFAI Lifecycle"),
                    dbc.CardImg(src=get_asset_url('lifecycle.svg'))
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

app.layout = html.Div([header, body])

if __name__ == "__main__":
    app.run_server(debug=False)
