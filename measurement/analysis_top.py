# Libraries
import sys
import os
import re
import glob
import webbrowser
import natsort
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly
from sklearn.preprocessing import MaxAbsScaler
from IPython.display import display, HTML

# Arguments
# 
# Example: python3 analysis.py c++ nbody_2.c 50000000 nbody_50000000_4
language=sys.argv[1]
command=sys.argv[2]
directory=sys.argv[3]

# Define path
path=language + '/' + directory + '/top/'
actual_directory = os.getcwd() + '/'

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

js_releaseDates = {
    '20.5.1': '2023-08-09',
    '19.9.0': '2023-04-10',
    '18.17.1': '2023-08-08',
    '17.9.1': '2022-06-01',
    '16.20.2': '2023-08-08',
    '15.14.0': '2021-04-06',
    '14.21.3': '2023-02-16',
    '13.14.0': '2020-04-29',
    '12.22.12': '2022-04-05',
    '11.15.0': '2019-04-30',
    '10.24.1': '2021-04-06',
    '9.11.2': '2018-06-12',
    '8.17.0': '2019-12-17',
    '7.10.1': '2017-07-11',
    '6.17.1': '2019-04-03',
    '5.12.0': '2016-06-23',
    '4.9.1': '2018-03-29',
    '3.3.1': '2015-09-15',
    '2.5.0': '2015-07-28',
    '1.8.4': '2015-07-09',
    '0.12.18': '2017-02-22',
    '0.10.48': '2016-10-18',
    '0.8.28': '2014-07-31'
}

# Function to get release date for a given Python version
def get_release_date(version):
    if language == 'python':
        return python_releaseDates.get(version, 'Unknown')
    elif language == 'c++':
        return cplusplus_releaseDates.get(version, 'Unknown')
    elif language == 'java':
        return java_releaseDates.get(version, 'Unknown')
    elif language == 'js':
        return js_releaseDates.get(version, 'Unknown')

# Function to convert "g" to "k"
def convert_g_to_k(value):
    value_str = str(value)
    if value_str[-1].lower() == 'g':
        g_value = float(value_str[:-1])
        k_value = g_value * 1000000  # 1 giga = 1000000 kilo
        return int(k_value)
    return value

# Function to extract information
def from_CSVfile(file):
     # Read CSV file
    df = pd.read_csv(file)
    if language == 'js': df['version'] = df['version'].str.replace('v', '')

    # New column 'release_date' as the second 
    df['release_date'] = df['version'].apply(get_release_date)
    df.insert(1, 'release_date', df.pop('release_date'))

    # Convert date into datetime
    df['release_date'] = pd.to_datetime(df['release_date'])

    # Changes in the 'version' column
    if language == 'python': df['version'] = df['version'].str.replace('Python ', '')
    if language == 'c++': df['version'] = df['version'].str.split().str[0]

    df.replace(to_replace='-', value=0, inplace=True)
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #     print(df)

    df = df.dropna(subset=['command'])

    # Apply the conversion function to the DataFrame column
    df['res'] = df['res'].apply(convert_g_to_k)
    df['virt'] = df['virt'].apply(convert_g_to_k)

    # # Drop the original column if needed
    # df.drop(columns=['res'], inplace=True)
    # df.rename(columns={'res_k': 'res'}, inplace=True)
    df['res'] = pd.to_numeric(df['res'], errors='coerce')

    # df.drop(columns=['virt'], inplace=True)
    # df.rename(columns={'virt_k': 'virt'}, inplace=True)
    df['virt'] = pd.to_numeric(df['virt'], errors='coerce')

    return df

def from_CSVfiles(path, filename_start):

    all_df = pd.DataFrame()
    list_files = os.listdir(path)

    # Get list of all files only in the given directory
    list_files = natsort.natsorted(list_files)

    for file_name in list_files:
        if file_name.startswith(filename_start) and file_name.endswith('.csv'):
            df = from_CSVfile(path + file_name)
            all_df = pd.concat([all_df, df])

    all_df.to_csv(path + "top_data_allVersions.csv", index=False)

    return all_df

# Function to normalize Top data
def TopData_normalized(df):
    df_data = df[['version', 'release_date', 'appplication']]
    df_metric = df.loc[:, ~df.columns.isin(['version', 'release_date', 'appplication'])]

    transformer = MaxAbsScaler().fit(df_metric)
    scaled = transformer.transform(df_metric)

    df_norm = pd.DataFrame(scaled, columns=df_metric.columns)
    df = pd.concat([df_data,df_norm.reindex(df_data.index)], axis=1)
    return df

# Function to plot the trends
def line_plot(df, filename_plot, x_data, y_data, text_data, norm):
    
    if norm: filename_plot = filename_plot + "_Normalized"

    fig = px.line(df,
                  x = x_data,
                  y = y_data,
                  text=text_data,
                  title=language + ' ' + command)
    fig.update_traces(textposition="bottom right")
    plot = plotly.offline.plot(fig, filename=path + filename_plot + '.html', auto_open=False)
    return filename_plot + ".html"

