import numpy as np

class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']

office_order = ['mouse', 'laptop', 'keyboard', 'book', 'potted plant', 'cup', 'chair', 'vase']
office_order_index = ['65', '64', '67', '74', '59', '42', '57', '76']
print(class_names.index('vase'))
result_order=[]
iword = 'keyboard'
for j in range(len(office_order)):
    if iword == office_order[j]:
        result_order.append(office_order[j])

numresult_order = []

for p in range(len(result_order)):
    
    num = class_names.index(result_order[p])
    numresult_order.append(num)

xx = []
yy = []
for q in range(len(office_order_index)):
    for m in range(len(numresult_order)):
        if int(office_order_index[q]) == numresult_order[m]:
            
            xx.append(q)
            yy.append(m)

target = numresult_order[min(yy)]
s=np.array(office_order_index)
ss = np.where(s==target)
print(s,ss)