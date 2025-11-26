import time
from datetime import datetime
from ping3 import ping

with open('cel.txt', 'r') as plik_konfig:
    cel = plik_konfig.read().strip()

with open('logi.txt', 'a') as plik_logi:
    teraz = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    plik_logi.write(f"====== {teraz} ======\n")

    for i in range(5):
        wynik = ping(cel, unit='ms')
        if wynik is None:
            linia_do_zapisu = "Timeout (Brak odpowiedzi)\n"
        else:
            linia_do_zapisu = f"{round(wynik, 2)} ms\n"
        plik_logi.write(linia_do_zapisu)
        time.sleep(1)
    plik_logi.write("=======koniec======\n\n")
