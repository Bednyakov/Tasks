#from zipfile import ZipFile
#my_zip = ZipFile('voyna-i-mir.zip')
#my_zip.extractall()

file = open('voyna-i-mir.txt', 'r', encoding='UTF-8')
symbols = dict()
abc = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
ru_abc = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()

for words in file.read().split():
    for sym in words:
        if sym.lower() in abc or sym.lower() in ru_abc:
            if sym not in symbols:
                symbols[sym] = 1
            else:
                symbols[sym] += 1

sorted_tuple = sorted(symbols.items(), key=lambda x: x[1], reverse=True)
result = open('result.txt', 'w', encoding='UTF-8')
result.write('Количество букв в отрывке романа "Война и мир: "\n')

for i in sorted_tuple:
    result.write(str(i[0]) + '-' + str(i[1]) + '\n')

file.close()
result.close()





