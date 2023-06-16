import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash import callback, Input, Output
from dash import html, dcc
from dash_bootstrap_templates import ThemeSwitchAIO
from plotly.subplots import make_subplots

from src.components.graph_card import create_graph_card
# local imports
from src.components.page_header import create_page_header_box
from src.components.prepare_dataset_charts import basic_EDA, get_summary_table, to_styled_dict_table, get_dataframe
from src.components.step_progress_bar import create_step_progress_bar

dash.register_page(
    __name__,
    path='/data-analysis/tabular',
    title='Data Analysis (Tabular)'
)

dataset_name = html.Div(
    dbc.Label("Dataset:"),
    id="dataset_name_tabular"
)

prev_step_btn = dbc.Button("back", outline=True, color="primary", href="/select-data", disabled=False)
next_step_btn = dbc.Button("next step", outline=False, color="primary", href="/model-settings", disabled=False)

# the page header
card_content = create_page_header_box(
    icon='fa fa-2x fa-magnifying-glass-chart',
    title='Data Analysis (Tabular)',
    description='Good and balanced data is the fuel for a good AI System.',
    prev_step=None,
    next_step=next_step_btn,
    extension=dataset_name
)

summary_table_tabular = create_graph_card(card_type='table', title='Summary', card_id='summary_table_tabular')
basic_eda_tabular = create_graph_card(card_type='table', title='Basic Exploratory Data Analysis', card_id='basic_eda_tabular')
bar_chart_tabular = create_graph_card(card_type='custom_graph', card_id='bar_chart_tabular')
pie_chart_figure_tabular = create_graph_card(card_type='custom_graph', card_id='pie_chart_figure_tabular')
corr_m_tabular = create_graph_card(card_type='custom_graph', card_id='corr_m_tabular')

