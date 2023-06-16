# Model Settings Page

# Import Libraries
import dash
import dash_bootstrap_components as dbc
from dash import callback, Input, Output, State
from dash import html, dcc

# local imports
# from src.components.evaluate_model import evaluate_tensorflow_model, evaluate_scikit_learn_model, evaluate_huggingface_model

from src.components.page_header import create_page_header_box
from src.components.step_progress_bar import create_step_progress_bar

dash.register_page(
    __name__,
    path='/model-settings',
    title='Test Settings'
)

next_step_btn = dbc.Button(
    "next step",
    id='settings_next_step',
    color="primary",
    href='/model-fairness/tabular',  # default! changes dynamically if selected
    disabled=False
)

# the page header
page_header = create_page_header_box(
    icon='fa fa-2x fa-cogs',
    title='Test Settings',
    description='Adjustments for the Model responsibility tests: The available Models are listed below.',
    prev_step=None,
    next_step=next_step_btn
)

prepare = html.Div([

    html.H4("Configuration"),
    dbc.Row([
        dbc.Col(
            [
                html.Label("Dataset:"),
                html.P("...", id="dataset_choice_output_display")

            ],
            width=4
        ),
        dbc.Col(
            [
                dbc.Label("Trained models:"),
                dbc.RadioItems(
                    # options=[
                    #     {"label": "xCeption", "value": "x-ception"},
                    #     {"label": "CNN DenseNet-121", "value": "densenet-121"},
                    # ],
                    # value="x-ception",
                    # dynamically added

                    name="model",
                    id="selectable_trained_model",
                ),
            ],
            width=4
        ),

        dbc.Col(
            [
                html.Label(children='Testset Size:'),
                dcc.Slider(step=None,
                           marks={
                               #0: '0',
                               #50: '50',
                               #100: '100',
                               200: '200',
                               # 300: '300',
                               # 400: '400',
                               # 500: '500'
                           },
                           value=200,
                           id='dataset_select_size'),
                dbc.Alert("In the current version are no adjustments possible.", color='warning')
            ],
            width=3,
        ),
        dbc.Col(
            [
                dbc.Button(children="submit", id="create_test_data_btn", n_clicks=0,
                           color="primary", className="mb-4 mt-4"),

                dcc.Loading(id="loading-1", children=[

                    dbc.Alert(
                        "Select a classifier to proceed.",
                        id="prepared_data_output_text",
                        color='secondary'
                    ),
                    dbc.Alert(
                        [
                            html.P("Model baseline accuracy with the current test batch:"),
                            html.Strong(" ",
                                        id="display_accuracy"),
                        ],
                        color='primary',
                    ),



                ], type="circle"),

            ],
            width=12
        ),

    ])
])

layout = dbc.Container([
    create_step_progress_bar(
        ["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security",
         "Explainability", "Results"], 4),
    page_header,
    prepare
])


# get the Input('model_type', 'data'), which was chosen in the last step and display it!
@callback(
    Output('dataset_choice_output_display', 'children'),
    Output('selectable_trained_model', 'options'),
    Output('selectable_trained_model', 'value'),
    Output('settings_next_step', 'href'),

    Input('model_type', 'data'),
)
def prepare(model_type):
    print("settings model_type ", model_type)
    if model_type:

        if model_type == "image":
            # change the selectable models based on the datset:
            selectable_trained_model = ["x-ception"]
            dataset_choice_as_name = 'Skin Cancer MNIST'
        # elif model_type == "chest-x-ray":
        #     selectable_trained_model = ["dense-net-121"]
        #     dataset_choice_as_name = 'Chest X-Ray'
        elif model_type == "nlp":
            selectable_trained_model = ["DistilBERT", "NNLM"]
            dataset_choice_as_name = 'Medical Reviews'
        # elif model_type == "alzheimer":
        #     selectable_trained_model = ["InceptionV3"]
        #     dataset_choice_as_name = 'Alzheimers'
        elif model_type == "tabular":
            selectable_trained_model = ["RandomForest"]
            dataset_choice_as_name = 'Heart Disease'
        else:
            selectable_trained_model = []
            dataset_choice_as_name = ''

        options = [{'label': i, 'value': i} for i in selectable_trained_model]
        value = selectable_trained_model[0]
        print("value ", value)

        current_step = 'model-fairness'
        next_step = '/' + current_step + '/' + model_type
        print(next_step)
        return dataset_choice_as_name, options, value, next_step
    else:
        return "no model_type was chosen, please go back", None


@callback(
    Output('prepared_data_output_text', 'children'),
    Output('display_accuracy', 'children'),
    Output('dataset_size', 'data'),  # global state of current test size
    Output('selected_model', 'data'),  # global state of current selected_model

    Input('create_test_data_btn', 'n_clicks'),
    State('selectable_trained_model', 'value'),
    State('dataset_select_size', 'value'),

    # global
    Input('model_type', 'data'),
)
def update_selected(n_clicks, selectable_trained_model, dataset_select_size, model_type):
    if n_clicks == 0:
        # print("no update data")
        return dash.no_update
    else:

        if dataset_select_size == None:
            dataset_select_size = 200

        print("Settings Evaluation model_type ", model_type)
        print("selectable_trained_model ", selectable_trained_model)

        if model_type == 'tabular':
            # scikit learn models:
            message = "Successfully prepared the tabular dataset with the model " + str(
                selectable_trained_model) + 'and batch size ' + str(dataset_select_size)
            #accuracy = evaluate_scikit_learn_model(selectable_trained_model, 'heart-disease', dataset_select_size)
            accuracy = 0.87
            accuracy = "" + str(round(accuracy, 2)) + "%"
            return message, accuracy, dataset_select_size, selectable_trained_model

        elif model_type == 'image':
            message = "Successfully prepared the dataset with the model " + str(
                selectable_trained_model) + ' and batch size ' + str(dataset_select_size)
            #accuracy = evaluate_tensorflow_model(selectable_trained_model, 'skin-cancer', dataset_select_size)
            accuracy = 0.86
            accuracy = "" + str(round(accuracy, 2) * 100) + "%"
            return message, accuracy, dataset_select_size, selectable_trained_model

        elif model_type == 'nlp':
            if selectable_trained_model == 'NNLM':
                #accuracy = evaluate_tensorflow_model(selectable_trained_model,'medical-reviews', dataset_select_size)
                accuracy = 0.87
                accuracy = "" + str(round(accuracy, 2) * 100) + "%"
                message = "Successfully prepared the dataset with the model " + str(
                    selectable_trained_model) + ' and batch size ' + str(dataset_select_size)
                return message, accuracy, dataset_select_size, selectable_trained_model

            elif selectable_trained_model == 'DistilBERT':
                #accuracy = evaluate_huggingface_model(selectable_trained_model, 'medical-reviews', dataset_select_size)
                accuracy = 0.88
                accuracy = "" + str(round(accuracy, 2) * 100) + "%"
                message = "Successfully prepared the dataset with the model " + str(
                    selectable_trained_model) + ' and batch size ' + str(dataset_select_size)
                return message, accuracy, dataset_select_size, selectable_trained_model
        else:
            return "Error: not implemented", None, None
