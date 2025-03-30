class odict_lazy(dict):
    def __init__(self, name,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.name = name
        self.keys = list()
        self.to_sort = True
        self.overwrite = False
        #self.default_step = 1

    def __setitem__(self, key, value):
        assert self.overwrite  or key not in self, f"{self}: auto advance {key=} already present"

        self.keys.append(key)
        dict.__setitem__(self,key, value)
        #dict.__setitem__(self, value, key)

    def __getitem__(self, key):
        self.lazy_sort()
        return dict.__getitem__(self,key)


    def __delitem__(self, key):

        value = self[key]
        self.keys.remove(key)
        dict.__delitem__(self,key)
        #dict.__delitem__(self,value)
        return value

    def lazy_sort(self):
        if self.to_sort:
            self.keys.sort()
            self.to_sort = False


    def items(self):
        self.lazy_sort()
        for key in self.keys:
            yield key, dict.__getitem__(self,key)

    def values(self):
        self.lazy_sort()
        return [self[key] for key in self.keys]

    def get_keys(self):
        self.lazy_sort()
        return self.keys


    def __str__(self):
        return f"odict_lazy|{self.name}|"

    def __repr__(self):
        return f"odict_lazy|{self.name}|"

    def pp(self):
        print(f"--- { self} --- ")
        for k,v in self.items():
            print(f"{k}:{v}")


class odict(dict):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.keys = list()
        #self.default_step = 1

    def __setitem__(self, key, value):
        if key not in self:
            self.keys.append(key)
        dict.__setitem__(self,key, value)

    def sort(self):
        self.keys.sort()

    def __delitem__(self, key):
        dict.__delitem__(self,key)
        self.keys.remove(key)


    def items(self):
        for key in self.keys:
            yield key, dict.__getitem__(self,key)

    def items_list(self):
        return [(key, self[key]) for key in self.keys]

    def values(self):
        return [self[key] for key in self.keys]

    def __str__(self):
        return f"odict|{self.keys}|"

    def __repr__(self):
        return f"odict|{self.keys}|"

    def pp(self):
        print(f"--- { self} --- ")
        for k,v in self.items():
            print(f"{k}:{v}")
