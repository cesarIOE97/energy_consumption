# Libraries
import re
import sys
import os
import glob
import webbrowser
import natsort
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from sklearn.preprocessing import MaxAbsScaler
from IPython.display import display, HTML
from plots_general import *

# Arguments
# 
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
    '1.8.0_382': '2023-07-18',
    '9.0.4': '2018-01-16',
    '10.0.2': '2018-07-17',
    '11.0.19': '2020-10-20',
    '11.0.20': '2023-07-18',
    '11.0.20.1': '2023-08-22',
    '12.0.2': '2019-07-16',
    '13.0.2': '2020-01-14',
    '14.0.2': '2020-07-14',
    '15.0.2': '2021-01-19',
    '16.0.2': '2021-07-20',
    '17.0.7': '2023-04-18',
    '17.0.8': '2023-07-18',
    '17.0.8.1': '2023-08-22',
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

# Define a function to remove units from a string
def remove_units(cell_value):
    # Use regular expressions to remove units
    cell_value = re.sub(r'[A-Za-z]+', '', str(cell_value))
    return cell_value
    
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
        if directory_name != "waiting" and directory_name != "older" and directory_name != "test" and directory_name != "general_plots" and directory_name != "general_plots_v1" and directory_name != "mainPrograms_plots":
            
            path=language + '/' + directory_name + '/' + tool + '/'
            
            if tool == "top":

                df = pd.DataFrame()
                list_files = os.listdir(path)

                # Get list of all files only in the given directory
                list_files = natsort.natsorted(list_files)

                for file_name in list_files:
                    if file_name.startswith("temp_top_data_") and file_name.endswith('.csv'):
                        df_Top = from_CSVfile(path + file_name, directory_name, tool)
                        df = pd.concat([df, df_Top])

                # Split the your_column into minutes, seconds, and hundredths
                df[['minutes', 'seconds_hundredths']] = df['time'].str.split(':', expand=True)

                # Convert minutes, seconds, and hundredths to seconds
                df['time'] = pd.to_numeric(df['minutes']) * 60 + pd.to_numeric(df['seconds_hundredths'])

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
                df['Pkg+RAM_J'] = df['Pkg_J'] + df['RAM_J']
                df['Pkg_Watt'] = df['Pkg_J'] / df['time_elapsed']
                df['RAM_Watt'] = df['RAM_J'] / df['time_elapsed']
                df['Pkg+RAM_Watts'] = df['Pkg_Watt'] + df['RAM_Watt']
            elif tool == "perf": 
                # path = path + tool
                df = pd.DataFrame()
                list_files = os.listdir(path)

                # Get list of all files only in the given directory
                list_files = natsort.natsorted(list_files)
            
                for file_name in list_files:
                    if file_name.startswith("perf_performance_data") and file_name.endswith('.csv'):
                        df_Perf= from_CSVfile(path + file_name, directory_name, tool)
                        df = pd.concat([df, df_Perf])

                # Extract the units contained in the every measurement, for instance, the column 'time_elapsed'
                # contains values in msec; so this convert into secs and remove the unit "msec" to add it in the header
                parameters = ["time_elapsed","freq_cycles","cpu_clock","freq_cpu_cycles","task_clock","cpu_thermal_margin"]

                for parameter in parameters:
                    colname = df[parameter].str.extract(r'\s(.+)$').iloc[0, 0]
                    if parameter == "time_elapsed":
                        df[parameter] = df[parameter].str.replace(colname, '').astype(int)
                        df['time_elapsed'] = df['time_elapsed'] / 1000000000
                        df.rename(columns={parameter: f'{parameter}_sec'}, inplace=True)
                    else:
                        df[parameter] = df[parameter].str.replace(colname, '').astype(float)
                        df.rename(columns={parameter: f'{parameter}_{colname}'}, inplace=True)
                df = df.rename(columns={"IPC": "IPC_perf"})

                df.to_csv(path + "perf_data_allVersions_10times.csv", index=False)
            else:
                # df = from_CSVfile(path + '_data_allVersions.csv', directory_name, tool)
                # if norm: df = Data_normalized(df, tool)
                print("Error selecting the tool. Please check an appropriate too.")
            all_df = pd.concat([all_df, df])

    return all_df

