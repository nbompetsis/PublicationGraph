# Publication Graph / RestAPI

## Curl commands of RestAPI requests

Below you will find the requests / responses of RestAPI which returns the information from cypher queries of PublicationGraph project ([link here](../../Neo4jQueries/README.md)) via HTTP protocol.

1.  Find the titles (title, year) of publications that a particular author has published.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query1?name=Sanjay%20Jain%200001'
```
* Response
```
[
    {
        "TITLE": "Connections Between Inductive Inference and Machine Learning.",
        "YEAR": "2017"
    },
    {
        "TITLE": "Query-Based Learning.",
        "YEAR": "2017"
    },
    {
        "TITLE": "Inductive Inference.",
        "YEAR": "2017"
    },
    {
        "TITLE": "Complexity of Inductive Inference.",
        "YEAR": "2017"
    },
    {
        "TITLE": "Computational Complexity of Learning.",
        "YEAR": "2010"
    },
    {
        "TITLE": "Complexity of Inductive Inference.",
        "YEAR": "2010"
    },
    {
        "TITLE": "Inductive Inference.",
        "YEAR": "2010"
    },
    {
        "TITLE": "Query-Based Learning.",
        "YEAR": "2010"
    },
    {
        "TITLE": "Connections Between Inductive Inference and Machine Learning.",
        "YEAR": "2010"
    }
]
```

2.  Find the co-authors of an author (name, number of co-authorships) for a particular year.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query2?name=Christoph%20Meinel&year=1997'
```
* Response
```
[
    {
        "NAME": "Christoph Meinel",
        "NUM_CO_AUTHORS": 7
    }
]
```

3.  
    a.  Find the top-K authors (name, count) with regard to most conference.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query3/conferences?k=2'
```
* Response
```
[
    {
        "NAME": "E. F. Codd",
        "NUM_PUB": 1
    },
    {
        "NAME": "Arnon Rosenthal",
        "NUM_PUB": 1
    }
]
```

3.  
    b.  Find the top-K authors (name, count) with regard to most journal.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query3/journals?k=2'
```
* Response
```
[
    {
        "NAME": "Christoph Meinel",
        "NUM_PUB": 54
    },
    {
        "NAME": "Dieter Baum",
        "NUM_PUB": 21
    }
]
```

4.  Find the top-K authors (name, count) with regard to most co-authors in a single work.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query4?k=5'
```
* Response
```
[
    {
        "NAME": "Michael John",
        "NUM_CO_AUTHORS": 30
    },
    {
        "NAME": "Claudia Spindler",
        "NUM_CO_AUTHORS": 28
    },
    {
        "NAME": "Tobias Leipold",
        "NUM_CO_AUTHORS": 28
    },
    {
        "NAME": "Fabienne Waidelich",
        "NUM_CO_AUTHORS": 28
    },
    {
        "NAME": "Sibylle Meyer",
        "NUM_CO_AUTHORS": 28
    }
]
```

5.  Find the top-K authors (name, count) with regard to most co-authors in a particular year.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query5?k=5&year=2018'
```
* Response
```
[
    {
        "NAME": "Mike Hamburg",
        "NUM_CO_AUTHORS": 9
    },
    {
        "NAME": "Daniel Genkin",
        "NUM_CO_AUTHORS": 9
    },
    {
        "NAME": "Michael Schwarz 0001",
        "NUM_CO_AUTHORS": 9
    },
    {
        "NAME": "Paul Kocher",
        "NUM_CO_AUTHORS": 9
    },
    {
        "NAME": "Yuval Yarom",
        "NUM_CO_AUTHORS": 9
    }
]
```

6.  Find the top-K authors (name, count) with regard to most active years.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query6?k=5'
```
* Response
```
[
    {
        "AUTHOR": "Christoph Meinel",
        "MOST_ACTIVE_YEAR": 12
    },
    {
        "AUTHOR": "Dieter Baum",
        "MOST_ACTIVE_YEAR": 9
    },
    {
        "AUTHOR": "Rainer Tichatschke",
        "MOST_ACTIVE_YEAR": 9
    },
    {
        "AUTHOR": "Alexander Kaplan",
        "MOST_ACTIVE_YEAR": 9
    },
    {
        "AUTHOR": "Helmut Seidl",
        "MOST_ACTIVE_YEAR": 8
    }
]
```

7.  Find the top-K authors (name, count) with regard to most distinct pairs of co-authors that have not published together.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query7?k=10' 
```
* Response
```
[
    {
        "AUTHOR": "Constantine Stephanidis",
        "FINAL_SUM": 113
    },
    {
        "AUTHOR": "Auroop R. Ganguly",
        "FINAL_SUM": 83
    },
    {
        "AUTHOR": "Lindsey Bressler",
        "FINAL_SUM": 70
    },
    {
        "AUTHOR": "Daniele Nardi",
        "FINAL_SUM": 54
    },
    {
        "AUTHOR": "Borko Furht",
        "FINAL_SUM": 52
    },
    {
        "AUTHOR": "Christodoulos A. Floudas",
        "FINAL_SUM": 50
    },
    {
        "AUTHOR": "Peter H. Schmitt",
        "FINAL_SUM": 37
    },
    {
        "AUTHOR": "Christoph Beierle",
        "FINAL_SUM": 35
    },
    {
        "AUTHOR": "Saso Tomazic",
        "FINAL_SUM": 34
    },
    {
        "AUTHOR": "Thorsten Strufe",
        "FINAL_SUM": 34
    }
]
```

