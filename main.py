input_data =open("input.txt","r")
data =input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
for n in range(0,43630):
 i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
    p = str(i)
output_data = open("output.txt","w")
output_data.write(p)
output_data.close()
input_data.close()