# Automatic HTML reports using Jinja2

### Use Jinja2 templating to auto generate a static site given a template. This is useful when you have to report a large number of results of separate experiments, each of which can be represented in a general fixed template of results we wish to display

All templates and html that is embedded must be kept in the templates folder. The template file is usually called **index.html** . 

The Source directory should contain images and tabels that we wish to embed. The target directory will have the generated website ; a copied template and index.html file and (possibly) the rendered .html file (unless we choose a separate save directory for the generated html file)

The paths to the figures and variables can be passed as a dictionary to the template renderer. The aspect ratios of images are calculated on the fly as well and passed to the template

To generate the .html static page run the following: 

```python generate_html_from_file.py```

This would create the .html rendered page in the target path provided to save the html
