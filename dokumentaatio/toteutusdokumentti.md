# Toteutus

## Rakenne

Ohjelmassa on vain tekstikäyttöliittymä. Käyttöliittymäluokkia on yksi, Kayttoliittyma. Se pyytää lauseet Generaattori-luokalta, joka luo niitä Markovin ketjujen avulla. Generaattorin tarvitseman datan opiskelee harjoitteluaineistosta Sanalaskija-luokka. Apuna on trie-tietorakenne ja sen solmu, jotka ovat omat luokkansa.

## Aikavaativuudet

### Aineiston opettelu

Aineiston lukemisen aikavaativuus on O(n), missä n on aineiston koko. Kukin sana lisätään triehen 1-k kertaa, missä k on Markovin ketjun aste, ja lisäksi kerran tarkistustriehen. Lisäys vie aikaa n, missä n on merkkien määrä. Listaan ja jonoon lisäminen tai jonon lopusta poistaminen toimivat kukin vakioajassa ja niitä tehdään korkeintaan kerran kutakin per sana. Jonon luominen on suhteessa Markovin ketjun asteeseen, eli aineiston koon suhteen vakioaikainen. Näin ollen opettelu vie aikaa O(n), missä n on edelleen merkkien määrä.

### Generointi

Kun opetusdatasta on luotu generointiin tarvittavat tietorakenteet, ensimmäisten sanojen valinnan aikavaativuus riippuu käyttäjän syöttämistä asetuksista. Jos käyttäjä on antanut teeman ja Markovin ketjujenaste on 2 tai enemmän, aloitusanojen valinnan aikavaativuus on O(n), sillä kaikki merkkijonot aloitussanojen listassa käydään läpi teeman etsimiseksi. Jos teema on annettu mutta aste on 1, aloitussanat löytyvät ajassa O(m), missä m on teemasanan pituus tai nopeammin. Jos teemaa ei ole annettu, aloitussanat valitaan satunnaisesti listasta eli vakioajassa.

Edellisten sanojen jonon (jonka pituus on Markovin ketjujen aste) luonti geeneroidessa tapahtuu suhteessa annettuun asteeseen mutta aineiston koosta riippumatta. Siihen lisääminen ja poistaminen ovat vakioaikaisia toimintoja. Aikavaativuus sille, että vaihtoehdot seuraavaksi sanaksi haetaan triestä, on O(m), missä m on edelliset-listassa olevein sanojen merkkimäärä yhteensä, eli sekin on riippuvainen asteesta muttei aineiston koosta.

Kun seuraava sana arvotaan vaihtoehdoista, kaikki vaihtoehdot käydään läpi, ja vaihtoehtojen määrä on suhteessa aineiston kokoon, joten tämän kohdan voidaan katsoa olevan aikavaativuudeltaan O(n) suhteessa sanojen määrään aineistossa. Sanojen valinnassa siis korkein aikavaativuus n O(n), ja sanoja valitaan enintään 20. Sanojen valinnan kokonaisaikavaativuus on siis O(n).

Sanalistan muuttaminen merkkijonoksi ja sen hakeminen tarkistustriesta tapahtuvat suhteessa lauseen pituuteen. Jos lause ei läpäise alkuperäisyystarkistusta eli on täysin sama kuin aineistossa, koko generointi tehdään uudestaan. Normaalisti se käy enintään muutaman kerran. Näin ollen koko generoinnin aikavaativuus on O(n), missä n on harjoitusaineiston koko.

## Tilavaativuudet