import os


def found_and_save():
    #ищем пути до папок с логами
    paths = []
    path0 = input("введите путь: ")
    paths = os.listdir(path0)
    path0 += "\ "
    path0 = path0[:-1]
    txt = ""
    for path in paths:
        #проверяем папку на наличие файла Tokens.txt в директории Discord
        pathway = path0 + path + "\Discord\Tokens.txt"
        pathway.encode('unicode_escape')
        try:
            with open(pathway, 'r', encoding="utf-8") as file:
                lines = [line.strip() for line in file.readlines()]
        except Exception as e:
            continue
        for line in lines:
            txt+=f"{line}\n" #парсим все токены
    print(txt)
    #сохраняем результат
    with open("result.txt",'w',encoding="utf-8") as file:
        file.write(txt)
    a = input(f"All tokens have been parced\nДля выхода отправьте любое сообщение: ")

if __name__ == '__main__':
    found_and_save()