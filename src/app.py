import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import get_asset_url, dcc
# from flask import Flask

from src.components import footer, navbar

# server = Flask(__name__)
app = dash.Dash(
    __name__,
    # server=server,
    use_pages=True,  # turn on Dash pages
    external_stylesheets=[
        dbc.themes.FLATLY,
        dbc.icons.FONT_AWESOME
    ],  # fetch the proper css items we want
    meta_tags=[
        {  # check if device is a mobile device. This is a must if you do any mobile styling
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1'
        }
    ],
    suppress_callback_exceptions=True,
    title='VERIFAI'
)


storage = html.Div([
    # global storages
    dcc.Store(id="model_type", data=[], storage_type="session"),
    dcc.Store(id="dataset_size", data=[], storage_type="session"),
    dcc.Store(id="selected_model", data=[], storage_type="session"),

    # TODO: delete if storage works for individual models!
    # dcc.Store(id="fairness_score", data=[], storage_type="session"),
    # dcc.Store(id="privacy_score", data=[], storage_type="session"),
    # dcc.Store(id="security_score", data=[], storage_type="session"),
    # dcc.Store(id="explainability_score", data=[], storage_type="session"),

    # model specific data storages:
    # Image:
    dcc.Store(id="fairness_score_img", data=[], storage_type="session"),
    dcc.Store(id="privacy_score_img", data=[], storage_type="session"),
    dcc.Store(id="security_score_img", data=[], storage_type="session"),
    dcc.Store(id="explainability_score_img", data=[], storage_type="session"),

    # do the same for nlp
    dcc.Store(id="fairness_score_nlp", data=[], storage_type="session"),
    dcc.Store(id="privacy_score_nlp", data=[], storage_type="session"),
    dcc.Store(id="security_score_nlp", data=[], storage_type="session"),
    dcc.Store(id="explainability_score_nlp", data=[], storage_type="session"),

    # and tabular
    dcc.Store(id="fairness_score_tabular", data=[], storage_type="session"),
    dcc.Store(id="privacy_score_tabular", data=[], storage_type="session"),
    dcc.Store(id="security_score_tabular", data=[], storage_type="session"),
    dcc.Store(id="explainability_score_tabular", data=[], storage_type="session"),

    # TODO later: and add a custom data storage for uploads

])

def serve_layout():
    """Define the layout of the application"""
    return html.Div(
        [
            navbar,
            storage,
            dash.page_container,
            footer,

        ]
    )


app.layout = serve_layout  # set the layout to the serve_layout function
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True,
                   port=8080
                   )
