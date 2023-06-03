def logwriter(doc):
    with open(doc, 'r', encoding='UTF-8') as file, \
            open('registrations_good.log', 'w', encoding='UTF-8') as good_log, \
            open('registrations_bad.log', 'w', encoding='UTF-8') as bad_log:
        for line in file:
            try:
                reg_list = line.split()
                if len(reg_list) < 3:
                    raise IndexError
                if reg_list[0].isalpha() == False:
                    raise NameError
                if '@' not in reg_list[1] or '.' not in reg_list[1]:
                    raise SyntaxError
                if 99 < int(reg_list[2]) or int(reg_list[2]) < 0:
                    raise ValueError
            except IndexError:
                bad_log.writelines(str(line) + '\t(!)НЕ присутствуют все три поля\n')
            except NameError:
                bad_log.writelines(str(line) + '\t(!)Поле «Имя» содержит НЕ только буквы\n')
            except SyntaxError:
                bad_log.writelines(str(line) + '\t(!)Поле «Имейл» НЕ содержит @ и . (точку)\n')
            except ValueError:
                bad_log.writelines(str(line) + '\t(!)Поле «Возраст» НЕ является числом от 10 до 99\n')
            else:
                good_log.writelines(str(line))

logwriter('registrations.txt')
