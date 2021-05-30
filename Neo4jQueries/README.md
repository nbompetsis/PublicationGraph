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
WHERE p.year = '1997'
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
RETURN a1.name, COUNT(a2) as NUM_CO_AUTHORS
ORDER BY NUM_CO_AUTHORS DESC
LIMIT 5 // K = 5
```

5.  Find the top-K authors (name, count) with regard to most co-authors in a particular year.
```
MATCH (a1:Author)-[:PUBLISHED]->(p:Publication)<-[:PUBLISHED]-(a2:Author)
WHERE p.year = '2018'
RETURN a1.name, COUNT(a2) as NUM_CO_AUTHORS
ORDER BY NUM_CO_AUTHORS DESC
LIMIT 5 // K = 5
```

6.  Find the top-K authors (name, count) with regard to most active years.
```
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)
WHERE p.year <> ''
WITH a1, size(collect(distinct p.year)) as activeYears
return a1.name, activeYears as MOST_ACTIVE_YEAR
ORDER BY MOST_ACTIVE_YEAR DESC
LIMIT 5 // K = 5
```

7.  Find the top-K authors (name, count) with regard to most distinct pairs of co-authors that have not published together.
```
MATCH (a1:Author)-[r1:PUBLISHED]->(p1:Publication)<-[:PUBLISHED]-(a2:Author), (a1:Author)-[r2:PUBLISHED]->(p2:Publication)<-[:PUBLISHED]-(a3:Author)
WHERE p1.id <> p2.id 
with a1, a2, a3, r1, r2
WHERE NOT ((a2)-[:PUBLISHED]->(:Publication)<-[:PUBLISHED]-(a3))
return distinct a1.name, count(distinct r1) + count(distinct r2) as MOST_DISTINCT_PAIRS
ORDER BY MOST_DISTINCT_PAIRS ASC
LIMIT 5 // K = 5

A, B, C -> P1 // A -> P1 <- B, A -> P1 <- C

A, D, E -> P2 // A -> P2 <- D, A -> P2 <- E

C, E -> P3


MATCH (a1:Author)-[:PUBLISHED]->(p1:Publication)<-[:PUBLISHED]-(a2:Author), (a1:Author)-[r2:PUBLISHED]->(p2:Publication)<-[:PUBLISHED]-(a3:Author)
WHERE p1.id <> p2.id and a2 <> a3
return distinct a1.name //, count(distinct r1) + count(distinct r2) as MOST_DISTINCT_PAIRS
ORDER BY MOST_DISTINCT_PAIRS ASC
LIMIT 5 // K = 5



MATCH (a1:Author)-[:PUBLISHED]->(p1:Publication)<-[:PUBLISHED]-(a2:Author), (a1:Author)-[:PUBLISHED]->(p2:Publication)<-[:PUBLISHED]-(a3:Author)
WHERE p1.id <> p2.id
WI
MATCH (p2)-[:CAST]->(m:Movie)<-[:CAST]-(p:Person)
WHERE p.id <> 1090464 AND p2 <> p
WITH DISTINCT p
MATCH (p1:Person {id: 1090464})
WHERE NOT (p)-[:CAST]->(:Movie)<-[:CAST]-(p1)
RETURN p.id AS id, p.name AS name


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
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)
WHERE p.year = '1997'
WITH a1, size(collect(distinct p)) as PUBLICATION
WHERE PUBLICATION >= 3
RETURN a1.name, PUBLICATION as COUNT
ORDER BY COUNT DESC
```

11.  Find the number of pages that a particular author has published in a given year.
```
MATCH (a1:Author{name:'Gerrit Bleumer'})-[PUBLISHED]->(p:Publication)
WHERE p.year = '2011'
return a1.name, sum(toInteger(p.pages))
```

12.  Find the top-K authors (name, count) with regard to articles published in a particular journal as a first/last author in a given year. (2 methods)
```
MATCH (a1:Author)-[pub:PUBLISHED]->(p:Publication)-[ISSUED]->(j:Journal) 
WHERE p.year = '2018' and j.name = 'meltdownattack.com' and (pub.order = 'first' or pub.order = 'last')
return a1.name, count(p)
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
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)
WHERE p.year <> ''
WITH a1, p
ORDER BY p.year
WITH a1, (collect(distinct toInteger(p.year))) as YEARS
WITH a1, reduce(acc = [], i IN range(0, size(YEARS) - 1) | 
    CASE YEARS[i] = YEARS[i-1] + 1
      WHEN true THEN [j IN range(0, size(acc) - 1) |
          CASE j = size(acc) - 1
            WHEN true THEN acc[j] + [YEARS[i]]
            ELSE acc[j]
          END
        ]
      ELSE acc + [[YEARS[i]]]
    END
  ) AS AGG__CONS_YEARS // (1)
UNWIND AGG__CONS_YEARS AS CONS_YEARS
WITH a1, CONS_YEARS
WHERE size(CONS_YEARS) >= 5 // K = 5
RETURN a1.name, CONS_YEARS
```

16.  Find the top-K authors with regard to average number of co-authors in their publications.
```
Cypher Query
```

17.  Find the authors of consecutively published papers with more than a given amount of years between them.
```
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)
WHERE p.year <> ''
WITH a1, p
ORDER BY p.year
WITH a1, (collect(distinct toInteger(p.year))) as YEARS
WITH a1, YEARS, [i in range(0, size(YEARS)-2) WHERE YEARS[i+1] = YEARS[i] + 37 | i] AS CONS_YEARS // K=37
WHERE size(CONS_YEARS) >= 1
RETURN a1.name, YEARS, CONS_YEARS
```

18.  Find the author (name, count) with the most parts in a single book of collective works.
```
Cypher Query
```
