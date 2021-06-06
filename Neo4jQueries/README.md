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
MATCH (a1:Author)-[:PUBLISHED]->(p1:Publication)<-[:PUBLISHED]-(a2:Author)
with a1, a2, p1
MATCH (a1)-[:PUBLISHED]->(p2:Publication)<-[:PUBLISHED]-(a3:Author)
with a1, a2, a3, p1, p2
where p1 <> p2 and a1 <> a2 and a1 <> a3 and a2 <> a3 
and ID(p1) < ID(p2) and ID(a1) < ID(a3) and ID(a2) < ID(a3) 
and not (a2)-[:PUBLISHED]->(:Publication)<-[:PUBLISHED]-(a3)
with collect(DISTINCT {author1: a1.name, author2: a2.name, author3: a3.name}) AS AUTHORS
UNWIND AUTHORS as row
with row.author1 as author1, row.author2 as author2, row.author3 as author3
order by author1 desc
with author1, size(collect(author2)) as CNT_PAIR_1 , size(collect(author3)) as CNT_PAIR_2 
return author1, (CNT_PAIR_1 + CNT_PAIR_2) / 2 as FINAL_SUM
order by FINAL_SUM desc
limit 10 // k =10

```

8.  Find the top-K authors (name, count) with regard to largest average number of journal publications per year (consider only active years).
```
MATCH (p1:Publication)-[:ISSUED]->(j:Journal)<-[:ISSUED]-(p2:Publication)
with p1, p2
MATCH (p1)<-[:PUBLISHED]-(a1:Author)-[:PUBLISHED]->(p2)
WHERE p1.year <> '' AND p2.year <> '' AND p1.year = p2.year
WITH a1, collect(DISTINCT {year: p1.year, title: p1.title}) AS YEAR_PUB
UNWIND YEAR_PUB as row
with a1, row.year as year
order by year
with a1, year, count(year) as CNT_PER_YEAR
return a1.name, round(AVG(CNT_PER_YEAR)) as AVG_PER_YEAR
order by AVG_PER_YEAR DESC
LIMIT 10 // K=10
```

9.  Find the top-K authors (name, count) that a given author has not worked with, with regard to most co-authorships with authors that the given author has worked with.
```
MATCH (a1)-[:PUBLISHED]->(p:Publication)<-[:PUBLISHED]-(a2:Author{name: 'Christoph Meinel'})
WHERE a1 <> a2
WITH DISTINCT a1, a2, p
MATCH (a1)-[:PUBLISHED]->(:Publication)<-[:PUBLISHED]-(a3:Author)
WHERE a1 <> a3 and a2 <> a3
WITH DISTINCT a3, a1, a2, p
WHERE NOT (a3)-[:PUBLISHED]->(:Publication)<-[:PUBLISHED]-(a2)
WITH a3, size(collect(distinct p)) as CO_AUTHORS
RETURN a3.name, CO_AUTHORS
ORDER BY CO_AUTHORS DESC
LIMIT 5 // k=5
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
MATCH (p:Publication)-[ISSUED]->(j:Journal{name: 'Universität Trier, Mathematik/Informatik, Forschungsbericht'})
with p
MATCH (a1:Author)-[:PUBLISHED]->(p)<-[:PUBLISHED]-(a2:Author)
with a1, a2, p
MATCH (a1:Author)-[:PUBLISHED]->(p)<-[:PUBLISHED]-(a3:Author)
with a1, a2, a3, p
MATCH (a2:Author)-[:PUBLISHED]->(p)<-[:PUBLISHED]-(a3:Author)
where a1 <> a2 and a1 <> a3 and a2 <> a3 and ID(a1) < ID(a2) and ID(a1) < ID(a3) and ID(a2) < ID(a3)
with a1, a2 , a3, size(collect(p)) as cnt
with collect(DISTINCT {author1: a1.name, author2: a2.name, author3: a3.name, cnt: cnt}) AS AUTHORS
UNWIND (AUTHORS) as row
with row.author1 as author1, row.author2 as author2, row.author3 as author3, row.cnt as cnt
return author1, author2, author3, cnt
order by cnt
```

14.  Find pairs of authors that have appeared in different parts of the same book and have never co-authored a work.
```
MATCH (a1:Author)-[:PUBLISHED]->(p1:Publication)-[:ISSUED]->(c:Conference)<-[:ISSUED]-(p2:Publication)<-[:PUBLISHED]-(a2:Author)
with a1, a2
where a1 <> a2 and ID(a1) < ID(a2) and not (a1)-[:PUBLISHED]->(:Publication)<-[:PUBLISHED]-(a2)
with collect(DISTINCT {author1: a1.name, author2: a2.name}) AS PAIRS
UNWIND PAIRS as row
with row.author1 as author1, row.author2 as author2
return author1, author2

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
MATCH (a1:Author)-[PUBLISHED]->(p:Publication)<-[:PUBLISHED]-(a2:Author)
WITH distinct a1, count(distinct a2) as COUNT_AUTHORS, count(distinct p) as COUNT_PUB 
RETURN a1.name,  COUNT_AUTHORS, COUNT_PUB, COUNT_AUTHORS / COUNT_PUB as AVG_CO_AUTHORS
ORDER BY AVG_CO_AUTHORS DESC
LIMIT 5 // K = 5
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
MATCH (a1:Author)-[:PUBLISHED]->()-[:ISSUED]->(c:Conference)
WITH a1, c
MATCH (a1)-[:PUBLISHED]->(p:Publication)-[:ISSUED]->(c)
WITH a1, c, size(collect(distinct p)) as NUM_PUB
return a1.name, NUM_PUB, c.name
ORDER BY NUM_PUB DESC
```