8.  Find the top-K authors (name, count) with regard to largest average number of journal publications per year (consider only active years).
* Request
```
curl --location --request GET 'http://localhost:5000/api/query8?k=10'
```
* Response
```
[
    {
        "AUTHOR": "Egon Börger",
        "AVG_PER_YEAR": 5.0
    },
    {
        "AUTHOR": "Klaus Jansen",
        "AVG_PER_YEAR": 5.0
    },
    {
        "AUTHOR": "Lothar Breuer",
        "AVG_PER_YEAR": 5.0
    },
    {
        "AUTHOR": "Christoph Meinel",
        "AVG_PER_YEAR": 5.0
    },
    {
        "AUTHOR": "Stasys Jukna",
        "AVG_PER_YEAR": 4.0
    },
    {
        "AUTHOR": "Manfred Laumen",
        "AVG_PER_YEAR": 4.0
    },
    {
        "AUTHOR": "Harald Sack",
        "AVG_PER_YEAR": 4.0
    },
    {
        "AUTHOR": "Stefan Böttcher",
        "AVG_PER_YEAR": 4.0
    },
    {
        "AUTHOR": "Thomas Ludwig 0001",
        "AVG_PER_YEAR": 4.0
    },
    {
        "AUTHOR": "Jürgen Huschens",
        "AVG_PER_YEAR": 4.0
    }
]
```

9.  Find the top-K authors (name, count) that a given author has not worked with, with regard to most co-authorships with authors that the given author has worked with.
* Request
```
curl --location --request GET 'localhost:5000/api/query9?k=5&name=Christoph%20Meinel'
```
* Response
```
[
    {
        "AUTHOR": "Ulrich Holtmann",
        "CO_AUTHORS": 6
    },
    {
        "AUTHOR": "Katja Lenz",
        "CO_AUTHORS": 1
    },
    {
        "AUTHOR": "Jirí Sgall",
        "CO_AUTHORS": 1
    },
    {
        "AUTHOR": "Igor E. Shparlinski",
        "CO_AUTHORS": 1
    },
    {
        "AUTHOR": "Stasys Jukna",
        "CO_AUTHORS": 1
    }
]
```

10.  Find the authors (name, count) that have published more than three works in a given single year.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query10?year=1997'
```
* Response
```
[
    {
        "AUTHOR": "Christoph Meinel",
        "COUNT": 5
    },
    {
        "AUTHOR": "Helmut Seidl",
        "COUNT": 3
    }
]
```

11.  Find the number of pages that a particular author has published in a given year.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query11?year=2011&name=Gerrit%20Bleumer'
```
* Response
```
[
    {
        "AUTHOR": "Gerrit Bleumer",
        "TOTAL_PAGES": 83
    }
]
```

12. 
    a.  Find the top-K authors (name, count) with regard to articles published in a particular journal as a first author in a given year.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query12/first?year=2018&journal=meltdownattack.com'
```
* Response
```
[
    {
        "AUTHOR": "Paul Kocher",
        "COUNT": 1
    },
    {
        "AUTHOR": "Moritz Lipp",
        "COUNT": 1
    }
]
```

12. 
    b.  Find the top-K authors (name, count) with regard to articles published in a particular journal as a last author in a given year.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query12/last?year=2018&journal=meltdownattack.com'
```
* Response
```
[
    {
        "AUTHOR": "Yuval Yarom",
        "COUNT": 1
    },
    {
        "AUTHOR": "Mike Hamburg",
        "COUNT": 1
    }
]
```

13.  Find the three authors that have appeared as co-authors for the most times in a particular journal.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query13?journal=Universit%C3%A4t%20Trier,%20Mathematik/Informatik,%20Forschungsbericht'
```
* Response
```
[
    {
        "AUTHOR_1": "Anna Slobodová",
        "AUTHOR_2": "Jochen Bern",
        "AUTHOR_3": "Christoph Meinel",
        "COUNT": 9
    },
    ...
    ...
    {
        "AUTHOR_1": "Elena Dubrova",
        "AUTHOR_2": "Harald Sack",
        "AUTHOR_3": "Christoph Meinel",
        "COUNT": 1
    }
]
```

14.  Find pairs of authors that have appeared in different parts of the same book and have never co-authored a work.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query14'
```
* Response
```
[
    {
        "AUTHOR_1": "Brigitte Bartsch-Spörl",
        "AUTHOR_2": "Roland Seiffert"
    },
    {
        "AUTHOR_1": "Brigitte Bartsch-Spörl",
        "AUTHOR_2": "Michael Herweg"
    },
    ...
    ...
    {
        "AUTHOR_1": "Brigitte Bartsch-Spörl",
        "AUTHOR_2": "Mohammed Nadjib Khenkhar"
    },
    {
        "AUTHOR_1": "Brigitte Bartsch-Spörl",
        "AUTHOR_2": "Simone Pribbenow"
    }
]
```