# CREATING A GENERAL DF WITH ALL IMPORTANT PARAMETERS
def general_df(df_turbostat, df_perf, df_top):
    df1 = df_turbostat.groupby(["path","version","release_date"], sort=False)[['time_elapsed',
                        'Pkg_J','Cor_J','RAM_J','GFX_J', 'Avg_MHz', 'Busy%', 'IPC', 'IRQ', 'POLL', 'C1%','C1E%','C3%','C6%','C7s%','C8%',
                        'C9%','C10%','CPU%c1','CPU%c3','CPU%c6','CPU%c7','CoreTmp','PkgTmp','GFX%rc6','Totl%C0','Any%C0','GFX%C0','CPUGFX%']].median().reset_index()
    df2 = df_perf.groupby(["path","version","release_date"], sort=False)[['time_elapsed_sec','CPU_Utilization','Retiring','Frontend_Bound','Bad_Speculation','Backend_Bound',
                            'CPI','ILP','IPC_perf','cycles','freq_cycles_GHz','instructions',
                            'Kernel_Utilization', 'L1D_Cache_Fill_BW', 'Turbo_Utilization', 'cycles',
                            'instructions', 'insn_per_cycle', 'cpu_clock_msec', 'no_cpus', 'cpu_cycles', 'freq_cpu_cycles_GHz',
                            'cpu_migrations','ref_cycles','bus_cycles','task_clock_msec','no_cpus_task_clock',
                            'cpu_thermal_margin_C','branches','branch_misses','mem_loads','mem_stores','page_faults','minor_faults','major_faults',
                            'cache_references','cache_misses','percent_cache_misses','L1_dcache_loads','L1_dcache_load_misses',
                            'LLC_loads','LLC_load_misses','L1_icache_load_misses','dTLB_loads',
                            'dTLB_load_misses','iTLB_loads','iTLB_load_misses']].median().reset_index()
    df3 = df_top.groupby(["path","version","release_date"], sort=False)[['time','virt','res','shr','percent_cpu','percent_mem','nTH','P',
                        'SWAP','CODE','DATA','nMaj','nDRT','USED']].median().reset_index()

    df_merged = pd.merge(df1, df2, on=["path","version","release_date"], how='left')
    df = pd.merge(df_merged, df3, on=["path","version","release_date"], how='left')


    path=language + '/'
    df.to_csv(path + "dataframe_General_medianValues.csv", index=False)

    return df



def html_generalPlots(df_turbostat, df_top, df_perf, df):
    
      
    scatterplot_matrix = two_plotsMatrix(language, df_turbostat, "Scatterplot Matrix",
                                  filename_plot="turbostat_scatterplot_matrix", 
                                  type="scattermatrixTurbo")
    
    scatterplot_Program = two_plotsMatrix(language, df_turbostat, "Scatterplot per Program (Energy vs Time elapsed)",
                                  filename_plot="turbostat_scatterplot_perProgram", 
                                  type="scatterTurbo_program")
    
    scatterplot = two_plotsMatrix(language, df_turbostat, "Scatterplot per Version(Energy vs Time elapsed)",
                                  filename_plot="turbostat_scatterplot_perVersion", 
                                  type="scatterTurbo_version")
    
    energy = two_plots(language, df_turbostat, "Energy Consumption (Pkg + RAM)",
                    filename_plot="turbostat_Pkg+RAM_J", 
                    x_data="version", 
                    y_data="Pkg+RAM_J", 
                    color_data="path",
                    type="lineTurbo")

    div_html = energy + scatterplot_matrix + scatterplot_Program + scatterplot
    
    return div_html

