import math
input_data =open("input.txt","r")
data =input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
for n in range(0,43630):
    math.lcm(a, b) 
    p = math.lcm(a, b)
output_data = open("output.txt","w")
output_data.write(str(p))
output_data.close()
input_data.close()