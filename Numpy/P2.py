import numpy as np
l = [[[1,2,3],[4,'5',6],[6,7,8]],[[1,2,3],[4,5,6],[6,7,8]]]
arr = np.array(l)
print(arr)
print("Dimesnion: .",arr.ndim)          #used to display the dimension of the array
print("Order: ",arr.shape)              #used to display the shape of the array(2 times 3X3 array)
print("Size: ",arr.size)                #used to display the number of elements
print("Item Size: ", arr.itemsize)      #used to display item size
print("DataType: ",arr.dtype)           #used to display the datatype of the array
