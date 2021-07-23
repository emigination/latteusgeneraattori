#nopea kokeiluversio

import io
import random

with io.open('opetusdata.txt', encoding='utf-8') as tiedosto:
    data = []
    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")
        data.append(rivi)

seuraavat = {}
maarat = {}
sanalista = []
ensimmaiset = []

for rivi in data:
    sanat = rivi.split(' ')
    sanoja = len(sanat)
    ensimmaiset.append(sanat[0])
    for i, sana in enumerate(sanat):
        if sana not in seuraavat:
            # todennakoisyydet[sana]={}
            seuraavat[sana]=[]
            maarat[sana] = 0
            sanalista.append(sana)
        if i+1 < sanoja:
            seuraava = sanat[i+1]
        else:
            seuraava = 'LOPPU'
        # if seuraava not in todennakoisyydet[sana]:
        #     todennakoisyydet[sana][seuraava] = 1
        # else:
        #     todennakoisyydet[sana][seuraava] += 1
        seuraavat[sana].append(seuraava)
        maarat[sana] += 1

# print(todennakoisyydet['Älä'])
# print(maarat)

sana = ensimmaiset[random.randint(0, len(ensimmaiset)-1)]
# print(satunnainen_sana)
lause = sana
while len(lause)<200:
    seuraava = seuraavat[sana][random.randint(0, len(seuraavat[sana])-1)]
    if seuraava == 'LOPPU':
        if len(lause) > 30:
            break
        seuraava = ensimmaiset[random.randint(0, len(ensimmaiset)-1)]
    lause += ' ' + seuraava
    sana = seuraava
print(lause)
