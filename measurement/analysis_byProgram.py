# Libraries
import sys
import os
import glob
import webbrowser
import natsort
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import MaxAbsScaler
from IPython.display import display, HTML

# Arguments
# 
# Example: python3 analysis.py c++ nbody_2.c 50000000 nbody_50000000_4
language = sys.argv[1]
html_filename = sys.argv[2]
# directory=sys.argv[3]

# Directory
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

# Function to convert "g", "m" or KiB to "byte"
def convert_g_to_byte(value):
    value_str = str(value)
    if value_str[:-1] == "":
        Byte_value = 0
    elif value_str[-1].lower() == 'g':
        g_value = float(value_str[:-1])
        Byte_value = g_value * 1024 * 1024 * 1024  # 1 giga = 1,000,000,000
    elif value_str[-1].lower() == 'm':
        m_value = float(value_str[:-1])
        Byte_value = m_value * 1024 * 1024 # 1 giga = 1,000,000
    elif value_str[-1].lower() == 'k':
        k_value = float(value_str[:-1])
        Byte_value = k_value * 1024 # 1 kilo = 1,000
    else:
        k_value = float(value_str)
        Byte_value = k_value * 1024 # 1 kilo = 1,000
    return int(Byte_value)

def convert_toUnit(column):
    column = column.apply(convert_g_to_byte)
    column = pd.to_numeric(column, errors='coerce')
    return column
    
def Data_normalized(df, tool):
    df_data = df[['version', 'release_date', 'path', 'appplication']]
    if tool == "turbostat": 
        df_metric = df.loc[:, ~df.columns.isin(['version', 'release_date', 'path', 'appplication'])]
    elif tool == "top":
        df_metric = df[['virt', 'res', 'shr', 'percent_cpu', 'percent_mem',
                    'nTH', 'P', 'SWAP', 'CODE', 'DATA', 'nMaj',
                    'nDRT', 'USED']]

    transformer = MaxAbsScaler().fit(df_metric)
    scaled = transformer.transform(df_metric)

    df_norm = pd.DataFrame(scaled, columns=df_metric.columns)
    df = pd.concat([df_data,df_norm.reindex(df_data.index)], axis=1)
    return df

# Function to extract information in every file
def from_CSVfile(file, directory, tool):
     # Read CSV file
    df = pd.read_csv(file)
    if language == 'js': df['version'] = df['version'].str.replace('v', '')
    
    # New column 'release_date' as the second 
    df['release_date'] = df['version'].apply(get_release_date)
    df.insert(1, 'release_date', df.pop('release_date'))

    # Convert date into datetime
    df['release_date'] = pd.to_datetime(df['release_date'])

    # New column 'path' as the third
    df['path'] = directory
    df.insert(2, 'path', df.pop('path'))

    # Clean and remove the unnecessary rows
    df.replace(to_replace='-', value=0, inplace=True)

    # Apply the conversion function to the DataFrame column
    if tool == "top":
        df = df.dropna(subset=['command'])
        df['virt'] = convert_toUnit(df['virt'])
        df['res'] = convert_toUnit(df['res'])
        df['shr'] = convert_toUnit(df['shr'])
        df['CODE'] = convert_toUnit(df['CODE'])
        df['DATA'] = convert_toUnit(df['DATA'])
        df['SWAP'] = convert_toUnit(df['SWAP'])
        df['USED'] = convert_toUnit(df['USED'])
        df['nMin'] = convert_toUnit(df['nMin'])
        df['nMaj'] = convert_toUnit(df['nMaj'])

    # Changes in the 'version' column
    if language == 'python': df['version'] = df['version'].str.replace('Python ', '')
    if language == 'c++': df['version'] = df['version'].str.split().str[0]

    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #     print(df)

    return df

