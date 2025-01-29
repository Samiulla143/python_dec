class plane:
    def land(self):
        print('plane is landing')
    def takeoff(self):
        print('plane takeoff')
class passenger(plane):
    def carry_passenger(self):
        print('plane carries passenger')
class cargo(plane):
    def carry_goods(self):
        print('plane carries goods')
class fighter(plane):
    def carry_weapons(self):
        print('carry weapons')

p=passenger()
p.land()
p.takeoff()
p.carry_passenger()

c=cargo()
c.land()
c.takeoff()
c.carry_goods()

f=fighter()
f.land()
f.takeoff()
f.carry_weapons()

