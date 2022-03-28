# import paddle.fluid as fluid
import paddle
import numpy as np
import os
import matplotlib.pyplot as plt
# BUF_SIZE=500
# BATCH_SIZE=20

# #用于训练的数据提供器，每次从缓存中随机读取批次大小的数据
# train_reader = paddle.batch(
#     paddle.reader.shuffle(paddle.dataset.uci_housing.train(), 
#                           buf_size=BUF_SIZE),                    
#     batch_size=BATCH_SIZE)   
# #用于测试的数据提供器，每次从缓存中随机读取批次大小的数据
# test_reader = paddle.batch(
#     paddle.reader.shuffle(paddle.dataset.uci_housing.test(),
#                           buf_size=BUF_SIZE),
#     batch_size=BATCH_SIZE)  
    #设置默认的全局dtype为float64
paddle.set_default_dtype("float64")
#下载数据
print('下载并加载训练数据')
train_dataset = paddle.text.datasets.UCIHousing(mode='train')
eval_dataset = paddle.text.datasets.UCIHousing(mode='test')
train_loader = paddle.io.DataLoader(train_dataset, batch_size=32, shuffle=True)
eval_loader = paddle.io.DataLoader(eval_dataset, batch_size = 8, shuffle=False)

print('加载完成')

# 定义全连接网络
class Regressor(paddle.nn.Layer):
    def __init__(self):
        super(Regressor, self).__init__()
        # 定义一层全连接层，输出维度是1，激活函数为None，即不使用激活函数
        self.linear = paddle.nn.Linear(13, 1, None)
    
    # 网络的前向计算函数
    def forward(self, inputs):
        x = self.linear(inputs)
        return x

Batch=0
Batchs=[]
all_train_accs=[]
def draw_train_acc(Batchs, train_accs):
    title="training accs"
    plt.title(title, fontsize=24)
    plt.xlabel("batch", fontsize=14)
    plt.ylabel("acc", fontsize=14)
    plt.plot(Batchs, train_accs, color='green', label='training accs')
    plt.legend()
    plt.grid()
    plt.show()

all_train_loss=[]
def draw_train_loss(Batchs, train_loss):
    title="training loss"
    plt.title(title, fontsize=24)
    plt.xlabel("batch", fontsize=14)
    plt.ylabel("loss", fontsize=14)
    plt.plot(Batchs, train_loss, color='red', label='training loss')
    plt.legend()
    plt.grid()
    plt.show()

model=Regressor() # 模型实例化
model.train() # 训练模式
mse_loss = paddle.nn.MSELoss()
opt=paddle.optimizer.SGD(learning_rate=0.0005, parameters=model.parameters())

epochs_num=200 #迭代次数
for pass_num in range(epochs_num):
    for batch_id,data in enumerate(train_loader()):
        image = data[0]
        label = data[1]
        predict=model(image) #数据传入model
        # print(predict)
        # print(np.argmax(predict,axis=1))
        loss=mse_loss(predict,label)
        # acc=paddle.metric.accuracy(predict,label.reshape([-1,1]))#计算精度
        # acc = np.mean(label==np.argmax(predict,axis=1))
        
        if batch_id!=0 and batch_id%10==0:
            Batch = Batch+10
            Batchs.append(Batch)
            all_train_loss.append(loss.numpy()[0])
            # all_train_accs.append(acc.numpy()[0]) 
            print("epoch:{},step:{},train_loss:{}".format(pass_num,batch_id,loss.numpy()[0])  )      
        loss.backward()       
        opt.step()
        opt.clear_grad()   #opt.clear_grad()来重置梯度
paddle.save(model.state_dict(),'Regressor')#保存模型
draw_train_loss(Batchs,all_train_loss)

#模型评估
para_state_dict = paddle.load("Regressor") 
model = Regressor()
model.set_state_dict(para_state_dict) #加载模型参数
model.eval() #验证模式

losses = []
infer_results=[]
groud_truths=[]
for batch_id,data in enumerate(eval_loader()):#测试集
    image=data[0]
    label=data[1] 
    groud_truths.extend(label.numpy())    
    predict=model(image) 
    infer_results.extend(predict.numpy())      
    loss=mse_loss(predict,label)
    losses.append(loss.numpy()[0])
    avg_loss = np.mean(losses)
print("当前模型在验证集上的损失值为:",avg_loss)



#绘制真实值和预测值对比图
def draw_infer_result(groud_truths,infer_results):
    title='Boston'
    plt.title(title, fontsize=24)
    x = np.arange(1,20) 
    y = x
    plt.plot(x, y)
    plt.xlabel('ground truth', fontsize=14)
    plt.ylabel('infer result', fontsize=14)
    plt.scatter(groud_truths, infer_results,color='green',label='training cost') 
    plt.grid()
    plt.show()

draw_infer_result(groud_truths,infer_results)