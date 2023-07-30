class TaskManager:
    def __init__(self):
        self.__stack = list()

    def new_task(self, task: str, num: int):
        count_hit = 0
        if len(self.__stack) > 0:
            for i in self.__stack:
                if i[0] == num:
                    i[1] = f'{i[1]}; {task}'
                    count_hit += 1
            if count_hit == 0:
                self.__stack.append([num, task])
        else:
            self.__stack.append([num, task])
        self.__stack = self.__sort_stack(self.__stack)


    def __sort_stack(self, stack: list):
        return sorted(stack, key=lambda task: task[0])

    def del_task(self, num):
        count = 0
        for i in self.__stack:
            if i[0] == num:
                self.__stack.pop(count)
                print(f'Задача {num} удалена.\n')
                break
            count += 1

    def __str__(self):
        print('Список задач:')
        result = ''
        for i in self.__stack:
            result += f'{i[0]} {i[1]}\n'
        return result


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.del_task(4)
print(manager)