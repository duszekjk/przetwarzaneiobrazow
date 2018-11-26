import numpy as np

a = np.array(30*[10*[[255,0,0]], 10*[[0,255,0]], 10*[[0,0,255]]]).astype(np.uint8)
b = np.array(30*[10*[[0,255,255]], 10*[[255,0,255]], 10*[[255,255,0]]]).astype(np.uint8)
c = np.array(30*[10*[[120,120,0]], 10*[[120,130,0]], 10*[[0,130,140]]]).astype(np.uint8)
d = np.array([[[255, 0, 0], [255, 0, 0], [255, 0, 0]],
             [[0, 255, 0], [0, 255, 0], [0, 255, 0]],
             [[0, 0, 255], [0, 0, 255], [0, 0, 255]]]).astype(np.uint8)
e = np.array(30*[10*[[0,0,0]], 10*[[0,255,0]], 10*[[0,255,255]]]).astype(np.uint8)
f = np.array([[  0,  10, 100, 255]], dtype=np.uint8)
g = np.array(30*[10*[[10.2,0.,0.]], 10*[[0.,10.2,0.]], 10*[[0.,10.2,10.2]]])
h = np.array(30*[10*[[51,0,0]], 10*[[0,51,0]], 10*[[0,51,51]]]).astype(np.uint8)
i = np.array(30*[10*[[11,11,11]], 10*[[37,37, 37]], 10*[[40,40,40]]]).astype(np.uint8)
m = np.array(30*[10*[0], 10*[120], 10*[180]]).astype(np.uint8)

hisim = np.array([5*[13], 5*[133], 5*[244], 5*[12], 5*[56]]).astype(np.uint8)
hisimb = np.array([5*[13], 5*[133], 5*[244], 5*[12], 5*[56], 5*[12], 5*[12], 5*[12], 5*[12], 5*[12]]).astype(np.uint8)
#hisimc = np.array([5*[1], 3*[127], 5*[254]]).astype(np.uint8)
hisimc = np.array([5*[13], 5*[133], 5*[244]]).astype(np.uint8)

def zadC1(image):
    hist, bins = np.histogram(image, density = True, bins = range(0,257))
    return hist
def testC1():
    testset = np.array(256*[0]).astype(float)
#    print(testset)
    testset[12] = 0.6
    testset[13] = 0.1
    testset[133] = 0.1
    testset[244] = 0.1
    testset[56] = 0.1
    if np.array_equal(zadC1(hisimb), testset):
        return True
    else:
        return False
def zadC2(image):
    return np.rint(255.0*(image-np.min(image))/(np.max(image)-np.min(image)))
def testC2():
    testset = np.array(256*[0]).astype(float)
    #    print(testset)
    testset[0] = 0.6
    testset[1] = 0.1
    testset[133] = 0.1
    testset[255] = 0.1
    testset[48] = 0.1
    if np.array_equal(zadC1(zadC2(hisimb)), testset):
        return True
    else:
        return False

def zadC3(image):
    D = np.cumsum(image/255.0)
    print(D)
    D0 = D[D != 0][0]
    N = ((D-D0)/(1.0-D0))
    return np.rint(255.0*(N/np.max(N)))
def testC3():
    testset = np.array(256*[0]).astype(float)
    #    print(testset)
    testset[0] = 0.6
    testset[1] = 0.1
    testset[133] = 0.1
    testset[255] = 0.1
    testset[48] = 0.1
    if np.array_equal(zadC1(zadC2(hisimb)), testset):
        return True
    else:
        return False
#print(zadA2(a), 30))
#print(c)
print(zadC3(hisimc))
print(zadC1(zadC3(hisimc)))
#print(testC2())
#print(f)
#print(testA4())
# python3 checker.pyc a.py zadA2
