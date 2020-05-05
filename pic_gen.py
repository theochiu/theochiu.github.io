from pprint import pprint
import os, shutil

PAGE_SIZE = 5
IMG_EXT = [".gif", ".jpg", ".jpeg", ".png", ".bmp"]

def change_names(files, path):
	''' takes list of file names starting with oldest and ending with the 
		newest. Then changes names of each file to numbers with 1 being
		the oldest and the highest number being the newest. Then returns
		a list of the same order but with renamd file names. Some files might
		already be numbered '''

	name_num = 1 
	i = 0
	names = [(os.path.split(file)[1]) for file in files]
	file_dict = {os.path.splitext(file)[0]: os.path.splitext(file)[1] for file in names}
	res = []

	# populate res with already numbered files
	# remove this files fomr names
	this_name = str(name_num)
	while this_name in file_dict:
		res.append(this_name + file_dict[this_name])
		names.remove(this_name + file_dict[this_name])
		name_num += 1
		this_name = str(name_num)

	while names:
		this_name = str(name_num)
		root, ext = os.path.splitext(names[i])
		os.rename(os.path.join(path, names[i]), os.path.join(path, this_name + ext))
		name_num += 1
		res.append(this_name)
		names.remove(names[i])

	return [os.path.join(path, file) for file in res]

def get_pics(path):
	files = []

	# populate list of images
	for file in os.listdir(path):
		root, ext = os.path.splitext(file)
		if ext.lower() in IMG_EXT:
			files.append(file)
	
	full_list = [os.path.join(path,i) for i in files]
	reversed_files = sorted(full_list, key=os.path.getctime)				# ordered newest last

	reversed_files = change_names(reversed_files, path)

	return reversed_files[::-1]		# reverse the order

def make_html(path, dest, background="/static/pagepics/beach_cam.jpg"):
	files = get_pics(path)

	# REVERSE
	# files = files[::-1]

	if os.path.isdir(dest):
		shutil.rmtree(dest)
		os.mkdir(dest)
	else:
		os.mkdir(dest)

	# where i is the markdown page we're on
	for i in range(1, (len(files) + PAGE_SIZE - 1)// PAGE_SIZE + 1):

		f = open(dest+"/page{}.md".format(i), "w")

		f.write("---\n")
		f.write('layout: post\n')
		f.write('title:  "Page {}"\n'.format(i))
		f.write("background: '"+background+"'\n")
		f.write('author: "Theodore Chiu"\n')
		f.write("order: {}\n".format(i))
		f.write("---\n\n")

		# where j is the index of the image to write to the page
		for j in range((i-1) * PAGE_SIZE, (i-1) * PAGE_SIZE + PAGE_SIZE):
			if j >= len(files): continue
			# print(j)
			f.write('<a href="{{ "'+files[j]+'" | relative_url}}">\n')
			f.write('\t<img class="img-fluid" src="{{ "' +files[j]+'" | relative_url}}" alt="Demo Image">\n')
			f.write('</a>\n\n')

		f.close()



if __name__ == '__main__':
	# make_html("static/pics", "_pictures")
	make_html("static/zuko", "_zuko_pics", "/static/pagepics/zuko_back.jpg")
	# make_html("static/car_pics", "_car_pics", "/static/pagepics/bmw2002.jpeg")
	print("success")
	# pprint(get_pics("static/zuko"))


