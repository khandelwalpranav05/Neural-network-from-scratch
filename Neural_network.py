import numpy as np

def sig(x,derive=False):
	if(derive==True):
		return x*(1-x)

	return 1/(1+np.exp(-x))

X = np.array([[0,0,1],
			 [0,1,1],
			 [1,0,1],
			 [1,1,1]])

y = np.array([[0],
			  [1],
			  [1],
			  [0]])

np.random.seed(1)

#synapses
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

for j in range(6000):
    
    layer0 = X
    layer1 = sig(np.dot(layer0,syn0))
    layer2 = sig(np.dot(layer1,syn1))
    
    layer2_error = y - layer2
    
    if(j % 1000) == 0:
        print('Error ' + str(np.mean(np.abs(layer2_error))))
        
    layer2_delta = layer2_error*sig(layer2,derive = True)
    
    layer1_error = layer2_delta.dot(syn1.T)
    
    layer1_delta = layer1_error*sig(layer1,derive = True)
    
    syn1 += layer1.T.dot(layer2_delta)
    syn0 += layer0.T.dot(layer1_delta)
    