def html_matrixPlots(df_turbostat, df_top, df_perf, df):

    corr_gral = two_plotsMatrix(language, df, "General Correlation (median values for each version and application)",
                              filename_plot="general_correlation_MedianValues", 
                              type="corrGeneral")

    corr_turbostat = two_plotsMatrix(language, df_turbostat, "Correlation (Turbostat tool)",
                              filename_plot="turbostat_correlation_General", 
                              type="corrTurbo")
    
    corr_perf = two_plotsMatrix(language, df_perf, "Correlation (Perf tool)",
                              filename_plot="perf_correlation_General", 
                              type="corrPerf")
    
    corr_top = two_plotsMatrix(language, df_top, "Correlation (Top tool)",
                              filename_plot="top_correlation_General", 
                              type="corrTop")
    
    div_html = corr_gral + corr_turbostat + corr_perf + corr_top

    return div_html

def html_matrixAnalysis(df_turbostat, df_top, df_perf, df):

    # Per versions
    if language == "python":
        text1 = "ONLY Versions 3.11.3, 3.12.0b1, and 3.13.0a.0"
        text2 = "WITHOUT Versions 3.11.3, 3.12.0b1, and 3.13.0a.0"
        filter_1 = 'version == "3.11.3" or version == "3.12.0b1" or version == "3.13.0a0"'
        filter_2 = 'version != "3.11.3" and version != "3.12.0b1" and version != "3.13.0a0"'
    elif language == "c++":
        text1 = "Binary Trees Version 2 of B using -O3"
        text2 = "Binary Trees Version 6 of B using -O3"
        filter_1 = 'path == "binaryTrees_v2_21_original_O3flag"'
        filter_2 = 'path == "binaryTrees_v6_21_original_O3flag"'
    elif language == 'java':
        text1 = "ONLY Versions 1.8.0_382, 9.0.4, and 10.0.2"
        text2 = "WITHOUT Versions 1.8.0_382, 9.0.4, and 10.0.2"
        filter_1 = 'version == "1.8.0_382" or version == "9.0.4" or version == "10.0.2"'
        filter_2 = 'version != "1.8.0_382" and version != "9.0.4" and version != "10.0.2"'
    elif language == 'js':
        text1 = "ONLY Versions 6.17.1 and 7.10.1 in the Nbody program"
        text2 = "WITHOUT Versions 6.17.1 and 7.10.1 in the Nbody program"
        filter_1 = 'path == "nbody_50000000_original" and (version == "6.17.1" or version == "7.10.1")'
        filter_2 = 'path == "nbody_50000000_original" and (version != "6.17.1" and version != "7.10.1")'

    df_filtered_1 = df.query(filter_1)
    df_filtered_2 = df.query(filter_2)

    df_turbostat_filtered_1 = df_turbostat.query(filter_1)
    df_turbostat_filtered_2 = df_turbostat.query(filter_2)

    df_top_filtered_1 = df_top.query(filter_1)
    df_top_filtered_2 = df_top.query(filter_2)

    df_perf_filtered_1 = df_perf.query(filter_1)
    df_perf_filtered_2 = df_perf.query(filter_2)

    div_html = ""

    
    div_html = div_html + two_plotsMatrix(language, df_filtered_1, "General Correlation (median values for each version and application) - " + text1,
                                     filename_plot="general_correlation_MedianValues_FilteredVersion1", 
                                     type="corrGeneral")
    
    div_html = div_html + two_plotsMatrix(language, df_filtered_2, "General Correlation (median values for each version and application) - " + text2,
                                     filename_plot="general_correlation_MedianValues_FilteredVersion2", 
                                     type="corrGeneral")

    div_html = div_html + two_plotsMatrix(language, df_turbostat_filtered_1, "Correlation (Turbostat tool) - " + text1,
                              filename_plot="turbostat_correlation_General_FilteredVersion1", 
                              type="corrTurbo")
    
    div_html = div_html + two_plotsMatrix(language, df_turbostat_filtered_2, "Correlation (Turbostat tool) - " + text2,
                              filename_plot="turbostat_correlation_General_FilteredVersion2", 
                              type="corrTurbo")
    
    div_html = div_html + two_plotsMatrix(language, df_perf_filtered_1, "Correlation (Perf tool) - " + text1,
                              filename_plot="perf_correlation_General_FilteredVersion1", 
                              type="corrPerf")
    
    div_html = div_html + two_plotsMatrix(language, df_perf_filtered_2, "Correlation (Perf tool) - " + text2,
                              filename_plot="perf_correlation_General_FilteredVersion2", 
                              type="corrPerf")
    
    div_html = div_html + two_plotsMatrix(language, df_top_filtered_1, "Correlation (Top tool) - " + text1,
                              filename_plot="top_correlation_General_FilteredVersion1", 
                              type="corrTop")
    
    div_html = div_html + two_plotsMatrix(language, df_top_filtered_2, "Correlation (Top tool) - " + text2,
                              filename_plot="top_correlation_General_FilteredVersion2", 
                              type="corrTop")
    
    # Per program
    return div_html

