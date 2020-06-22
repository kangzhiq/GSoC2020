# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:15:10 2020

@author: zhiqi
"""

import numpy as np
import cv2
import face_alignment
import pickle

import argparse
from tqdm import tqdm


def load_args():
    parser = argparse.ArgumentParser(description="Video2landmarks")
    parser.add_argument('--video_path', type=str, default='', help="Path of the video")
    parser.add_argument('--device', type=str, default='cpu', help="'cpu' or 'cuda'")
    parser.add_argument('--save_path', type=str, default=None, help="Path to save transformed frames")

    args = parser.parse_args()
    
    return args

def save_frames(video_path, frame_path):
    vidcap = cv2.VideoCapture(video_path)
    count = 0
    success,image = vidcap.read()
    while success:
      cv2.imwrite(frame_path + "frame%03d.jpg" % count, image) # save frame as JPEG file
      success,image = vidcap.read()           
      count += 1


def video2landmarks(video_path, save_path, device):           
    LMs = []    
    init_frame = []

    vidcap = cv2.VideoCapture(video_path)
    count = 0
    success,image = vidcap.read()
    u_max, v_max = image.shape[:2]
    while success:
        init_frame.append(image)
        success,image = vidcap.read()
        count += 1
    
    # Extracting landmarks
    print("Extracting landmarks:")
    fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device=device)
    for i in tqdm(range(len(init_frame)), position=0, leave=True):
        LMs.append(fa.get_landmarks(init_frame[i])[0])
        
    if save_path:
        with open(save_path+'landmarks.pickle', 'wb') as handle:
            pickle.dump(LMs, handle, protocol=pickle.HIGHEST_PROTOCOL)
            
    else:
        print("No save path!")
        return
        
    print("Landmarks saved at {}landmarks.pickle".format(save_path))
    
    

def main():
    args = load_args()
    print(args)
    video2landmarks(args.video_path,
                    save_path = args.save_path, 
                    device = args.device)
    

if __name__ == "__main__":
    main()