page_content = dcc.Loading(
    id="loading-data-analysis",
    children=[
        dbc.Row(
            [
                # dbc.Col(
                #     summary_table_tabular,
                #     width=6,
                #     className="mb-4",
                # ),

                dbc.Col(
                    bar_chart_tabular,
                    width=6,
                    className="mb-4",
                ),

                dbc.Col(
                    pie_chart_figure_tabular,
                    width=6,
                    className="mb-4",
                ),

                # dbc.Col(
                #     corr_m_tabular,
                #     width=6,
                #     className="mb-4",
                # ),

                # dbc.Col(
                #     basic_eda_tabular,
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
    Output('dataset_name_tabular', 'children'),
    #Input('dataset_input', 'data'),
    Input('model_type', 'data'),
)
def get_dataset(model_input):
    #print("model_type name: ", model_input)
    if model_input == 'tabular':
        dataset_name_text = 'Heart Disease'
        return 'Analyzing the data of: ' + str(dataset_name_text)


# callback for the charts
@callback(
    Output('bar_chart_tabular', 'figure'),
    Output('pie_chart_figure_tabular', 'figure'),
    #Output('corr_m_tabular', 'figure'),

    Input('model_type', 'data'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def summary_table(model_type, theme_switch):
    if model_type is not None:
        print("EDA model_type ", model_type)
        template = "cosmo" if theme_switch else "superhero"

        # TODO dynamic loading of datasets
        dataset_choice = 'heart-disease'
        df = get_dataframe(dataset_choice)
        basic_eda = basic_EDA(df)
        basic_eda_plot = to_styled_dict_table(basic_eda, template)
        get_summary = get_summary_table(df)
        summary = to_styled_dict_table(get_summary, template)

        df_histo = df[['sex', 'age', 'target']]
        df_histo['sex'].replace({1: 'Male', 0: 'Female'}, inplace=True)
        df_histo['target'].replace({1: 'Heart Patient', 0: 'Healthy'}, inplace=True)

        histo = make_subplots(rows=1, cols=2, specs=[[{"type": "histogram"}, {"type": "histogram"}]])
        histo.add_trace(
            go.Histogram(
                x=df_histo['age'].where(df_histo['target'] == 'Heart Patient'),
                name='Heart Patient',
                nbinsx=20,
                showlegend=False,
                marker={"color": 'rgb(8,48,107)'}
            ),
            row=1, col=1
        )
        histo.add_trace(
            go.Histogram(
                x=df_histo['age'].where(df_histo['target'] == 'Healthy'),
                name='Healthy',
                nbinsx=20,
                showlegend=False,
                marker={"color": 'rgb(66,146,198)'}
            ),
            row=1, col=1
        )
        histo.add_trace(
            go.Histogram(
                x=df_histo['sex'].where(df_histo['target'] == 'Heart Patient'),
                name='Heart Patient',
                nbinsx=20,
                marker={"color": 'rgb(8,48,107)'}
            ),
            row=1, col=2
        )
        histo.add_trace(
            go.Histogram(
                x=df_histo['sex'].where(df_histo['target'] == 'Healthy'),
                name='Healthy',
                nbinsx=20,
                marker={"color": 'rgb(66,146,198)'}
            ),
            row=1, col=2
        )

        histo.update_layout(height=500,
                            title_text="Age & Gender Distribution",
                            title_font_size=20,
                            bargap=0.1,
                            template=template,
                            plot_bgcolor="rgba(0,0,0,0)",
                            paper_bgcolor='rgba(0,0,0,0)',
                            )
        histo.update_xaxes(title_text="Age", row=1, col=1)
        histo.update_yaxes(title_text="Count", row=1, col=1)
        histo.update_xaxes(title_text="Gender", row=1, col=2)
        histo.update_yaxes(title_text="Count", row=1, col=2)

        cp1 = df.where(df['target'] == 0).groupby(by=["cp"]).size().reset_index(name="Count")
        cp0 = df.where(df['target'] == 1).groupby(by=["cp"]).size().reset_index(name="Count")

        cp0['cp'].replace({0: 'Type 1', 1: 'Type 2', 2: 'Type 3', 3: 'Type 4'}, inplace=True)
        cp1['cp'].replace({0: 'Type 1', 1: 'Type 2', 2: 'Type 3', 3: 'Type 4'}, inplace=True)

        df1 = df[['thalach', 'chol', 'target', 'age', 'trestbps']]
        df1['targetname'] = df1['target'].replace({1: 'Heart Patient', 0: 'Healthy'})

        histo2 = make_subplots(rows=1, cols=2, specs=[[{"type": "histogram"}, {"type": "scatter"}]])
        histo2.add_trace(
            go.Bar(
                x=cp0['cp'], y=cp0.Count, marker={"color": 'rgb(66,146,198)'}, name='Healthy'
            ),
            row=1, col=1
        )
        histo2.add_trace(
            go.Bar(
                x=cp1['cp'], y=cp1.Count, marker={"color": 'rgb(8,48,107)'}, name='Heart Patient'
            ),
            row=1, col=1
        )
        histo2.add_trace(
            go.Scatter(x=df1.thalach, y=df1.age, mode='markers', text=df1['targetname'], showlegend=False,
                       marker=dict(
                           color=df1.target,
                           colorscale=['rgb(66,146,198)', 'rgb(8,48,107)'],
                           line_width=1)
                       ),
            row=1, col=2
        )
        histo2.update_layout(height=500,
                          title_text="Chest Pain & Max Heart Rate",
                          title_font_size=20,
                          bargap=0.1,
                          template=template,
                          plot_bgcolor="rgba(0,0,0,0)",
                          paper_bgcolor='rgba(0,0,0,0)'
                          )
        histo2.update_xaxes(title_text="Chest Pain Type", row=1, col=1)
        histo2.update_yaxes(title_text="Count", row=1, col=1)

        histo2.update_xaxes(title_text="Max. Heart Rate", row=1, col=2)
        histo2.update_yaxes(title_text="Age", row=1, col=2)

        # corr_m = px.imshow(df.corr(), height=500, color_continuous_scale=px.colors.sequential.Blues_r,
        #           template=template)
        # corr_m.update_layout(height=500,
        #                      title_text="Correlation Matrix",
        #                      title_font_size=20,
        #                      template=template,
        #                      plot_bgcolor="rgba(0,0,0,0)",
        #                      paper_bgcolor='rgba(0,0,0,0)')

        return histo, histo2
