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
from plots_mainPrograms import *

# FORMAT TO THE PLOTS
# fig.update_layout(
#     title="Plot Title",
#     xaxis_title="X Axis Title",
#     yaxis_title="Y Axis Title",
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="RebeccaPurple"
#     )
# )

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

def plot_Compare(language, df, filename_plot, x_data, y_data, color_data, type, diff_flag):

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
        program_df['Percentage_Difference'] = round(program_df[y_data].pct_change()*100,2)
        # program_df['Percentage_DifferenceFromMean'] = program_df.apply(lambda row: 0 if (mean == 0) else 100 * (row["DifferenceFromMean"] / mean), axis=1)
        if diff_flag:
            hover_texts = [custom_hover_median(program, x, median, diff, percent_diff) for x, diff, percent_diff in zip(program_df[x_data],program_df['Difference'],program_df['Percentage_Difference'])]
            bar_trace = go.Bar(x=program_df[x_data], y=program_df['Percentage_Difference'],
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
                       yaxis=dict(title='(%) Difference from Mean of ' + y_data, zeroline=False))
        

    fig = go.Figure(data=bar_traces, layout=layout)
    if language == 'js': fig.update_xaxes(categoryorder='array', categoryarray= ['0.8.28', '0.10.48', '0.12.18', '1.8.4', '2.5.0', '3.3.1', '4.9.1', '5.12.0', '6.17.1', '7.10.1', '8.17.0', '9.11.2', '10.24.1', '11.15.0', '12.22.12', '13.14.0', '14.21.3', '15.14.0', '16.20.2', '17.9.1', '18.17.1', '19.9.0', '20.5.1'])
    if language == 'python': fig.update_xaxes(categoryorder='array', categoryarray= ['2.5.6', '2.7.18', '3.0.1',  '3.4.10', '3.5.10', '3.6.15', '3.7.16', '3.8.16', '3.9.16','3.10.11', '3.11.3', '3.12.0b1', '3.13.0a0'])


    fig.update_traces(
        textfont_size=18
    )

    # Check if the directory exists
    directory = language + '/mainPrograms_plots/'
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)

    filename_plot_wDir = directory + filename_plot
    plot = plotly.offline.plot(fig, filename= filename_plot_wDir + '.html', auto_open=False)
    return 'mainPrograms_plots/' + filename_plot + ".html"

