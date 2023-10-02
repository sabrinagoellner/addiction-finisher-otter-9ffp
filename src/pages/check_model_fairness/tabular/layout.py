import dash
import dash_bootstrap_components as dbc
import dash_dangerously_set_inner_html
from dash import callback, Input, Output, html, dcc
from dash_bootstrap_templates import ThemeSwitchAIO

from src.components import create_explanation_card, get_explanation_text
from src.components.graph_card import create_graph_card
# local imports
from src.components.page_header import create_page_header_box
from src.components.step_progress_bar import create_step_progress_bar

# TODO TEST
#from src.components.fairness.fairness import measure_fairness_on_tabular_data


dash.register_page(
    __name__,
    path='/model-fairness/tabular',
    title='Check Model Fairness (Tabular)'
)

next_step_btn = dbc.Button(
    "next step",
    color="primary",
    href='/model-privacy/tabular',  # default! changes dynamically if selected
    disabled=False
)

# the page header
page_header = create_page_header_box(
    icon='fa fa-2x fa-scale-balanced',
    title='Model Fairness (Tabular)',
    description='A fair model is the baseline for a responsible AI System. Fairness is defined as: non-biased and non-discriminating in any way. ',
    prev_step=None,
    next_step=next_step_btn,
)


fairness_report_table = create_graph_card(card_type='html_div',
                                          title='Fairness Measure Report',
                                          description='We have a bias in the metrics: Disparate Impact Ratio, Equal '
                                                      'Odds Ratio and Statistical parity Difference. ',
                                          card_id='fairness_report_table')

bias_table = create_graph_card(card_type='html_div',
                               title='Stratified Bias Table',
                               description='The bias indicates a higher likelihood of detecting heart disease in '
                                          'male patients as opposed to female patients',
                               card_id='bias_table')

explanation = create_explanation_card(
    card_title='Fairness Performance',
    explanation='The metrics determine how fair the model can predict among classes individually.',
    metric_result='fairness_results',
    metric_explanation='fairness_explanation',
    image_name='fairness'
)

select_protected_attr = dbc.Card(
    dbc.Select(
        options=[
            {"label": "Gender", "value": "sex"},
            {"label": "Age", "value": "age"},
        ],
        value="sex",
        id="radioitems-input",
    ),
)

fairness = dcc.Loading([
    dbc.Row(
        [
            # explains decision:
            dbc.Col(
                explanation,
                width=12,
                className="mb-4",
            ),
            dbc.Col(
                bias_table,
                width=12,
                className="mb-4",
                id="bias_table_container"
            ),
            dbc.Col(
                [
                    select_protected_attr,
                    fairness_report_table,
                ],
                width=6,
                className="mb-4",
                id="fairness_report_table_container"
            ),
        ]),
],
    type="circle",
    id="loading-5"
)

layout = dbc.Container([
    create_step_progress_bar(
        ["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security",
         "Explainability", "Results"], 5),
    page_header,
    fairness
])


@callback(
    [
        Output('fairness_report_table', 'children'),
        Output('bias_table', 'children'),
        Output('fairness_results', 'children'),
        Output('fairness_explanation', 'children'),
        Output('fairness_score_tabular', 'data')],

    [
        Input('model_type', 'data'),
        Input('dataset_size', 'data'),
        Input('selected_model', 'data'),
        Input(ThemeSwitchAIO.ids.switch("theme"), "value")
    ],
)
def update_selected(model_type, dataset_size, selected_model, theme_switch):
    print(model_type)

    if model_type is None:
        return dash.no_update
    else:
        template = "cosmo" if theme_switch else "superhero"

        # open static files:
        r_as_html = open("assets/plots/fairness/fmlh/report_as_html.html", "r")
        report_as_html = r_as_html.read()
        b_as_html = open("assets/plots/fairness/fmlh/bias_as_html.html", "r")
        bias_as_html = b_as_html.read()
        fairness_proportion = 0.82
        fairness_score = 8


        # if template is dark, load the light styles for the tables via css, dark otherwise:
        if template == "superhero":
            fairness_report_table = dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <div class="table__dark_template">''' + report_as_html + '''</div>''')
            bias_table = dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <div class="table__dark_template">''' + bias_as_html + '''</div>''')
        else:
            fairness_report_table = dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <div class="table__light_template">''' + report_as_html + '''</div>''')
            bias_table = dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <div class="table__light_template">''' + bias_as_html + '''</div>''')

        fairness_explanation = get_explanation_text(fairness_score, 'fairness')
        fairness_score_ui = str(fairness_proportion) + " (" + str(fairness_score) + "/10)"

        return fairness_report_table, bias_table, fairness_score_ui, fairness_explanation, fairness_score
