import pydicom
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

####refer to https://blog.csdn.net/u011764992/article/details/84501300

INPUT_PATH = 'tumour'
OUT_PATH = 'tumour_jpg'


def dicom2jpg(img, low_window, high_window, save_path):
    lungwin = np.array([low_window * 1., high_window * 1.])
    new_img = (img - lungwin[0]) / (lungwin[1] - lungwin[0])
    new_img = (new_img * 255)
    cv2.imwrite(save_path + '.jpg', new_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


def dicom_to_jpg(input_path, out_path):
    if not os.path.exists(out_path):
        os.makedirs(out_path)
        print('Create path : {}'.format(out_path))

    patients_name = os.listdir(input_path)
    for patient in patients_name:

        if not os.path.exists(os.path.join(out_path, patient)):
            os.makedirs(os.path.join(out_path, patient))
        pictures_list = os.listdir(os.path.join(input_path, patient))

        for picture in pictures_list:
            picture_path = os.path.join(input_path, patient, picture)

            dicom_img = pydicom.read_file(picture_path)
            silence_num = dicom_img.InstanceNumber
            img_array = dicom_img.pixel_array

            high = np.max(img_array)
            low = np.min(img_array)
            out_jpg_path = os.path.join(out_path, patient, str(silence_num))

            dicom2jpg(img_array, low, high, out_jpg_path)
        print('Tranfroming {}\'s pictures successfully!'.format(patient))
    print('------------------------------------')
    print('Tranfrom complete!')

if __name__ == "__main__":
    input_path = INPUT_PATH
    out_path = OUT_PATH
    dicom_to_jpg(input_path, out_path)