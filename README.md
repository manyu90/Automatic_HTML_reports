# Automatic_HTML_reports using Jinja2

##Use Jinja2 templating to auto generate a static site given a template. This demonstrates the general layout

All templates and html that is embedded must be kept in the templates folder. The template file is usually called *index.html* . There is also a .html table called df_info.html which is insered into the template (I generated the table from a pandas dataframe (convert to html feature of the df))

THe paths to the figures and variables can be passed as a dictionary to the template renderer. 

To generate the .html static page run the following:
```python generate_from_filesystem.py```

This would create the .html rendered page in the \html folder
