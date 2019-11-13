import json
import os
import shutil
import sys
import cv2

def area(x1, y1, x2, y2):
	return abs(int(x1-x2)*int(y1-y2))

def cut_picture(pict_srcpath, pict_outpath,  x1, y1, x2, y2):
	img = cv2.imread(pict_srcpath)
	x1 = int(min(int(x1), int(x2)))
	x2 = int(max(int(x1), int(x2)))
	y1 = int(min(int(y1), int(y2)))
	y2 = int(max(int(y1), int(y2)))
	new_img = img[y1:y2, x1:x2]
	cv2.imwrite(pict_outpath , new_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

def createlabel(inpath, outpath, pict_inpath, pict_outpath):
    if os.path.exists(outpath):
        print('find file {}'.format(outpath))
    f = open(outpath, 'w')
    patients_name = os.listdir(inpath)
    for patient in patients_name:
        jsonfilelist = os.listdir(os.path.join(inpath, patient))
        left_x1 = 0
        left_y1 = 0
        left_x2 = 0
        left_y2 = 0
        left_start = 0
        left_count = 0
        right_x1 = 0
        right_y1 = 0
        right_x2 = 0
        right_y2 = 0
        right_start = 0
        right_count = 0

        for patientjson in jsonfilelist:
        	num = 0
        	jsonpath = os.path.join(inpath, patient, patientjson)
        	jsonname = patientjson.split('.')[0]
        	# print('jsonname:', jsonname)        	
        	with open(jsonpath, 'r', encoding='utf-8') as file:
        		data_complete = json.load(file)
        		high = data_complete['imageHeight']
        		wide = data_complete['imageWidth']
        		data = data_complete['shapes']
        		# print(high)
        	for i in range(len(data)):
        		
        		# print(data[i]['label'])
        		# print(data[i]['points'])
        		if data[i]['points'][0][0]<wide/2:
        			local = 'left'
        			left_label = data[i]['label']
        			left_count +=1
        			if left_start == 0:
        				left_start = jsonname
        			if area(data[i]['points'][0][0], data[i]['points'][0][1], data[i]['points'][1][0], data[i]['points'][1][1]) > area(left_x1, left_y1, left_x2, left_y2):
        				left_x1 = data[i]['points'][0][0]
        				left_y1 = data[i]['points'][0][1]
        				left_x2 = data[i]['points'][1][0]
        				left_y2 = data[i]['points'][1][1]

        		elif data[i]['points'][0][0]>wide/2:
        			local = 'right'
        			right_label = data[i]['label']
        			right_count += 1
        			if right_start == 0:
        				right_start = jsonname
        			if area(data[i]['points'][0][0], data[i]['points'][0][1], data[i]['points'][1][0], data[i]['points'][1][1]) > area(right_x1, right_y1, right_x2, right_y2):
        				right_x1 = data[i]['points'][0][0]
        				right_y1 = data[i]['points'][0][1]
        				right_x2 = data[i]['points'][1][0]
        				right_y2 = data[i]['points'][1][1]

        for local in ['left', 'right']:
        	if local == 'left':
        		if left_label == 'tumour':
        			label = 0
        		elif left_label == 'normal':
        			label = 1
        		now_path = os.path.join(pict_outpath, patient+'_left')
        		f.write(str(now_path)+' '+str(label)+'\n')
        		for i in range(left_count):
        			# print('left:', i)
        			pict_srcpath = os.path.join(pict_inpath, patient)
        			pict_srcpath = os.path.join(pict_srcpath, str(int(left_start)+i)+'.jpg')
        			# print('left path:', pict_srcpath)
        			path = os.path.join(pict_outpath, patient+'_left')        			
        			if not os.path.exists(path):
        				os.makedirs(path)        			
        			pict_despath = os.path.join(path, str(i)+'.jpg')
        			cut_picture(pict_srcpath, pict_despath,  left_x1, left_y1, left_x2, left_y2)

        	if local == 'right':
        		if right_label == 'tumour':
        			label = 0
        		elif right_label == 'normal':
        			label = 1
        		f.write(str(os.path.join(pict_outpath, patient+'_right'))+' '+str(label)+'\n')
        		for i in range(right_count):
        			# print('right:', i)
        			pict_srcpath = os.path.join(pict_inpath, patient, str(int(right_start)+i)+'.jpg')
        			# print('right path', pict_srcpath)
        			path = os.path.join(pict_outpath, patient+'_right')
        			if not os.path.exists(path):
        				os.makedirs(path)
        			pict_despath = os.path.join(path, str(i)+'.jpg')
        			cut_picture(pict_srcpath, pict_despath,  right_x1, right_y1, right_x2, right_y2)
        print("{} create successfully!".format(patient))
        # sys.exit(0) 

        	       	
    f.close()
    print('complement!!!!!!!!')
        	 
        	
                # x_center = (data[i]['points'][0][0] + data[i]['points'][1][0]) / (2*wide)
                # y_center = (data[i]['points'][0][1] + data[i]['points'][1][1]) / (2 * high)
                # width = abs(data[i]['points'][0][0] - data[i]['points'][1][0]) / (wide)
                # height = abs(data[i]['points'][0][1] - data[i]['points'][1][1]) / (high)

                # f.write(str(des_label)+' '+str(x_center)+' '+str(y_center)+' '+str(width)+' '+str(height)+'\n')
			
            # print('exit')
            
            
            


if __name__ == '__main__':
    inpath = 'normal_annotation_final'
    outpath = 'D:\csy\\tumour-classification-3d-cnn-PyTorch-master\labels\\normal_labels.txt'
    pict_inpath = 'normal_jpg'
    pict_outpath = 'D:\csy\\tumour-classification-3d-cnn-PyTorch-master\images'
    createlabel(inpath, outpath, pict_inpath, pict_outpath)

