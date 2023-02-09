from datetime import datetime
from datetime import timedelta

from WallStreetConfig import *


print("Demarrage 'launch.py'")

#subprocess.call('start /wait python WallofGraphes.py', shell=True)

# Launch the Flask server
# launch the main loop

# Nb_de_Periodes = int(input("\nCombien de manches de '{0}' minutes voulez vous jouer ?\nAttention ! La partie ne peut être arrêtée en cours et les prix norm'sss kfet seront automatiquement remis à la fin. : \n".format(time_period)))
# print("Le mode WallStreet sera actif pendant '{0}' minutes. NE PAS ETEINDRE LA VM pendant (sinon faudra rechanger les prix modifiés à la main ...)".format(time_period * Nb_de_Periodes))

GAME_DURATION_min = int(input("Combien de minutes veux-tu jouer: "))    # durée du jeu souhaité en minutes

GAME_DURATION_STEP = GAME_DURATION_min * 60 / REFRESH_INTERVAL  # Nombre de pas joués

fin = (datetime.now() + timedelta(minutes=GAME_DURATION_min)).strftime("%H:%M:%S")
print("--------------------------------------------")
print("le jeu va durer {} pas de {} secondes (fin à {})".format(GAME_DURATION_STEP, REFRESH_INTERVAL, fin))
print("la fenêtre de temps est de {} minutes".format(PERIOD_SIZE/60))
print("--------------------------------------------\n\n")


exec(open('/home/justin/Dev_n_Class/WallStreetKfet/WallStreetMode.py').read())
