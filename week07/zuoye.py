"""
具体要求：
1、定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化。
2、动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，
    是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
3、猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。
4、动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
"""
from abc import  ABCMeta, abstractmethod

class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.__animals = set()

    def add_animal(self,animal):
        if animal not in self.__animals:
            self.__animals.add(animal)
            return True
        return False

    def __getattr__(self, item):
        return any(i.__class__.__name__ == item for i in self.__animals)

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, type, size, character, ferocious=False):
        self.name = name
        self.type = type
        self.size = size
        self.character = character
        self.ferocious = False

    @property
    def is_ferocious(self):
        if self.type == '食肉' and self.character == '凶猛' and self.size != '小':
            return self.ferocious is True

class Cat(Animal):
    sounds = "miao~~"
    def __init__(self,name, type, size, character, ferocious=False):
        super().__init__(name, type, size, character, ferocious)
        self.is_pet = True

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print(have_cat)
