# Load csv commands

Execute the following command to import csv files into Neo4J

```
# Author constraints
CREATE CONSTRAINT author_name_unique ON (author:Author) ASSERT author.name IS UNIQUE

# Load Authors
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///authors.csv' AS row
WITH row WHERE row.author_name IS NOT NULL
MERGE (a:Author {name: row.author_name});


# Publications constraints
CREATE CONSTRAINT publication_title_unique ON (p:Publication) ASSERT p.id IS UNIQUE

# DROP CONSTRAINT
# ON (n:Publication)
# ASSERT n.title IS UNIQUE

# Load Publications
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///publications.csv' AS row
FIELDTERMINATOR '|'
WITH row WHERE row.id IS NOT NULL
CREATE (p:Publication {
                        id: row.id,
                        title: row.title,
					    type: row.type,
					    year: coalesce(row.year, ''),
					    pages: coalesce(row.pages, '')});


# LOAD relationship author - PUBLISHED -> publication
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///relationship.csv' AS line
FIELDTERMINATOR '|'
MERGE (a1:Author {name:line.author_name})
MERGE (o2:Publication {id:line.id})
CREATE (a1)-[con:PUBLISHED {order: line.author_order}]->(o2) 

# :auto USING PERIODIC COMMIT
# LOAD CSV WITH HEADERS FROM 'file:///relationship.csv' AS line
# MATCH (a:Author {name: line.author_name}),(p:Publication {title:line.title})
# CREATE (a)-[pub:PUBLISHED_NEW {order: line.author_order}]->(p)


# Journals constraint
CREATE CONSTRAINT journal_name_unique ON (j:Journal) ASSERT j.name IS UNIQUE

# Load Journals
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///journals.csv' AS row
WITH row WHERE row.name IS NOT NULL
MERGE (j:Journal {name: row.name});

# LOAD relationship Publications - ISSUED -> Journals
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///journals_relationship.csv' AS line
FIELDTERMINATOR '|'
MERGE (a1:Publication {id:line.id})
MERGE (a2:Journal {name:line.name})
CREATE (a1)-[iss:ISSUED]->(a2) 


# Conferences constraint
CREATE CONSTRAINT conference_name_unique ON (c:Conference) ASSERT c.name IS UNIQUE

# Load Conferences
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///conferences.csv' AS row
WITH row WHERE row.name IS NOT NULL
MERGE (con:Conference {name: row.name});

# LOAD relationship Publications - ISSUED -> Conferences
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///conferences_relationship.csv' AS line
FIELDTERMINATOR '|'
MERGE (a1:Publication {id:line.id})
MERGE (a2:Conference {name:line.name})
CREATE (a1)-[iss:ISSUED]->(a2) 
```