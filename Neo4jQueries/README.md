# Neo4j cypher queries on Computer Science Publication

According to the graph schema of project, below you will find 18 cypher queries which indicate the powerful features and effectiveness of a graph database like Neo4j. 

## Queries

1.  Find the titles (title, year) of publications that a particular author has published.
```
MATCH (Author {name: 'Sanjay Jain 0001'})-[:PUBLISHED]->(p:Publication)
WHERE p.year <> '' AND p.title <> ''
RETURN p.title AS TITLE, p.year AS YEAR
```

2.  Find the co-authors of an author (name, number of co-authorships) for a particular year.
```
MATCH (a1:Author{name: 'Christoph Meinel'})-[:PUBLISHED]->(p:Publication)<-[:PUBLISHED]-(a2:Author)
WHERE p.year = '1997'
RETURN a1.name AS NAME , size(collect(distinct a2)) AS NUM_CO_AUTHORS
ORDER BY NUM_CO_AUTHORS DESC
```

3.  Find the top-K authors (name, count) with regard to most conference/journal publications. (2 methods)
```
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)-[ISSUED]->()
RETURN a1.name AS NAME, COUNT(p) AS NUM_PUB
ORDER BY NUM_PUB DESC
LIMIT 5 // K = 5
```

4.  Find the top-K authors (name, count) with regard to most co-authors in a single work.
```
MATCH (a1:Author)-[:PUBLISHED]->(p:Publication)<-[:PUBLISHED]-(a2:Author)
WITH a1, a2, size(collect(p)) AS COMMON_PUB
WHERE COMMON_PUB = 1
RETURN a1.name AS NAME, size(collect(distinct a2)) AS NUM_CO_AUTHORS
ORDER BY NUM_CO_AUTHORS DESC
LIMIT 5 // K = 5
```

5.  Find the top-K authors (name, count) with regard to most co-authors in a particular year.
```
MATCH (a1:Author)-[:PUBLISHED]->(p:Publication)<-[:PUBLISHED]-(a2:Author)
WHERE p.year = '2018'
RETURN a1.name AS NAME, size(collect(distinct a2)) AS NUM_CO_AUTHORS
ORDER BY NUM_CO_AUTHORS DESC
LIMIT 5 // K = 5
```

6.  Find the top-K authors (name, count) with regard to most active years.
```
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)
WHERE p.year <> ''
WITH a1, size(collect(distinct p.year)) AS MOST_ACTIVE_YEAR
return a1.name AS AUTHOR, MOST_ACTIVE_YEAR
ORDER BY MOST_ACTIVE_YEAR DESC
LIMIT 5 // K = 5
```

7.  Find the top-K authors (name, count) with regard to most distinct pairs of co-authors that have not published together.
```
MATCH (a1:Author)-[:PUBLISHED]->(p1:Publication)<-[:PUBLISHED]-(a2:Author)
WITH a1, a2, p1
MATCH (a1)-[:PUBLISHED]->(p2:Publication)<-[:PUBLISHED]-(a3:Author)
WITH a1, a2, a3, p1, p2
WHERE p1 <> p2 AND a1 <> a2 AND a1 <> a3 AND a2 <> a3 
AND ID(p1) < ID(p2) AND ID(a1) < ID(a3) AND ID(a2) < ID(a3) 
AND NOT (a2)-[:PUBLISHED]->(:Publication)<-[:PUBLISHED]-(a3)
WITH collect(DISTINCT {author1: a1.name, author2: a2.name, author3: a3.name}) AS AUTHORS
UNWIND AUTHORS AS row
WITH row.author1 AS author1, row.author2 AS author2, row.author3 AS author3
ORDER BY author1 DESC
WITH author1, size(collect(author2)) AS CNT_PAIR_1 , size(collect(author3)) AS CNT_PAIR_2 
RETURN author1 AS AUTHOR , (CNT_PAIR_1 + CNT_PAIR_2) / 2 AS FINAL_SUM
ORDER BY FINAL_SUM DESC
LIMIT 10 // k = 10
```

8.  Find the top-K authors (name, count) with regard to largest average number of journal publications per year (consider only active years).
```
MATCH (p1:Publication)-[:ISSUED]->(j:Journal)<-[:ISSUED]-(p2:Publication)
WITH p1, p2
MATCH (p1)<-[:PUBLISHED]-(a1:Author)-[:PUBLISHED]->(p2)
WHERE p1.year <> '' AND p2.year <> '' AND p1.year = p2.year
WITH a1, collect(DISTINCT {year: p1.year, title: p1.title}) AS YEAR_PUB
UNWIND YEAR_PUB AS row
WITH a1, row.year AS YEAR, row.title AS TITLE
ORDER BY YEAR
WITH a1, YEAR, count(TITLE) as CNT_PER_YEAR
RETURN a1.name AS AUTHOR, round(AVG(CNT_PER_YEAR)) AS AVG_PER_YEAR
ORDER BY AVG_PER_YEAR DESC
LIMIT 10 // K = 10
```

9.  Find the top-K authors (name, count) that a given author has not worked with, with regard to most co-authorships with authors that the given author has worked with.
```
MATCH (a1)-[:PUBLISHED]->(p:Publication)<-[:PUBLISHED]-(a2:Author{name: 'Christoph Meinel'})
WHERE a1 <> a2
WITH DISTINCT a1, a2, p
MATCH (a1)-[:PUBLISHED]->(:Publication)<-[:PUBLISHED]-(a3:Author)
WHERE a1 <> a3 AND a2 <> a3
WITH DISTINCT a3, a1, a2, p
WHERE NOT (a3)-[:PUBLISHED]->(:Publication)<-[:PUBLISHED]-(a2)
WITH a3, size(collect(distinct p)) AS CO_AUTHORS
RETURN a3.name AS AUTHOR, CO_AUTHORS
ORDER BY CO_AUTHORS DESC
LIMIT 5 // k = 5
```