def line_plot_3variables(df, filename_plot, x_data, y_data, color_data, text_data, norm):
    normalized = ''
    if norm: normalized = "_Normalized"

    fig = px.line(df,
                  x = x_data,
                  y = y_data,
                  color = color_data,
                  text=text_data,
                  title=language + ' ' + command)
    fig.update_traces(textposition="bottom right")
    plot = plotly.offline.plot(fig, filename=path + filename_plot + normalized + '.html', auto_open=False)
    return filename_plot + ".html"

# def line_plot_3variables(df, filename_plot, x_data, y_data, color_data, text_data, norm):

#     if norm: filename_plot = filename_plot + "_Normalized"

#     fig = px.scatter(x=df['virt'], y=df['virt'],
# 	         size=df['no_measurement'], color=df['version'],
#                  hover_name=df['version'])

#     fig.update_traces(textposition="bottom right")
#     plot = plotly.offline.plot(fig, filename=path + filename_plot + '.html', auto_open=False)
#     return filename_plot + ".html"

def plot_TopData(df, normalized):

    if normalized: df = TopData_normalized(df)

    print("Analysis of Top data")

    first_url = line_plot_3variables(df=df, filename_plot='plotTop1_virtualMemory',
              x_data="no_measurement", 
              y_data="virt",
              color_data="version",
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)
    
    second_url = line_plot_3variables(df=df, filename_plot='plotTop2_residentMemory',
              x_data="no_measurement", 
              y_data="res",
              color_data="version",
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)

    third_url = line_plot_3variables(df=df, filename_plot='plotTop3_sharedMemory',
              x_data="no_measurement", 
              y_data="shr",
              color_data="version",
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)
    
    fourth_url = line_plot_3variables(df=df, filename_plot='plotTop4_percentCPU',
              x_data="no_measurement", 
              y_data="percent_cpu",
              color_data="version",
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)

    fifth_url = line_plot_3variables(df=df, filename_plot='plotTop5_percentMemory',
              x_data="no_measurement", 
              y_data="percent_mem",
              color_data="version",
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)

    return first_url, second_url, third_url, fourth_url, fifth_url
    
def plot_TopDataLine(df, normalized):

    if normalized: df = TopData_normalized(df)

    print("Analysis of Top data")

    first_url = line_plot(df=df, filename_plot='plotTop1_memoryData',
              x_data="version", 
              y_data=["virt","res","shr"],
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)
    
    second_url = line_plot(df=df, filename_plot='plotTop2_percentData',
              x_data="version", 
              y_data=["percent_cpu","percent_mem"],
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)
    
    return first_url, second_url

if __name__ == '__main__':
    
    df = from_CSVfiles(path, 'temp_top_data_')
    display(df)
    
    first_plot, second_plot, third_plot, fourth_plot, fifth_plot = plot_TopData(df, normalized=False)
    first_plotMemory, second_plotPercent = plot_TopDataLine(df, normalized=False)

    summary_table = df.groupby('version')[['virt','res','shr','percent_cpu','percent_mem']].agg(['max','min'])
    summary_table = summary_table.to_html().replace('<table border="1" class="dataframe">','<table class="table table-striped">') # use bootstrap styling
    table = df.to_html().replace('<table border="1" class="dataframe">','<table class="table table-striped">')

    # Obtain all files starting with 'plot'

    html_string = '''
    <html>
        <head>
            <title>Top data</title>
            <link rel="shortcut icon" type="x-icon" href="''' + "../../../" + "aalto.ico" + '''"> </link>
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
            </style>
        </head>
        <body>
            <h1>Top data in in <b>''' + language + '''</b> through <b>''' + command + '''</b> </h1>
            <div class="row">
                <div class="column">
                    <h2>Top Data</h2>
                    <!-- *** Section 1 *** --->
                    <h3>Section 1: Virtual memory through different versions</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + first_plot + '''"></iframe>
                    <p>Notes: </p>
                    <!-- *** Section 2 *** --->
                    <h3>Section 2: Resident memory through different versions</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + second_plot + '''"></iframe>
                    <p>Notes</p>

                    <!-- *** Section 3 *** --->
                    <h3>Section 3: Shared memory through different versions</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + third_plot + '''"></iframe>
                    <p>Notes</p>

                    <!-- *** Section 4 *** --->
                    <h3>Section 4: Percent of CPU used through different versions</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + fourth_plot + '''"></iframe>
                    <p>Notes</p>

                    <!-- *** Section 5 *** --->
                    <h3>Section 5: Percent of Memory used through different versions</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + fifth_plot + '''"></iframe>
                    <p>Notes</p>
                </div>
                <div class="column">
                    <h2>Top Data</h2>
                    <!-- *** Section 1 *** --->
                    <h3>Section 1: Memory information through different versions </h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + first_plotMemory + '''"></iframe>
                    <p>Notes: </p>
                    <!-- *** Section 2 *** --->
                    <h3>Section 2: CPU and Memory percent through different versions</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + second_plotPercent + '''"></iframe>
                    <p>Notes</p>
                </div>
            </div>
            
            <h2>Summary table of Top dataset</h2>
            ''' + summary_table + '''
        </body>
    </html>'''

    f = open(path + 'report_Top.html','w')
    f.write(html_string)
    f.close()

    # webbrowser.open_new_tab(path + 'report_Top.html')