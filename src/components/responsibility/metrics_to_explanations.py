def get_explanation_text(metric_value, task):
    if task == 'privacy':
        privacy_text_map = {
            0: 'There are big privacy issues according to this test.',
            1: 'There are privacy issues according to this test.',
            2: 'There are privacy issues according to this test.',
            3: 'There are privacy issues according to this test.',
            4: 'There are privacy issues according to this test.',
            5: 'There was information leaked. You should improve privacy protection',
            6: 'There was information leaked. You should improve privacy protection',
            7: 'There was information leaked. You should improve privacy protection',
            8: 'There are few privacy leakages according to this test.',
            9: 'There are very few privacy leakages according to this test.',
            10: 'There are no privacy leakages according to this test.',
        }
        result = privacy_text_map[metric_value]

    elif task == 'security':
        security_text_map = {
            0: 'The model is not robust at all according to this test.',
            1: 'The model is vulnerable to adversarial attacks.',
            2: 'The model is vulnerable to adversarial attacks.',
            3: 'The model is vulnerable to adversarial attacks.',
            4: 'The model is vulnerable to adversarial attacks.',
            5: 'The model is vulnerable to adversarial attacks.We recommend improving robustness.',
            6: 'The model is vulnerable to adversarial attacks.We recommend improving robustness.',
            7: 'The model is vulnerable to adversarial attacks.We recommend improving robustness.',
            8: 'It looks like the model robustness could be improved further according to this test.',
            9: 'There are only little robustness issues according to this test.',
            10: 'There are no robustness issues according to this test.',
        }
        result = security_text_map[metric_value]

    elif task == 'fairness':

        fairness_text_map = {
            0: 'There are big fairness issues according to this test. Please adjust the data and model with fairness techniques.',
            1: 'There are fairness issues according to this test. We suggest improvement.',
            2: 'There are fairness issues according to this test. We suggest improvement.',
            3: 'There are fairness issues according to this test. We suggest improvement.',
            4: 'There are fairness issues according to this test. We suggest improvement.',
            5: 'The model does not decide fair along the classes. We suggest improvement.',
            6: 'The model does not decide fair along the classes. We suggest improvement.',
            7: 'The model does not decide fair along the classes. We suggest improvement.',
            8: 'It is a quite fair result, but could be improved further.',
            9: 'There are only little fairness issues according to this test.',
            10: 'There are no fairness issues according to this test.',
        }
        result = fairness_text_map[metric_value]

    elif task == 'explainability':

        explainability_text_map = {
            0: 'Please consider anther method for the models explainability.',
            1: 'We suggest considering another explainability method.',
            2: 'We suggest considering another explainability method.',
            3: 'We suggest considering another explainability method.',
            4: 'We suggest considering another explainability method.',
            5: 'Using this XAI method may not be optimal, we suggest comparison with other methods.',
            6: 'Using this XAI method may not be optimal, we suggest comparison with other methods.',
            7: 'Using this XAI method may not be optimal, we suggest comparison with other methods.',
            8: 'Explainability of the model works well using this XAI method, but could be improved further.',
            9: 'The model explainability works well according to this test.',
            10: 'The model explainability works well according to this test.',
        }

        result = explainability_text_map[metric_value]
    else:
        result = 'error, not implemented'

    return result


def get_explanation_color(metric_value):
    color_map = {
        0: 'danger',
        1: 'danger',
        2: 'danger',
        3: 'danger',
        4: 'danger',
        5: 'warning',
        6: 'warning',
        7: 'warning',
        8: 'success',
        9: 'success',
        10: 'success'
    }

    result = color_map[metric_value]

    return result
