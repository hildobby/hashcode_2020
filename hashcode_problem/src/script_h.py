with open ("/Users/hildebert/gits/hashcode/hashcode_problem/src/input/a_example.txt", "rt") as input_file:
    file_content = input_file.readlines()

for i in range(len(file_content)):
    file_content[i] = list(map(int, file_content[i].strip("\n").split(' ')))

input_data = {'books': file_content[0][0],
              'libraries': file_content[0][1],
              'deadline': file_content[0][2],
              'book_score': file_content[1]}

for j in range(int(len(file_content)/2-1)):
    input_data['library_{}'.format(j)] = {'book_count': file_content[j+2][0],
                                          'signup_time': file_content[j+2][1],
                                          'max_shipment_per_day': file_content[j+2][2],
                                          'book_scores': file_content[j+3]}

print(input_data)

curr_score = 0
signed_up_libraries = 0


print("The current score is ", curr_score)

#with open("/Users/hildebert/gits/hashcode/hashcode_problem/src/output/output_h.txt", "a") as output_file:
#    output_file.write('Hello\n')