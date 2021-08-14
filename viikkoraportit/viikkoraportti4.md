Viikkoraportti 4

Tällä viikolla muutin trien ja generoinnin toteutustapaa, minkä suunnittelu vei kohtalaisen paljon aikaa, kuten myös bugien korjaaminen muutosten jälkeen. Todennäköisyydet eivät ole enää erillisessä taulukossa, vaan ne lasketaan trieen tallennettujen määrien perusteella generointivaiheessa. Generaattori toimii nyt eri asteen Markovin ketjuilla, vaikka itse sovellus käyttää edelleen ensimmäisen asteen ketjuja, koska muuten se toistaiseksi tuottaisi pääasiassa opetusaineistossa olevia lauseita sellaisinaan. Testit on päivitetty vastaamaan uutta toteutusta, mutta kaikkia docstringeja ei ole vielä päivitetty.

Pieninä lisäyksinä generaattori osaa nyt myös lisätä pisteen virkkeen loppuun, jos viimeisessä sanassa ei ole sitä valmiina, ja generoitavan lausahduksen pituuteen on lisätty satunnaisuutta. Testaus- ja toteutusdokumentit ovat nyt olemassa, mutta niissä ei ole vielä kovin paljon sisältöä. suorituskykytestauksen tms. tekemiseen ei nyt jäänyt aikaa.

Tarkoituksena olisi palauttaa ominaisuus, että ketju "katkeaa" virkkeen päättyessä ja mahdollisen seuraavan virkkeen alku valitaan satunnaisesti sanoista, jotka voivat aloittaa virkkeitä, koska se vähentäisi opetusdatassa olevien lauseiden generoimista. Sen toteutus/muokkaaminen nykyiseen versioon sopivaksi jää kuitenkin seuraavaan viikkoon. Suunnittelen myös kehittää generaattoria niin, että se ottaa huomioon merkkijonon pituuden lisäksi virkkeiden määrän etsiessään sopivaa paikkaa lopettaa mietelauseen kasvattaminen.

Käytetty aika: 12 h