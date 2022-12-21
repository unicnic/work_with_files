def count_str_file (file_name):
    count_str_file = 0
    with open(file_name, 'r', encoding='utf8') as f:
        for line in f:
            count_str_file += 1
    return count_str_file

def get_text (file_name):
    f = open(file_name, 'r', encoding='utf8')
    text = f.readlines()
    return text

def sort_list_file_size (file_list):
    sort_list_file_size = []
    for file in file_list:
        sort_list_file_size.append([count_str_file(file), file])
    sort_list_file_size.sort()

    return sort_list_file_size

def join_files (file_list):
    for count_str, file_name in sort_list_file_size(file_list):
            with open(file_name, 'r', encoding='utf8') as f:
                res = open('res.txt', 'a', encoding='utf8')
                string = file_name + '\n' + str(count_str) + '\n' + "".join(get_text(file_name)) + '\n'
                res.write(string)
                res.close()

join_files(['1.txt', '2.txt', '3.txt'])
