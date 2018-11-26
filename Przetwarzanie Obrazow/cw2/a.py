import numpy as np

a = np.array(30*[10*[[255,0,0]], 10*[[0,255,0]], 10*[[0,0,255]]])
b = np.array(30*[10*[[0,255,255]], 10*[[255,0,255]], 10*[[255,255,0]]])
#print(a)


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
#def zadA2(image, thr):
#    return 255*(np.min((image//thr), 1))
#
#def zadA4(image):
#    return np.rint(image[:, :, 0] * 0.21 + image[:, :, 1] * 0.72 + image[:, :, 2] * 0.07)
#
#print(zadA2(a), 30))

# python3 checker.pyc a.py zadA1
