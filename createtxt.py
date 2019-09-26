import os

def patientname(normal_path, tumour_path):
	normal_patient = os.listdir(normal_path)
	tumour_patient = os.listdir(tumour_path)

	return normal_patient, tumour_patient


def creattxt(images_path, traintxt_path, valtxt_path, normal_patient, tumour_patient):
	normal_train = normal_patient[10: ]
	normal_val = normal_patient[0: 10]
	tumour_train = tumour_patient[4: ]
	tumour_val = tumour_patient[0: 4]

	# print(normal_train+tumour_train)

	ftrain = open(traintxt_path, 'w')
	fval = open(valtxt_path, 'w')

	images = os.listdir(images_path)
	for image in images:
		path = os.path.join(images_path, image)

		iamge_name = '_'.join(image.split('.')[0].split('_')[: -1])
		if iamge_name in (normal_train+tumour_train):
			ftrain.write(path+'\n')
		elif iamge_name in (normal_val+tumour_val):
			fval.write(path+'\n')
	ftrain.close()
	fval.close()



if __name__ == '__main__':
	normal_path = 'D:\csy\CT_detect/normal_jpg'
	tumour_path = 'D:\csy\CT_detect/tumour_jpg'
	normal_patient, tumour_patient = patientname(normal_path, tumour_path)
	# print(normal_patient)
	# print(tumour_patient)

	images_path = 'D:\csy\PyTorch-YOLOv3-master\data\custom\images'
	traintxt_path = 'D:\csy\PyTorch-YOLOv3-master\data\custom/train.txt'
	valtxt_path = 'D:\csy\PyTorch-YOLOv3-master\data\custom/valid.txt'
	creattxt(images_path, traintxt_path, valtxt_path, normal_patient, tumour_patient)