# Extract all information from ALL files
def from_CSVfiles(tool, norm):

    all_df = pd.DataFrame()

    list_directories = next(os.walk(language))[1]
    list_directories.sort()

    for directory_name in list_directories:
        if directory_name != "older" and directory_name != "test" and directory_name != "general_plots" and directory_name != "general_plots_v1":
            
            path=language + '/' + directory_name + '/' + tool + '/'
            if tool == "perf": path = path + tool

            if tool == "top":

                df = pd.DataFrame()
                list_files = os.listdir(path)

                # Get list of all files only in the given directory
                list_files = natsort.natsorted(list_files)

                for file_name in list_files:
                    if file_name.startswith("temp_top_data_") and file_name.endswith('.csv'):
                        df_Top = from_CSVfile(path + file_name, directory_name, tool)
                        df = pd.concat([df, df_Top])

                df.to_csv(path + "top_data_allVersions.csv", index=False)
            elif tool == "turbostat":
                df = pd.DataFrame()
                list_files = os.listdir(path)

                # Get list of all files only in the given directory
                list_files = natsort.natsorted(list_files)

                for file_name in list_files:
                    if file_name.startswith("turbostat_performance_data") and file_name.endswith('.csv') and file_name != "turbostat_performance_data_allVersions.csv":
                        df_Turbo = from_CSVfile(path + file_name, directory_name, tool)
                        df = pd.concat([df, df_Turbo])

            else:
                df = from_CSVfile(path + '_data_allVersions.csv', directory_name, tool)
                if norm: df = Data_normalized(df, tool)
            all_df = pd.concat([all_df, df])

    return all_df


# PLOTTING
def custom_hover_mean(program, x, y, mean, diff, percent_diff, diff_flag):
    percent_difffromMean = 0 if mean == 0 else 100 * (y/mean)
    if diff_flag:
        hover = f'Version: {x}<br>Program: {program}<br><b><i>Percentage Difference:</i> {percent_diff:.2f}%<br>Difference: {diff:.2f}<br></b><i>Percentage Difference from Mean:</i> {percent_difffromMean:.2f}%<br>Difference From Mean: {y:.2f}<br>Mean: {mean:.2f}<br>'
    else:
        hover = f'Version: {x}<br>Program: {program}<br><i>Percentage Difference:</i> {percent_diff:.2f}%<br>Difference: {diff:.2f}<br><b><i>Percentage Difference from Mean:</i> {percent_difffromMean:.2f}%<br>Difference From Mean: {y:.2f}</b><br>Mean: {mean:.2f}<br>'
    return hover

def custom_hover_median(program, x, median, diff, percent_diff):
    hover = f'Version: {x}<br>Program: {program}<br><b><i>Percentage Difference:</i> {percent_diff:.2f}%<br>Difference: {diff:.2f}<br>Median: {median:.2f}<br>'
    return hover

