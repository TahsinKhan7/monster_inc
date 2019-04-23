from monster_base import Monster_base

# print(Monster_base())
# print(type(Monster_base()))
# print(Monster_base().eyes)        #can do class.attrubute to return result


#monster_1 = Monster_base('Fred', 'No fur', 3, 4)
# print('name:', monster_1.name)
# print('fur', monster_1.fur)
# print('eyes',  monster_1.eyes)
# print('limbs', monster_1.limbs)


##Define two methods for the monster objects
## they should take in arguments
## one of the methods should take in options

###############
monster_1 = Monster_base()

print(monster_1.monster_attack_1('laser'))
print(monster_1.monster_attack_2('headbutt', 'sword attack'))

print(monster_1.show_type())