15.  Find the authors that have published work for K consecutive years.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query15?k=5'
```
* Response
```
[
    {
        "AUTHOR": "Peter H. Schmitt",
        "CONS_YEARS": [
            1986,
            1987,
            1988,
            1989,
            1990
        ]
    },
    {
        "AUTHOR": "Jochen Dörre",
        "CONS_YEARS": [
            1987,
            1988,
            1989,
            1990,
            1991
        ]
    },
    {
        "AUTHOR": "Christoph Beierle",
        "CONS_YEARS": [
            1987,
            1988,
            1989,
            1990,
            1991,
            1992
        ]
    },
    {
        "AUTHOR": "Udo Pletat",
        "CONS_YEARS": [
            1987,
            1988,
            1989,
            1990,
            1991
        ]
    },
    {
        "AUTHOR": "Peter Gritzmann",
        "CONS_YEARS": [
            1992,
            1993,
            1994,
            1995,
            1996,
            1997
        ]
    },
    {
        "AUTHOR": "Christoph Meinel",
        "CONS_YEARS": [
            1992,
            1993,
            1994,
            1995,
            1996,
            1997,
            1998,
            1999
        ]
    },
    {
        "AUTHOR": "Victor Klee",
        "CONS_YEARS": [
            1993,
            1994,
            1995,
            1996,
            1997
        ]
    },
    {
        "AUTHOR": "Anna Slobodová",
        "CONS_YEARS": [
            1993,
            1994,
            1995,
            1996,
            1997,
            1998
        ]
    },
    {
        "AUTHOR": "Christoph W. Keßler",
        "CONS_YEARS": [
            1994,
            1995,
            1996,
            1997,
            1998,
            1999
        ]
    },
    {
        "AUTHOR": "Rainer Tichatschke",
        "CONS_YEARS": [
            1995,
            1996,
            1997,
            1998,
            1999,
            2000,
            2001,
            2002
        ]
    },
    {
        "AUTHOR": "Alexander Kaplan",
        "CONS_YEARS": [
            1995,
            1996,
            1997,
            1998,
            1999,
            2000,
            2001,
            2002
        ]
    },
    {
        "AUTHOR": "Helmut Seidl",
        "CONS_YEARS": [
            1995,
            1996,
            1997,
            1998,
            1999
        ]
    },
    {
        "AUTHOR": "Lothar Breuer",
        "CONS_YEARS": [
            1998,
            1999,
            2000,
            2001,
            2002
        ]
    }
]
```

16.  Find the top-K authors with regard to average number of co-authors in their publications.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query16?k=5'
```
* Response
```
[
    {
        "AUTHOR": "Sibylle Meyer",
        "AVG_CO_AUTHORS": 28,
        "COUNT_AUTHORS": 28,
        "COUNT_PUB": 1
    },
    {
        "AUTHOR": "Claudia Spindler",
        "AVG_CO_AUTHORS": 28,
        "COUNT_AUTHORS": 28,
        "COUNT_PUB": 1
    },
    {
        "AUTHOR": "Tobias Leipold",
        "AVG_CO_AUTHORS": 28,
        "COUNT_AUTHORS": 28,
        "COUNT_PUB": 1
    },
    {
        "AUTHOR": "Fabienne Waidelich",
        "AVG_CO_AUTHORS": 28,
        "COUNT_AUTHORS": 28,
        "COUNT_PUB": 1
    },
    {
        "AUTHOR": "Norbert Pieth",
        "AVG_CO_AUTHORS": 28,
        "COUNT_AUTHORS": 28,
        "COUNT_PUB": 1
    }
]
```

17.  Find the authors of consecutively published papers with more than a given amount of years between them.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query17?years=37'
```
* Response
```
[
    {
        "AUTHOR": "Dines Bjørner"
    }
]
```

18.  Find the author (name, count) with the most parts in a single book of collective works.
* Request
```
curl --location --request GET 'http://localhost:5000/api/query18'
```
* Response
```
[
    {
        "AUTHOR": "E. F. Codd",
        "NUM_PUB": 1
    },
    {
        "AUTHOR": "Arnon Rosenthal",
        "NUM_PUB": 1
    }
]
```