import pandas as pd 
import pydicom
import numpy as np 
import os

def extractdicominfo(filepath):
	medifile = os.listdir(filepath)
	df = pd.DataFrame()
	for i in range(len(medifile)):
		filename = os.listdir(filepath + '/' + medifile[i])
		for j in range(len(filename)):
			information = {}
			filename_path = filepath + '/' + medifile[i] + '/' + filename[j]
			information['FilePath'] = filename_path
			ds = pydicom.read_file(filename_path)
			information['PatientID'] = ds.PatientID
			information['PatientName'] = ds.PatientName
			information['InstanceNumber'] = ds.InstanceNumber
			df = df.append(information, ignore_index = True)
	df.to_csv(filepath + '_' + 'information.csv', index = None)
	print('save'+ filepath + '_' + 'information Sucessfully!')


if __name__ == '__main__':

	extractdicominfo('20190915')