def html_TimePlots(df):
    
    time_elapsed = two_plots(language, df, "Time Elapsed",
                    filename_plot="turbostat_time_elapsed", 
                    x_data="version", 
                    y_data="time_elapsed", 
                    color_data="path",
                    type="lineTurbo")

    div_html = time_elapsed
    
    return div_html

def html_EnergyPlots(df):
    
    pkg = two_plots(language, df, "Package Energy Consumption",
                    filename_plot="turbostat_Pkg_J", 
                    x_data="version", 
                    y_data="Pkg_J", 
                    color_data="path",
                    type="lineTurbo")
    RAM = two_plots(language, df, "RAM Energy Consumption",
                    filename_plot="turbostat_RAM_J", 
                    x_data="version", 
                    y_data="RAM_J", 
                    color_data="path",
                    type="lineTurbo")
    Cor = two_plots(language, df, "Core Energy Consumption",
                    filename_plot="turbostat_Cor_J", 
                    x_data="version", 
                    y_data="Cor_J", 
                    color_data="path",
                    type="lineTurbo")
    GFX = two_plots(language, df, "GFX Energy Consumption",
                    filename_plot="turbostat_GFX_J", 
                    x_data="version", 
                    y_data="GFX_J", 
                    color_data="path",
                    type="lineTurbo")

    div_html = pkg + RAM + Cor + GFX
    
    return div_html

def html_MemoryPlots(df_turbo, df_top):

    mem_usage = two_plots(language, df_top, "Mean of Percentage of Memory usage",
                         filename_plot="top_percent_mem", 
                         x_data="version", 
                         y_data="percent_mem", 
                         color_data="path",
                         type="lineTop")
    
    virt_Box = one_plot(language, df_top, "Virtual Memory",
                         filename_plot="top_virt_box", 
                         x_data="version", 
                         y_data="virt", 
                         color_data="path",
                         type="box")
    
    virt_Bar = two_plots(language, df_top, "Mean of Virtual Memory",
                         filename_plot="top_virt", 
                         x_data="version", 
                         y_data="virt", 
                         color_data="path",
                         type="barTop")
    
    res_Box = one_plot(language, df_top, "Resident Memory",
                         filename_plot="top_res_box", 
                         x_data="version", 
                         y_data="res", 
                         color_data="path",
                         type="box")
    
    res_Bar = two_plots(language, df_top, "Mean of Resident Memory",
                         filename_plot="top_res", 
                         x_data="version", 
                         y_data="res", 
                         color_data="path",
                         type="barTop")
    
    shr_Box = one_plot(language, df_top, "Shared Memory",
                         filename_plot="top_shr_box", 
                         x_data="version", 
                         y_data="shr", 
                         color_data="path",
                         type="box")
    
    shr_Bar = two_plots(language, df_top, "Mean of Shared Memory",
                         filename_plot="top_shr", 
                         x_data="version", 
                         y_data="shr", 
                         color_data="path",
                         type="barTop")
    
    code_Box = one_plot(language, df_top, "Code Memory",
                         filename_plot="top_shr_box", 
                         x_data="version", 
                         y_data="CODE", 
                         color_data="path",
                         type="box")
    
    code_Bar = two_plots(language, df_top, "Mean of Code Memory",
                         filename_plot="top_shr", 
                         x_data="version", 
                         y_data="CODE", 
                         color_data="path",
                         type="barTop")
    
    data_Box = one_plot(language, df_top, "DATA Memory",
                         filename_plot="top_shr_box", 
                         x_data="version", 
                         y_data="DATA", 
                         color_data="path",
                         type="box")
    
    data_Bar = two_plots(language, df_top, "Mean of DATA Memory",
                         filename_plot="top_shr", 
                         x_data="version", 
                         y_data="DATA", 
                         color_data="path",
                         type="barTop")


    div_html = mem_usage + virt_Box + virt_Bar + res_Box + res_Bar + shr_Box + shr_Bar + code_Box + code_Bar + data_Box + data_Bar
    
    return div_html

