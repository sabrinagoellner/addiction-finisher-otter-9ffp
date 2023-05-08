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
            html.H2("VERIFAI - Evaluating the Responsibility of AI-Systems."),
            html.P([
                    "In recent years, significant advancements in the field of artificial intelligence (AI) have "
                    "transformed the way industries and organizations operate. Breakthroughs in machine learning and "
                    "deep learning techniques have enabled AI systems to perform remarkably in tasks such as computer "
                    "vision, natural language processing, and decision-making. These developments have led to the "
                    "widespread adoption of AI in various sectors, including healthcare, finance, and transportation. "
                    "Moreover, AI is becoming increasingly ingrained in daily life, leading to discussions about the "
                    "roles of technologies like ChatGPT as artificial generators of text, code, and more. Therefore "
                    "concerns about the security, explainability, privacy, and ethics of AI systems have emerged, "
                    "prompting researchers to explore methods of evaluating and ensuring responsible AI practices. "
                ],
                className="lead",
                ),
            html.P("Therefore we have created ’VERIFAI’ (eValuating thE ResponsibIlity oF AI-systems),which builds on "
                   "top of our previous work and provides a "
                   "comprehensive assessment of AI systems in terms of their responsibility and performance across "
                   "various dimensions. By leveraging this framework, researchers and practitioners can better "
                   "understand the strengths and weaknesses of their AI systems and make informed decisions to "
                   "improve their overall responsibility level.",
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
