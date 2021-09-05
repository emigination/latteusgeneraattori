# Testaus

## Yksikkötestaus
Yksikkötestaus on toteutettu Pytestillä, minkä lisäksi on manuaalisesti tehty järjestelmätestejä. Automaattiset testit voi suorittaa projektin juurikansiossa komennolla "poetry run invoke test". Testikattavuuden ja sen kehityksen näkee [Codecovista](https://codecov.io/gh/emigination/latteusgeneraattori). Kattavuusraportin voi myös luoda komennolla "poetry run invoke coverage-report" juurikansiossa.

Yksikkötestit on tehty luokille generaattori, sanalaskija ja trie, eli kaikille sovelluslogiikan luokille lukuun ottamatta solmua, joka on hyvin yksinkertainen. Koska generaattorin testit nojaavat myös sanalaskijaan, joka puolestaan nojaa triehen ja trie nojaa solmuun, niin yksikkötestit testaavat samalla myös sovelluslogiikan toimivuutta kokonaisuutena. Yksikkötesteissä käytetty data on testejä varten kirjoitettua ja hyvin suppeaa, jotta satunnaisuutta sisältäviä metodejakin voidaan testata järkevästi ja tehokkaasti.

## Suorituskykytestaus

Suorituskykytestit on tehty manuaalisesti niin, että ohjelma tulostaa opetteluun ja generointiin käytetyt ajat. Testauksessa on käytetty vain 1. ja 2. asteen ketjuja.

Oikealla opetusdatalla (runsaat 21 000 merkkiä ja 3 000 sanaa) testatessa "oppimiseen" menee noin 0,37 sekuntia. Generointiin menevä aika vaihtelee välillä 0,07–0,9 ms, tyypillisesti noin 0,22 ms.

Noin sata kertaa isommalla aineistolla, noin 2,1 miljoonaa merkkiä ja yli 300 000 sanaa automaattisesti generoituja tekstejä (esim. Lorem ipsum), oppimiseen menee noin 5,2 s. Generointiin menee 0,2–1,2 ms, paitsi jos käytetään teemaa ja2. asteen ketjuja, jolloin generointiaika on luokkaa 5–20 ms.

Vielä kymmenenkunta kertaa isomalla aineistolla, hieman päällä 22 miljoonaa merkkiä, oppimiseen menee noin 49 sekuntia. Generointiin menee edelleen vain 0,5–1,2 ms, paitsi jos on annettu teema ja 2. asteen ketjut, jolloin aikaa menee 60–120 ms.

Isommilla aineistoilla tehtyjen testien perusteella O(n) kuvaa hyvin datan opettelun aikavaativuutta. Sen sijaan generointiin menevään aikaan aineiston koko vaikuttaa vain vähän, mikä voi johtua siitä, että vakioaikaiset operaatiot vievät paljon aikaa. Voi myös olla, ettei keskimääräinen yhtä sanaa seuraavien sanojen määrä ole kovin voimakkaasti yhteydessä datan kokoon. Poikkeuksena sääntöön on 2. asteen ketjujen käyttö teeman kanssa, missä erot aineiston koossa jo näkyvät empiirisesti, mikä johtuu siitä, että näillä asetuksilla ohjelma käy kaikki aloitussanaparit kertaalleen läpi.

Heikkouksena tässä testauksessa on se, että on epäselvää, kuinka paljon testidatana käytetty automaattigeneroitu teksti poikkeaa oikeasta luonnollisesta kielestä mm. sanaston vaihtelevuudessa ja sanojen esiintymisen säännöllisyydessä.