import numpy as np
import time

def quicksort(a):
    if len(a) <= 1:
        return a  
    a = list(a)
    left  = [x for x in a[1:] if x <= a[0]]  
    right = [x for x in a[1:] if x >  a[0]] 
    return quicksort(left) + [a[0]] + quicksort(right)

seqLen = 1000000
np.random.seed(123)
arry = np.random.rand(1, seqLen)[0]
start = time.clock()
arrySeq = np.array(quicksort(arry))
end = time.clock()
print("矩神快速排序用时：",round(end-start,2))


def quickSort(arrySeq):
	def seg(lowC,highC):
		if lowC>=highC:
			return
		flag = arrySeq[highC]
		lowCurse = lowC-1
		for highCurse in range(lowC,highC+1):
			if arrySeq[highCurse]>flag:
				pass
			else:
				lowCurse+=1
				if lowCurse < highCurse:
					arrySeq[lowCurse],arrySeq[highCurse] = arrySeq[highCurse],arrySeq[lowCurse]				 
		lowCurse+=1
		if lowCurse<highC:
			arrySeq[lowCurse],arrySeq[highC] = arrySeq[highC],arrySeq[lowCurse]
		seg(lowC,lowCurse-2)
		seg(lowCurse,highC)

	seg(0,len(arrySeq)-1)
	return 1
np.random.seed(123)
arry = np.random.rand(1, seqLen)[0]
start = time.clock()
arrySeq = quickSort(arry)
end = time.clock()
print("略屌快速排序用时：",round(end-start,2))
