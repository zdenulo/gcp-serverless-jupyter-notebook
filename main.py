import datetime

import papermill as pm



def main():

    input_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    parameters = {
        'date': input_date
    }
    pm.execute_notebook(
        'covid_stats.ipynb',
        'covid_stats_out.ipynb',
        parameters=parameters
    )


if __name__ == '__main__':
    main()