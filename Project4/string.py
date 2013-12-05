import sys


samplestring = "0 1A-2B-3C-4D-5E-6F 11-22-33-44-55-66"
double_Array = [[0 for x in xrange(1)] for x in xrange(3)]


print(double_Array)


split= samplestring.split(" ")
print(split)
# index = 0
# i = 0
# #loop
# while (i < 4):
# 	j = 0
# 	while (j < 4):
# 		double_Array[j] = (split[index])
# 		index +=1
# 		j+=1
# 	i+=1
# return double_Array
# double_Array[0] = split[0]
# double_Array[1] = split[1]
# double_Array[2] = split[2]

# incoming_interface = double_Array[0]
# print(incoming_interface)
# source_Mac = double_Array[1]
# print (source_Mac)
# destination_Mac = double_Array[2]
# print(destination_Mac)

index = 0
j = 0
len1=len(split)
print(len1)
len2 = len(double_Array)
print(len2)

for list in split:
	
	double_Array[j] = split[j]
	j=j+1
print(double_Array)