def plot_Compare(df, filename_plot, x_data, y_data, color_data, type, diff_flag):

    # if type == "barTop": df = df.groupby([x_data,color_data], sort=False)[[y_data]].mean().reset_index()
    # if type == "lineTop": df = df.groupby([x_data,color_data], sort=False)[[y_data]].mean().reset_index()
    if type == "barTop" or type == "lineTop" or type == "barTurbo" or type == "lineTurbo": 
        df = df.groupby([x_data,color_data], sort=False)[[y_data]].median().reset_index()

    median_per_program = df.groupby(color_data)[y_data].median()
    # mean_per_program = df.groupby(color_data)[y_data].mean()

    # df['DifferenceFromMean'] = df.apply(lambda row: row[y_data] - mean_per_program[row[color_data]], axis=1)

    # Create grouped bar traces for each program
    bar_traces = []
    for program in df[color_data].unique():
        program_df = df[df[color_data] == program]
        # mean = mean_per_program[program]
        median = median_per_program[program]
        program_df['Difference'] = program_df[y_data].diff()
        program_df['Percentage_Difference'] = program_df[y_data].pct_change()*100
        # program_df['Percentage_DifferenceFromMean'] = program_df.apply(lambda row: 0 if (mean == 0) else 100 * (row["DifferenceFromMean"] / mean), axis=1)
        if diff_flag:
            hover_texts = [custom_hover_median(program, x, median, diff, percent_diff) for x, diff, percent_diff in zip(program_df[x_data],program_df['Difference'],program_df['Percentage_Difference'])]
            bar_trace = go.Bar(x=program_df[x_data], y=program_df['Difference'],
                            name=f'{program} - Median: { format(median_per_program[program], ".2f")}',
                            hovertemplate=hover_texts,
                            text=program_df["Percentage_Difference"])
        # else:
            # hover_texts = [custom_hover_mean(program, x, y, median, diff, percent_diff, diff_flag) for x, y, diff, percent_diff in zip(program_df[x_data], program_df['DifferenceFromMean'],program_df['Difference'],program_df['Percentage_Difference'])]
            # bar_trace = go.Bar(x=program_df[x_data], y=program_df['DifferenceFromMean'],
            #                name=f'{program} - Mean: { format(median_per_program[program], ".2f")}',
            #                hovertemplate=hover_texts,
            #                text=program_df["Percentage_DifferenceFromMean"])
        bar_traces.append(bar_trace)
        # bar_traces.append(median_trace)

    layout = go.Layout(title='Comparison of ' + y_data,
                       xaxis=dict(title=x_data),
                       yaxis=dict(title='Difference from Mean of ' + y_data, zeroline=False))
        

    fig = go.Figure(data=bar_traces, layout=layout)
    if language == 'js': fig.update_xaxes(categoryorder='array', categoryarray= ['0.8.28', '0.10.48', '0.12.18', '1.8.4', '2.5.0', '3.3.1', '4.9.1', '5.12.0', '6.17.1', '7.10.1', '8.17.0', '9.11.2', '10.24.1', '11.15.0', '12.22.12', '13.14.0', '14.21.3', '15.14.0', '16.20.2', '17.9.1', '18.17.1', '19.9.0', '20.5.1'])

    # Check if the directory exists
    directory = language + '/general_plots/'
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)

    filename_plot_wDir = directory + filename_plot
    plot = plotly.offline.plot(fig, filename= filename_plot_wDir + '.html', auto_open=False)
    return 'general_plots/' + filename_plot + ".html"

