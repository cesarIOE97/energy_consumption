# Libraries
import os
import webbrowser
import pandas as pd


# Arguments
# 
# Example: python3 analysis.py c++ nbody_2.c 50000000 nbody_50000000_4
# language=sys.argv[1]
# command=sys.argv[2]
# directory=sys.argv[3]

# Directory
actual_directory = os.getcwd() + '/'

def get_source(row):
    if row['_indicator_python_c++'] == 'both':
        if row['_indicator_java'] == 'both':
            if row['_indicator_js'] == 'both':
                return 'common'
            else:
                return 'python, c++, java'
        else:
            if row['_indicator_js'] == 'both':
                return 'python, c++, js'
            else:
                return 'python, c++'
    elif row['_indicator_python_c++'] == 'left_only':
        if row['_indicator_java'] == 'left_only':
            if row['_indicator_js'] == 'both':
                return 'python, js'
            else:
                return 'python'
        else: 
            if row['_indicator_js'] == 'both':
                return 'python, java, js'
            else:
                return 'python, java'
    elif row['_indicator_python_c++'] == 'right_only':
        if row['_indicator_java'] == 'left_only':
            if row['_indicator_js'] == 'both':
                return 'c++, js'
            else:
                return 'c++'
        else: 
            if row['_indicator_js'] == 'both':
                return 'c++, java, js'
            else:
                return 'c++, java'
    elif row['_indicator_java'] == 'both':
        return 'common'
    elif row['_indicator_js'] == 'both':
        return 'common'
    elif row['_indicator_python_c++'] == 'left_only':
        return 'python'
    elif row['_indicator_java'] == 'left_only':
        return 'c++'
    elif row['_indicator_js'] == 'left_only':
        return 'java'
    else:
        return 'js'

def df_common_and_noncommon_Parameters(df_1, df_2, df_3, df_4, correlation_type):
    df_common_values = pd.merge(pd.merge(pd.merge(df_1, df_2, left_index=True, right_index=True, how='inner', suffixes=('_python', '_c++')),
                                         df_3, left_index=True, right_index=True, how='inner', suffixes=('', '_java')),
                                df_4, left_index=True, right_index=True, how='inner', suffixes=('', '_js'))
    # df_common_values = pd.merge(df_common_values, df_3, left_index=True, right_index=True, how='inner')
    # df_common_values = df_common_values.drop_duplicates()
    # df_common_values = pd.merge(df_common_values, df_4, left_index=True, right_index=True, how='inner')
    df_common_values = df_common_values.drop_duplicates()

    # df_non_common_values = pd.merge(df_1, df_2, left_index=True, right_index=True, how='outer', indicator=True).query('_merge != "both"').drop('_merge', axis=1)
    # df_non_common_values = pd.merge(df_non_common_values, df_4, left_index=True, right_index=True, how='outer', indicator=True).query('_merge != "both"').drop('_merge', axis=1)
    df_non_common_values = pd.merge(pd.merge(pd.merge(df_1, df_2, left_index=True, right_index=True, how='outer', indicator='_indicator_python_c++', suffixes=('_python', '_c++')),
                                     df_3, left_index=True, right_index=True, how='outer', indicator='_indicator_java', suffixes=('', '_java')),
                            df_4, left_index=True, right_index=True, how='outer', indicator='_indicator_js', suffixes=('', '_js'))
    df_non_common_values = df_non_common_values.drop_duplicates()

    df_non_common_values['Source'] = df_non_common_values.apply(lambda row: get_source(row), axis=1)
    second_column = df_non_common_values.pop('Source') 
    df_non_common_values.insert(0, 'Source', second_column)
    df_non_common_values = df_non_common_values.sort_values(by=['Source'])

    df_common_values['position'] = range(1,len(df_common_values)+1)
    first_column = df_common_values.pop('position') 
    df_common_values.insert(0, 'position', first_column)

    df_non_common_values['position'] = range(1,len(df_non_common_values)+1)
    first_column = df_non_common_values.pop('position') 
    df_non_common_values.insert(0, 'position', first_column)

    return df_common_values, df_non_common_values

def correlation_ProgrammingLanguages(correlation_type):
    if correlation_type == "general":
        df_python = pd.read_csv("python" + "/correlation_general_medianValues.csv", index_col=0)
        df_cplusplus = pd.read_csv("c++" + "/correlation_general_medianValues.csv", index_col=0)
        df_java = pd.read_csv("java" + "/correlation_general_medianValues.csv", index_col=0)
        df_js = pd.read_csv("js" + "/correlation_general_medianValues.csv", index_col=0)
    elif correlation_type == "turbostat":
        df_python = pd.read_csv("python" + "/correlation_turbostat_allData.csv", index_col=0)
        df_cplusplus = pd.read_csv("c++" + "/correlation_turbostat_allData.csv", index_col=0)
        df_java = pd.read_csv("java" + "/correlation_turbostat_allData.csv", index_col=0)
        df_js = pd.read_csv("js" + "/correlation_turbostat_allData.csv", index_col=0)
    elif correlation_type == "perf":
        df_python = pd.read_csv("python" + "/correlation_perf_allData.csv", index_col=0)
        df_cplusplus = pd.read_csv("c++" + "/correlation_perf_allData.csv", index_col=0)
        df_java = pd.read_csv("java" + "/correlation_perf_allData.csv", index_col=0)
        df_js = pd.read_csv("js" + "/correlation_perf_allData.csv", index_col=0)
    elif correlation_type == "top":
        df_python = pd.read_csv("python" + "/correlation_top_allData.csv", index_col=0)
        df_cplusplus = pd.read_csv("c++" + "/correlation_top_allData.csv", index_col=0)
        df_java = pd.read_csv("java" + "/correlation_top_allData.csv", index_col=0)
        df_js = pd.read_csv("js" + "/correlation_top_allData.csv", index_col=0)

    df_python.set_index(df_python.columns[0])
    df_cplusplus.set_index(df_cplusplus.columns[0])
    df_java.set_index(df_java.columns[0])
    df_js.set_index(df_js.columns[0])

    df_common_values, df_non_common_values = df_common_and_noncommon_Parameters(df_python, df_cplusplus, df_java, df_js, correlation_type)

    return df_common_values, df_non_common_values

