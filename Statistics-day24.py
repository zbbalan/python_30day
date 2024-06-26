import numpy as np
print('numpy:',np.__version__)
print(dir(np))
python_list = [1,2,3,4,5,6,7,8,9,10]
tow_dim_list = [[1,2,3],[4,5,6],[7,8,9]]
numpy_array_list = np.array(python_list)
print(numpy_array_list)
numpy_arry_list2 = np.array(tow_dim_list)
print(numpy_arry_list2)

numpy_list2 = [1,2,3,4,5,6]
numpy_arry_list3 = np.array(numpy_list2,dtype=float)  ###[1. 2. 3. 4. 5. 6.
print(numpy_arry_list3)
numpy_arry_list4 = np.array(numpy_list2,dtype=bool) ##[ True  True  True  True  True  True]
print(numpy_arry_list4)

#将numpy数组转换为列表
np_to_list =numpy_arry_list3.tolist()
print(np_to_list)
print(numpy_arry_list3.tolist())
##从元组创建numpy数组
python_typut = (1,2,3,4,5,6)
numpy_arry_list5 = np.array(python_typut)
print(numpy_arry_list5)

#shape方法将数组的形状作为元组提供。第一个是行，第二个是列。如果数组是一维的，则返回数组的大小
nums = np.array([1,2,3,4,5,6,7,8,9,10])
print(nums.shape)
nums2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(nums2.shape)
#numpy数组的数据类型
nums3 = [-3, -2, -1, 0, 1, 2,3]
print(np.array(nums3))
print(np.array(nums3).dtype)
print(np.array(nums3,dtype=float))
print(np.array(nums3,dtype=float).dtype)
##numpy数组的运算
numpy_array_num = np.array([1,2,3,4,5,6,7,8])
print(numpy_array_num)
the_plus_nums = numpy_array_num * 10
print(the_plus_nums)
##numpy数组转换
numpy_num_liat = np.array([1,2,3,4,5,6,7,8],dtype=float)
print(numpy_num_liat)
numpy_num_liat2 = np.array(numpy_array_list,dtype=int)
print(numpy_num_liat2)
##从numpy中获取元素
numpy_num_list3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(numpy_num_list3[0])
print(numpy_num_list3[1])
print(numpy_num_list3[2])
print(numpy_num_list3[0][2]) ##3
print(numpy_num_list3[:,0]) ##[1 4 7]
print(numpy_num_list3[:,1]) ##[2 5 8]
##从numpy中切片
numpy_num_list4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(numpy_num_list4[0:2]) ##[[1 2 3]
print(numpy_num_list4[0:2,1:3]) ##[[2 3] [5 6]]
##反转numpy数组
print(numpy_num_list4[::-1]) ##[[7 8 9] [4 5 6] [1 2 3]]
print(numpy_num_list4[:,::-1]) ##[[3 2 1] [6 5 4] [9 8 7]]
##更改值
numpy_num_list4[1,2] = 55
print(numpy_num_list4) ##[[1 2 3] [4 5 55] [7 8 9]]
#生成随机数
radom_nums = np.random.random()
print(radom_nums)
radom_nums2 = np.random.random(3)
print(radom_nums2)
radom_nums3 = np.random.random((3,3))
print(radom_nums3)
radom_nums4 = np.random.randint(0,5)
print(radom_nums4)
radom_nums5 = np.random.randint(2,10,size=8)
print(radom_nums5)
##numpy矩阵
for_you_num_martix = np.matrix(np.ones((3,3)),dtype=int)
print(for_you_num_martix)




