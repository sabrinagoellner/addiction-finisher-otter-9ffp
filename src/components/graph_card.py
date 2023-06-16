from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc


def create_graph_card(card_id, title='', description='', card_type='summary_table'):

    if card_type == 'table':
        graph_card = dbc.Card(
            dbc.CardBody(
                [
                    html.H4(title),
                    html.P(description),
                    dbc.Table(
                        id=card_id,
                    ),

                ]
            )
        )
        return graph_card

    elif card_type == 'custom_graph':

        graph_card = dbc.Card(
            dbc.CardBody(
                [
                    html.H4(title),
                    html.P(description),
                    dcc.Graph(
                        id=card_id,
                    ),

                ]
            )
        )
        return graph_card

    elif card_type == 'html_div':

        graph_card = dbc.Card(
            dbc.CardBody(
                [
                    html.H4(title),
                    html.P(description),
                    html.Div(
                        id=card_id,
                    ),

                ]
            )
        )
        return graph_card



    else:
        return None