def html_PerformancePlots(df_perf):
    frontend = two_plots(language, df_perf, "Mean of Percentage of Frontend_Bound",
                         filename_plot="perf_frontendBound", 
                         x_data="version", 
                         y_data="Frontend_Bound", 
                         color_data="path",
                         type="lineTop")
    backend = two_plots(language, df_perf, "Mean of Percentage of Backend_Bound",
                         filename_plot="perf_backendBound", 
                         x_data="version", 
                         y_data="Backend_Bound", 
                         color_data="path",
                         type="lineTop")
    badSpeculation = two_plots(language, df_perf, "Mean of Percentage of Bad Speculation",
                         filename_plot="perf_badSpeculation", 
                         x_data="version", 
                         y_data="Bad_Speculation", 
                         color_data="path",
                         type="lineTop")
    retiring = two_plots(language, df_perf, "Mean of Percentage of Retiring",
                         filename_plot="perf_retiring", 
                         x_data="version", 
                         y_data="Retiring", 
                         color_data="path",
                         type="lineTop")
    
    div_html = frontend + backend + badSpeculation + retiring
    
    return div_html

def html_ExtraParameters(df_turbostat, df_perf):
    IPC = two_plots(language, df_turbostat, "IPC (Instructions per Cycle/Clock) by TURBOSTAT",
                         filename_plot="turbostat_IPC", 
                         x_data="version", 
                         y_data="IPC", 
                         color_data="path",
                         type="lineTurbo")
    IRQ = two_plots(language, df_turbostat, "IRQ (Interrupt Request)",
                         filename_plot="turbostat_IRQ", 
                         x_data="version", 
                         y_data="IRQ", 
                         color_data="path",
                         type="lineTop")
    CPI = two_plots(language, df_perf, "CPI (Cycles per Instruction)",
                         filename_plot="perf_CPI", 
                         x_data="version", 
                         y_data="CPI", 
                         color_data="path",
                         type="lineTop")
    IPC_perf = two_plots(language, df_perf, "IPC (Instructions per Cycle/Clock) by PERF",
                         filename_plot="perf_IPC", 
                         x_data="version", 
                         y_data="IPC_perf", 
                         color_data="path",
                         type="lineTop")
    cycles = two_plots(language, df_perf, "Cycles by PERF",
                         filename_plot="perf_cycles", 
                         x_data="version", 
                         y_data="cycles", 
                         color_data="path",
                         type="lineTop")
    instructions = two_plots(language, df_perf, "Instructions by PERF",
                         filename_plot="perf_instructions", 
                         x_data="version", 
                         y_data="instructions", 
                         color_data="path",
                         type="lineTop")
    branches = two_plots(language, df_perf, "Branches by PERF",
                         filename_plot="perf_branches", 
                         x_data="version", 
                         y_data="branches", 
                         color_data="path",
                         type="lineTop")
    branch_misses = two_plots(language, df_perf, "Branches Misses by PERF",
                         filename_plot="perf_branch_misses", 
                         x_data="version", 
                         y_data="branch_misses", 
                         color_data="path",
                         type="lineTop")
    
    div_html = IPC + IRQ + CPI + IPC_perf + cycles + instructions + branches + branch_misses
    
    return div_html
    

