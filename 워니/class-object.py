class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self, to_name):
        print('hi '+to_name+' 내 이름은 '+ self.name + ' 야 '+str(self.age)+'살')

class police(person):
    def arrest(self, to_arrest):
        print(to_arrest+' 넌 체포되었다다')

class teacher(person):
    def lesson(self, to_lesson):
        print('이번시간은 '+ to_lesson)


p = person('미자', 25)
p.say('여희')

h = person('지수', 28)
h.say('철이')
h = police('지수', 1)
h.arrest('미자')

i = person('소현', 32)
i.say('지아')