def plot_Matrix(language, df, filename_plot, type, filtered_flag):

    if type == "corrTop":

        corrs = df[['time','virt','res','shr','percent_cpu','percent_mem','nTH','P',
                    'SWAP','CODE','DATA','nMaj','nDRT','USED']].corr()

        np.fill_diagonal(corrs.values, np.nan)

        corrs = corrs.head(1)

        if filtered_flag:
            corrs = corrs[(corrs > 0.7) | (corrs < -0.7)]
            corrs = corrs.dropna(how='all')
            corrs = corrs.sort_values(by=['time'], ascending=False)

            # SORT ACCORDING TO THE VALUES AND CHANGE TO A PLOT

        heat = go.Heatmap(z=corrs.values.round(2),
                        x=list(corrs.columns),
                        y=list(corrs.index),
                        xgap=1, ygap=1,
                        texttemplate="%{z}",
                        showscale=True,
                        colorbar_thickness=20,
                        colorbar_ticklen=3,
                        # zmax=1, zmin=0.1
                        )
        layout = go.Layout(title_x=0.5, 
                        xaxis_showgrid=False,
                        yaxis_showgrid=False,
                        yaxis_autorange='reversed')
        fig=go.Figure(data=[heat], layout=layout)
        fig.update_layout(title=language + ' - ' + filename_plot,
                            xaxis_nticks=36)
        fig['layout']['xaxis']['side'] = 'top'

    elif type == "corrTurbo":

        corrs = df[['time_elapsed','Pkg_J','Cor_J','RAM_J','GFX_J',
                    'Avg_MHz', 'Busy%', 'IPC', 'IRQ', 'POLL', 
                    'C1%','C1E%','C3%','C6%','C7s%','C8%','C9%','C10%',
                    'CPU%c1','CPU%c3','CPU%c6','CPU%c7','CoreTmp','PkgTmp',
                    'GFX%rc6','Totl%C0','Any%C0','GFX%C0','CPUGFX%']].corr()

        np.fill_diagonal(corrs.values, np.nan)

        # corrs = corrs.head(5)
        corrs = corrs.T.head(5).T

        if filtered_flag:
            corrs = corrs[(corrs > 0.7) | (corrs < -0.7)]
            corrs = corrs.dropna(how='all')
            corrs = corrs.sort_values(by=['time_elapsed', 'Pkg_J','Cor_J','RAM_J','GFX_J'], ascending=False)

        heat = go.Heatmap(z=corrs.values.round(2),
                        x=list(corrs.columns),
                        y=list(corrs.index),
                        xgap=1, ygap=1,
                        texttemplate="%{z}",
                        showscale=True,
                        colorbar_thickness=20,
                        colorbar_ticklen=3,
                        # zmax=1, zmin=0.1
                        )
        layout = go.Layout(title_x=0.5, 
                        xaxis_showgrid=False,
                        yaxis_showgrid=False,
                        yaxis_autorange='reversed')
        fig=go.Figure(data=[heat], layout=layout)
        fig.update_layout(title=language + ' - ' + filename_plot,
                            xaxis_nticks=36)
        fig['layout']['xaxis']['side'] = 'top'

    elif type == "corrPerf" or type == "corrPerf2" or type == "corrPerf3":
        if type == "corrPerf1":
            corrs = df[['time_elapsed_sec','CPU_Utilization','Retiring','Frontend_Bound','Bad_Speculation','Backend_Bound',
                        'CPI','ILP','IPC_perf','cycles','freq_cycles_GHz','instructions',
                        'Kernel_Utilization', 'L1D_Cache_Fill_BW', 'Turbo_Utilization', 'cycles',
                        'instructions', 'insn_per_cycle', 'cpu_clock_msec', 'no_cpus', 'cpu_cycles', 'freq_cpu_cycles_GHz']].corr()
        elif type == "corrPerf2":
            corrs = df[['time_elapsed_sec','cpu_migrations','ref_cycles','bus_cycles','task_clock_msec','no_cpus_task_clock',
                        'cpu_thermal_margin_C','branches','branch_misses','mem_loads','mem_stores','page_faults','minor_faults','major_faults',
                        'cache_references','cache_misses','percent_cache_misses','L1_dcache_loads','L1_dcache_load_misses']].corr()

        elif type == "corrPerf":
            corrs = df[['time_elapsed_sec','CPU_Utilization','Retiring','Frontend_Bound','Bad_Speculation','Backend_Bound',
                        'CPI','ILP','IPC_perf','cycles','freq_cycles_GHz','instructions',
                        'Kernel_Utilization', 'L1D_Cache_Fill_BW', 'Turbo_Utilization', 'cycles',
                        'instructions', 'insn_per_cycle', 'cpu_clock_msec', 'no_cpus', 'cpu_cycles', 'freq_cpu_cycles_GHz',
                        'cpu_migrations','ref_cycles','bus_cycles','task_clock_msec','no_cpus_task_clock',
                        'cpu_thermal_margin_C','branches','branch_misses','mem_loads','mem_stores','page_faults','minor_faults','major_faults',
                        'cache_references','cache_misses','percent_cache_misses','L1_dcache_loads','L1_dcache_load_misses',
                        'LLC_loads','LLC_load_misses','L1_icache_load_misses','dTLB_loads',
                        'dTLB_load_misses','iTLB_loads','iTLB_load_misses']].corr()


        np.fill_diagonal(corrs.values, np.nan)

        corrs = corrs.T.head(1).T

        if filtered_flag:
            corrs = corrs[(corrs > 0.7) | (corrs < -0.7)]
            corrs = corrs.dropna(how='all')
            corrs = corrs.sort_values(by=['time_elapsed_sec'], ascending=False)

        heat = go.Heatmap(z=corrs.values.round(2),
                        x=list(corrs.columns),
                        y=list(corrs.index),
                        xgap=1, ygap=1,
                        texttemplate="%{z}",
                        showscale=True,
                        colorbar_thickness=20,
                        colorbar_ticklen=3,
                        # zmax=1, zmin=0.1
                        )
        layout = go.Layout(title_x=0.5, 
                        xaxis_showgrid=False,
                        yaxis_showgrid=False,
                        yaxis_autorange='reversed')
        fig=go.Figure(data=[heat], layout=layout)
        fig.update_layout(title=language + ' - ' + filename_plot,
                            xaxis_nticks=36)
        fig['layout']['xaxis']['side'] = 'top'
        
    elif type == "corrGeneral":
        corrs = df[['time_elapsed','Pkg_J','Cor_J','RAM_J','GFX_J',
                    'Avg_MHz', 'Busy%', 'IPC', 'IRQ', 'POLL', 
                    'C1%','C1E%','C3%','C6%','C7s%','C8%','C9%','C10%',
                    'CPU%c1','CPU%c3','CPU%c6','CPU%c7','CoreTmp','PkgTmp',
                    'GFX%rc6','Totl%C0','Any%C0','GFX%C0','CPUGFX%',
                    'time','virt','res','shr','percent_cpu','percent_mem','nTH','P',
                    'SWAP','CODE','DATA','nMaj','nDRT','USED',
                    'time_elapsed_sec','CPU_Utilization','Retiring','Frontend_Bound','Bad_Speculation','Backend_Bound',
                        'CPI','ILP','IPC_perf','cycles','freq_cycles_GHz','instructions',
                        'Kernel_Utilization', 'L1D_Cache_Fill_BW', 'Turbo_Utilization', 'cycles',
                        'instructions', 'insn_per_cycle', 'cpu_clock_msec', 'no_cpus', 'cpu_cycles', 'freq_cpu_cycles_GHz',
                        'cpu_migrations','ref_cycles','bus_cycles','task_clock_msec','no_cpus_task_clock',
                        'cpu_thermal_margin_C','branches','branch_misses','mem_loads','mem_stores','page_faults','minor_faults','major_faults',
                        'cache_references','cache_misses','percent_cache_misses','L1_dcache_loads','L1_dcache_load_misses',
                        'LLC_loads','LLC_load_misses','L1_icache_load_misses','dTLB_loads',
                        'dTLB_load_misses','iTLB_loads','iTLB_load_misses'
                        ]].corr()
        np.fill_diagonal(corrs.values, np.nan)

        # corrs = corrs.head(5)
        corrs = corrs.T.head(5).T

        if filtered_flag:
            corrs = corrs[(corrs > 0.7) | (corrs < -0.7)]
            corrs = corrs.dropna(how='all')
            corrs = corrs.sort_values(by=['time_elapsed','Pkg_J','Cor_J','RAM_J','GFX_J'], ascending=False)

        heat = go.Heatmap(z=corrs.values.round(2),
                        x=list(corrs.columns),
                        y=list(corrs.index),
                        xgap=1, ygap=1,
                        texttemplate="%{z}",
                        showscale=True,
                        colorbar_thickness=20,
                        colorbar_ticklen=3,
                        # zmax=1, zmin=0.1
                        )
        layout = go.Layout(title_x=0.5, 
                        xaxis_showgrid=False,
                        yaxis_showgrid=False,
                        yaxis_autorange='reversed')
        fig=go.Figure(data=[heat], layout=layout)
        fig.update_layout(title=language + ' - ' + filename_plot,
                            xaxis_nticks=36)
        fig['layout']['xaxis']['side'] = 'top'

    elif type == "scattermatrixTurbo":

        # fig = ff.create_scatterplotmatrix(df[['time_elapsed', 'Pkg_J', 'RAM_J', 'version']], 
        #                           height=1000,
        #                           width=1000,
        #                           diag='histogram',
        #                           text=df['version'],
        #                           index='version')
        
        fig = px.scatter(df, x='time_elapsed', y='Pkg+RAM_J', color='path',
                 animation_frame="version",
                 range_x=[df['time_elapsed'].min(),df['time_elapsed'].max()], range_y=[df['Pkg_J'].min(),df['Pkg_J'].max()]
                 )
    elif type == "scatterTurbo_program":

        fig = px.scatter(df, x='time_elapsed', y='Pkg+RAM_J', color="path")

    elif type == "scatterTurbo_version":

        fig = px.scatter(df, x='time_elapsed', y='Pkg+RAM_J', color="version")

    # Check if the directory exists
    directory = language + '/mainPrograms_plots/'
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)

    filename_plot_wDir = directory + filename_plot
    plot = plotly.offline.plot(fig, filename= filename_plot_wDir + '.html', auto_open=False)

    html_fig = 'mainPrograms_plots/' + filename_plot + ".html"

    if filtered_flag:

            # Classify rows as "POSITIVE" or "NEGATIVE" based on the values in the first two columns
            if type == "corrPerf":
                positive_rows = (corrs['time_elapsed_sec'] > 0)
                negative_rows = (corrs['time_elapsed_sec'] < 0)
                df_negative = corrs.loc[negative_rows]
                df_negative = df_negative.sort_values(by=['time_elapsed_sec'], ascending=True)
                df_positive = corrs.loc[positive_rows]
                df_positive = df_positive.drop_duplicates(subset=['time_elapsed_sec'], keep='first')
                df_negative = df_negative.drop_duplicates(subset=['time_elapsed_sec'], keep='first')

            elif type == "corrTop":
                positive_rows = (corrs['time'] > 0)
                negative_rows = (corrs['time'] < 0)
                df_negative = corrs.loc[negative_rows]
                df_negative = df_negative.sort_values(by=['time'], ascending=True)
                df_positive = corrs.loc[positive_rows]
                df_positive = df_positive.drop_duplicates(subset=['time'], keep='first')
                df_negative = df_negative.drop_duplicates(subset=['time'], keep='first')

            else:
                positive_rows = (corrs['time_elapsed'] > 0) | (corrs['Pkg_J'] > 0) | (corrs['Cor_J'] > 0) | (corrs['RAM_J'] > 0) | (corrs['GFX_J'] > 0)
                negative_rows = (corrs['time_elapsed'] < 0) | (corrs['Pkg_J'] < 0) | (corrs['Cor_J'] < 0) | (corrs['RAM_J'] < 0) | (corrs['GFX_J'] < 0)
                df_negative = corrs.loc[negative_rows]
                df_negative = df_negative.sort_values(by=['time_elapsed'], ascending=True)
                df_positive = corrs.loc[positive_rows]
                df_positive = df_positive.drop_duplicates(subset=['time_elapsed', 'Pkg_J','Cor_J','RAM_J','GFX_J'], keep='first')
                df_negative = df_negative.drop_duplicates(subset=['time_elapsed', 'Pkg_J','Cor_J','RAM_J','GFX_J'], keep='first')

            df_negative['position'] = range(1,len(df_negative)+1)
            first_column = df_negative.pop('position') 
            df_negative.insert(0, 'position', first_column)

            df_positive['position'] = range(1,len(df_positive)+1)
            first_column = df_positive.pop('position') 
            df_positive.insert(0, 'position', first_column) 

            positive = df_positive.to_html().replace('<table border="1" class="dataframe">','<table class="table table-striped">')
            negative = df_negative.to_html().replace('<table border="1" class="dataframe">','<table class="table table-striped">')

            no_pos = str(len(df_positive))
            no_neg = str(len(df_negative))

            return html_fig, positive, negative, no_pos, no_neg, corrs

    return html_fig


