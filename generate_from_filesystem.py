from jinja2 import Environment, FileSystemLoader
import os
 
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('index.html')
 
 
filename = os.path.join(root, 'html', 'motifs.html')
variables = {'motifs':os.path.join(root,'plot_motifs.jpg'),
			'clustermap':os.path.join(root,'clustermap_long_patterns.jpg'),
			'TF':'Any Old TF: ZNF273',
			'meme':os.path.join(root,'meme_motif.jpg')}
with open(filename, 'w') as fh:
    fh.write(template.render(vars = variables))


 
