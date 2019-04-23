from monster_base import Monster_base

class Monster_giant(Monster_base):
    def __init__(self, name_big):
        super().__init__(name_big)
        self.height = 'HUGE'
        #self.name = name_big
        #self.name= name_big

    def show_type(self):
        return self.__monster_type

    def monster_attack_1(self, attack_1_dam):
        self.laser = attack_1_dam
        return f'{self.name} uses {attack_1_dam} and burns a hole through a wall'

    def monster_attack_2(self, attack_2_dam, melee):
        self.headbutt = attack_2_dam
        self.sword = melee
        return f'{self.name} uses {attack_2_dam} and {melee}'

    def monster_attack_3(self, attack_3_dam):
        self.lightning = attack_3_dam