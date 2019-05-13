import os
import cv2

lst = ['src_old/%s'%x for x in os.listdir('src_old')]
o_lst = ['src/%s'%x for x in os.listdir('src_old')]

print(lst)
print('-----------------')
print(o_lst)

for i, one in enumerate(lst):
    img = cv2.imread(one, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (600, 800), cv2.INTER_AREA)
    cv2.imwrite(o_lst[i], img)
