import datetime
import logging

from flask import Flask
import papermill as pm

app = Flask(__name__)


#
# @app.route('/')
# def main(request):
#     return main(request)

@app.route('/')
def main(request=None):
    logging.info("starting job")
    input_date = ''
    if request:
        input_date = request.args.get('input_date', '')
        print(input_date)
    if not input_date:
        input_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    parameters = {
        'date': input_date
    }
    pm.execute_notebook(
        'covid_stats.ipynb',
        '/tmp/covid_stats_out.ipynb',
        parameters=parameters
    )
    logging.info("job completed")
    return 'ok'


if __name__ == '__main__':
    import os

    port = os.environ.get('POST', '8080')
    app.run(port=port)
