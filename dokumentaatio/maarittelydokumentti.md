# Määrittelydokumentti

Aineopintojen harjoitustyö: tietorakenteet ja algoritmit -kurssin harjoitustyö (TKT-kandiohjelma)

Ohjelma on latteusgenerattori. Se luo automaattisesti mietelauseita Markovin ketjun avulla. Generaattorin opettamiseen käytettävä data on "voimalauseita", aforismeja, elämän"viisauksia" jne. Projektin kieli on suomi. Sanojen esiintymiskertojen määrä kunkin sanan tai sanayhdistelmän jälkeen tallenetaan trie-rakenteeseen. Sanayhdistelmien pituus riippuu siitä, minkä asteen Markovin ketjuja käytetään, niin että ensimmäisen asteen ketjuissa ne ovat yksittäisiä sanoja Tällä hetkellä sovellus käyttää vain ensimmäisen asteen ketjuja, mutta tietorakenteet on tehty niin, että myös korkeammat asteet ovat mahdollisia, joskin opetusdataa pitäisi olla enemmän jotta niiden käyttö olisi mielekästä.

Markovin ketju valitttiin algoritmiksi, koska sen avulla pystytään tuottamaan suhteellisen luonnolisen kaltaista kieltä ja se on riittävän yksinkertainen toteutettavaksi käytettävissä olevan ajan puitteissa. Trietä käytetään, jotta seuraavat mahdolliset sanat ja niiden määrät, joista voidaan siis laskea todennäköisyydet, on haettavissa tehokkaasti.

Ohjelmalle annetaan syötteeksi teema, johon liittyvän lausahduksen se sitten luo. Mikäli teemaksi annettu sana löytyy ohjelman aineistosta, se rupeaa luomaan lausetta suoraan siitä. Jos se ei tunne sanaa, väliin lisätään muu sopiva, datasta jo löytyvä sana. (Tai mahdollisesti ei teemaa ja ohjelma vain luo satunnaisen latteuden).

Tavoitteena on, että valmis, opetettu ohjelma toimii ajassa O(m+n), missä m on trien pisimmän sanayhdistelmän pituus ja n on lauseeseen tulevien sanojen määrä. Syötteen suhteen ohjelma toimii vakioajassa. Opetusvaiheen algoritmin aikavaativuus on O(n²), missä n on aineistossa olevien eri sanojen määrä. Myös tilavaativuus on luokkaa O(n²), koska matriisi vaatii sen verran tilaa.


Lähteet:

https://en.wikipedia.org/wiki/Trie

https://www.geeksforgeeks.org/trie-insert-and-search/

https://towardsdatascience.com/markov-chains-how-to-train-text-generation-to-write-like-george-r-r-martin-cdc42786e4b6

https://www.codingninjas.com/blog/2020/09/22/using-trie-in-data-structures/