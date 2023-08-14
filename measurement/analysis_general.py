# Libraries
import os
import webbrowser


# Arguments
# 
# Example: python3 analysis.py c++ nbody_2.c 50000000 nbody_50000000_4
# language=sys.argv[1]
# command=sys.argv[2]
# directory=sys.argv[3]

# Directory
actual_directory = os.getcwd() + '/'

# Function by programming language to create the html string
def html_Language(language, active):

    html_filename = language + "/report_" + language

    command = "python3 analysis_byProgram.py " + language + " " + html_filename
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