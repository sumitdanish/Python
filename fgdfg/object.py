import os
import sys
import random

class Animal:
    __name = None
    __weight = 0
    __height = 0
    __sound = None

    def __init__(self, name, weight, height, sound):
        """

        :rtype : object
        """
        self.__name = name
        self.__weight = weight
        self.__height = height
        self.__sound = sound


    def set_name(self, name):
        self.__name = name

    def set_weight(self, weight):
        self.__weight = weight

    def set_height(self, height):
        self.__height = height

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilogram and say {}".format(self.__name,
                                                                self.__height,
                                                                self.__weight,
                                                                self.__sound)
cat = Animal('Jungli', 100, 123, 'Meow2')
print(cat.toString())


class Dog(Animal):
    __owner = None

    def __init__(self, name, weight, height, sound, owner):
        self.__owner = owner
        self.__animal_type = None
        super(Dog, self).__init__(name, weight, height, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    @property
    def toString(self):
        return "{} is {} cm tall and {} kilogram and say {} and owner {}".format(self.get_name(),
                                                                                 self.get_height(),
                                                                                 self.get_weight(),
                                                                                 self.get_sound(),
                                                                                 self.get_owner())


dog = Dog('Saddam', 'Jungli', 100, 123, 'Meow2')
print(dog.toString)