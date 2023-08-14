# Libraries
import sys
import os
import glob
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly
from sklearn.preprocessing import MaxAbsScaler
from IPython.display import display, HTML

# Directory
actual_directory = os.getcwd() + '/'

# language=sys.argv[1]

python_releaseDates = {
    'Python 3.13.0a0': '2023-06-07',
    'Python 3.12.0b1': '2023-05-22',
    'Python 3.11.3': '2023-04-05',
    'Python 3.10.11': '2023-04-05',
    'Python 3.9.16': '2022-12-06',
    'Python 3.8.16': '2022-12-06',
    'Python 3.7.16': '2022-12-06',
    'Python 3.6.15': '2021-09-04',
    'Python 3.5.10': '2020-09-05',
    'Python 3.4.10': '2019-03-18',
    'Python 3.3.7': '2017-09-19',
    'Python 3.2.6': '2014-10-11',
    'Python 3.1.5': '2012-04-09',
    'Python 3.0.1': '2009-02-13',
    'Python 2.7.18': '2020-04-20',
    'Python 2.6.9': '2013-10-29',
    'Python 2.5.6': '2011-05-26',
}

cplusplus_releaseDates = {
    'g++-4.4 4.4.7': '2012-03-13',
    'g++-4.6 4.6.4': '2013-04-12',
    'g++-4.7 4.7.4': '2014-06-12',
    'g++-4.8 4.8.5': '2015-06-23',
    'g++-4.9 4.9.3': '2015-06-26',
    'g++-5 5.5.0': '2017-10-10',
    'g++-6 6.5.0': '2018-10-26',
    'g++-7 7.5.0': '2019-11-14',
    'g++-8 8.5.0': '2021-05-14',
    'g++-8 ': '2021-05-14',
    'g++-9 9.5.0': '2022-05-27',
    'g++-10 10.4.0': '2022-06-28',
    'g++-10 10.5.0': '2023-07-07',
    'g++-11 11.4.0': '2023-05-29',
    'g++-12 12.3.0': '2023-05-08',
    'g++-13 13.1.0': '2023-04-26',
}

java_releaseDates = {
    '1.8.0_362': '2023-04-18',
    '9.0.4': '2018-01-16',
    '10.0.2': '2018-07-17',
    '11.0.19': '2020-10-20',
    '12.0.2': '2019-07-16',
    '13.0.2': '2020-01-14',
    '14.0.2': '2020-07-14',
    '15.0.2': '2021-01-19',
    '16.0.2': '2021-07-20',
    '17.0.7': '2023-04-18',
    '18.0.2-ea': '2022-07-19',
    '19.0.2': '2023-01-17',
    '20.0.2': '2023-07-18',
}


# Function to get release date for a given Python version
def get_release_date(version, language):
    if language == 'python':
        return python_releaseDates.get(version, 'Unknown')
    elif language == 'c++':
        return cplusplus_releaseDates.get(version, 'Unknown')
    elif language == 'java':
        return java_releaseDates.get(version, 'Unknown')
    

def TopData_normalized(df):
    df_data = df[['version', 'release_date', 'path', 'appplication']]
    # df_metric = df.loc[:, ~df.columns.isin(['version', 'release_date', 'path', 'appplication'])]
    # 'nMin'
    df_metric = df[['virt', 'res', 'shr', 'percent_cpu', 'percent_mem',
                    'nTH', 'P', 'SWAP', 'CODE', 'DATA', 'nMaj',
                    'nDRT', 'USED']]

    transformer = MaxAbsScaler().fit(df_metric)
    scaled = transformer.transform(df_metric)

    df_norm = pd.DataFrame(scaled, columns=df_metric.columns)
    df = pd.concat([df_data,df_norm.reindex(df_data.index)], axis=1)
    return df
    
