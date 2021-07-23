# Määrittelydokumentti

Aineopintojen harjoitustyö: tietorakenteet ja algoritmit -kurssin harjoitustyö (TKT-kandiohjelma)

Ohjelma on latteusgenerattori. Se luo automaattisesti mietelauseita Markovin ketjun avulla. Generaattorin opettamiseen käytettävä data on "voimalauseita", aforismeja, elämän"viisauksia" jne. Projektin kieli on ainakin alustavasti suomi. Sanojen esiintymistodennäköisyydet tietyn kunkin sanan jälkeen tallenetaan kaksiuloitteiseen matriisiin. Sanat ja niiden indeksit tallenetaan trie-rakenteeseen.

Markovin ketju valitttiin algoritmiksi, koska sen avulla pystytään tuottamaan suhteellisen luonnolisen kaltaista kieltä ja se on riittävän yksinkertainen toteutettavaksi käytettävissä olevan ajan puitteissa. Trietä käytetään, jotta sanan indeksi on nopea löytää oppimisvaiheessa.

Ohjelmalle annetaan syötteeksi teema, johon liittyvän lausahduksen se sitten luo. Mikäli teemaksi annettu sana löytyy ohjelman aineistosta, se rupeaa luomaan lausetta suoraan siitä. Jos se ei tunne sanaa, väliin lisätään muu sopiva, datasta jo löytyvä sana. (Tai mahdollisesti ei teemaa ja ohjelma vain luo satunnaisen latteuden).

Tavoitteena olevat aika- ja tilavaativuudet (m.m. O-analyysit)
Lähteet