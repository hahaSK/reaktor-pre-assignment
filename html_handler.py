"""
    Author: Ing. Juraj Lahvička
    2020
"""

html_header = """<!DOCTYPE html> 
                                <html lang="en">
                                <head>
                                <title>Packages</title>
                                <style>
                                body, html {height: 100%; margin-top: 0;}
                                h3 {color: #117A1C;}
                                #summary {background: lightgray; text-align: center;}
                                #summary table {margin: auto;}
                                </style>
                                </head>"""


def create_summary(packages):
    """Function creates summary (indexing) table"""
    summary_table = '<div id="summary">'
    summary_table += '<table class="summary_table">' \
                     '<tr>' \
                     '<th>Packages</th>' \
                     '</tr>'
    for package in packages:
        summary_table += '<tr>'
        summary_table += f'<td><a href="#{package.Name}">{package.Name}</a></td>'
        summary_table += '</tr>'

    summary_table += '</table></div>'
    return summary_table


def create_list(depends_list, cls_name) -> str:
    """Function creates specified list"""
    html_list = f'<ul class="{cls_name}">'
    for depend in depends_list:
        html_list += f'<li><a href="#{depend}">{depend}</a></li>'
    html_list += '</ul>'
    return html_list


def create_package_details(packages):
    """Function creates package details html part"""
    package_details = '<div id="package_details><h2>Package Details</h2>'
    for package in packages:
        package_details += f'<div id="{package.Name}">'
        package_details += f'<h3>{package.Name}</h3>'

        package_details += '<h4>Description</h4>'
        package_details += f'<p>{package.Description}</p>'

        package_details += '<h4>Dependencies</h4>'
        package_details += create_list(package.DependsList, "depends_list")

        package_details += '<h4>Reverse dependencies</h4>'
        package_details += create_list(package.ReverseDependencies, "reverse_depends_list")

        package_details += '</div>'

    package_details += '</div>'
    return package_details


def create_html(packages):
    """Creates html page and saves it to file"""
    summary_table = create_summary(packages)
    details = create_package_details(packages)

    html_page = html_header + '<body>' + summary_table + details + '</body>'
    with open('output.html', 'w+') as f:
        f.write(html_page)
