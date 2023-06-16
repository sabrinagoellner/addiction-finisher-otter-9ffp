import dash_html_components as html


def create_step_progress_bar(steps, current_step):
    step_elements = []
    for i, step in enumerate(steps):
        step_element = html.Div(
            [
                html.Div(
                    className="step-circle" + (" step-active" if i == current_step else ""),
                ),
                html.Div(step, className="step-label" + (" label-active" if i == current_step else "")),
            ],
            className="step",
        )
        step_elements.append(step_element)

    progress_bar = html.Div(
        [
            html.Div(step_elements, className="step-container"),
        ]
    )
    return progress_bar
