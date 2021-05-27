# Neo4j cypher queries

Your database should be able to answer the following queries.

## Queries

1.  Find the titles (title, year) of publications that a particular author has published.
```
MATCH (Author {name: 'Sanjay Jain 0001'})-[:PUBLISHED]->(p:Publication)
WHERE p.year <> '' AND p.title <> ''
RETURN p.title AS Title, p.year AS YEAR
```

2.  Find the co-authors of an author (name, number of co-authorships) for a particular year.
```
MATCH (a1:Author{name: 'Christoph Meinel'})-[:PUBLISHED]->(p:Publication)<-[:PUBLISHED]-(a2:Author)
WHERE p.year <> '' AND p.year = '1997'
RETURN a1.name , COUNT(a2) as NUM_CO_AUTHORS
ORDER BY NUM_CO_AUTHORS DESC
```

3.  Find the top-K authors (name, count) with regard to most conference/journal publications. (2 methods)
```
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)-[ISSUED]->()
RETURN a1.name , COUNT(p) as NUM_PUB
ORDER BY NUM_PUB DESC
LIMIT 5 // K = 5
```

4.  Find the top-K authors (name, count) with regard to most co-authors in a single work.
```
MATCH (a1:Author)-[:PUBLISHED]->(p:Publication)<-[:PUBLISHED]-(a2:Author)
WITH a1, a2, size(collect(p)) as commonPublications
WHERE commonPublications = 1
RETURN a1, COUNT(a2) as NUM_CO_AUTHORS
ORDER BY NUM_CO_AUTHORS DESC
LIMIT 5 // K = 5
```

5.  Find the top-K authors (name, count) with regard to most co-authors in a particular year.
```
Cypher Query
```

6.  Find the top-K authors (name, count) with regard to most active years.
```
Cypher Query
```

7.  Find the top-K authors (name, count) with regard to most co-authors that have not published together.
```
Cypher Query
```

8.  Find the top-K authors (name, count) with regard to largest average number of journal publications per year (consider only active years).
```
Cypher Query
```

9.  Find the top-K authors (name, count) that a given author has not worked with, with regard to most co-authorships with authors that the given author has worked with.
```
Cypher Query
```

10.  Find the authors (name, count) that have published more than three works in a given single year.
```
Cypher Query
```

11.  Find the number of pages that a particular author has published in a given year.
```
Cypher Query
```

12.  Find the top-K authors (name, count) with regard to articles published in a particular journal as a first/last author in a given year. (2 methods)
```
Cypher Query
```

13.  Find the three authors that have appeared as co-authors for the most times in a particular journal.
```
Cypher Query
```

14.  Find pairs of authors that have appeared in different parts of the same book and have never co-authored a work.
```
Cypher Query
```

15.  Find the authors that have published work for K consecutive years.
```
Cypher Query
```

16.  Find the top-K authors with regard to average number of co-authors in their publications.
```
Cypher Query
```

17.  Find the authors of consecutively published papers with more than a given amount of years between them.
```
Cypher Query
```

18.  Find the author (name, count) with the most parts in a single book of collective works.
```
Cypher Query
```