def html_PerformanceEachOnePlots(df_perf):

    x_data = "version"
    categories = ["Retiring","Bad_Speculation","Frontend_Bound","Backend_Bound"]
    programs = df_perf["path"].unique()
    div_html = ''
    flag = True

    for program in programs:
        df = df_perf.groupby([x_data,"path"], sort=False)[categories].median().reset_index()
        # df = df[df['version'].str.contains("2.5.6|2.7.18|3.0.1|3.4.10|3.5.10") == False]
        df = df.query('path == "'+ program +'"')
        df = df.drop('path', axis=1)
        
        df_IPC = df_perf.groupby([x_data,"path"], sort=False)['IPC_perf'].median().reset_index()
        df_IPC = df_IPC.query('path == "'+ program +'"')
        df_IPC = df_IPC.drop('path', axis=1)
        
        # if language == "python": color_list = ["DodgerBlue", "DeepSkyBlue", "OrangeRed", "Salmon", "MediumSeaGreen", "LightGreen", "SlateBlue", "Plum", "Gray", "LightGray"]
        # if language == "c++": color_list = ["DodgerBlue", "DeepSkyBlue", "OrangeRed", "Salmon", "MediumSeaGreen", "LightGreen", "SlateBlue", "Plum", "Gray", "LightGray"]

        color_list = ["MediumSeaGreen", "OrangeRed", "SlateBlue", "DodgerBlue"]

        df_melted = pd.melt(df, id_vars=['version'], var_name='Perf_parameters', value_name='Value')
        df_melted_2 = pd.melt(df_IPC, id_vars=['version'], var_name='IPC_perf', value_name='Value')
        
        fig = px.bar(df_melted,
                x = "version",
                y = "Value",
                color = "Perf_parameters",
                color_discrete_sequence=color_list,
                title="Performance of " + program + " in " + language)
        
        fig.add_trace(
            go.Scatter(
                x=df_melted_2["version"],
                y=df_melted_2["Value"],
                mode="lines",
                yaxis="y2",
                marker=dict(color="black"),
                name="IPC"
            )
        )

        fig.update_layout(
            legend=dict(orientation="h"),
            yaxis=dict(
                title=dict(text="Top-Level"),
                side="left",
                range=[0, 1],
            ),
            yaxis2=dict(
                title=dict(text="Instuctions per Cycle"),
                side="right",
                range=[0, 4],
                overlaying="y",
                tickmode="sync",
            ),
        )

        # Check if the directory exists
        directory = language + '/general_plots/'
        if not os.path.exists(directory):
            # If it doesn't exist, create it
            os.makedirs(directory)

        filename_plot_wDir = directory + program + "_performanceTopAnalysis"
        plot = plotly.offline.plot(fig, filename= filename_plot_wDir + '.html', auto_open=False)
        fig = 'general_plots/' + program + "_performanceTopAnalysis" + ".html"

        if flag:
                div_html = div_html + '''
                <div class="row">
        '''

        div_string = '''
                    <div class="column">
                            <h3>Section:  ''' + "Performance of " + program + '''</h3>
                            <iframe class="plot" frameborder="0" seamless="seamless" scrolling="no" \
                                src="''' + fig + '''"></iframe>
                            <p>Notes: </p>
                    </div>
        '''
        div_html = div_html + div_string
        if not flag:
            div_html = div_html + '''
                </div>
            ''' 
            flag = True
        else:
            flag = False
    
    if not flag:
        div_html = div_html + '''
                </div>
            ''' 
    return div_html
                         
    


def html_CPUPlots(df_turbo, df_top):

    cpu_usage = two_plots(language, df_top, "Mean of Percentage of CPU usage",
                         filename_plot="top_percent_cpu", 
                         x_data="version", 
                         y_data="percent_cpu", 
                         color_data="path",
                         type="lineTop")
    
    Avg_MHz = two_plots(language, df_turbo, "Average Frequency (MHz)",
                        filename_plot="turbostat_Avg_MHz", 
                        x_data="version", 
                        y_data="Avg_MHz", 
                        color_data="path",
                        type="lineTurbo")
    
    Totl_C0 = two_plots(language, df_turbo, "Total Percent in C0 state (active)",
                        filename_plot="turbostat_Totl_C0", 
                        x_data="version", 
                        y_data="Totl%C0", 
                        color_data="path",
                        type="lineTurbo")
    
    # Busy%, Bzy_MHz (C0 state), IPC, IRQ, POLL (CPU)
    
    nTH = two_plots(language, df_top, "Number of threads",
                        filename_plot="turbostat_noThreads", 
                        x_data="version", 
                        y_data="nTH", 
                        color_data="path",
                        type="lineTop")

    div_html = cpu_usage + Avg_MHz + Totl_C0
    
    return div_html

