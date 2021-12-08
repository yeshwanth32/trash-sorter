import cv2
import matplotlib.pyplot as plt
import cv2
import numpy as np
import tensorflow as tf
import os, subprocess, re
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
# import matplotlib
# matplotlib.use('GTK3Cairo')  # or 'GTK3Cairo'
import shutil
import json
from google.protobuf import text_format
import pprint
import random
from pathlib import Path
from google.protobuf import text_format
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
import cv2

import tkinter as tk
from PIL import ImageTk, Image

pb_path = 'ssd_mobilenet_v2_taco_2018_03_29.pb'
LABEL_PATH = "labelmap.pb.txt"
NCLASSES = 60

label_map = label_map_util.load_labelmap(LABEL_PATH)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NCLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

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
def image2np(image):
    (w, h) = image.size
    return np.array(image.getdata()).reshape((h, w, 3)).astype(np.uint8)

def image2tensor(image):
    npim = image2np(image)
    return np.expand_dims(npim, axis=0)

def detect_picture(detection_graph, test_image_path):
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
            print(np.squeeze(scores))
            npim = image2np(image)
            vis_util.visualize_boxes_and_labels_on_image_array(
                npim,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=30,
                min_score_thresh=.6)
            temp = [category_index.get(i) for i in classes[0]]
            print(temp)
            for i in range(0, len(temp)):
                if (temp[i] != None):
                    return temp[i]
            
            plt.figure(figsize=(12, 8))
            #cv2.imshow("Output",npim)
            plt.imshow(npim, interpolation='nearest')
            plt.savefig("taco_test.jpg")

trained_detection_graph = reconstruct('frozen_inference_graph_taco.pb')
detect_picture(trained_detection_graph, 'C:\\Users\\yeshw\\OneDrive\\Desktop\\Desktop\\Umass\\UMass\\Umass\\CICS256\\final_project\\trash_sorter\\trash-sorter\\cup.jpg')

if __name__ == "__main__":
    