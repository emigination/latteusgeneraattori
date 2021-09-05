# Käyttöohje

## Aloitus
Ennen ohjelman käyttöä tulee asentaa riippuvuudet komennolla "poetry install" ohjeleman juurikansiossa. Ohjelman voi suorittaa komennolla "poetry run invoke start", edelleen juurikansiossa.

## Käyttö
Ohjelmassa on vain tekstikäyttöliittymä. Ohjelman käyttö on yksinkertaista; sille voi syöttää teeman, josta se generoi latteuden, tai jättää teeman tyhjäksi, jolloin generoidaan satunnainen latteus. Syöttämällä 0 ohjelmaa sulkeutuu.

Käyttäjä valitsee myös käytettävän Markovin ketjun asteen, mieluiten 1 tai 2. Asteella 1 seuraava sana valitaan vain edellisen sanan perusteella, asteella 2 valinta perustuu kahteen edelliseen sanan, ja niin edelleen. Myös korkeampia asteita kuin 2 voi syöttää, mutta tällöin syntyvät lauseet ovat hyvin suoraan aineistosta.

## Teemat

Jos käyttäjä antaa teeman, ohjelma tutkii, onko sanaa valmiina aineistossa ja sopivassa kohtaa lausetta, ja jos on, hyödyntää sitä valitessaan seuraavaa sanaa. Jos teemaa ei ole aineistossa, se asetetaan lauseen ensimmäiseksi sanaksi. Ensimmäisen asteen ketjuissa seuraava sana valitaan satunnaisesti muutamasta ennalta valitusta sanasta, jotka sopivat perusmuotoisen substantiivin perään (koska oletetaan että teema annetaan tällaisessa muodossa) ovat myös aineistossa; n-asteen ketjuilla seuraavat n sanaa valitaan satunnaisesti aineistosta, mikä valitettavasti tarkoittaa sitä että teema ei välttämättä kieliopillisesti istu lauseeseen.

Parhaita lauseita generaattori tuottaa ilman teemaa, toisen asteen ketjuilla.

## Testaus
Testit voi suoritaa juurikansiossa komennolla "poetry run invoke test", testikattavuusraportin generoida komennolla "poetry run invoke coverage-report" ja koodin laatua tarkastella komennolla "poetry run invoke lint". Enemmän tietoa testauksesta on [testausdokumentissa](https://github.com/emigination/latteusgeneraattori/blob/main/dokumentaatio/testausdokumentti.md).