def html_Cstates(df):

    C1 = two_plots(language, df, "Linux requested the C1 idle state",
                    filename_plot="turbostat_C1", 
                    x_data="version", 
                    y_data="C1", 
                    color_data="path",
                    type="lineTurbo")
    
    C1E = two_plots(language, df, "Linux requested the C1E idle state",
                    filename_plot="turbostat_C1E", 
                    x_data="version", 
                    y_data="C1E", 
                    color_data="path",
                    type="lineTurbo")

    C3 = two_plots(language, df, "Linux requested the C3 idle state",
                    filename_plot="turbostat_C3", 
                    x_data="version", 
                    y_data="C3", 
                    color_data="path",
                    type="lineTurbo")
    
    C6 = two_plots(language, df, "Linux requested the C6 idle state",
                    filename_plot="turbostat_C6", 
                    x_data="version", 
                    y_data="C6", 
                    color_data="path",
                    type="lineTurbo")
    
    C7s = two_plots(language, df, "Linux requested the C7s idle state",
                    filename_plot="turbostat_C7s", 
                    x_data="version", 
                    y_data="C7s", 
                    color_data="path",
                    type="lineTurbo")
    
    C8 = two_plots(language, df, "Linux requested the C8 idle state",
                    filename_plot="turbostat_C8", 
                    x_data="version", 
                    y_data="C8", 
                    color_data="path",
                    type="lineTurbo")
    
    C9 = two_plots(language, df, "Linux requested the C9 idle state",
                    filename_plot="turbostat_C9", 
                    x_data="version", 
                    y_data="C9", 
                    color_data="path",
                    type="lineTurbo")
    
    C10 = two_plots(language, df, "Linux requested the C10 idle state",
                    filename_plot="turbostat_C10", 
                    x_data="version", 
                    y_data="C10", 
                    color_data="path",
                    type="lineTurbo")
    
    C1_percent = two_plots(language, df, "Linux requested the C1% idle state",
                    filename_plot="turbostat_C1_percent", 
                    x_data="version", 
                    y_data="C1%", 
                    color_data="path",
                    type="lineTurbo")
    
    C1E_percent = two_plots(language, df, "Linux requested the C1E% idle state",
                    filename_plot="turbostat_C1E_percent", 
                    x_data="version", 
                    y_data="C1E%", 
                    color_data="path",
                    type="lineTurbo")

    C3_percent = two_plots(language, df, "Linux requested the C3% idle state",
                    filename_plot="turbostat_C3_percent", 
                    x_data="version", 
                    y_data="C3%", 
                    color_data="path",
                    type="lineTurbo")
    
    C6_percent = two_plots(language, df, "Linux requested the C6% idle state",
                    filename_plot="turbostat_C6_percent", 
                    x_data="version", 
                    y_data="C6%", 
                    color_data="path",
                    type="lineTurbo")
    
    C7s_percent = two_plots(language, df, "Linux requested the C7s% idle state",
                    filename_plot="turbostat_C7s_percent", 
                    x_data="version", 
                    y_data="C7s%", 
                    color_data="path",
                    type="lineTurbo")
    
    C8_percent = two_plots(language, df, "Linux requested the C8% idle state",
                    filename_plot="turbostat_C8_percent", 
                    x_data="version", 
                    y_data="C8%", 
                    color_data="path",
                    type="lineTurbo")
    
    C9_percent = two_plots(language, df, "Linux requested the C9% idle state",
                    filename_plot="turbostat_C9_percent", 
                    x_data="version", 
                    y_data="C9%", 
                    color_data="path",
                    type="lineTurbo")
    
    C10_percent = two_plots(language, df, "Linux requested the C10% idle state",
                    filename_plot="turbostat_C10_percent", 
                    x_data="version", 
                    y_data="C10%", 
                    color_data="path",
                    type="lineTurbo")

    # div_html = C1 + C1_percent + C1E + C1E_percent + C3 + C3_percent + C6 + C6_percent + C7s + C7s_percent + C8 + C8_percent + C9 + C9_percent + C10 + C10_percent
    div_html = C1_percent + C1E_percent + C3_percent + C6_percent + C7s_percent + C8_percent + C9_percent + C10_percent

    return div_html

