from model.odict import odict_lazy

d = odict_lazy("test odict")
d.default_step = 10
d[2]= "two"
d[2.5] = "two half"
d[1] = "one"
#d[None] = "three"


d.pp()
del d[1]

#print("two" in d)
assert 2 in d
d.pp()
#del d[None]
d.pp()
#d[None] = "three"
d.pp()