10.  Find the authors (name, count) that have published more than three works in a given single year.
```
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)
WHERE p.year = '1997'
WITH a1, size(collect(distinct p)) AS PUBLICATION
WHERE PUBLICATION >= 3
RETURN a1.name AS AUTHOR, PUBLICATION AS COUNT
ORDER BY COUNT DESC
```

11.  Find the number of pages that a particular author has published in a given year.
```
MATCH (a1:Author{name:'Gerrit Bleumer'})-[PUBLISHED]->(p:Publication)
WHERE p.year = '2011'
RETURN a1.name AS AUTHOR, sum(toInteger(p.pages)) AS TOTAL_PAGES
```

12.  Find the top-K authors (name, count) with regard to articles published in a particular journal as a first/last author in a given year. (2 methods)
```
MATCH (a1:Author)-[pub:PUBLISHED]->(p:Publication)-[ISSUED]->(j:Journal) 
WHERE p.year = '2018' AND j.name = 'meltdownattack.com' AND (pub.order = 'first' OR pub.order = 'last')
RETURN a1.name AS AUTHOR, count(DISTINCT p) AS COUNT
```

13.  Find the three authors that have appeared as co-authors for the most times in a particular journal.
```
MATCH (p:Publication)-[ISSUED]->(j:Journal{name: 'Universität Trier, Mathematik/Informatik, Forschungsbericht'})
MATCH (a1:Author)-[:PUBLISHED]->(p)<-[:PUBLISHED]-(a2:Author)
WITH a1, a2, p
MATCH (a1:Author)-[:PUBLISHED]->(p)<-[:PUBLISHED]-(a3:Author)
WITH a1, a2, a3, p
MATCH (a2:Author)-[:PUBLISHED]->(p)<-[:PUBLISHED]-(a3:Author)
WHERE a1 <> a2 AND a1 <> a3 AND a2 <> a3 AND ID(a1) < ID(a2) AND ID(a1) < ID(a3) AND ID(a2) < ID(a3)
WITH a1, a2 , a3, size(collect(p)) AS cnt
WITH collect(DISTINCT {author1: a1.name, author2: a2.name, author3: a3.name, cnt: cnt}) AS AUTHORS
UNWIND (AUTHORS) AS row
WITH row.author1 AS author1, row.author2 AS author2, row.author3 AS author3, row.cnt AS COUNT
RETURN author1 AS AUTHOR_1, author2 AS AUTHOR_2, author3 AS AUTHOR_3, COUNT
ORDER BY COUNT DESC
```

14.  Find pairs of authors that have appeared in different parts of the same book and have never co-authored a work.
```
MATCH (a1:Author)-[:PUBLISHED]->(p1:Publication)-[:ISSUED]->(c:Conference)<-[:ISSUED]-(p2:Publication)<-[:PUBLISHED]-(a2:Author)
WHERE a1 <> a2 AND ID(a1) < ID(a2) AND NOT (a1)-[:PUBLISHED]->(:Publication)<-[:PUBLISHED]-(a2)
WITH collect(DISTINCT {author1: a1.name, author2: a2.name}) AS PAIRS
UNWIND PAIRS AS row
with row.author1 AS AUTHOR_1, row.author2 AS AUTHOR_2
return AUTHOR_1, AUTHOR_2
```

15.  Find the authors that have published work for K consecutive years.
```
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)
WHERE p.year <> ''
WITH a1, p
ORDER BY p.year
WITH a1, (collect(DISTINCT toInteger(p.year))) AS YEARS
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
  ) AS AGG_CONS_YEARS
UNWIND AGG_CONS_YEARS AS CONS_YEARS
WITH a1, CONS_YEARS
WHERE size(CONS_YEARS) >= 5 // K = 5
RETURN a1.name AS AUTHOR, CONS_YEARS
```

16.  Find the top-K authors with regard to average number of co-authors in their publications.
```
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)<-[:PUBLISHED]-(a2:Author)
WITH DISTINCT a1, size(collect(DISTINCT a2)) AS COUNT_AUTHORS, size(collect(DISTINCT p)) AS COUNT_PUB 
RETURN a1.name AS AUTHOR, COUNT_AUTHORS, COUNT_PUB, COUNT_AUTHORS / COUNT_PUB AS AVG_CO_AUTHORS
ORDER BY AVG_CO_AUTHORS DESC
LIMIT 5 // K = 5
```

17.  Find the authors of consecutively published papers with more than a given amount of years between them.
```
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)
WHERE p.year <> ''
WITH a1, p
ORDER BY p.year
WITH a1, (collect(distinct toInteger(p.year))) AS YEARS
WITH a1, YEARS, [i in range(0, size(YEARS)-2) WHERE YEARS[i+1] = YEARS[i] + 37 | i] AS CONS_YEARS // K = 37
WHERE size(CONS_YEARS) >= 1
RETURN a1.name AS AUTHOR
```

18.  Find the author (name, count) with the most parts in a single book of collective works.
```
MATCH (a1:Author)-[:PUBLISHED]->()-[:ISSUED]->(c:Conference)
WITH a1, c
MATCH (a1)-[:PUBLISHED]->(p:Publication)-[:ISSUED]->(c)
WITH a1, c, size(collect(distinct p)) AS NUM_PUB
RETURN a1.name as AUTHOR, NUM_PUB
ORDER BY NUM_PUB DESC
```
