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
n = np.array(30*[10*[[128,128,128]], 10*[[128,128,128]], 10*[[128,128,128]]]).astype(np.uint8)


def zadA1(image):
    return 255 - image

def testA1():
    if np.array_equal(zadA1(a), b):
        return True
    else:
        return False

#if(testA1()):
#    print("tak")
#else:
#    print("nie")
#print(testA1())
#print(b)
#
def zadA2(image, thr):
    img = image
    thr += 1
    return (255*np.minimum(((abs(img//thr)).astype(np.uint8)), 1)).astype(np.uint8)

def testA2():
    if np.array_equal(zadA2(c, 125), e):
        return True
    else:
        return False

def zadA3(image, gamma):
    img = image.astype(float)
    return np.rint((np.power(img/255.0, gamma)*255.0))

def testA3():
    if np.array_equal(zadA3(h, 2.0), np.rint(g)):
        return True
    else:
        return False
#    aa = zadA3(h, 2.0)
#    for i in range(0, 9):
#        for j in range(0, 9):
#            for k in range(0, 2):
#                if(aa[i][j][k] != g[i][j][k]):
#                    print( aa[i][j][k], g[i][j][k])

def zadA4(image):
    img = image.astype(float)
    bb = img[:, :, 0]*0.21+img[:, :, 1]*0.72+img[:, :, 2]*0.07
    nimg = np.dstack([bb, bb, bb])
    return np.rint(nimg)

def testA4():
    aa = zadA4(h)
    for l in range(0, 9):
        for j in range(0, 9):
            for k in range(0, 2):
                if(aa[l][j][k] != i[l][j][k]):
                    print( aa[l][j][k], i[l][j][k])
    if np.array_equal(zadA4(h), np.rint(i)):
        return True
    else:
        return False



def zadA5(image):
    imgb = image/255.0
    return np.rint((np.degrees(np.arctan2((np.sqrt(3.0)*(imgb[:, :, 1] - imgb[:, :, 2]))/2.0, ((2.0*imgb[:, :, 0]) - imgb[:, :, 1] - imgb[:, :, 2])/2.0)))%360)

def testA5():
    aa = zadA5(h)
    for l in range(0, 9):
        for j in range(0, 9):
            if(aa[l][j] != m[l][j]):
                print( aa[l][j], m[l][j])
    if np.array_equal(zadA5(h), np.rint(m)):
        return True
    else:
        return False


def zadA6(imagea, imageb, alpha):
    imga = imagea.astype(float)
    imgb = imageb.astype(float)
    return np.rint(imga*alpha+imgb*(1.0-alpha))
def testA6():
    aa = zadA6(a, b, 0.5)
    for l in range(0, 9):
        for j in range(0, 9):
            for k in range(0, 2):
                if(aa[l][j][k] != i[l][j][k]):
                    print( aa[l][j][k], n[l][j][k])
    if np.array_equal(zadA6(a, b, 0.5), np.rint(n)):
        return True
    else:
        return False
#
#print(zadA2(a), 30))
#print(c)
print(zadA6(a, b, 0.5))
#print(f)
print(testA6())
# python3 checker.pyc a.py zadA2
