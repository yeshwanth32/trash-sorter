import cv2
import matplotlib.pyplot as plt
import cv2
import numpy as np
import tensorflow as tf
import os, subprocess, re
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import shutil
import json
from google.protobuf import text_format
import pprint
import random
from pathlib import Path
from google.protobuf import text_format
thres = 0.45 # Threshold to detect object
nms_threshold = 0.2
# cap = cv2.VideoCapture(0)
# # cap.set(3,1280)
# # cap.set(4,720)
# # cap.set(10,150)

# # cap = cv2.VideoCapture(0)
# # cap.set(3,1280)
# # cap.set(4,720)
# # cap.set(10,70)

# classNames= []
# classFile = r'C:\Users\yeshw\OneDrive\Desktop\Desktop\Umass\UMass\Umass\CICS256\final_project\trash_sorter\trash-sorter\coco.names'
# with open(classFile,'rt') as f:
#     classNames = f.read().rstrip('\n').split('\n')
# print(len(classNames))
# #image =cv2.imread(r"C:\Users\yeshw\OneDrive\Desktop\Desktop\Umass\UMass\Umass\CICS256\final_project\trash_sorter\trash-sorter\lena.png", cv2.IMREAD_COLOR)
# # cv2.imshow("OpenCV Image Reading", image)
# # cv2.waitKey(0)
# # plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# # plt.show()
# configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
# weightsPath = 'frozen_inference_graph.pb'

# net = cv2.dnn_DetectionModel(weightsPath,configPath)
# net.setInputSize(320,320)
# net.setInputScale(1.0/ 127.5)
# net.setInputMean((127.5, 127.5, 127.5))
# net.setInputSwapRB(True)

# while True:
#     success,img = cap.read()
#     classIds, confs, bbox = net.detect(img,confThreshold=thres)
#     bbox = list(bbox)
#     confs = list(np.array(confs).reshape(1,-1)[0])
#     confs = list(map(float,confs))
#     #print(type(confs[0]))
#     #print(confs)

#     indices = cv2.dnn.NMSBoxes(bbox,confs,thres,nms_threshold)
#     print(indices)

#     for i in indices:
#         #i = i[0]
#         box = bbox[i]
#         x,y,w,h = box[0],box[1],box[2],box[3]
#         cv2.rectangle(img, (x,y),(x+w,h+y), color=(0, 255, 0), thickness=2)
#         cv2.putText(img,classNames[classIds[i][0]-1].upper(),(box[0]+10,box[1]+30),
#         cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

#     cv2.imshow("Output",img)
#     cv2.waitKey(1)

pb_path = 'ssd_mobilenet_v2_taco_2018_03_29.pb'
def reconstruct(pb_path):
    if not os.path.isfile(pb_path):
        print("Error: %s not found" % pb_path)

    print("Reconstructing Tensorflow model")
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.compat.v1.GraphDef()
        with tf.io.gfile.GFile(pb_path, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    print("Success!")
    return detection_graph
detection_graph = reconstruct(pb_path=pb_path)
def image2np(image):
    (w, h) = image.size
    return np.array(image.getdata()).reshape((h, w, 3)).astype(np.uint8)

def image2tensor(image):
    npim = image2np(image)
    return np.expand_dims(npim, axis=0)
def detect(detection_graph, test_image_path):
    with detection_graph.as_default():
        gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.01)
        with tf.compat.v1.Session(graph=detection_graph,config=tf.compat.v1.ConfigProto(gpu_options=gpu_options)) as sess:
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            image = Image.open(test_image_path)
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: image2tensor(image)}
            )

            npim = image2np(image)
            # vis_util.visualize_boxes_and_labels_on_image_array(
            #     npim,
            #     np.squeeze(boxes),
            #     np.squeeze(classes).astype(np.int32),
            #     np.squeeze(scores),
            #     category_index,
            #     use_normalized_coordinates=True,
            #     line_thickness=15)
            # plt.figure(figsize=(12, 8))
            # plt.imshow(npim)
            # plt.show()

detect(detection_graph, 'C:\\Users\\yeshw\\OneDrive\\Desktop\\Desktop\\Umass\\UMass\\Umass\\CICS256\\final_project\\trash_sorter\\trash-sorter\\lena.png')
import cv2
import numpy as np
thres = 0.45 # Threshold to detect object
nms_threshold = 0.2
cap = cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
# cap.set(10,150)

classNames= []
classFile = r'C:\Users\yeshw\OneDrive\Desktop\Desktop\Umass\UMass\Umass\CICS256\final_project\trash_sorter\trash-sorter\coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
print(len(classNames))

#print(classNames)
#configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'
# configPath = 'ssd_mobilenet_v2_taco_2018_03_29.pb'
# weightsPath = 'frozen_inference_graph_taco.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1,-1)[0])
    confs = list(map(float,confs))
    #print(type(confs[0]))
    #print(confs)

    indices = cv2.dnn.NMSBoxes(bbox,confs,thres,nms_threshold)
    #print(indices)
    #break

    for i in indices:
        #i = i[0]
        box = bbox[i]
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(img, (x,y),(x+w,h+y), color=(0, 255, 0), thickness=2)
        cv2.putText(img,classNames[classIds[i]-1].upper(),(box[0]+10,box[1]+30),
        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    cv2.imshow("Output",img)
    cv2.waitKey(1)