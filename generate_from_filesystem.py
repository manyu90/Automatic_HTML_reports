from jinja2 import Environment, FileSystemLoader
import os
 
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('index.html')
 
 
filename = os.path.join(root, 'html', 'motifs.html')
variables = {'motifs':'/Users/abhimanyu/Dropbox/Documents/Research/DL_for_Genomics/C2H2_ZNF/html_reports/example_figures/plot_motifs.jpg',
			'clustermap':'/Users/abhimanyu/Dropbox/Documents/Research/DL_for_Genomics/C2H2_ZNF/html_reports/example_figures/clustermap_long_patterns.jpg',
			'TF':'Any Old TF: ZNF273'}
#motifs_path = '/Users/abhimanyu/Dropbox/Documents/Research/DL_for_Genomics/C2H2_ZNF/html_reports/example_figures/plot_motifs.jpg'
with open(filename, 'w') as fh:
    fh.write(template.render(vars = variables))


 