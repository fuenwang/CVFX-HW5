import os
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt
import imageio

def getHomography(lst):
    kp_lst = []
    des_lst = []
    orb = cv2.ORB_create()
    #orb = cv2.xfeatures2d.SIFT_create()
    #orb = cv2.xfeatures2d.SURF_create()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    #bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
    for one in lst:
        kp, d = orb.detectAndCompute(one, None)
        #kp_lst.append(np.array([x.pt for x in kp], np.float32))
        #print ([x.pt for x in kp])
        #exit()
        kp_lst.append(kp)
        des_lst.append(d)

    homo_lst = [np.eye(3).astype(np.float32)]
    [h, w, c] = lst[0].shape
    
    #center_idx = len(lst) // 2
    center_idx = 1
    center_img = lst[center_idx]
    valid_indice = []
    r_x = (230, 400)
    r_y = [260, 470]
    aaa = []
    for i, x in enumerate(kp_lst[center_idx]):
        if True:
            if x.pt[0] >= r_x[0] and x.pt[0] <= r_x[1] and x.pt[1] >= r_y[0] and x.pt[1] <= r_y[1]:
                valid_indice.append(i)
    tmp = np.zeros_like(center_img).astype(np.float32).copy() 
    for i in range(len(lst)):
        matches = bf.match(des_lst[i], des_lst[center_idx])
        matches = [x for x in matches if x.trainIdx in valid_indice]
        kp1 = [kp_lst[i][x.queryIdx] for x in matches]
        kp2 = [kp_lst[center_idx][x.trainIdx] for x in matches]
        kp1 = np.array([x.pt for x in kp1], np.float32)
        kp2 = np.array([x.pt for x in kp2], np.float32)


        H = cv2.findHomography(kp1, kp2, method=cv2.RANSAC)[0].astype(np.float32)
        #H = cv2.getPerspectiveTransform(kp1, kp2).astype(np.float32)
        #kp1 = np.concatenate([kp1, np.ones([kp1.shape[0], 1])], axis=1)
        #kp2 = np.concatenate([kp2, np.ones([kp2.shape[0], 1])], axis=1)
        #print kp1.shape
        #H = cv2.estimateRigidTransform(kp1, kp2, fullAffine=False)
        print H
        #continue
        #exit()
        new_img = cv2.warpPerspective(lst[i], H, (w, h))
        #tmp = tmp + new_img.astype(np.float32)
        '''
        plt.subplot('121')
        plt.imshow(center_img)
        plt.subplot('122')
        plt.imshow(new_img)
        plt.show()
        '''
        aaa.append(new_img)
    return aaa
lst = ['./src/%s' %x for x in sorted(os.listdir('./src')) if x.endswith('.jpg') and x.startswith('tt')]
img_lst = [cv2.imread(x, cv2.IMREAD_COLOR) for x in lst]
img_lst = [x[:,:,::-1] for x in img_lst][:]
print(lst)
h, w, c = img_lst[0].shape
aaa = getHomography(img_lst[:])
aaa = [x[100:-100, 100:-100, :] for x in aaa]
imageio.mimsave('ttt.gif', aaa)
'''
video=cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc('P','I','M','1'), frameSize=(w, h), fps=8)
for one in aaa:
    video.write(one)
video.release()
'''
