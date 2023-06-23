import collections

with open("links.txt", 'r') as f:
    file_data_str = f.read()
    print(file_data_str)

file_data_list = file_data_str.split('\n')[:-1]

print(file_data_list)

file_data_list = collections.Counter(file_data_list)
print(file_data_list)
