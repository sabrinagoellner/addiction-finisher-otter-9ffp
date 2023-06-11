import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import get_asset_url

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY, dbc.icons.FONT_AWESOME],
    use_pages=True,  # turn on Dash pages
)

def serve_layout():
    """Define the layout of the application"""
    return html.Div(
        [
            #header,
            dash.page_container,
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
