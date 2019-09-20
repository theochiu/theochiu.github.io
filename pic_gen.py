from pprint import pprint
import os, shutil

PAGE_SIZE = 5
IMG_EXT = [".gif", ".jpg", ".jpeg", ".png", ".bmp"]

def get_pics(path):
	files = []
	for file in os.listdir(path):
		_, ext = os.path.splitext(file)
		if ext.lower() in IMG_EXT:
			files.append(file)
	
	full_list = [os.path.join(path,i) for i in files]
	files = sorted(full_list, key=os.path.getmtime)
	# pprint(files)
	return files[::-1]

def make_html(path, dest, background="/static/pagepics/beach_cam.jpg"):
	files = get_pics(path)

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
	make_html("static/pics", "_pictures")
	make_html("static/zuko", "_zuko_pics", "/static/pagepics/zuko_back.jpg")
	make_html("static/car_pics", "_car_pics", "/static/pagepics/bmw2002.jpeg")
	print("success")
	# pprint(get_pics("static/zuko"))
