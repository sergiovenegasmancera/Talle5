import cv2
from camera_model import *
import numpy as np
import glob
import os
import json

if __name__ == '__main__':
    json_file = r"C:\Users\Personal-Pc\Desktop\Proc. de imagenes\Taller 5\Imagenes_CEL\calibration.json"
    with open(json_file) as fp:
        json_data = json.load(fp)

    # intrinsics parameters
    width = 960
    height = 720

    #extrinsics parameters
    R = set_rotation(json_data["tilt"], json_data["pan"], 0)
    t = np.array([0, -1*json_data["d"], json_data["h"]])

    # create camera
    camera = projective_camera(json_data["K"], width, height, R, t)

    square_3D1 = np.array([[0, 0, 0], [1, 0, 0], [1, -1, 0], [0, -1, 0]])
    square_3D2 = np.array([[0, 0, 1], [1, 0, 1], [1, -1, 1], [0, -1, 1]])
    line1 = np.array([[0, 0, 1], [1, 0, 1]])

    square_2D = projective_camera_project(square_3D1, camera)
    square_2D2 = projective_camera_project(square_3D2, camera)

    image_projective = 255 * np.ones(shape=[camera.height, camera.width, 3], dtype=np.uint8)

    cv2.line(image_projective, (square_2D[0][0], square_2D[0][1]), (square_2D[1][0], square_2D[1][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D[1][0], square_2D[1][1]), (square_2D[2][0], square_2D[2][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D[2][0], square_2D[2][1]), (square_2D[3][0], square_2D[3][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D[3][0], square_2D[3][1]), (square_2D[0][0], square_2D[0][1]), (200, 1, 255), 3)

    cv2.line(image_projective, (square_2D2[0][0], square_2D2[0][1]), (square_2D2[1][0], square_2D2[1][1]),(200, 1, 255), 3)
    cv2.line(image_projective, (square_2D2[1][0], square_2D2[1][1]), (square_2D2[2][0], square_2D2[2][1]),(200, 1, 255), 3)
    cv2.line(image_projective, (square_2D2[2][0], square_2D2[2][1]), (square_2D2[3][0], square_2D2[3][1]),(200, 1, 255), 3)
    cv2.line(image_projective, (square_2D2[3][0], square_2D2[3][1]), (square_2D2[0][0], square_2D2[0][1]),(200, 1, 255), 3)

    cv2.line(image_projective, (square_2D[0][0], square_2D[0][1]), (square_2D2[0][0], square_2D2[0][1]), (200, 1, 255),3)
    cv2.line(image_projective, (square_2D[1][0], square_2D[1][1]), (square_2D2[1][0], square_2D2[1][1]), (200, 1, 255),3)
    cv2.line(image_projective, (square_2D[2][0], square_2D[2][1]), (square_2D2[2][0], square_2D2[2][1]), (200, 1, 255),3)
    cv2.line(image_projective, (square_2D[3][0], square_2D[3][1]), (square_2D2[3][0], square_2D2[3][1]), (200, 1, 255),3)

    cv2.imshow("Image", image_projective)
    cv2.waitKey(0)

