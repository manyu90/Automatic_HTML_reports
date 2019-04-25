from jinja2 import Environment, FileSystemLoader
import os,glob,shutil
import pandas as pd
from PIL import Image
import numpy as np

def copy_files(base_dir='./',source_dir='./',target_dir_base='./'):
	assert(os.path.exists(base_dir))
	assert(os.path.exists(source_dir))
	if not os.path.exists(target_dir_base):
		os.makedirs(target_dir_base)
		os.makedirs(os.path.join(target_dir_base,'templates'))
	else:
		if target_dir_base!=base_dir:
			print("Target Dir exists! Proceeding to remove contents")
			shutil.rmtree(target_dir_base)
			os.makedirs(target_dir_base)
			os.makedirs(os.path.join(target_dir_base,'templates'))

	target_templates_dir = os.path.join(target_dir_base,'templates')
	base_templates_dir = os.path.join(base_dir,'templates')
	assert(os.path.exists(base_templates_dir))
	index_file = os.path.join(base_templates_dir,'index.html')
	assert(os.path.exists(index_file))
	target_index_file = os.path.join(target_templates_dir,'index.html')
	##If the target is different from the source, must copy relevant files
	if target_dir_base!=base_dir:
		#Copy index files first
		shutil.copyfile(index_file, target_index_file)

		filenames = ['long_patterns_clustermap.jpg','long_patterns_info.html',\
		'meme_motif.jpg','model_perfofmances.html',\
		'long_patterns.jpg','short_patterns_clustermap.jpg',\
		'short_patterns_info.html','short_patterns.jpg']
		images = []
		tables = []
		for e in filenames:
			if 'jpg' in e:
				images.append(e)
			if 'html' in e:
				tables.append(e)
		
		source_table_paths = [os.path.join(source_dir,_) for _ in tables]
		target_table_paths = [os.path.join(target_templates_dir,_) for _ in tables]

		source_image_paths = [os.path.join(source_dir,_) for _ in images]
		target_image_paths = [os.path.join(target_dir_base,_) for _ in images]

		for s,t in zip(source_table_paths, target_table_paths):
			try:
				shutil.copyfile(s, t)
			except:
				continue


		
		for s,t in zip(source_image_paths, target_image_paths):
			try:
				shutil.copyfile(s, t)
			except:
				continue
		
		print("Copied all the files over to the target directory")


	return

def get_structural_annotation(tf):
    path_to_tf_data_table = '/Users/abhimanyu/Dropbox/Documents/Research/DL_for_Genomics/C2H2_ZNF/allZnfPotentiallyReliablePeakFiltSelectedStats.xlsx'
    test_df = pd.read_excel(path_to_tf_data_table,sheet_name='Sheet1')
    annotation = test_df.loc[test_df['TF']==tf]['Subfamily'].values[0]
    return(str(annotation))

def aspect_ratio(path_to_image):
	image = Image.open(path_to_image)
	image_arr = np.array(image)
	height,width,channels = image_arr.shape
	aspect_ratio = float(height)/float(width)
	return(aspect_ratio)


def generate_html(tf,target_dir,target_dir_html=None):
	'''Base dir is the path to the cloned github repo
	   Source dir is the path to TF motif files and html tables
	   target_dir is where we want to host (ie. would have the template and the files ; would be on the hosting server)
	   target_dir_html : If we want the final generated html to be in a different location from the target dir (for a cleaner look)

	'''
	#copy_files(base_dir,source_dir,target_dir)

	root = os.path.realpath(target_dir)
	templates_dir = os.path.join(root, 'templates')
	env = Environment( loader = FileSystemLoader(templates_dir) )
	template = env.get_template('index.html')
	 
	if not target_dir_html:
		filename = os.path.join(root,'{}_Modisco_report.html'.format(tf))
		target_dir_html = root
	else:
		assert(os.path.exists(target_dir_html))
		filename = os.path.join(target_dir_html,'{}_Modisco_report.html'.format(tf))

	#Important to use relative paths to load images on the server
	rel_root = os.path.relpath(root,target_dir_html)

	variables = {'short_patterns':os.path.join(rel_root,'short_patterns.jpg'),
				'short_patterns_clustermap':os.path.join(rel_root,'short_patterns_clustermap.jpg'),
				'long_patterns':os.path.join(rel_root,'long_patterns.jpg'),
				'long_patterns_clustermap':os.path.join(rel_root,'long_patterns_clustermap.jpg'),
				'meme_motif':os.path.join(rel_root,'meme_motif.jpg'),
				'short_patterns_info':os.path.join(templates_dir,'short_patterns_info.html'),
				'long_patterns_info':os.path.join(templates_dir,'long_patterns_info.html'),
				'model_perfofmances':os.path.join(templates_dir,'model_perfofmances.html'),
				'Subfamily':get_structural_annotation(tf),
				'TF':tf
				}

	bools = {'short_patterns':os.path.exists(os.path.join(root,'short_patterns.jpg')),
				'short_patterns_clustermap':os.path.exists(os.path.join(root,'short_patterns_clustermap.jpg')),
				'long_patterns':os.path.exists(os.path.join(root,'long_patterns.jpg')),
				'long_patterns_clustermap':os.path.exists(os.path.join(root,'long_patterns_clustermap.jpg')),
				'meme_motif':os.path.exists(os.path.join(root,'meme_motif.jpg')),
				'short_patterns_info':os.path.exists(os.path.join(templates_dir,'short_patterns_info.html')),
				'long_patterns_info':os.path.exists(os.path.join(templates_dir,'long_patterns_info.html')),
				'model_perfofmances':os.path.exists(os.path.join(templates_dir,'model_perfofmances.html'))}

	patterns_width = 800
	short_height = None
	long_height = None
	try:
		short_patterns_aspect_ratio = aspect_ratio(variables['short_patterns'])
		#print("short_patterns aspect ratio: {}".format(str(short_patterns_aspect_ratio)))
		short_height = int(short_patterns_aspect_ratio*patterns_width)
	except Exception as e:
		print(str(e))
		pass
	try:
		long_patterns_aspect_ratio = aspect_ratio(variables['long_patterns'])
		long_height = int(long_patterns_aspect_ratio*patterns_width)
	except:
		pass


	aspect = {'width':'800px','short_height':'{}px'.format(str(short_height)),'long_height':'{}px'.format(str(long_height))}
	
	with open(filename, 'w') as fh:
	    fh.write(template.render(vars=variables,bools=bools,aspect=aspect))


	print("Generated html at {}".format(filename))
	return


		
		
		
		
if __name__=='__main__':
	copy_files('./','CTCF','target_CTCF')
	generate_html('CTCF','./target_CTCF','./')

		
		



	

