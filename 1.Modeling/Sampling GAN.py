import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 정규분포로부터 데이터를 샘플링한다

data = pd.read_csv('compare.csv')
data = data.dropna()
realData = np.array([data['Count'],data['Search'], data['Index']]).T
realData.shape
realData
a=data['Count']
# log 안에 0이 들어가는 것을 방지한다.
def myLog(x):
    return tf.log(x + 1e-8)

# Discriminator Network을 생성한다.
nDInput = realData.shape[1]
nDHidden = 64
nDOutput = 1

tf.reset_default_graph()
xavier = tf.contrib.layers.xavier_initializer()
x = tf.placeholder(tf.float32, shape=[None, nDInput], name='x')
D_Wh = tf.Variable(xavier([nDInput, nDHidden]), name='D_Wh')
D_Bh = tf.Variable(tf.zeros(shape=[nDHidden]), name='D_Bh')
D_Wo = tf.Variable(xavier([nDHidden, nDOutput]), name='D_Wo')
D_Bo = tf.Variable(tf.zeros(shape=[nDOutput]), name='D_Bo')
thetaD = [D_Wh, D_Bh, D_Wo, D_Bo]

# Generator Network을 생성한다
nGInput = 8
nGHidden = 64
nGOutput = nDInput

z = tf.placeholder(tf.float32, shape=[None, nGInput], name='z')
G_Wh = tf.Variable(xavier([nGInput, nGHidden]), name='G_Wh')
G_Bh = tf.Variable(xavier(shape=[nGHidden]), name='G_Bh')
G_Wo = tf.Variable(xavier([nGHidden, nGOutput]), name='G_Wo')
G_Bo = tf.Variable(xavier(shape=[nGOutput]), name='G_Bo')
thetaG = [G_Wh, G_Bh, G_Wo, G_Bo]

def Discriminator(x):
    D_Ho = tf.nn.relu(tf.matmul(x, D_Wh) + D_Bh)
    D_Out = tf.matmul(D_Ho, D_Wo) + D_Bo
    return tf.nn.sigmoid(D_Out)

def Generator(z):
    G_Ho = tf.nn.relu(tf.matmul(z, G_Wh) + G_Bh)
    G_Out = tf.matmul(G_Ho, G_Wo) + G_Bo
    return G_Out

def getNoise(m, n=nGInput):
    z = np.random.uniform(-1., 1., size=[m, n])
    return z

# 각 Network의 출력값
Gz = Generator(z)
Dx = Discriminator(x)
DGz = Discriminator(Gz)

# Loss function : 위 논문의 Section 3. 식 - (1)
D_loss = -tf.reduce_mean(myLog(Dx) + myLog(1 - DGz))
G_loss = -tf.reduce_mean(myLog(DGz)) # G_Loss는 이렇게 쓰는 것이 더 좋다

trainD = tf.train.AdamOptimizer(0.0001).minimize(D_loss, var_list = thetaD)
trainG = tf.train.AdamOptimizer(0.0001).minimize(G_loss, var_list = thetaG)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

histLossD = []      # Discriminator loss history 저장용 변수
histLossG = []      # Generator loss history 저장용 변수
histKL = []         # KL divergence history 저장용 변수
nBatchCnt = 5       # Mini-batch를 위해 input 데이터를 n개 블록으로 나눈다.
nBatchSize = int(realData.shape[0] / nBatchCnt)  # 블록 당 Size
nK = 1              # Discriminator 학습 횟수 (위 논문에서는 nK = 1을 사용하였음)
k = 0

for i in range(100): #기본값 10000, 
    # Mini-batch 방식으로 학습한다
    np.random.shuffle(realData)
    
    for n in range(nBatchCnt):
        # input 데이터를 Mini-batch 크기에 맞게 자른다
        nFrom = n * nBatchSize
        nTo = n * nBatchSize + nBatchSize
        
        # 마지막 루프이면 nTo는 input 데이터의 끝까지.
        if n == nBatchCnt - 1:
            nTo = realData.shape[0]
               
        # 학습 데이터를 준비한다
        bx = realData[nFrom : nTo]
        bz = getNoise(m=bx.shape[0], n=nGInput)

        _, lossDHist = sess.run([trainD, D_loss], feed_dict={x : bx, z : bz})
        _, lossGHist = sess.run([trainG, G_loss], feed_dict={x : bx, z : bz})
    
    # 100번 학습할 때마다 Loss, KL의 history를 보관해 둔다
    if i % 100 == 0:
        histLossD.append(lossDHist)
        histLossG.append(lossGHist)
        print("%d) D-loss = %.4f, G-loss = %.4f" % (i, lossDHist, lossGHist))

plt.figure(figsize=(6, 3))
plt.plot(histLossD, label='Loss-D')
plt.plot(histLossG, label='Loss-G')
plt.legend()
plt.title("Loss history")
plt.show()

# 가짜 데이터 생성
fakeData = sess.run(Gz, feed_dict={z : getNoise(m=realData.shape[0])})
print(fakeData)

qq = pd.DataFrame(fakeData)
qq.corr()
qq.to_csv('sample2.csv')
