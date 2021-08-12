# Toteutus

## Rakenne

Ohjelmassa on vain komentorivikäyttöliittymä. Käyttöliittymäluokkia on yksi, Kayttoliittyma. Se pyytää lauseet Generaattori-luokalta, joka luo niitä Markovin ketjujen avulla. Generaattorin tarvitseman datan opiskelee harjoitteluaineistosta Sanalaskija-luokka. Apuna on Trie-tietorakenne, joka on oma luokkansa.