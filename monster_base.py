class Monster_base():

    __monster_type = 'Base monster'

    def __init__(self, name_input = 'Ringo', fur_amount = 'lots', eyes = 67, limbs = 1):     #Abstaction of what it looks like
        self.fur = fur_amount
        self.eyes = eyes
        self.limbs = limbs
        self.name = name_input
        self.height = 'normal'

    def show_type(self):
        return self.__monster_type

    def monster_attack_1 (self, attack_1_dam):
        self.laser = attack_1_dam
        return f'{self.name} uses {attack_1_dam} and burns a hole through a wall'

    def monster_attack_2(self, attack_2_dam, melee):
        self.headbutt = attack_2_dam
        self.sword = melee
        return f'{self.name} uses {attack_2_dam} and {melee}'

    def monster_attack_3(self, attack_3_dam):
        self.lightning = attack_3_dam

