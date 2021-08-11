print("\033[32m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m")
print("             \033[36mJokenPô\033[m")
print("\033[32m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m")
import random
from time import sleep
#pedra_comp = 1
#papel_comp = 2
#tesoura_comp = 3
sleep (0.5)
print(" 3 ")
sleep (0.5)
print(" 2 ")
sleep (0.5)
print(" 1 ")
print(" \033[35mVamos lá!\033[m")
print('')
resp_comp = random.randint(1,3)
print("Qual vai jogar?: ")
print("[ 1 ] Pedra")
print("[ 2 ] Papel")
print("[ 3 ] Tesoura")
resp_user = int(input("Opção: "))
print('-------------------------------------')
if resp_user == 1 and resp_comp == 1:
    print("\033[34mEmpate\033[m")
    print("Você jogou pedra e eu também!")
elif resp_user == 2 and resp_comp == 2:
    print("\033[34mEmpate\033[m")
    print("Você jogou papel e eu também!")
elif resp_user == 3 and resp_comp == 3:
    print("\033[34mEmpate\033[m")
    print("Você jogou tesoura e eu também")
elif resp_user == 1 and resp_comp == 2:
    print("\033[31mVocê perdeu!\033[m")
    print("Você jogou pedra e eu joguei papel!")
elif resp_user == 1 and resp_comp == 3:
    print("\033[33mVocê ganhou!\033[m")
    print("Você jogou pedra e eu joguei tesoura!")
elif resp_user == 2 and resp_comp == 1:
    print("\033[33mVocê ganhou!\033[m")
    print("Você jogou papel e eu joguei pedra!")
elif resp_user == 2 and resp_comp == 3:
    print("\033[31mVocê perdeu!\033[m")
    print("Você jogou papel e eu joguei tesoura!")
elif resp_user == 3 and resp_comp == 2:
    print("\033[33mVocê ganhou!\033[m")
    print("Você jogou tesoura e eu joguei papel!")
elif resp_user == 3 and resp_comp == 1:
    print("\033[31mVocê perdeu!\033[m")
    print("Você jogou tesoura e eu joguei pedra!")
