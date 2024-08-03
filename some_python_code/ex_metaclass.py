class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self. class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = 'title'
    content = 'content'
    photo = 'photo'


w = Women()
print(w.__dict__)
# using for API ORM Django
