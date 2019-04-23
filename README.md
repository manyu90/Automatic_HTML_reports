# Automatic HTML reports using Jinja2

### Use Jinja2 templating to auto generate a static site given a template. This is useful when you have to report a large number of results of separate experiments, each of which can be represented in a general fixed template of results we wish to display

All templates and html that is embedded must be kept in the templates folder. The template file is usually called **index.html** . In this case there is  a .html table called *df_info.html* which we wish to  insert into the template (I generated the html table from a pandas dataframe version of it using pandas.DataFrame.to_html )

The paths to the figures and variables can be passed as a dictionary to the template renderer. 

To generate the .html static page run the following:

```python generate_from_filesystem.py```

This would create the .html rendered page in the */html* folder
