# Load csv commands

Execute the following command to import csv files into Neo4J

```
# Author contraints
CREATE CONSTRAINT author_name_unique ON (author:Author) ASSERT author.name IS UNIQUE

# Load Authors
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///authors.csv' AS row
WITH row WHERE row.author_name IS NOT NULL
MERGE (a:Author {name: row.author_name});


# Publications contraints
# CREATE CONSTRAINT publication_title_unique ON (p:Publication) ASSERT p.title IS UNIQUE

# DROP CONSTRAINT
# ON (n:Publication)
# ASSERT n.title IS UNIQUE

# Load Publications
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///publications.csv' AS row
FIELDTERMINATOR '|'
WITH row WHERE row.title IS NOT NULL
CREATE (p:Publication {title: row.title,
					  type: row.type,
					  year: coalesce(row.year, ''),
					  conf_type: coalesce(row.conference_type, ''),
					  conf_name: coalesce(row.conference_name, ''),
					  pages: coalesce(row.pages, '')});


# LOAD relationShip
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///relationship.csv' AS line
FIELDTERMINATOR '|'
MERGE (a1:Author {name:line.author_name})
MERGE (o2:Publication {title:line.title})
CREATE (a1)-[con:PUBLISHED_NEW {order: line.author_order}]->(o2) 

# :auto USING PERIODIC COMMIT
# LOAD CSV WITH HEADERS FROM 'file:///relationship.csv' AS line
# MATCH (a:Author {name: line.author_name}),(p:Publication {title:line.title})
# CREATE (a)-[pub:PUBLISHED_NEW {order: line.author_order}]->(p)
```