# Function to extract information
def from_CSVfile(file, directory, language):
     # Read CSV file
    df = pd.read_csv(file)

    # # New column 'release_date' as the second 
    # df['release_date'] = df['version'].apply(get_release_date, language=language)
    # df.insert(1, 'release_date', df.pop('release_date'))

    # New column 'path' as the third
    df['path'] = directory
    df.insert(2, 'path', df.pop('path'))

    # df = df.dropna(subset=['command'])
    # df.to_csv('df_test.csv')
    # Convert date into datetime
    # df['release_date'] = pd.to_datetime(df['release_date'])

    # Changes in the 'version' column
    if language == 'python': df['version'] = df['version'].str.replace('Python ', '')
    if language == 'c++': df['version'] = df['version'].str.split().str[0]

    df.replace(to_replace='-', value=0, inplace=True)
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #     print(df)

    return df

def from_CSVfiles(language, tool, norm):

    extra = ''
    all_df = pd.DataFrame()

    if tool == "turbostat": extra = "_performance"

    list_directories = next(os.walk(language))[1]
    list_directories.sort()

    for directory_name in list_directories:
        if directory_name != "older" and directory_name != "test" and directory_name != "general_plots":
            path=language + '/' + directory_name + '/' + tool + '/' + tool + extra
            df = from_CSVfile(path + '_data_allVersions.csv', directory_name, language)
            if norm: df = TopData_normalized(df)
            all_df = pd.concat([all_df, df])

    return all_df

# PLOTS
def plot_3variables(language, df, filename_plot, x_data, y_data, color_data, type, norm):
    
    normalized = ''
    if norm: normalized = "_Normalized"

    if type == "box":
        fig = px.box(df,
                    x = x_data,
                    y = y_data,
                    color = color_data,
                    title=language + ' ' + normalized)
        #fig.update_traces(textposition="bottom right")

        buttons=list([
                    dict(
                        args=[{"type": "bar"}],
                        label="Bar Chart",
                        method="restyle"
                    ),dict(
                        args=[{"type": "line",}],
                        label="Line Chart",
                        method="restyle"
                    )
                ])
        
    elif type == "bar":
        fig = px.bar(df.groupby([x_data,color_data])[[y_data]].mean().reset_index(),
                  x = x_data,
                  y = y_data,
                  color = color_data,
                  title=language + ' ' + normalized)
        
        buttons=list([
                    dict(
                        args=[{"type": "bar"}],
                        label="Bar Chart",
                        method="restyle"
                    ),dict(
                        args=[{"type": "line",}],
                        label="Line Chart",
                        method="restyle"
                    )
                ])
        
    updatemenus = list([
        dict(
            type="dropdown",
            direction="down",
            x=0.1,
            y=1.12,
            xanchor="left",
            yanchor="top",
            pad={"r": 10, "t": 10},
            buttons=buttons
        ),
        dict(
            type="dropdown",
            direction="down",
            x=0.37,
            y=1.12,
            xanchor="left",
            yanchor="top",
            pad={"r": 10, "t": 10},
            buttons=list([
                dict(
                    args=[{"yaxis.type": "linear"}],
                    label="Linear Scale",
                    method="relayout"
                ),
                dict(
                    args=[{"yaxis.type": "log"}],
                    label="Log Scale",
                    method="relayout"
                )
            ])
        ),
    ])

    annotations=[
        dict(text="Plot type:", x=-0.01, xref="paper", y=1.08, yref="paper",
                             align="left", showarrow=False),
        dict(text="Scale:", x=0.3, xref="paper", y=1.08,
                             yref="paper", showarrow=False),
    ]
    fig.update_layout(updatemenus=updatemenus, annotations=annotations)

    # Check if the directory exists
    directory = language + '/general_plots/'
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)

    filename_plot = directory + filename_plot + normalized + "_" + type
    plot = plotly.offline.plot(fig, filename= filename_plot + '.html', auto_open=False)
    return filename_plot + ".html"

