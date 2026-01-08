path = input("Введите полный путь к файлу: ")  # c:\\WebServers\\home\\testsite\\www\\myfile.txt

last_index = path.rfind('\\')

if last_index != -1:
    filename = path[last_index + 1:]
else:
    filename = path

last_dot_index = filename.rfind('.')

namefile = filename[:last_dot_index] if last_dot_index != -1 else filename

print("Имя файла:",namefile)
