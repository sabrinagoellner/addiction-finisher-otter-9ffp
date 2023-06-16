import dash
import dash_bootstrap_components as dbc
from dash import callback, Input, Output
from dash import html, dcc
from dash_bootstrap_templates import ThemeSwitchAIO

from src.components.graph_card import create_graph_card
# local imports
from src.components.page_header import create_page_header_box
from src.components.prepare_dataset_charts import basic_EDA, get_summary_table, to_styled_dict_table, create_wordcloud, \
    get_dataframe, to_styled_bar_chart, to_styled_pie_chart
from src.components.step_progress_bar import create_step_progress_bar

dash.register_page(
    __name__,
    path='/data-analysis/nlp',
    title='Data Analysis (NLP)'
)

dataset_name_text = html.Div(
    dbc.Label("Dataset:"),
    id="dataset_name_text"
)

prev_step_btn = dbc.Button("back", outline=True, color="primary", href="/select-data", disabled=False)
next_step_btn = dbc.Button("next step", outline=False, color="primary", href="/model-settings", disabled=False)

# the page header
card_content = create_page_header_box(
    icon='fa fa-2x fa-magnifying-glass-chart',
    title='Data Analysis (NLP)',
    description='Good and balanced data is the fuel for a good AI System.',
    prev_step=None,
    next_step=next_step_btn,
    extension=dataset_name_text
)

# summary_table_nlp = create_graph_card(card_type='table', title='Summary', card_id='summary_table_nlp')
# basic_eda_nlp = create_graph_card(card_type='table', title='Basic Exploratory Data Analysis', card_id='basic_eda_nlp')
bar_chart_nlp = create_graph_card(card_type='custom_graph',
                                  card_id='bar_chart_nlp',
                                  title="Distribution of classes (rating)",
                                  description="The graph shows we have unbalanced classes. The most common rating for a drug was 10. "
                                  )

pie_chart_nlp = create_graph_card(card_type='custom_graph',
                                  card_id='pie_chart_nlp',
                                  title="Distribution of positive and negative",
                                  description="The distribution is very unbalanced. We have three times as many positive ratings in relation to negative ones."
                                  )

image = create_graph_card(card_type='custom_graph',
                          card_id='heatmap_nlp',
                          title="Word Cloud",
                          description="WordCloud shows the frequency of words in our reviews and also shows that words such as 'side' (side effect) and 'take' are particularly common. Which is to be expected when it comes to medicine.")

page_content = dcc.Loading(
    id="loading-data-analysis",
    children=[
        dbc.Row(
            [
                # dbc.Col(
                #     summary_table_nlp,
                #     width=6,
                #     className="mb-4",
                # ),

                dbc.Col(
                    bar_chart_nlp,
                    width=6,
                    className="mb-4",
                ),

                dbc.Col(
                    pie_chart_nlp,
                    width=6,
                    className="mb-4",
                ),

                dbc.Col(
                    image,
                    width=6,
                    className="mb-4",
                ),

                # dbc.Col(
                #     basic_eda_nlp,
                #     width=12,
                #     className="mb-4",
                # ),

            ])
    ], type="circle")

layout = html.Div([
    create_step_progress_bar(["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security", "Explainability", "Results"], 3),
    card_content,
    page_content
])


# get the dataset which was chosen in the last step
@callback(
    Output('dataset_name_text', 'children'),
    #Input('dataset_input', 'data'),
    Input('model_type', 'data'),
)
def get_dataset(model_input):
    print("model_type name: ", model_input)
    if model_input == 'nlp':
        dataset_name_text = 'Medical Reviews'
        return 'Analyzing the data of: ' + str(dataset_name_text)


# callback for the charts
@callback(
    # Output('summary_table_nlp', 'children'),
    #Output('basic_eda_nlp', 'children'),
    Output('bar_chart_nlp', 'figure'),
    Output('pie_chart_nlp', 'figure'),
    Output('heatmap_nlp', 'figure'),

    #Input('dataset_input', 'data'),
    Input('model_type', 'data'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def summary_table(model_type, theme_switch):
    #print("nlp model_type ", model_type)

    if model_type is not None:
        template = "cosmo" if theme_switch else "superhero"
        print("EDA model_type ", model_type)


        # TODO feature engineering is hard coded here,
        #  but will be dynamically in future, we rely on one model in the current state of the art
        dataset_input = "medical-reviews"

        df = get_dataframe(dataset_input)
        # basic_eda = basic_EDA(df)
        # basic_eda_plot = to_styled_dict_table(basic_eda, template)

        # create the resulting table:
        # get_summary = get_summary_table(df)
        # summary = to_styled_dict_table(get_summary, template)

        # bar chart
        px_bar_chart = to_styled_bar_chart(
            dataframe=df['rating'].value_counts(),
            title="",
            template=template)

        # sentiment pie chart:
        # let's make a new column review sentiment
        df.loc[(df['rating'] >= 5), 'sentiment'] = 1
        df.loc[(df['rating'] < 5), 'sentiment'] = 0

        px_pie_chart = to_styled_pie_chart(
            dataframe=df['sentiment'].value_counts(),
            title="",
            values='sentiment',
            classes=['positive', 'negative'],
            template=template)

        # word cloud image:
        px_wordcloud = create_wordcloud(df['review'], template=template, title='')
        return px_bar_chart, px_pie_chart, px_wordcloud


