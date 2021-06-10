# Load graph data (CSV files)

Execute the following commands to create constraints and import data to Neo4j

1.  Author 
```
# Author constraint
CREATE CONSTRAINT author_name_unique ON (author:Author) ASSERT author.name IS UNIQUE

# Load Authors
:auto USING PERIODIC COMMIT 5000
LOAD CSV WITH HEADERS FROM 'file:///authors.csv' AS row
WITH row WHERE row.author_name IS NOT NULL
MERGE (a:Author {name: row.author_name});
```

2.  Publication
```
# Publications constraint
CREATE CONSTRAINT publication_title_unique ON (p:Publication) ASSERT p.id IS UNIQUE

# Load Publications
:auto USING PERIODIC COMMIT 5000
LOAD CSV WITH HEADERS FROM 'file:///publications.csv' AS row
FIELDTERMINATOR '|'
WITH row WHERE row.id IS NOT NULL
CREATE (p:Publication {
                        id: row.id,
                        title: row.title,
						year: coalesce(row.year, ''),
					    pages: coalesce(row.pages, '')});

```

3. Author -[PUBLISHED] -> Publication relationship
```
# LOAD relationship author - PUBLISHED -> publication
:auto USING PERIODIC COMMIT 5000
LOAD CSV WITH HEADERS FROM 'file:///relationship.csv' AS line
FIELDTERMINATOR '|'
MERGE (a1:Author {name:line.author_name})
MERGE (o2:Publication {id:line.id})
CREATE (a1)-[con:PUBLISHED {order: line.author_order}]->(o2) 

# :auto USING PERIODIC COMMIT
# LOAD CSV WITH HEADERS FROM 'file:///relationship.csv' AS line
# MATCH (a:Author {name: line.author_name}),(p:Publication {id:line.id})
# CREATE (a)-[pub:PUBLISHED {order: line.author_order}]->(p)

```

4. Journal
```
# Journals constraint
CREATE CONSTRAINT journal_name_unique ON (j:Journal) ASSERT j.name IS UNIQUE

# Load Journals 5000
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///journals.csv' AS row
WITH row WHERE row.name IS NOT NULL
MERGE (j:Journal {name: row.name});
```

5. Publication -[ISSUED]-> Journal relationship
```
# LOAD relationship Publications - ISSUED -> Journals
:auto USING PERIODIC COMMIT 5000
LOAD CSV WITH HEADERS FROM 'file:///journals_relationship.csv' AS line
FIELDTERMINATOR '|'
MERGE (a1:Publication {id:line.id})
MERGE (a2:Journal {name:line.name})
CREATE (a1)-[iss:ISSUED]->(a2) 

```

6. Conference
```
# Conferences constraint
CREATE CONSTRAINT conference_name_unique ON (c:Conference) ASSERT c.name IS UNIQUE

# Load Conferences
:auto USING PERIODIC COMMIT 5000
LOAD CSV WITH HEADERS FROM 'file:///conferences.csv' AS row
WITH row WHERE row.name IS NOT NULL
MERGE (con:Conference {name: row.name});

```

7. Publication -[ISSUED]-> Conference
```
# LOAD relationship Publications - ISSUED -> Conferences
:auto USING PERIODIC COMMIT 5000
LOAD CSV WITH HEADERS FROM 'file:///conferences_relationship.csv' AS line
FIELDTERMINATOR '|'
MERGE (a1:Publication {id:line.id})
MERGE (a2:Conference {name:line.name})
CREATE (a1)-[iss:ISSUED]->(a2) 
```