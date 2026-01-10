#--------------------------------------NUMPY------------------------------

# NUMPY is a powerful library in python used to create for numerical computing. it provides support for arrays , matrices, and large datasets, along with a wide range mathematical functions to operate on these arrays. the primary object in numpy is the ndarray , which stands for 'N-dimensional array'. its a high ly efficient , multidimensional container for homogeneous data 

# # key features of numpy 
# 1. Efficient multi-dimensional arrays (ndarrays)
# 2. Mathematical functions to perform operations on data efficiency 
# 3. Linear algebra operations like matrix multiplication, eigenvalue computation etc. 
# 4. Fourier transforms, signal processiing and random number generation  


# list1 = list(range(1,10))  # using list takes more time execute  
# import time 

# start = time.time() 
# new_list = [i*2 for i in list1] 
# end = time.time() 
# print(end-start)  


# import numpy as np  # numpy module takes less time to execute  (low level language in c-language)
# arr1 = np.range(1,100)  #here will happen vectorize operations (all will done at once)
# start = time.time() 
# arr2 = arr1*2 
# end = time.time() 
# print(end-start) 

# # --------------------------NUMPY------------------------------ 

# # 1. you can multiply a numpy array with number 
# # 2. Applying same discount to all the prices in the array 
# # 3. Working with mathematical operations 

# # WHY numpy faster ? 
# # written in c --> executes at compiled speed 
# # vectorized operations --> entire array processor at open
# # continous memory --> cpu caching is efficient 
# # no python loop overhead 

# #  COMPONENTS OF NUMPY 
# # -------------------------------
# # ndarray (N-dimensional array) 

# # The ndarray is the most important object in numpy. It is a grid of values, all of the same type, and indexed by a non-negative integers . 

# # creating an ndarray 
# #---------------------

# import numpy as np 
# print("==1D==") 
# arr = np.array([1,2,3,4,5]) # creating an ndarray froma python list 
# print(arr) 
# print('==2D==') 
# arr2d = np.array([[1,2,3],[4,5,6]]) # creating an 2D array 
# print(arr2d) 

# # ATTRIBUTES OF NDARRAY
# #-----------------------------------------
# # 1. ndarray.shape: tuple representing the dimensions of the array 
# # 2. ndarray.ddim: Number of dimensions of the array 
# # 3. ndarray.size: Total number of elements in the array 
# # 4. ndaaray.dtype: Datatype of the leemnts array elements 
# # 5. ndarray.itemsize: size in bytes of each element  

# import numpy as np 
# array2d = np.array([[1,2,3],[4,5,6]])
# print(arr2d.shape)
# print(arr2d.ndim) 
# print(arr2d.size)
# print(arr2d.dtype)
# print(arr2d.itemsize) 

# # ----ARRAY CREATION Functions 
# #--------------------------------------------
# a). np.zeroes() ---> creates an arrray of zeroes 

# inport numpy as np 
# arr = np.zeros((3,3)) # 3x3 array of zeros 
# print(arr) 

# b). np.ones() --> creates an array of ones 

# import numpy as np 
# arr = np.ones((2,4))  # 2x4 arrays of ones 
# print(arr) 

# c). np.arrange() --> cretaes an array with regular spaces values 

# import numpy as np 
# arr = np.arrange((0,10,2)) # from 0 to 10 with stpe2 
# print(arr) 

# d). nd.linspace() --> creates an array with eveenly spaced numbers over a specific range 

# import numpy as np 
# arr = np.linspace(0,10,5) # 5 numbers evenly spaced b/w 0 and 10 
# print(arr) 

# e). np.eye() --> cretaes an identity matrix 

# import numpy as np 
# arr = np.eye(3) # 3x3 identity matrix 
# print(arr) 

# # ARRAY Reshaping and Resizing 
# #----------------------------------- 
# a). np.reshape() - Reshape an array without changing its data 

# import numpy as np 
# arr = np.arrange(9)  #o to 9 elements  3 cross 3 
# reshaped = arr.reshaped (3,3) 
# print(reshaped) 

