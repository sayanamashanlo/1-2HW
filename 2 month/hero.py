
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase ):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        print(f" HERO NAME:{self.name}")

    def double_health(self):
        self.heath_points *= 2

    def __str__(self):
        return f"NICKNAME: {self.nickname}, SUPERPOWER: {self.superpower}, HEALTH POINTS: {self.health_points}"
    def __len__(self):
        return len(self.catchphrase)

Hero=SuperHero("Tony Starck', 'Iron Man', 'гений, миллиардер, плэйбой, филантроп', '99', 'I am IRON MAN")

Hero.double_health()
Hero.display_name()
print(Hero)
print(f'lenght of catchphrase: {len(Hero)}')


class AirHero(SuperHero):
    people2 = 'people2'
    def __init__(self,name, nickname, superpower, health_points, catchphrase,damage ):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
    def double_health(self):
        self.health_points **= 2
        self.fly = True
    def true_in_the_true_phrase(self):
        print('True in the True_phrase')

class SpaceHero(AirHero):
    pass

class Villain(AirHero):
    people = 'monster'

    def gen_x(self):
        pass
    def crit(self):
        self.damage **=2

airhero = AirHero(name='Khel Dzhordan', nickname='Green Lantern ', superpower='flight', health_points= 99,
                  catchphrase="LET'S FLY", damage=99)
spacehero = SpaceHero(name='Stephen', nickname='Dr. Strange ', superpower='sorcery', health_points= 99,
                      catchphrase= 'everything i lost can be mine again.', damage= 99)
antihero = Villain(name = 'Tanos', nickname='Безумный титан Танос', superpower='power', health_points= 99,
                  catchphrase= 'I am going to take over the universe', damage= 99 )

airhero.double_health()
airhero.true_in_the_true_phrase()

spacehero.double_health()
spacehero.true_in_the_true_phrase()

antihero.double_health()
antihero.true_in_the_true_phrase()


print(airhero)
print(spacehero)
print(antihero)
