with open ("/Users/hildebert/gits/hashcode/hashcode_problem/src/input/a_example.txt", "rt") as input_file:
    file_content = input_file.readlines()

for i in range(len(file_content)):
    file_content[i] = list(map(int, file_content[i].strip("\n").split(' ')))

print(len(file_content)/2-1)

input_data = {}
input_data['info'] = file_content[0]
for j in range(int(len(file_content)/2-1)):
    input_data['library_{}'.format(j)] = {}
    input_data['library_{}'.format(j)]['book_count'] = file_content[j+1][0]
    input_data['library_{}'.format(j)]['signup_time'] = file_content[j+1][1]
    input_data['library_{}'.format(j)]['max_shipment_per_day'] = file_content[j+1][2]
    input_data['library_{}'.format(j)]['book_scores'] = file_content[j+2]

print(input_data)

with open("/Users/hildebert/gits/hashcode/hashcode_problem/src/output/output_h.txt", "a") as output_file:
    output_file.write('Hello\n')