def plot_Type(df, filename_plot, x_data, y_data, color_data, type):

    if type == "line" or type == "lineTop" or type == "lineTurbo":
        
        if type == "lineTop": df = df.groupby([x_data,color_data], sort=False)[[y_data]].median().reset_index()
        if type == "lineTurbo": df = df.groupby([x_data,color_data], sort=False)[[y_data]].median().reset_index()

        fig = px.line(df,
                x = x_data,
                y = y_data,
                color = color_data,
                title=language + ' - ' + filename_plot)
        fig.update_traces(textposition="bottom right")
        buttons=list([
                     dict(
                          args=[{"type": "line",}],
                          label="Line Chart",
                          method="restyle"
                        ),
                     dict(
                          args=[{"type": "bar"}],
                          label="Bar Chart",
                          method="restyle"
                     )
                   ])

    elif type == "bar" or type == "barTop":

        if type == "barTop": df = df.groupby([x_data,color_data], sort=False)[[y_data]].median().reset_index()
        if type == "barTurbo": df = df.groupby([x_data,color_data], sort=False)[[y_data]].median().reset_index()

        fig = px.bar(df,
                     x = x_data,
                     y = y_data,
                     color = color_data,
                     title=language + ' - ' + filename_plot)
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

    elif type == "box":
        fig = px.box(df,
                        x = x_data,
                        y = y_data,
                        color = color_data,
                        title=language + ' - ' + filename_plot)
        # fig.update_traces(textposition="bottom right")

        buttons=list([
                      dict(
                           args=[{"type": "box"}],
                           label="Box Plot",
                           method="restyle"
                      )])

    
    updatemenus = list([
            dict(
                type="dropdown",
                direction="down",
                x=0.12,
                y=1.12,
                xanchor="left",
                yanchor="top",
                pad={"r": 10, "t": 10},
                buttons=buttons
            ),
            dict(
                type="dropdown",
                direction="down",
                x=0.44,
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
            dict(text="Scale:", x=0.4, xref="paper", y=1.08,
                                yref="paper", showarrow=False),
       ]

    fig.update_layout(updatemenus=updatemenus, annotations=annotations, hovermode="x unified")
    if language == 'js': fig.update_xaxes(categoryorder='array', categoryarray= ['0.8.28', '0.10.48', '0.12.18', '1.8.4', '2.5.0', '3.3.1', '4.9.1', '5.12.0', '6.17.1', '7.10.1', '8.17.0', '9.11.2', '10.24.1', '11.15.0', '12.22.12', '13.14.0', '14.21.3', '15.14.0', '16.20.2', '17.9.1', '18.17.1', '19.9.0', '20.5.1'])


    # Check if the directory exists
    directory = language + '/general_plots/'
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)

    filename_plot_wDir = directory + filename_plot
    plot = plotly.offline.plot(fig, filename= filename_plot_wDir + '.html', auto_open=False)
    return 'general_plots/' + filename_plot + ".html"

def three_plots(df, title, filename_plot, x_data, y_data, color_data, type):
    fig1 = plot_Type(df, filename_plot, x_data, y_data, color_data, type)
    fig2 = plot_Compare(df, filename_plot + "_Comparison_Diff", x_data, y_data, color_data, type, diff_flag=True)
    fig3 = plot_Compare(df, filename_plot + "_Comparison_DiffFromMean", x_data, y_data, color_data, type, diff_flag=False)

    div_string = '''
                <div class="row">
                    <!-- *** Section 1 *** --->
                    <h3>Section:  ''' + title + '''</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + fig1 + '''"></iframe>
                    <p>Notes: </p>
                    </div>
                </div>
                <div class="row">
                    <div class="column">
                        <!-- *** Section 2 *** --->
                        <h3>Section:  Difference of ''' + title + '''</h3>
                        <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                            src="''' + fig2 + '''"></iframe>
                        <p>Notes: Detect major changes between version to another</p>
                    </div>
                    <div class="column">
                        <!-- *** Section 3 *** --->
                        <h3>Section: Difference from Mean of ''' + title + '''</h3>
                        <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                            src="''' + fig3 + '''"></iframe>
                        <p>Notes: Detect the trend in general considering all versions</p>
                    </div>
                </div>
    '''

    return div_string

def two_plots(df, title, filename_plot, x_data, y_data, color_data, type):

    fig1 = plot_Type(df, filename_plot, x_data, y_data, color_data, type)
    fig2 = plot_Compare(df, filename_plot + "_Comparison_Diff", x_data, y_data, color_data, type, diff_flag=True)

    div_string = '''
                <div class="row">
                    
                    <!-- *** Section 1 *** --->
                    <h3>Section:  ''' + title + '''</h3>
                    <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                        src="''' + fig1 + '''"></iframe>
                </div>
                <details>
                    <summary style="background-color: #E5E4E2;">Section: Difference of ''' + title + '''</summary>
                    <div class="row">
                            <!-- *** Section 2 *** --->
                            <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                                src="''' + fig2 + '''"></iframe>
                            <p>Notes: Detect major changes between version to another</p>
                    </div>
                </details>
    '''

    return div_string

def one_plot(df, title, filename_plot, x_data, y_data, color_data, type):

    fig1 = plot_Type(df, filename_plot, x_data, y_data, color_data, type)

    div_string = '''
                <div class="row">
                        <!-- *** Section 1 *** --->
                        <h3>Section:  ''' + title + '''</h3>
                        <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                            src="''' + fig1 + '''"></iframe>
                        <p>Notes: </p>
                    </div>
                </div>
    '''

    return div_string

def html_TimePlots(df):
    
    time_elapsed = two_plots(df, "Time Elapsed",
                    filename_plot="turbostat_time_elapsed", 
                    x_data="version", 
                    y_data="time_elapsed", 
                    color_data="path",
                    type="bar")

    div_html = time_elapsed
    
    return div_html

def html_EnergyPlots(df):
    
    pkg = two_plots(df, "Package Energy Consumption",
                    filename_plot="turbostat_Pkg_J", 
                    x_data="version", 
                    y_data="Pkg_J", 
                    color_data="path",
                    type="bar")
    RAM = two_plots(df, "RAM Energy Consumption",
                    filename_plot="turbostat_RAM_J", 
                    x_data="version", 
                    y_data="RAM_J", 
                    color_data="path",
                    type="bar")
    Cor = two_plots(df, "Core Energy Consumption",
                    filename_plot="turbostat_Cor_J", 
                    x_data="version", 
                    y_data="Cor_J", 
                    color_data="path",
                    type="bar")
    GFX = two_plots(df, "GFX Energy Consumption",
                    filename_plot="turbostat_GFX_J", 
                    x_data="version", 
                    y_data="GFX_J", 
                    color_data="path",
                    type="bar")

    div_html = pkg + RAM + Cor + GFX
    
    return div_html

def html_MemoryPlots(df_turbo, df_top):

    mem_usage = two_plots(df_top, "Mean of Percentage of Memory usage",
                         filename_plot="top_percent_mem", 
                         x_data="version", 
                         y_data="percent_mem", 
                         color_data="path",
                         type="lineTop")
    
    virt_Box = one_plot(df_top, "Virtual Memory",
                         filename_plot="top_virt_box", 
                         x_data="version", 
                         y_data="virt", 
                         color_data="path",
                         type="box")
    
    virt_Bar = two_plots(df_top, "Mean of Virtual Memory",
                         filename_plot="top_virt", 
                         x_data="version", 
                         y_data="virt", 
                         color_data="path",
                         type="barTop")
    
    res_Box = one_plot(df_top, "Resident Memory",
                         filename_plot="top_res_box", 
                         x_data="version", 
                         y_data="res", 
                         color_data="path",
                         type="box")
    
    res_Bar = two_plots(df_top, "Mean of Resident Memory",
                         filename_plot="top_res", 
                         x_data="version", 
                         y_data="res", 
                         color_data="path",
                         type="barTop")
    
    shr_Box = one_plot(df_top, "Shared Memory",
                         filename_plot="top_shr_box", 
                         x_data="version", 
                         y_data="shr", 
                         color_data="path",
                         type="box")
    
    shr_Bar = two_plots(df_top, "Mean of Shared Memory",
                         filename_plot="top_shr", 
                         x_data="version", 
                         y_data="shr", 
                         color_data="path",
                         type="barTop")
    
    code_Box = one_plot(df_top, "Code Memory",
                         filename_plot="top_shr_box", 
                         x_data="version", 
                         y_data="CODE", 
                         color_data="path",
                         type="box")
    
    code_Bar = two_plots(df_top, "Mean of Code Memory",
                         filename_plot="top_shr", 
                         x_data="version", 
                         y_data="CODE", 
                         color_data="path",
                         type="barTop")
    
    data_Box = one_plot(df_top, "DATA Memory",
                         filename_plot="top_shr_box", 
                         x_data="version", 
                         y_data="DATA", 
                         color_data="path",
                         type="box")
    
    data_Bar = two_plots(df_top, "Mean of DATA Memory",
                         filename_plot="top_shr", 
                         x_data="version", 
                         y_data="DATA", 
                         color_data="path",
                         type="barTop")


    div_html = mem_usage + virt_Box + virt_Bar + res_Box + res_Bar + shr_Box + shr_Bar + code_Box + code_Bar + data_Box + data_Bar
    
    return div_html

def html_CPUPlots(df_turbo, df_top):

    cpu_usage = two_plots(df_top, "Mean of Percentage of CPU usage",
                         filename_plot="top_percent_cpu", 
                         x_data="version", 
                         y_data="percent_cpu", 
                         color_data="path",
                         type="lineTop")
    
    Avg_MHz = two_plots(df_turbo, "Average Frequency (MHz)",
                        filename_plot="turbostat_Avg_MHz", 
                        x_data="version", 
                        y_data="Avg_MHz", 
                        color_data="path",
                        type="line")
    
    Totl_C0 = two_plots(df_turbo, "Total Percent in C0 state (active)",
                        filename_plot="turbostat_Totl_C0", 
                        x_data="version", 
                        y_data="Totl%C0", 
                        color_data="path",
                        type="line")
    
    # Busy%, Bzy_MHz (C0 state), IPC, IRQ, POLL (CPU)
    
    nTH = two_plots(df_top, "Number of threads",
                        filename_plot="turbostat_noThreads", 
                        x_data="version", 
                        y_data="nTH", 
                        color_data="path",
                        type="lineTop")

    div_html = cpu_usage + Avg_MHz + Totl_C0
    
    return div_html

def html_Cstates(df):

    C1 = two_plots(df, "Linux requested the C1 idle state",
                    filename_plot="turbostat_C1", 
                    x_data="version", 
                    y_data="C1", 
                    color_data="path",
                    type="line")
    
    C1E = two_plots(df, "Linux requested the C1E idle state",
                    filename_plot="turbostat_C1E", 
                    x_data="version", 
                    y_data="C1E", 
                    color_data="path",
                    type="line")

    C3 = two_plots(df, "Linux requested the C3 idle state",
                    filename_plot="turbostat_C3", 
                    x_data="version", 
                    y_data="C3", 
                    color_data="path",
                    type="line")
    
    C6 = two_plots(df, "Linux requested the C6 idle state",
                    filename_plot="turbostat_C6", 
                    x_data="version", 
                    y_data="C6", 
                    color_data="path",
                    type="line")
    
    C7s = two_plots(df, "Linux requested the C7s idle state",
                    filename_plot="turbostat_C7s", 
                    x_data="version", 
                    y_data="C7s", 
                    color_data="path",
                    type="line")
    
    C8 = two_plots(df, "Linux requested the C8 idle state",
                    filename_plot="turbostat_C8", 
                    x_data="version", 
                    y_data="C8", 
                    color_data="path",
                    type="line")
    
    C9 = two_plots(df, "Linux requested the C9 idle state",
                    filename_plot="turbostat_C9", 
                    x_data="version", 
                    y_data="C9", 
                    color_data="path",
                    type="line")
    
    C10 = two_plots(df, "Linux requested the C10 idle state",
                    filename_plot="turbostat_C10", 
                    x_data="version", 
                    y_data="C10", 
                    color_data="path",
                    type="line")
    
    C1_percent = two_plots(df, "Linux requested the C1% idle state",
                    filename_plot="turbostat_C1_percent", 
                    x_data="version", 
                    y_data="C1%", 
                    color_data="path",
                    type="line")
    
    C1E_percent = two_plots(df, "Linux requested the C1E% idle state",
                    filename_plot="turbostat_C1E_percent", 
                    x_data="version", 
                    y_data="C1E%", 
                    color_data="path",
                    type="line")

    C3_percent = two_plots(df, "Linux requested the C3% idle state",
                    filename_plot="turbostat_C3_percent", 
                    x_data="version", 
                    y_data="C3%", 
                    color_data="path",
                    type="line")
    
    C6_percent = two_plots(df, "Linux requested the C6% idle state",
                    filename_plot="turbostat_C6_percent", 
                    x_data="version", 
                    y_data="C6%", 
                    color_data="path",
                    type="line")
    
    C7s_percent = two_plots(df, "Linux requested the C7s% idle state",
                    filename_plot="turbostat_C7s_percent", 
                    x_data="version", 
                    y_data="C7s%", 
                    color_data="path",
                    type="line")
    
    C8_percent = two_plots(df, "Linux requested the C8% idle state",
                    filename_plot="turbostat_C8_percent", 
                    x_data="version", 
                    y_data="C8%", 
                    color_data="path",
                    type="line")
    
    C9_percent = two_plots(df, "Linux requested the C9% idle state",
                    filename_plot="turbostat_C9_percent", 
                    x_data="version", 
                    y_data="C9%", 
                    color_data="path",
                    type="line")
    
    C10_percent = two_plots(df, "Linux requested the C10% idle state",
                    filename_plot="turbostat_C10_percent", 
                    x_data="version", 
                    y_data="C10%", 
                    color_data="path",
                    type="line")

    div_html = C1 + C1_percent + C1E + C1E_percent + C3 + C3_percent + C6 + C6_percent + C7s + C7s_percent + C8 + C8_percent + C9 + C9_percent + C10 + C10_percent

    return div_html

def html_Temperature(df):

    CoreTmp = two_plots(df, "Degrees Celsius reported by the per-core Digital Thermal Sensor",
                         filename_plot="top_CoreTmp", 
                         x_data="version", 
                         y_data="CoreTmp", 
                         color_data="path",
                         type="line")
    
    PkgTmp = two_plots(df, "Degrees Celsius reported by the per-package Package Thermal Monitor",
                        filename_plot="turbostat_PkgTmp", 
                        x_data="version", 
                        y_data="PkgTmp", 
                        color_data="path",
                        type="line")

    div_html = CoreTmp + PkgTmp
    
    return div_html

def html_PageFaults(df_top, df_perf):

    page_faults = two_plots(df_perf, "Page Faults",
                         filename_plot="top_page_faults", 
                         x_data="version", 
                         y_data="page_faults", 
                         color_data="path",
                         type="line")
    
    minor_faults = two_plots(df_perf, "Minor Faults",
                         filename_plot="top_minor_faults", 
                         x_data="version", 
                         y_data="minor_faults", 
                         color_data="path",
                         type="line")

    # nMaj (memory), nMin (memory)
    nMaj = two_plots(df_top, "Major Page Fault Count",
                         filename_plot="top_nMaj", 
                         x_data="version", 
                         y_data="nMaj", 
                         color_data="path",
                         type="lineTop")
    
    nMin = two_plots(df_top, "Minor Page Fault Count",
                         filename_plot="top_nMin", 
                         x_data="version", 
                         y_data="nMin", 
                         color_data="path",
                         type="lineTop")

    div_html = page_faults + minor_faults + nMaj + nMin
    
    return div_html

def html_Information(title, parameter, color):

    df_turbostat = from_CSVfiles("turbostat", norm=False)
    df_top = from_CSVfiles("top", norm=False)
    df_perf = from_CSVfiles("perf", norm=False)

    if parameter == "general":
        div_Information = html_EnergyPlots(df_turbostat)
    elif parameter == "energy":
        div_Information = html_EnergyPlots(df_turbostat)
    elif parameter == "memory":
        div_Information = html_MemoryPlots(df_turbostat, df_top)
    elif parameter == "time":
        div_Information = html_TimePlots(df_turbostat)
    elif parameter == "cpu":
        div_Information = html_CPUPlots(df_turbostat, df_top)
    elif parameter == "temperature":
        div_Information = html_Temperature(df_turbostat)
    elif parameter == "cstates":
        div_Information = html_Cstates(df_turbostat)
    elif parameter == "pageFaults":
        div_Information = html_PageFaults(df_top, df_perf)

    # perf
    # freq_cycles_GHz, cpu_clock_msec, no_cpus, cpu_cycles, cpu_migrations, ref_cycles (CPU)

    # turbostat
    # Avg_MHz, Busy%, Bzy_MHz (C0 state), IPC, IRQ, POLL (CPU)

    # GFX%rc6	GFXMHz	GFXAMHz	Totl%C0	Any%C0	GFX%C0	CPUGFX%


    div_string = '''
            <details>
                <summary style="background-color: ''' + color + ''';">''' + title + '''</summary>
                ''' + div_Information + '''
            </details>
    '''
    return div_string


if __name__ == '__main__':

    div_general = html_Information("General Information", "general", "#B3B6B7")
    div_energy = html_Information("Energy Consumption", "energy", "#28B463")
    div_memory = html_Information("Memory Consumption", "memory", "#3498DB")
    div_time = html_Information("Time Elapsed", "time", "#F39C12")
    div_cpu = html_Information("CPU usage", "cpu", "#F1C40F")
    div_temp = html_Information("Temperature", "temperature", "#9B59B6")
    div_cstates = html_Information("Cstates", "cstates", "#F7DC6F")
    div_pageFaults = html_Information("Page Faults", "pageFaults", "#5DADE2")

    print("Creating the general report for " + language + "...")
    
    html_string = '''
    <html>
        <head>
            <title>Analysis of ''' + language + '''</title>
            <link rel="shortcut icon" type="x-icon" href="''' + "../aalto.ico" + '''"> </link>
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
            <h1>Programmming Language is  <b>''' + language + '''</b> </h1>
            ''' + div_general + '''
            ''' + div_energy + '''
            ''' + div_time + '''
            ''' + div_memory + '''
            ''' + div_cpu + '''
            ''' + div_cstates + '''
            ''' + div_temp + '''
            ''' + div_pageFaults + '''
        </body>
    </html>'''

    f = open(html_filename + '.html','w')
    f.write(html_string)
    f.close()