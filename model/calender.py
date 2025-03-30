class CustomDaytime:
    """
    Represents custom daytime - with custom measure units,
    for example starting from days till minutes or seconds
    Units are given by order.
    For example, common daytime would be in form:
    order = [days, hours, minutes, seconds]
    The measuer units should always be the same.
    This is why this is not suitable for usual calender with different amounts of days in monthes or years.
    For common calender, use for example extention class with both usual calender and this custom daytime support.
    The limit of very first units (for example days) is ignored.
    Not suitable for high performance logicks.
    """
    max_prefix = "max_"
    def __init__(self,*order,**units_and_limits):
        self.order = order
        self.positions_in_order = dict()
        for n, key in enumerate(self.order):
            self.positions_in_order[key] = n
            self.__setattr__(self.max_prefix+key, units_and_limits[key])
            self.__setattr__(key, 0)

    def clone_of_type(self):
        return CustomDaytime(*self.order,**dict(self.items()))

    def clone(self):
        cloned = self.clone_of_type()
        cloned.update(**dict(self.items()))
        return cloned

    def items(self):
        for key in self.order:
            yield key, getattr(self,key )

    def values(self):
        for key in self.order:
            yield getattr(self, key)


    def update(self, ** values):
        for key, value in values.items():
            assert key in self.__dict__
            assert isinstance(value, (int, float))
            setattr(self,key, value)

    def set(self, *values):
        for n, value in enumerate(values):
            key = self.order[n]
            setattr(self, key, value)


    def advance(self, key, value):
        order_of_key = self.positions_in_order[key]
        while value and order_of_key:
            old_value = getattr(self, key)
            new_value = old_value + value

            limit = getattr(self, self.max_prefix + key)

            value_left = new_value % limit
            rest = (new_value - value_left) // limit
            setattr(self,key, value_left)
            order_of_key-=1
            key = self.order[order_of_key]
            value = rest

        if value:
            setattr(self, key, getattr(self, key) + value)

    def __repr__(self):
        return "CustomDaytime(" + ", ".join(f"{key}:{value}" for key, value in self.items()) + ")"


    def __str__(self):
        return repr(self)








class DaytimeEvent:

    def __init__(self,name, details,begin,end):
        self.name = name
        self.details = details
        self.begin = begin
        self.end = end



class CalenderOfDays:

    def __init__(self,current_date):
        self.current_date = current_date
        self.events = []
        self.last_event_index = 0


    def advance(self, value):
        self.current_date.advance(value)

    def next_event_from_current_date(self):
        index = self.last_event_index
        while (index < len(self.events)):
            event = self.events[index]
            if self.current_date <= event.begin:
                return index, event

        return index, None

    def set_next_event_from_current_date(self):
        index, event = self.next_event_from_current_date()
        self.last_event_index = index

    def update_current_date_after_event(self):
        last_event = self.events[self.last_event_index]
        self.current_date = self.last_event.end




#-- test of common date:

date = CustomDaytime("days", "hours", "minutes", "seconds", days = 0, hours = 24, minutes = 60, seconds = 60)

date.set(1010,2,5,35)

print(date)

date.advance("minutes",60)
print(date)
date.advance("seconds",60)
print(date)
date.advance("seconds",25)
print(date)

date.advance("seconds",3601*24)
print(date)

date2 = date.clone()

print(date2)
