import random
import time
def min_copiok(copipi, targit):
    
    spisok_minsuma = [float("inf")] * (targit + 1)
    spisok_minsuma[0] = 0 

    for copipi in copipi:
        for i in range(copipi, targit + 1):
            spisok_minsuma[i] = min(spisok_minsuma[i], spisok_minsuma[i - copipi] + 1)

    return spisok_minsuma[targit]

nomel = [2, 5] 
amput = random.randint(1, 100)

resultat = min_copiok(nomel, amput)
print("який був номінал: ", amput ) 
time.sleep(0.4)
print("мінімальна число комійок: ",  resultat)