def correlations():

    correlations_df_html = "correlations_all_data.html"
    with open(correlations_df_html, 'w') as f:
        f.write('<html><head><title>Correlations Dataframes</title>')
        f.write('<link rel="shortcut icon" type="x-icon" href="aalto.ico"> </link>')
        f.write('<style>')
        f.write('body { font-family: Arial, sans-serif; margin: 20px; }')
        f.write('table { border-collapse: collapse; width: 100%; margin-top: 20px; }')
        f.write('th, td { border: 1px solid #dddddd; text-align: left; padding: 8px; }')
        f.write('th { background-color: #f2f2f2; }')
        f.write('</style>')
        f.write('</head><body>')

        list = ['general', 'turbostat', 'perf', 'top']

        for correlation_type in list:
            print("")
            print("")
            print("                             -------------------" + correlation_type + "-------------------")
            df_common_values, df_non_common_values = correlation_ProgrammingLanguages(correlation_type)
            print("")
            print("COMMON Correlation " + correlation_type)
            print(df_common_values)
            print("")
            print("NON-COMMON Correlation " + correlation_type)
            print(df_non_common_values)
            print("")
            
            f.write("<h2>COMMON Correlation " + correlation_type + "</h2>")
            f.write(df_common_values.to_html())
            f.write("<h2>NON-COMMON Correlation " + correlation_type + "</h2>")
            f.write(df_non_common_values.to_html())

        f.write('</body></html>')

    webbrowser.open(correlations_df_html)

# Function by programming language to create the html string
def html_Language(language, active):

    html_filename = language + "/report_" + language

    command = "python3 analysis_byProgram_general.py " + language + " " + html_filename
    os.system(command)

    nav_link = "nav-link"
    if active: nav_link = nav_link + " active"
    select = "true" if active else "false"

    src = "loadTab('" + html_filename + "')"

    div_html = '''
            <li class="nav-item">
                <a class="''' + nav_link + '''" id="''' + language + '''-tab" data-toggle="tab" href="#''' + language + '''" role="tab" aria-controls="''' + language + '''" aria-selected="''' + select + '''" onclick=" ''' + src + '''">''' + language + '''</a>
            </li>
    '''

    return div_html
    

if __name__ == '__main__':

    html_python = html_Language("python", active = True)
    html_cplusplus = html_Language("c++", active = False)
    html_java = html_Language("java", active = False)
    html_js = html_Language("js", active=False)

    print("Creating the general report ...")
    html_string = '''

    <!DOCTYPE html>
    <html>
    <head>
        <title>General Report</title>
        <link rel="shortcut icon" type="x-icon" href="aalto.ico"> </link>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            /* Adjust the size of the iframes to fit your requirements */
            .iframe-container {
                width: 100%;
                height: 100%;
                margin: 5px 0;
            }
            html, body, iframe, #myTabContent, #turbostat, #perf, #top {
                width: 100%;
                height: 100%;
                margin: 5px 0;
            }
            h1 {text-align: center; margin: 5px 0;}
            @media (max-width: 1200px) {
                h1 {font-size: 1.5rem;}
            }
            details > summary {
                    padding: 4px;
                    width: 100%;
                    border: none;
                    box-shadow: 1px 1px 2px #bbbbbb;
                    cursor: pointer;
                    font-family: inherit;
                }

                details > p {
                    background-color: #eeeeee;
                    padding: 4px;
                    margin: 0;
                    box-shadow: 1px 1px 2px #bbbbbb;
                }
        </style>
    </head>
    <body>
        <h1 class="mb-4">Analysis of energy consumption, performance and memory usage in each language</b> </h1>
        <ul class="nav nav-tabs" id="myTab" role="tablist">
            ''' + html_python + '''
            ''' + html_cplusplus + '''
            ''' + html_java + '''
            ''' + html_js + '''
        </ul>

        <div class="tab-content" id="myTabContent"  >
            <iframe id="content" src="python/report_''' + "python" + '''.html" frameborder="0"></iframe>
        </div>

        <!-- Add Bootstrap and jQuery scripts -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        <script>
            function loadTab(tabName) {
            const iframe = document.getElementById('content');
            iframe.src = `${tabName}.html`;
            }
        </script>
    </body>
    </html>
    '''

    f = open('general_report.html','w')
    f.write(html_string)
    f.close()

    webbrowser.open_new_tab('general_report.html')

    correlations()