def plot_Type(language, df, filename_plot, x_data, y_data, color_data, type):

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
    if language == 'python': fig.update_xaxes(categoryorder='array', categoryarray= ['2.5.6', '2.7.18', '3.0.1',  '3.4.10', '3.5.10', '3.6.15', '3.7.16', '3.8.16', '3.9.16','3.10.11', '3.11.3', '3.12.0b1', '3.13.0a0'])


    if x_data == "time_elapsed":
        fig.update_layout(
            xaxis_title="Time Elapsed (sec)",
        )

    if y_data == "time_elapsed":
        fig.update_layout(
            yaxis_title="Time Elapsed (sec)",
        )

    # Check if the directory exists
    directory = language + '/mainPrograms_plots/'
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)

    filename_plot_wDir = directory + filename_plot
    plot = plotly.offline.plot(fig, filename= filename_plot_wDir + '.html', auto_open=False)
    return 'mainPrograms_plots/' + filename_plot + ".html"

def three_plots(language, df, title, filename_plot, x_data, y_data, color_data, type):
    fig1 = plot_Type(language, df, filename_plot, x_data, y_data, color_data, type)
    fig2 = plot_Compare(language, df, filename_plot + "_Comparison_Diff", x_data, y_data, color_data, type, diff_flag=True)
    fig3 = plot_Compare(language, df, filename_plot + "_Comparison_DiffFromMean", x_data, y_data, color_data, type, diff_flag=False)

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