def plot_TopData(language, df, plot, normalized):

    print("Analysis of Top data of " + language)

    fig1_url = plot_3variables(language, df, 
                                     filename_plot="top_virt", 
                                     x_data="version", 
                                     y_data="virt", 
                                     color_data="path",
                                     type=plot,
                                     norm=normalized)
    fig2_url = plot_3variables(language, df, 
                                     filename_plot="top_res", 
                                     x_data="version", 
                                     y_data="res", 
                                     color_data="path",
                                     type=plot,
                                     norm=normalized)
    
    fig3_url = plot_3variables(language, df, 
                                     filename_plot="top_shr", 
                                     x_data="version", 
                                     y_data="shr", 
                                     color_data="path",
                                     type=plot,
                                     norm=normalized)
    
    fig4_url = plot_3variables(language, df, 
                                     filename_plot="top_percent_cpu", 
                                     x_data="version", 
                                     y_data="percent_cpu", 
                                     color_data="path",
                                     type=plot,
                                     norm=normalized)
    
    fig5_url = plot_3variables(language, df, 
                                     filename_plot="top_percent_mem", 
                                     x_data="version", 
                                     y_data="percent_mem", 
                                     color_data="path",
                                     type=plot,
                                     norm=normalized)
    
    return fig1_url, fig2_url, fig3_url, fig4_url, fig5_url

def html_Plots(language, df, plot):
    
    fig1, fig2, fig3, fig4, fig5 = plot_TopData(language, df, plot, normalized=False)

    div_string = '''
                <div class="row">
                    <h2>''' + language + '''</h2>
                        <!-- *** Section 1 *** --->
                        <h3>Section 1: Virtual memory in ''' + language + '''</h3>
                        <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                            src="''' + fig1 + '''"></iframe>
                        <p>Notes: </p>
                        
                        <!-- *** Section 2 *** --->
                        <h3>Section 2: Resident memory in ''' + language + ''' </h3>
                        <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                            src="''' + fig2 + '''"></iframe>
                        <p>Notes</p>

                        <!-- *** Section 3 *** --->
                        <h3>Section 3: Shared memory in ''' + language + '''</h3>
                        <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                            src="''' + fig3 + '''"></iframe>
                        <p>Notes</p>

                        <!-- *** Section 4 *** --->
                        <h3>Section 4: CPU usage in ''' + language + '''</h3>
                        <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                            src="''' + fig4 + '''"></iframe>
                        <p>Notes</p>

                        <!-- *** Section 5 *** --->
                        <h3>Section 5: Memory usage in ''' + language + '''</h3>
                        <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                            src="''' + fig5 + '''"></iframe>
                        <p>Notes</p>
                    
                </div>
    '''
    
    return div_string

def html_Language(language, df, color):

    div_Box = html_Plots(language, df, "box")
    div_Bar = html_Plots(language, df, "bar")

    div_string = '''
            <details>
                <summary style="background-color: ''' + color + ''';">''' + language + '''</summary>
                ''' + div_Box + '''
                ''' + div_Bar + '''
            </details>
    '''
    return div_string


if __name__ == '__main__':
    
    df_python = from_CSVfiles("python", "top", norm=False)
    df_cplusplus = from_CSVfiles("c++", "top", norm=False)
    df_java = from_CSVfiles("java", "top", norm=False)

    # df_pythonNorm = from_CSVfiles("python", "top", norm=True)
    # df_cplusplusNorm = from_CSVfiles("c++", "top", norm=True)
    # df_javaNorm = from_CSVfiles("java", "top", norm=True)
    
    # All plots
    div_py = html_Language("python", df_python, "#f3c90f")
    div_cplusplus = html_Language("c++", df_cplusplus, "#0f9ff3")
    div_java = html_Language("java", df_java, "#c91032")

    # Obtain all files starting with 'plot'

    html_string = '''
    <html>
        <head>
            <title>Top General data</title>
            <link rel="shortcut icon" type="x-icon" href="''' + "aalto.ico" + '''"> </link>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
            <style>
                body{ margin:0 50; background:whitesmoke; }
                *{box-sizing: border-box;}
                .column {float: left; width: 50%; padding: 10px;}
                .row:after {content: ""; display: table; clear: both;}
                .plot {width: 100%; height: 600;}
                h1 {text-align: center}
                h2 {text-align: center}
                @media (max-width: 1200px) {
                    .column {
                    width: 100%;
                    float: none;
                    }
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
            <h1>Top data in <b>''' + 'all languages' + '''</b> </h1>
            ''' + div_py + '''
            ''' + div_cplusplus + '''
            ''' + div_java + '''
        </body>
    </html>'''

    f = open('' + 'report_Top.html','w')
    f.write(html_string)
    f.close()

    webbrowser.open_new_tab('report_Top.html')