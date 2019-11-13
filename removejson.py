
###step 1
###remove .json file from jpg file to annotation file

import os
import shutil
import sys

def remove(inpath, outpath):
	patients = os.listdir(inpath)

	for patient in patients:
		file_path = os.path.join(inpath, patient)
		file_list = os.listdir(file_path)

		for file_name in file_list:
			if file_name.endswith('.json'):
				full_path = os.path.join(file_path, file_name)

				if not os.path.exists(os.path.join(outpath, patient)):
					os.makedirs(os.path.join(outpath, patient))

				des_path = os.path.join(outpath, patient, file_name)
				shutil.move(full_path, des_path)
		print('{} \'s json has removed'.format(patient))

if __name__ == '__main__':

	inpath = 'tumour_jpg'
	outpath = 'tumour_annotation_final'
	remove(inpath, outpath)