def two_plots(language, df, title, filename_plot, x_data, y_data, color_data, type):

    fig1 = plot_Type(language, df, filename_plot, x_data, y_data, color_data, type)
    fig2 = plot_Compare(language, df, filename_plot + "_Comparison_Diff", x_data, y_data, color_data, type, diff_flag=True)

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

def two_plotsMatrix(language, df, title, filename_plot, type):

    if type == "scattermatrixTurbo" or type == "scatterTurbo_program" or type == "scatterTurbo_version":
        fig1 = plot_Matrix(language, df, filename_plot, type, filtered_flag = False)
    else:
        fig1 = plot_Matrix(language, df, filename_plot, type, filtered_flag = False)
        fig2, df_positive, df_negative, no_positive, no_negative, df = plot_Matrix(language, df, filename_plot + "_Filtered", type, filtered_flag=True)

    if type == "corrGeneral":
        height = "2000"
    elif type == "corrTurbo":
        height = "1000"
    elif type == "corrTop":
        height = "400"
    elif type == "corrPerf":
        height = "1000"
    else:
        height = "600"

    div_string = '''
                <div class="row">
                        <!-- *** Section 1 *** --->
                        <h3>Section:  ''' + title + '''</h3>
                        <iframe class="plot" style="height: ''' + height + '''" frameborder="0" seamless="seamless" scrolling="no" \
                            src="''' + fig1 + '''"></iframe>
                        <p>Notes: </p>
                    </div>
                </div>
    '''

    if type != "scattermatrixTurbo" and type != "scatterTurbo_program" and type != "scatterTurbo_version":

        div_extra = '''
                    <details>
                        <summary style="background-color: #E5E4E2;">Section: Filtered by HIGH ''' + title + '''</summary>
                        <div class="row">
                                <!-- *** Section 2 *** --->
                                <iframe class="plot" style="height: ''' + height + '''" frameborder="0" seamless="seamless" scrolling="no" \
                                    src="''' + fig2 + '''"></iframe>
                                <p>Notes: Detect the MAIN parameters</p>
                        </div>
                        <div class="row">
                                <!-- *** Section 3 *** --->
                                <h3> High <b>POSITIVE</b> Correlation (<b><u>''' + no_positive + '''</b></u> parameters)</h3>
                                ''' + df_positive + '''
                                <h3> High <b>NEGATIVE</b> Correlation (<b><u>''' + no_negative + '''</b></u> parameters)</h3>
                                ''' + df_negative + '''
                        </div>
                    </details>
            '''
        return div_string + div_extra, df

    return div_string

def one_plot(language, df, title, filename_plot, x_data, y_data, color_data, type):

    fig1 = plot_Type(language, df, filename_plot, x_data, y_data, color_data, type)

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