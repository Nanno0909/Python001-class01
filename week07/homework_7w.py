import abc

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, type, size, character):
        self.type = type
        self.size = ['small',' mid', 'big'] 
        self.character = character

    def is_ferocious(self):
        if (self.size == 'mid' or self.size == 'big') and self.type == 'meating' and self.character =='ferocious':
            self.ferocious = True
        else:
            self.ferocious = False

class Cat(Animal):

    voice = 'mew'

    def __init__(self, name, type, size, character):
        self.name = name
        super(Cat, self).__init__(type, size, character)

    def is_pet(self):
        return  not self.ferocious 
    
class Zoo(object):

    

    def __init__(self, name):
        self.name = name
        
    def add_animal(self, animal):
        list = []
        animal_id = id(animal)
        for i in list:
            if id(i) == id(animal):
                raise Exception('This animal has been repeated!')
            list.append(animal)

    def __getattr__(self, item):
        return False

               




	
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat') 