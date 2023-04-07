import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import get_asset_url

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY, dbc.icons.FONT_AWESOME],
    use_pages=True,  # turn on Dash pages
)

header = html.Div(
    dbc.Container(
        [
            html.H2("VERIFAI - A Step towards Evaluating the Responsibility of AI-Systems."),
            html.P([
                    "A first step towards a unified framework for RESPONSIBLE AI."
                ],
                className="lead",
                ),
            # html.P("The prototype is tested using healthcare datasets and can handle image, text, and tabular data. Since healthcare represents an area where automatic decisions affect decisions about human lives, building responsible AI in this area is therefore indispensable.")
            html.Hr(className="my-2"),
            dbc.Button("Research Paper", color="primary", size="lg", href="https://dl.gi.de/handle/20.500.12116/40372"),

        ],
        fluid=True,
        className="py-3 my-2",
    ),
    className="h-100 p-5 text-white bg-success",
)

def serve_layout():
    """Define the layout of the application"""
    return html.Div(
        [
            header,
            dbc.Container(
                [
                    dash.page_container,
                 ],
                class_name='my-2'
            ),

            dbc.Container(
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                'Index',
                                href='/'
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                'Privacy',
                                href='/privacy'
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                'Legal Notice',
                                href='/disclaimer'
                            )
                        ),
                    ]),
            ),

        ]
    )


app.layout = serve_layout  # set the layout to the serve_layout function
server = app.server


if __name__ == "__main__":
    app.run_server(debug=True)
