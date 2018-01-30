import sys
print(sys.argv)

if len(sys.argv) != 3:
    sys.exit("terminated: number of arguments exceeded 3")

value = sys.argv[1]
frequency = sys.argv[2]

file = open("data.txt","a+")

for num in range(0,int(frequency)):
    file.write(value + " ")

file.close()
