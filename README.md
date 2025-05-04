# Kirjafoorumi - Suunnitelma

• Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.

• Käyttäjä pystyy lisäämään sovellukseen kirja-arvosteluja, joihin kuuluu kirjoitettu arvostelu ja arvosana. Käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään arvosteluja. 

• Käyttäjä näkee sovellukseen lisätyt kirja-arvostelut. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät arvostelut.

• Käyttäjä pystyy etsimään kirja-arvosteluja esim. kirjan nimellä. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä arvosteluja.

• Sovelluksessa on käyttäjäsivut, jotka näyttävät lisätyistä kirja-arvosteluista tilastoja (esim. yleisarvosana) ja tietyn käyttäjän lisäämät arvostelut.

• Käyttäjä pystyy valitsemaan tietokohteelle yhden tai useamman luokittelun sen genren perusteella.

• Sovelluksessa on mahdollista myös kommentoida muiden käyttäjien kirja-arvosteluja ja näin keskustella kirjasta. 


# Välipalautus 2
Sovelluksesta löytyy nyt seuraavat ominaisuudet:

• Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.

• Käyttäjä pystyy lisäämään sovellukseen kirja-arvosteluja, joihin kuuluu otsikko, kirjan nimi, arvosana (tähtien määrä asteikolla 1-5) ja kirjoitettu arvostelu. Käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään arvosteluja. 

• Käyttäjä näkee sovellukseen lisätyt kirja-arvostelut. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät arvostelut.

• Käyttäjä pystyy etsimään kirja-arvosteluja kirjan nimellä ja arvostelussa esiintyvillä sanoilla. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä arvosteluja.

Mitään salaus/suojaustoimintoja ei sovelluksessa vielä ole koska en ehtinyt niitä tekemään. 

# Välipalautus 3

• Sovellukseen on lisätty erilaisia suojaustoimintoja, jotta sovelluksen käyttäjä pääsee käsittelemään niitä tietoja mitä hänen kuuluukin.

• Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjän lisäämät tietokohteet.

Muita ominaisuuksia, jotka tässä palautuksessa olisi pitänyt olla, ei vielä ole, koska en ehtinyt niitä tekemään :(

# Kirjafoorumi - Lopullinen palautus

**Sovelluksen toiminnot**

• Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.

• Käyttäjä pystyy lisäämään sovellukseen kirja-arvosteluja, joihin kuuluu otsikko, asteikolla 1-5 annettu arvosana (tähdet) ja itse arvostelu. Käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään arvosteluja. 

• Käyttäjä näkee sovellukseen lisätyt kirja-arvostelut. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät arvostelut.

• Käyttäjä pystyy etsimään kirja-arvosteluja kirjan nimellä ja arvostelussa esiintyvillä sanoilla. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä arvosteluja.

• Sovelluksessa on käyttäjäsivut, jotka kertovat kuinka monta arvostelua käyttäjä on lisännyt ja näistä annettujen tähtien keskiarvon. Sivuilla näkyy myös käyttäjän lisäämät arvostelut.

• Käyttäjä pystyy valitsemaan arvostelulleen luokittelun sen genren perusteella.

• Sovelluksessa on mahdollista kommentoida muiden käyttäjien kirja-arvosteluja keskustelualueella. Kommentteja voi poistaa. 


**Sovelluksen asennus**

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```










