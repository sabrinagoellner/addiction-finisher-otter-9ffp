import dash

import dash_bootstrap_components as dbc
from dash import get_asset_url
from dash import dcc
from dash import html

dash.register_page(
    __name__,
    path='/',
    redirect_from=['/home'],
    title='Home'
)

layout = html.Div([

    # Hero Section
    html.Section(id="hero", children=[
        html.Div(className="hero-container", children=[
            dbc.CardImg(src=get_asset_url('logos/verifai-logo-weiss.png'), style={"width": "500px"}),
            html.H4("Evaluating the Responsibility of AI-Systems", style={"color":"white"}),
            html.Hr(className="my-2"),

            dbc.ButtonGroup(
                [
                    dbc.Button("Try live demo", color="primary", size="lg", href='/start'),
                ],
            ),
        ]),
    ]),
    # Main Content
    html.Main([
        # Home Section
        html.Section(id="home", children=[
            html.Div(className="container", children=[
                html.H2("Research"),
                html.Div(children=[
                    html.P(
                        "In recent years, significant advancements in the field of artificial intelligence (AI) have transformed the way industries and organizations operate. Breakthroughs in machine learning and deep learning techniques have enabled AI systems to perform remarkably in tasks, such as computer vision and natural language processing."),
                    html.P(
                        "These developments have led to the widespread adoption of AI in various sectors, including healthcare, finance, and transportation. Moreover, AI is becoming increasingly ingrained in daily life, leading to discussions about the roles of technologies like ChatGPT, especially using GPT-4, as artificial generators of text, code, and more. Therefore, concerns about the security, explainability, privacy, and ethics of AI systems have emerged, prompting researchers to explore methods of evaluating and ensuring responsible AI practices."),
                    html.P(
                        "As AI systems continue to evolve, it is essential to develop metrics for measuring both discriminative models and generative models. To effectively assess the performance of various models in different scenarios and use cases, an approach for a unified framework is needed."),
                    html.P(
                        "Therefore, we have created 'VERIFAI' (eValuating thE ResponsibIlity oF AI-systems), for providing a comprehensive assessment of AI systems in terms of their responsibility and performance across various dimensions."),
                ]),
                dbc.Button("Research Papers", outline=True, color="secondary", size="lg",
                           href="https://sabrinagoellner.github.io", target="_blank"),
                dbc.Button("Git Repository", outline=True, color="secondary", size="lg",
                           href="https://gitlab.com/sabrinagoellner/VERIFAI", target="_blank"),
                
            ]),
        ]),

        # About Section
        html.Section(id="about", className="about", children=[
            html.Div(className="container", children=[
                html.Div(className="row", children=[
                    html.Div(className="col-lg-3", children=[
                        html.Img(src="assets/img/support.png", className="img-fluid", alt="About Image"),
                    ]),
                    html.Div(className="col-lg-9 pt-4 pt-lg-0", children=[
                        html.H2("Objectives"),
                        dbc.Row(children=[
                            dbc.Col([
                                html.I(className="fa fa-2x fa-check"),
                            ], width={"size": 1}),
                            dbc.Col([
                                html.Li(
                                    "Support different data types (image, tabular, text), models (HuggingFace, PyTorch, TensorFlow, ScikitLearn) and tasks (classification, generation)."),
                            ], width={"size": 11}, style={"list-style": "none"}),
                            dbc.Col([
                                html.I(className="fa fa-2x fa-check"),
                            ], width={"size": 1}),
                            dbc.Col([
                                html.Li(
                                    "Offer different metrics in 4 categories for an comprehensive evaluation"),
                            ], width={"size": 11}, style={"list-style": "none"}),
                            dbc.Col([
                                html.I(className="fa fa-2x fa-check"),
                            ], width={"size": 1}),
                            dbc.Col([
                                html.Li(
                                    "Supporting researchers and practitioners to better understand the strengths and weaknesses of their models."),
                            ], width={"size": 11}, style={"list-style": "none"}),
                            dbc.Col([
                                html.I(className="fa fa-2x fa-check"),
                            ], width={"size": 1}),
                            dbc.Col([
                                html.Li(
                                    "Towards certification and verification of all kinds of machine learning models."),
                            ], width={"size": 11}, style={"list-style": "none"}),
                        ]),
                    ]),
                ]),
            ]),
        ]),

        # Why Us Section
        html.Section(id="why-us", className="why-us section-bg", children=[
            html.Div(className="container", children=[
                html.Div(className="section-title", children=[
                    html.H2("Aspects of Responsible AI"),
                ]),
                html.Div(className="row", children=[
                    html.Div(className="col-lg-4 col-md-6 d-flex align-items-stretch", children=[
                        html.Div(className="card", children=[
                            html.Img(src="assets/img/fairness.png", className="card-img-top", alt="..."),
                            html.Div(className="card-icon", children=[
                                html.I(className="fa fa-scale-balanced"),
                            ]),
                            html.Div(className="card-body", children=[
                                html.H5(className="card-title", children=[
                                    html.Span("Ethics"),
                                ]),
                                html.P(className="card-text",
                                       children="Among the key requirements for ethical AI, fairness stands out as the most critical aspect according to the literature. Ensuring AI systems are non-biased and non-discriminating in all aspects of their operation is crucial in fostering trust and acceptance. Alongside fairness, accountability is essential, with AI systems justifying their decisions and actions transparently. Sustainability is another vital requirement, with AI systems designed to consider long-term consequences and align with Sustainable Development Goals. Lastly, compliance with robust laws and regulations guarantees that AI systems operate within legal and ethical boundaries. "),
                            ]),
                        ]),
                    ]),
                    html.Div(className="col-lg-4 col-md-6 d-flex align-items-stretch", children=[
                        html.Div(className="card", children=[
                            html.Img(src="assets/img/xai.png", className="card-img-top", alt="..."),
                            html.Div(className="card-icon", children=[
                                html.I(className="fa fa-lightbulb"),
                            ]),
                            html.Div(className="card-body", children=[
                                html.H5(className="card-title", children=[
                                    html.Span("Explainability"),
                                ]),
                                html.P(className="card-text",
                                       children="The black box problem in AI models has driven the development of Explainable AI (XAI) to understand the decision-making process, perceived as the main aspect for greater trustworthiness. XAI focuses on a human-centered approach, tailoring explanations to user needs and target groups. Numerous techniques are discussed in the current literature, with new ones being developed. An intuitive user interface and visually understandable language enhance comprehension and engagement. Explainability serves as both a functional and non-functional requirement, emphasizing the AI system's inner workings and effective communication. Ultimately, XAI aims to improve users' decision-making based on provided explanations, ensuring informed choices."),
                            ]),
                        ]),
                    ]),
                    html.Div(className="col-lg-4 col-md-6 d-flex align-items-stretch", children=[
                        html.Div(className="card", children=[
                            html.Img(src="assets/img/privacy.png", className="card-img-top", alt="..."),
                            html.Div(className="card-icon", children=[
                                html.I(className="fa fa-lock"),
                            ]),
                            html.Div(className="card-body", children=[
                                html.H5(className="card-title", children=[
                                    html.Span("Privacy"),
                                ]),
                                html.P(className="card-text",
                                       children="When handling sensitive data, Privacy is crucial in RAI systems. Compliance with regulations like the GDPR is vital, and technologies like Federated Learning can help. Organizational processes should complement these techniques to ensure robust data protection. Numerous security threats in machine learning include stealing the model or sensitive user information, reconstruction attacks, and membership inference attacks, with the latter being a rapidly evolving research branch. Hybrid Privacy-Preserving Machine Learning approaches balance ML performance and privacy overhead while minimizing communication and computational costs for enhanced efficiency and scalability."),
                            ]),
                        ]),
                    ]),
                    html.Div(className="col-lg-4 col-md-6 d-flex align-items-stretch", children=[
                        html.Div(className="card", children=[
                            html.Img(src="assets/img/security.png", className="card-img-top", alt="..."),
                            html.Div(className="card-icon", children=[
                                html.I(className="fa fa-shield"),
                            ]),
                            html.Div(className="card-body", children=[
                                html.H5(className="card-title", children=[
                                    html.Span("Security"),
                                ]),
                                html.P(className="card-text",
                                       children="Numerous security threats exist within the branch of machine learning that warrant attention. These threats encompass poisoning attacks, where the training data is manipulated to undermine the model's performance, and adversarial attacks, in which adversaries craft malicious input samples to deceive the model and induce incorrect predictions. The AI security domain is swiftly progressing, as researchers devise innovative techniques and countermeasures to combat these challenges."),
                            ]),
                        ]),
                    ]),
                    html.Div(className="col-lg-4 col-md-6 d-flex align-items-stretch", children=[
                        html.Div(className="card", children=[
                            html.Img(src="assets/img/trust.jpg", className="card-img-top", alt="..."),
                            html.Div(className="card-icon", children=[
                                html.I(className="fa fa-handshake"),
                            ]),
                            html.Div(className="card-body", children=[
                                html.H5(className="card-title", children=[
                                    html.Span("Trustworthiness"),
                                ]),
                                html.P(className="card-text",
                                       children="In the literature, trustworthiness is often connected to how the user perceives the system's reliability. To achieve this, AI systems must prioritize data protection, provide accurate predictions under uncertainty, and offer transparent, explainable reasoning to users. Additionally, these systems should be usable and accessible, act reliably 'as intended' in their applications, and be perceived as fair and useful. By focusing on these key aspects, developers can create RAI solutions that foster user trust and deliver value across a wide range of sectors, benefiting both users and society as a whole."),
                            ]),
                        ]),
                    ]),
                    html.Div(className="col-lg-4 col-md-6 d-flex align-items-stretch", children=[
                        html.Div(className="card", children=[
                            html.Img(src="assets/img/human-centered.jpg", className="card-img-top", alt="..."),
                            html.Div(className="card-icon", children=[
                                html.I(className="fa fa-user-circle"),
                            ]),
                            html.Div(className="card-body", children=[
                                html.H5(className="card-title", children=[
                                    html.Span("Human-Centered"),
                                ]),
                                html.P(className="card-text",
                                       children="This aspect is fundamental for RAI, emphasizing the need to consider user interaction and understanding when designing AI systems. This approach places the human user at the center of the AI experience, ensuring that the technology is not only efficient but also accessible and comprehensible to its users. One essential concept in human-centered AI is the Human-in-the-loop (HITL), which incorporates human input and feedback throughout the AI system's development and decision-making processes. This approach ensures that AI technologies are not solely reliant on algorithms but also benefit from human knowledge, experience, and intuition, allowing AI systems to better align with human values, expectations, and ethical considerations."),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        ]),
    ]),
])
