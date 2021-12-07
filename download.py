import requests
import argparse
import tqdm
import os

def place(filename):
	ext = filename.split('.')[-1]
	if ext in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
		return "Pictures"

	elif ext in ['mp4', 'mkv', 'flv', 'mpeg', 'mp3']:
		return 'Videos'

	elif ext in ['exe', 'msi', 'dmg', 'sh']:
		return 'programs'

	elif ext in ['rar', 'zip', '7z']:
		return 'compressed'

	elif ext in ['pdf', 'ppt', 'doc', 'docx', 'xls', 'xlsx', 'pptx']:
		return 'documents'

	else:
		return 'others'


ap = argparse.ArgumentParser()
ap.add_argument('-l', '--link', required= True, help = 'Link File')

# mengatur output programnya/ mengeluarkan progresbar
ap.add_argument('-v','--verbose', default=True)
args = vars(ap.parse_args())

r = requests.get(args['link'], stream=True)
filename = args['link'].split('/')[-1]
file_size = int(r.headers['Content-Length'])
print(file_size)

# membagi ukuran file download agar dapat mendownload secara paralel
chunk = 1
chunk_size = 1024
num_bars = int(file_size/chunk_size)
verbose = args['verbose']
if verbose:
	print(f"ukuran file : {file_size}")
	print(f"jumlah bar : {num_bars}")
	dir_ = os.path.join('D:', os.sep, 'PythonProject', 'project', 'livseminggu', 'project_sol','download',place(filename), filename)
	#print(dir_)
	# buka file
	with open(dir_, 'wb') as fp:
		for chunk in tqdm.tqdm(
								r.iter_content(chunk_size=chunk_size),
								total = num_bars,
								unit= 'KB',
								desc='ukuran dan waktu download',
								leave=True):
			fp.write(chunk)


