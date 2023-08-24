#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self,name1, name2):
        super().__init__(name1,name2)
        self.knowledge=list()
    
    def learn(self, string):
        self.knowledge.append(string)