import dash
import dash_bootstrap_components as dbc
from dash import callback, Input, Output
from dash import html, dcc
from dash_bootstrap_templates import ThemeSwitchAIO

from src.components.graph_card import create_graph_card
# local imports
from src.components.page_header import create_page_header_box
from src.components.prepare_dataset_charts import basic_EDA, get_summary_table, to_styled_dict_table, get_dataframe, \
    to_styled_bar_chart, to_styled_pie_chart
from src.components.prepare_dataset_charts import prepare_dataframe_skin, skin_heatmap
from src.components.step_progress_bar import create_step_progress_bar

dash.register_page(
    __name__,
    path='/data-analysis/image',
    title='Data Analysis'
)

dataset_name_image = html.Div(
    dbc.Label("Dataset:"),
    id="dataset_name_image"
)

prev_step_btn = dbc.Button("back", outline=True, color="primary", href="/select-data", disabled=False)
next_step_btn = dbc.Button("next step", outline=False, color="primary", href="/model-settings", disabled=False)

# the page header
card_content = create_page_header_box(
    icon='fa fa-2x fa-magnifying-glass-chart',
    title='Data',
    description='Good and balanced data is the fuel for a good AI System.',
    prev_step=None,
    next_step=next_step_btn,
    extension=dataset_name_image
)

summary_table_image = create_graph_card(card_type='table', title='Summary', card_id='summary_table_image')
basic_eda_image = create_graph_card(card_type='table', title='Basic Exploratory Data Analysis', card_id='basic_eda_image')


bar_chart_image = create_graph_card(card_type='custom_graph',
                                    card_id='bar_chart_image',
                                    title="Distribution of classes",
                                    description="The graph shows we have unbalanced classes. The most common class is melanocytic nevi.")

pie_chart_image = create_graph_card(card_type='custom_graph',
                                    card_id='pie_chart_image',
                                    title="Distribution of Gender",
                                    description="The distribution is almost fair."
                                    )
image = create_graph_card(card_type='custom_graph',
                          card_id='heatmap_image',
                          title="Heatmap of Localization",
                          description="The most of the skin anomalies are located on the back."
                          )

page_content = dcc.Loading(
    id="loading-data-analysis",
    children=[
        dbc.Row(
            [
                # dbc.Col(
                #     summary_table_image,
                #     width=6,
                #     className="mb-4",
                # ),

                dbc.Col(
                    bar_chart_image,
                    width=6,
                    className="mb-4",
                ),

                # dbc.Col(
                #     pie_chart_image,
                #     width=6,
                #     className="mb-4",
                # ),

                dbc.Col(
                    image,
                    width=6,
                    className="mb-4",
                ),

                # dbc.Col(
                #     basic_eda_image,
                #     width=12,
                #     className="mb-4",
                # ),

            ])
    ], type="circle")

layout = dbc.Container([
    create_step_progress_bar(["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security", "Explainability", "Results"], 3),
    card_content,
    page_content
])



# get the dataset which was chosen in the last step
@callback(
    Output('dataset_name_image', 'children'),
    #Input('dataset_input', 'data'),
    Input('model_type', 'data'),
)
def get_dataset(model_input):
    #print("model_type name: ", model_input)
    if model_input == 'image':
        dataset_name_image = 'Skin Cancer'
        return 'Analyzing the data of: ' + str(dataset_name_image)


# callback for the charts
@callback(
    #Output('summary_table_image', 'children'),
    #Output('basic_eda_image', 'children'),
    Output('bar_chart_image', 'figure'),
    # Output('pie_chart_image', 'figure'),
    Output('heatmap_image', 'figure'),

    Input('model_type', 'data'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def summary_table(model_type, theme_switch):
    if model_type is not None:
        print("EDA model_type ", model_type)
        template = "cosmo" if theme_switch else "superhero"

        dataset_choice = "skin-cancer"

        # data prep ->
        df = get_dataframe(dataset_choice)
        df_prep = prepare_dataframe_skin(df)
        get_summary = get_summary_table(df_prep)
        basic_eda = basic_EDA(df)

        # create the resulting styled tables:
        basic_eda_plot = to_styled_dict_table(basic_eda, template)
        summary = to_styled_dict_table(get_summary, template)

        px_bar_chart = to_styled_bar_chart(
            dataframe=df['cell_type'].value_counts(),
            title="Skin Lesions",
            template=template)

        # px_pie_chart = to_styled_pie_chart(
        #     dataframe=df['sex'].value_counts(),
        #     title="Gender",
        #     values='sex',
        #     classes=['male', 'female', 'unknown'],
        #     template=template)

        skin_mel = df.loc[:, ['age', 'sex', 'localization', 'cell_type']]
        px_heatmap = skin_heatmap(skin_mel, template)

        return px_bar_chart, px_heatmap


