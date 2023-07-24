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

# Arguments
# 
# Example: python3 analysis.py c++ nbody_2.c 50000000 nbody_50000000_4
language=sys.argv[1]
command=sys.argv[2]
directory=sys.argv[3]

# Define path
path=language + '/' + directory + '/turbostat/'
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

# Function to get release date for a given Python version
def get_release_date(version):
    if language == 'python':
        return python_releaseDates.get(version, 'Unknown')
    elif language == 'c++':
        return cplusplus_releaseDates.get(version, 'Unknown')
    
# Function to extract information
def from_CSVfile(file):
     # Read CSV file
    df = pd.read_csv(file)

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
    return df

# Function to normalize Turbostat data
def TurbostatData_normalized(df):
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

def plot_TurbostatData(df, normalized):

    if normalized: df = TurbostatData_normalized(df)

    print("Analysis of Turbostat data")

    first_url = line_plot(df=df, filename_plot='plot1_energyconsumption',
              x_data="version", 
              y_data=["time_elapsed","Pkg_J","Cor_J","GFX_J","RAM_J","Avg_MHz"],
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)
    
    second_url = line_plot(df=df, filename_plot='plot2_cpu',
              x_data="version", 
              y_data=["time_elapsed","Pkg_J","Avg_MHz","Busy%","Bzy_MHz","IPC","IRQ","POLL"],
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)

    third_url = line_plot(df=df, filename_plot='plot3_cstates',
              x_data="version", 
              y_data=["C1","C1E","C3","C6","C7s","C8"],
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)

    fourth_url = line_plot(df=df, filename_plot='plot4_temperature',
              x_data="version", 
              y_data=["CoreTmp","PkgTmp"],
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)

    fifth_url = line_plot(df=df, filename_plot='plot5_moreParameters',
              x_data="version", 
              y_data=["GFX%rc6","GFXMHz","Totl%C0","Any%C0","GFX%C0","CPUGFX%"],
              text_data=pd.to_datetime(df['release_date']).dt.year,
              norm=normalized)
    return first_url, second_url, third_url, fourth_url, fifth_url
    

if __name__ == '__main__':
    
    df = from_CSVfile(path + 'turbostat_performance_data_allVersions.csv')
    
    first_plot, second_plot, third_plot, fourth_plot, fifth_plot = plot_TurbostatData(df, normalized=False)
    first_plotNorm, second_plotNorm, third_plotNorm, fourth_plotNorm, fifth_plotNorm = plot_TurbostatData(df, normalized=True)

    summary_table = df.describe()
    summary_table = summary_table.to_html().replace('<table border="1" class="dataframe">','<table class="table table-striped">') # use bootstrap styling
    table = df.to_html().replace('<table border="1" class="dataframe">','<table class="table table-striped">')

    # Extract relevant columns
    version = df['version']
    release = df['release_date']
    time_elapsed = df['time_elapsed']
    avg_mhz = df['Avg_MHz']                       # no. of cycles executed divided by time elapsed
    busy_percent = df['Busy%']                    # % of time in C0 state
    busy_mhz = df['Bzy_MHz']                      # Avg clock rate while the CPU was not idle in C0 state
    ipc = df['IPC']
    irq = df['IRQ']
    poll = df['POLL']
    c1 = df['C1']
    c1e = df['C1E']
    c3 = df['C3']
    c6 = df['C6']
    c7s = df['C7s']
    c8 = df['C8']
    coreTemperature = df['CoreTmp']
    pkgTemperature = df['PkgTmp']
    gfx_percent = df['GFX%rc6']
    gfx_mhz = df['GFXMHz']
    total_c0_percent = df['Totl%C0']
    any_c0_percent = df['Any%C0']
    gfx_c0_percent = df['GFX%C0']
    cpugfx_percent = df['CPUGFX%']
    energy_pkg = df['Pkg_J']
    energy_core = df['Cor_J']
    energy_gfx = df['GFX_J']
    energy_ram = df['RAM_J']

    # Obtain all files starting with 'plot'

    html_string = '''
    <html>
        <head>
            <title>Turbostat data</title>
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
            </style>
        </head>
        <body>
            <h1>Turbostat data in <b>''' + language + '''</b> through <b>''' + command + '''</b> </h1>
            <div class="row">
                <div class="column">
                    <h2>Turbostat Data</h2>
                    <!-- *** Section 1 *** --->
                    <h3>Section 1: Energy consumption and time elapsed </h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + first_plot + '''"></iframe>
                    <p>Notes: </p>
                    
                    <!-- *** Section 2 *** --->
                    <h3>Section 2: CPU information</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + second_plot + '''"></iframe>
                    <p>Notes</p>

                    <!-- *** Section 3 *** --->
                    <h3>Section 3: Cstates</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + third_plot + '''"></iframe>
                    <p>Notes</p>

                    <!-- *** Section 4 *** --->
                    <h3>Section 4: Temperature</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + fourth_plot + '''"></iframe>
                    <p>Notes</p>

                    <!-- *** Section 5 *** --->
                    <h3>Section 5: More parameters</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + fifth_plot + '''"></iframe>
                    <p>Notes</p>
                </div>
                <div class="column">
                    <h2>Turbostat Data Normalized</h2>
                    <!-- *** Section 1 *** --->
                    <h3>Section 1: Energy consumption and time elapsed </h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + first_plotNorm + '''"></iframe>
                    <p>Notes: </p>
                    
                    <!-- *** Section 2 *** --->
                    <h3>Section 2: CPU information</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + second_plotNorm + '''"></iframe>
                    <p>Notes</p>

                    <!-- *** Section 3 *** --->
                    <h3>Section 3: Cstates</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + third_plotNorm + '''"></iframe>
                    <p>Notes</p>

                    <!-- *** Section 4 *** --->
                    <h3>Section 4: Temperature</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + fourth_plotNorm + '''"></iframe>
                    <p>Notes</p>

                    <!-- *** Section 5 *** --->
                    <h3>Section 5: More parameters</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + fifth_plotNorm + '''"></iframe>
                    <p>Notes</p>
                </div>
            </div>
            
            <h2>Turbostat dataset</h2>
            ''' + table + '''
            <h2>Summary table of Turbostat dataset</h2>
            ''' + summary_table + '''
        </body>
    </html>'''

    f = open(path + 'report_Turbostat.html','w')
    f.write(html_string)
    f.close()