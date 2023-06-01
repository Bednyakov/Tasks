
file = open('text.txt', 'r', encoding='UTF-8')
text = file.read()
abc = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
uniq_symb = {}
count = 0

for i in text.lower():
    if i in abc:
        count += 1
        if i not in uniq_symb:
            uniq_symb[i] = 1
        else:
            uniq_symb[i] += 1

for k, v in uniq_symb.items():
    uniq_symb[k] = round((v / count), 3)

res = [(k, v) for k, v in uniq_symb.items()]
res = sorted(res, key=lambda i:i[0])
res = sorted(res, key=lambda i:i[1], reverse=True)

new_file = open('analysis.txt', 'w', encoding='UTF-8')
for i in res:
    new_file.writelines(str(i) + '\n')

file.close()
new_file.close()


