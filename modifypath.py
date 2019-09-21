import os

def modify(inpath, outpath):
	ff = open(outpath, 'w')
	with open(inpath, 'r') as f:
		line_list = f.readlines()
		for line in line_list:
			path = line
			line_new = ''

			for i in range(5):
				path1 = os.path.split(path)[1]
				path0 = os.path.split(path)[0]
				if i == 0:
					line_new = path1
				else:
					line_new = os.path.join(path1, line_new)
				path = path0	

			ff.write(line_new)




if __name__ == '__main__':

	inpath = 'trainvalno5k.txt'
	outpath = 'trainvalno5kmodify.txt'
	modify(inpath, outpath)

