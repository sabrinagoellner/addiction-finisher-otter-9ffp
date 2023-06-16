# package imports
import dash
from dash import html, dcc, Output, Input, callback, State
import dash_bootstrap_components as dbc

# local imports
from src.components.model_card import create_model_card
from src.components.page_header import create_page_header_box
from src.components.step_progress_bar import create_step_progress_bar

dash.register_page(
    __name__,
    path='/select-data',
    title='Select Use Case'
)

app = dash.get_app()

page_header_ex = html.Div([
    dbc.RadioItems(
        options=[
            {"label": "Skin Cancer", "value": "image"},
            {"label": "Medical reviews", "value": "nlp"},
            {"label": "Heart Disease", "value": "tabular"},
            # {"label": "Alzheimers Desease", "value": "alzheimer"},
            # {"label": "Ohsumed", "value": "ohsumed"},
            # {"label": "Chest x-ray", "value": "chest-x-ray"},
        ],
        value="tabular",
        name="model_input",
        id="model_input",
    ),
])

prev_step_btn = dbc.Button("back", outline=True, color="primary", href="/start", disabled=True)
next_step_btn = dbc.Button(
    "next step",
    id='next_step',
    color="primary",
    href="/data-analysis/tabular",  # default! changes dynamically if selected
    disabled=False
)
# the page header
card_content = create_page_header_box(
    icon='fa fa-2x fa-database',
    title='Select Use Case and Task',
    description='The first step of the VERIFAI-Lifecycle is selecting the Use Case and Task. '
                'The available tasks are: Classification on Text, Image and Tabular Data ',
    prev_step=prev_step_btn,
    next_step=next_step_btn,
    extension=page_header_ex
)

skin_cancer = create_model_card(
    data_id='skin_cancer',
    image_src='images/skincancer.jpg',
    title='Skin Cancer',
    task='Classification of skin lesions on images',
    data_type='Image',
    framework='Tensorflow/Keras',
    model_kind='X-Ception Finetuned')

medical_reviews = create_model_card(
    data_id='medical_reviews',
    image_src='images/medical_reviews.png',
    title='Medical Reviews',
    task='Classification: sentiment analysis of drug experience and for recommendation of medicine by using reviews.',
    data_type='Text',
    framework='HuggingFace, Tensorflow',
    model_kind='DistilBERT, NNLM')

heart_disease = create_model_card(
    data_id='heart_diseases',
    image_src='images/heart_disease.png',
    title='Heart Diseases',
    task='Classification: Determine the presence of a heart disease in the patient.',
    data_type='Tabular Data',
    framework='Scikit Learn',
    model_kind='Random Forest')



dataset_columns = [heart_disease, medical_reviews, skin_cancer]
# dataset_columns = [heart_disease]

model_cards_row = dbc.Row([
                        dbc.Col([
                            dataset,
                        ],
                            width=4,
                            className="mb-4  mt-4"
                        )

                        for dataset in dataset_columns
                    ]),

layout = dbc.Container([
    create_step_progress_bar(
        ["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security",
         "Explainability", "Results"], 2),

    dbc.Col([
        dbc.Card([
            # dbc.CardHeader("Please select one of the available use cases:")
        ], id="please_select_use_case"),
        card_content,
    ],
        width=12,
        className="mb-4  mt-4",
    ),
    html.Hr(),

    dbc.Col(
        dbc.Card([
            dbc.CardHeader(
                html.H4("Model Cards"),
            ),
            dbc.Card([
                dbc.CardHeader(
                    html.H5("Scenario: Healthcare"),
                ),
                dbc.CardBody(
                    "The use of artificial intelligence (AI) in medical field is becoming a reality in many specialties. "
                    "AI is gradually becoming the main assistant of medical workers. "
                    "Machine learning algorithms help hospital administrators manage processes, doctors make more accurate medical decisions. "
                    "In general, AI makes medical services better and more efficient. "
                    "The introduction of AI-based systems is one of the key trends in modern healthcare.",
                ),
            ]),
            dbc.Card([
                dbc.CardHeader(
                    html.H5("Classification"),
                ),
                dbc.CardBody(
                    model_cards_row,
                ),
            ]),

        ]),
        width=12,
        className="mb-4  mt-4",
    ),

    # TODO:
    # CUSTOM UPLOAD:
    # Select Model Type
    # Select Data Type

])


# store the dataset which was chosen in this step
# the dcc.Store is in the app.py which is always present !
@callback(
    Output('model_type', 'data'),
    Output('next_step', 'href'),

    Input('model_input', 'value'),

    # TODO Input('task', 'value')
    # e.g. discriminative, generative
)
def select_model(model_input):
    print("model_input ", model_input)

    if model_input:
        # save session variables
        # of data and model input
        # dataset = dataset_input

        # routing = current-step + model_input
        # current_step = dash.page_registry()
        current_step = 'data-analysis'
        next_step = '/' + current_step + '/' + model_input

        print(next_step)

        return model_input, next_step
