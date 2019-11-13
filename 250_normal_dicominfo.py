import pandas as pd 
import pydicom
import numpy as np 
import os
import shutil
import sys






def get_pict_list(root_path, file, des_path):
	path1 = os.path.join(root_path, file)

	filelist2 = os.listdir(path1)

	for file2 in filelist2:
		path2 = os.path.join(path1, file2)
		if os.path.isdir(path2):
			filelist3 = os.listdir(path2)
			
			for file3 in filelist3:
				path3 = os.path.join(path2, file3)
				if os.path.isdir(path3):
					filelist4 = os.listdir(path3)[:-1]

					pict0 = os.path.join(path3, filelist4[0])
					ds = pydicom.read_file(pict0)
					patient_name = str(ds.PatientName)

					out_path = os.path.join(des_path, patient_name)
					if not os.path.exists(out_path):
						os.makedirs(out_path)

						for pict in filelist4:
							pict_path = os.path.join(path3, pict)
							shutil.copyfile(pict_path, os.path.join(out_path, pict))
						print(len(filelist4))



if __name__ == '__main__':
	path = 'D:/csy/CT_detect/听神经瘤 正常对照图像'
	des_path = 'D:\csy\CT_detect/250_normal'
	filelist = os.listdir(path)
	for file in filelist:
		pict_list = get_pict_list(path, file, des_path)