# b). np.ravel() - flatness a multidimensional array into a 1D array 

# import numpy as np 
# arr = np.array([[1,2],[3,4]])
# flatened = np.ravel(arr) 
# print(flatened) 

# c). np.resize() -resizes a array to a new shape, adding or removing elements 

# import numpy as np 
# arr = np.array([1,2,3,4]) 
# resized = np.resize(arr,2,3) 
# print(resized) 

# #-------ARRAY OPERATIONS-----
# #---------------------------
# a). Element-wise operations

# Numpy allows element-wise operations, including addition,substaraction,multiplication,division 

# import numpy as np 
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# print(arr1 + arr2) # addition 
# print(arr1 - arr2) # substraction 
# print(arr1 * arr2) # multiplication 
# print(arr1 / arr2) # division 

# b) . universal functions(ufuncs)

# Numpy provuides efficient functions for perfor,img oprations on arrays (such as trignometric, logaruthmic, and exponential functins) element-wise 
# import numpy as np 
# arr = np.array([1,4,9]) 
# print(np.sqrt(arr)) #square root 
# print(np.exp(arr)) # exponential 

# # Broadcasting 
# Broadcasting refers to have numpy handles element-wise binary operations with array of differenet smaller arrays are "broadcast"
# across larger arrays so that they have comptable shapes 

# # ---------Indexing and Slicing ---------------
# a). iNdexing 

# Numpy allows for advanced indexing enabling you to access individual elements or slices of arrays 

# import numpy as np 
# arr = np.array([10,20,30,40,50]) 
# print(arr[2]) # accessing an ele ments 

# b). Slicing 

# you can also since arrays, selecting portions of an array 

# import numpy as np 
# arr = np.array([1,2,3,4,5]) 
# print(arr[1:4]) # slicing an array 


# # ------------Random MODULE---------------------------
# # Numpy provides a random module for generating random numbers and performing random sampling 

# a). np.random.rand()  Generates random integers 

# import numpy as np  
# arr = np.random.rand(3,2) 
# print(arr)

# b). np.random.randint()  generates random integers 

# import numpy as np 
# arr = np.array(1,10, size=(3,3)) # random integers b/w 1 nad 10 
# print(arr) 

# c). np.random.choice()  - Randomly selectselements from an array 

# import numpy as np
# arr = np.array([1,2,3,4,5]) 
# chosen = np.random.choice(arr,3)
# print(chosen) 

# # ----Mathematical and statistical methods 
# #-----------------------------------------------
# a). sum, mean, and stanadrd deviation 
# sum: the total of all values in a dataset
# Mean: the average of all values in adataset, calculated by dividing the number of values 
# standard deviation: A measure of the standard spread or dispersion of values in a dataset, indicating how much the value defrom the mean 

# import numpy as np 
# arr = np.array([1,2,3,4,5]) 
# print(np.sum(arr)) 
# print(np.mean(arr)) 
# print(np.std(arr))

# b). Min, Max and argmin/argmax 

# min: the smallest value in a dataset 
# Max: the largest value in a dataset 
# Argmin/Argmax: The index of position of minimum.maximum value 

# import numpy as np 
# arr = np.array([10,20,30,40,50]) 
# #minimum and maximum 
# print(np.min(arr)) 
# print(np.max(arr)) 
# # Indices of min and max 
# print(np.argmin(arr)) 
# print(np.argmax(arr)) 

# # -----Linear Algebra Functions------------
# #------------------------------------------

# Numpy provides functions for linear algebra operators like matrix multiplication determinant, increase, eigenvalues etc 

# a). Matrix Multiplication 

# import numpy as np 
# A = np.array([[1,2],[3,4]]) 
# B = np.array([[5,6],[7,8]]) 
# #matrix product 
# result = np.dot(A,B) 

# b).Determinant and Inverse 

# import numpy as np 
# A = np.array([[1,2],[3,4]]) 

# #Determinant 
# det = np.linalg.det(A)
# print(det) 

# #Inverse 
# inv = np.linalg.inv(A) 
# print(inv)