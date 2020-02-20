with open ("input/a_example.in", "rt") as input_file:
    content = input_file.readlines()

for i in range(len(content)):
    content[i] = content[i].strip("\n")

input_1 = [int(k) for k in content[0].split(' ')]
input_2 = [int(k) for k in content[1].split(' ')]

print(input_1)
print(input_2)

with open("output/output_h.txt", "a") as output_file:
    output_file.write('Hello\n')