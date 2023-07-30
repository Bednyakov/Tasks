class MyDict(dict):

    def get(self, key, default=None):
        return super().get(key, 0)


mydict = MyDict()

a = MyDict()
a['1'] = 1

print(a)
print(a.get('1'))








