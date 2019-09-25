import json
import os

PICTURE_WIDE = 384
PICTURE_HIGH = 384

def createlabel(inpath, outpath):
    if os.path.exists(outpath):
        print('find file {}'.format(outpath))

    patients_name = os.listdir(inpath)
    for patient in patients_name:
        jsonfilelist = os.listdir(os.path.join(inpath, patient))
        for patientjson in jsonfilelist:
            jsonpath = os.path.join(inpath, patient, patientjson)
            jsonname = patientjson.split('.')[0]
            # print(jsonname)

            f = open(os.path.join(outpath, jsonname+'.txt'), 'w')
            with open(jsonpath, 'r', encoding='utf-8') as file:
                data = json.load(file)['shapes']
                # print(data)
            for i in range(len(data)):
                # print(data[i]['points'])
                if data[i]['label'] == 'tumear':
                    des_label = 0
                else:
                    des_label = 1

                x_center = (data[i]['points'][0][0] + data[i]['points'][1][0]) / (2*PICTURE_WIDE)
                y_center = (data[i]['points'][0][1] + data[i]['points'][1][1]) / (2 * PICTURE_HIGH)
                width = abs(data[i]['points'][0][0] - data[i]['points'][1][0]) / (PICTURE_WIDE)
                height = abs(data[i]['points'][0][1] - data[i]['points'][1][1]) / (PICTURE_HIGH)

                f.write(str(des_label)+' '+str(x_center)+' '+str(y_center)+' '+str(width)+' '+str(height)+'\n')
            f.close()
            print("%s .txt create successfully!"%jsonname)


if __name__ == '__main__':
    inpath = 'tumour_annotation'
    outpath = 'PyTorch-YOLOv3-master\data\custom\labels'
    pict_inpath = ''
    pict_outpath = 'PyTorch-YOLOv3-master\data\custom\'
    createlabel(inpath, outpath, pict_inpath, pict_outpath)