def html_Temperature(df):

    CoreTmp = two_plots(language, df, "Degrees Celsius reported by the per-core Digital Thermal Sensor",
                         filename_plot="top_CoreTmp", 
                         x_data="version", 
                         y_data="CoreTmp", 
                         color_data="path",
                         type="lineTurbo")
    
    PkgTmp = two_plots(language, df, "Degrees Celsius reported by the per-package Package Thermal Monitor",
                        filename_plot="turbostat_PkgTmp", 
                        x_data="version", 
                        y_data="PkgTmp", 
                        color_data="path",
                        type="lineTurbo")

    div_html = CoreTmp + PkgTmp
    
    return div_html

def html_PageFaults(df_top, df_perf):

    page_faults = two_plots(language, df_perf, "Page Faults",
                         filename_plot="top_page_faults", 
                         x_data="version", 
                         y_data="page_faults", 
                         color_data="path",
                         type="line")
    
    minor_faults = two_plots(language, df_perf, "Minor Faults",
                         filename_plot="top_minor_faults", 
                         x_data="version", 
                         y_data="minor_faults", 
                         color_data="path",
                         type="line")

    # nMaj (memory), nMin (memory)
    nMaj = two_plots(language, df_top, "Major Page Fault Count",
                         filename_plot="top_nMaj", 
                         x_data="version", 
                         y_data="nMaj", 
                         color_data="path",
                         type="lineTop")
    
    nMin = two_plots(language, df_top, "Minor Page Fault Count",
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

    df = general_df(df_turbostat, df_perf, df_top)

    if parameter == "general":
        div_Information = html_generalPlots(df_turbostat, df_top, df_perf, df)
    elif parameter == "matrix":
        div_Information = html_matrixPlots(df_turbostat, df_top, df_perf, df)
    elif parameter == "matrixAnalysis":
        div_Information = html_matrixAnalysis(df_turbostat, df_top, df_perf, df)
    elif parameter == "energy":
        div_Information = html_EnergyPlots(df_turbostat)
    elif parameter == "memory":
        div_Information = html_MemoryPlots(df_turbostat, df_top)
    elif parameter == "time":
        div_Information = html_TimePlots(df_turbostat)
    elif parameter == "extra_param":
        div_Information = html_ExtraParameters(df_turbostat, df_perf)
    elif parameter == "performance":
        div_Information = html_PerformancePlots(df_perf)
    elif parameter == "performance_top":
        div_Information = html_PerformanceEachOnePlots(df_perf)
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
    div_matrix = html_Information("Matrix Correlation for each tool", "matrix","#B3B6B7")
    div_matrxiAnalysis = html_Information("Matrix Correlation (Analysis according to the cases)", "matrixAnalysis","#B3B6B7")
    div_energy = html_Information("Energy Consumption", "energy", "#28B463")
    div_memory = html_Information("Memory Consumption", "memory", "#3498DB")
    div_extraParam = html_Information("Extra Parameters", "extra_param", "#E74C3C")
    div_time = html_Information("Time Elapsed", "time", "#F39C12")
    div_performance = html_Information("Performance", "performance", "#F1C40F")
    div_performance_Top = html_Information("Performance Top-Analysis", "performance_top", "#F1C40F")
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
            ''' + div_matrix + '''
            ''' + div_matrxiAnalysis + '''
            ''' + div_energy + '''
            ''' + div_time + '''
            ''' + div_memory + '''
            ''' + div_extraParam + '''
            ''' + div_cpu + '''
            ''' + div_performance + '''
            ''' + div_performance_Top + '''
            ''' + div_temp + '''
            ''' + div_pageFaults + '''
            ''' + div_cstates + '''
        </body>
    </html>'''

    f = open(html_filename + '.html','w')
    f.write(html_string)
    f.close()