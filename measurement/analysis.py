# Libraries
import sys
import os
import webbrowser

# Arguments
# 
# Example: python3 analysis.py c++ nbody_2.c 50000000 nbody_50000000_4
language=sys.argv[1]
command=sys.argv[2]
directory=sys.argv[3]

path=language + '/' + directory + '/'

if __name__ == '__main__':

    python_codeTurbostat='python3 analysis_turbostat.py ' + language + ' "' + command + '" ' + directory
    python_codePerf='python3 analysis_perf.py ' + language + ' "' + command + '" ' + directory
    python_codeTop='python3 analysis_top.py ' + language + ' "' + command + '" ' + directory

    os.system(python_codeTurbostat)
    os.system(python_codePerf)
    os.system(python_codeTop)

    print("Creating the general report ...")
    html_string = '''

    <!DOCTYPE html>
    <html>
    <head>
        <title>Report - ''' + language + ''' ''' + command + '''</title>
        <link rel="shortcut icon" type="x-icon" href="''' + "../../" + "aalto.ico" + '''"> </link>
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
        </style>
    </head>
    <body>
        <h1 class="mb-4">Analysis of energy consumption, performance and memory usage in <b>''' + language + '''</b> through <b>''' + command + '''</b> </h1>
        <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item">
                <a class="nav-link active" id="turbostat-tab" data-toggle="tab" href="#turbostat" role="tab" aria-controls="turbostat" aria-selected="true">Turbostat</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="perf-tab" data-toggle="tab" href="#perf" role="tab" aria-controls="perf" aria-selected="false">Perf</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="top-tab" data-toggle="tab" href="#top" role="tab" aria-controls="top" aria-selected="false">Top</a>
            </li>
        </ul>

        <div class="tab-content" id="myTabContent"  >
            <div class="tab-pane fade show active" id="turbostat" role="tabpanel" aria-labelledby="turbostat-tab">
                <div class="iframe-container">
                    <iframe src="turbostat/report_Turbostat.html" frameborder="0"></iframe>
                </div>
            </div>
            <div class="tab-pane fade" id="perf" role="tabpanel" aria-labelledby="perf-tab">
                <div class="iframe-container">
                    <iframe src="perf/report_Perf.html" frameborder="0"></iframe>
                </div>
            </div>
            <div class="tab-pane fade" id="top" role="tabpanel" aria-labelledby="top-tab">
                <div class="iframe-container">
                    <iframe src="top/report_Top.html" frameborder="0"></iframe>
                </div>
            </div>
        </div>

        <!-- Add Bootstrap and jQuery scripts -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

    </body>
    </html>
    '''

    f = open(path + 'report.html','w')
    f.write(html_string)
    f.close()

    webbrowser.open_new_tab(path + 'report.html')