# DBLP Parser

This project is a python parser for [DBLP dataset](https://dblp.uni-trier.de/), the XML format dumped file can be downloaded [here](http://dblp.org/xml/) from [DBLP Homepage](https://dblp.org/). 

DBLP parser focuses on the following essential entities.
```
• Article: An article published in a journal. Mandatory fields: author, title, year, journal.

• Inproceedings: Article that appeared in the proceedings of a conference. Mandatory fields: author, title, booktitle, year.

• Incollection: Part of a book having its own title. Mandatory fields: author, title, booktitle, publisher, year.

```

This parser requires `dtd` file, so make sure you have both `dblp-XXX.xml` and `dblp-XXX.dtd` located under dataset directory. Note that you also should guarantee that both `xml` and `dtd` files are in the same directory, and the name of `dtd` file should same as the name given in the `<!DOCTYPE>` tag of the `xml` file.

After processing data, parser collects the appropriate data and creates three csv files including authors, publications and the relationships between authors and publications.

## Run parser 

```
# Create Virtual environment
$ python3 -m pip install -r requirements.txt

# Execute parser
$ python3 src/parser.py -number <Number of publication>

# OR Execute parser with default argument (1000000 publication to be parsed)
$ python3 src/parser.py

# Copy extracted csv files into neo4j import directory 
$ cp ./dataset/authors.csv ../docker-compose-setup/neo4j/import
$ cp ./dataset/publications.csv ../docker-compose-setup/neo4j/import
$ cp ./dataset/relationship.csv ../docker-compose-setup/neo4j/import
```

## CSV files

* Authors csv file

```
author_name
Martín García
Yuxuan Shen
Yazhou Wang
Hüseyin Acan
Martina Slapkova
Vicente Bringas-Rico
Michael J. Harrison
Susanne Englert
Maria Daidone
Wensheng Song
...
...
```

* Publications csv file

```
title|type|year|conference_type|conference_name|pages
Spectre Attacks: Exploiting Speculative Execution.|article|2018|journal|meltdownattack.com|
Meltdown|article|2018|journal|meltdownattack.com|
An Evaluation of Object-Oriented DBMS Developments: 1994 Edition.|article|1994|journal|GTE Laboratories Incorporated|
DARWIN: On the Incremental Migration of Legacy Information Systems|article|1993|journal|GTE Laboratories Incorporated|
Integrating Heterogeneous, Autonomous, Distributed Applications Using the DOM Prototype.|article|1991|journal|GTE Laboratories Incorporated|
Object Model Capabilities For Distributed Object Management.|article|1989|journal|GTE Laboratories Incorporated|
Integrating Object-Oriented Applications and Middleware with Relational Databases.|article|1995|journal|GTE Laboratories Incorporated|
Towards a Transaction Management System for DOM.|article|1991|journal|GTE Laboratories Incorporated|
A 'RISC' Object Model for Object System Interoperation: Concepts and Applications.|article|1993|journal|GTE Laboratories Incorporated|
...
```

* Relationship csv file

```
author_name|title|author_order
Paul Kocher|Spectre Attacks: Exploiting Speculative Execution.|first
Daniel Genkin|Spectre Attacks: Exploiting Speculative Execution.|middle
Daniel Gruss|Spectre Attacks: Exploiting Speculative Execution.|middle
Werner Haas 0004|Spectre Attacks: Exploiting Speculative Execution.|middle
Mike Hamburg|Spectre Attacks: Exploiting Speculative Execution.|middle
Moritz Lipp|Spectre Attacks: Exploiting Speculative Execution.|middle
Stefan Mangard|Spectre Attacks: Exploiting Speculative Execution.|middle
Thomas Prescher 0002|Spectre Attacks: Exploiting Speculative Execution.|middle
Michael Schwarz 0001|Spectre Attacks: Exploiting Speculative Execution.|middle
Yuval Yarom|Spectre Attacks: Exploiting Speculative Execution.|last
Moritz Lipp|Meltdown|first
Michael Schwarz 0001|Meltdown|middle
Daniel Gruss|Meltdown|middle
Thomas Prescher 0002|Meltdown|middle
Werner Haas 0004|Meltdown|middle
Stefan Mangard|Meltdown|middle
Paul Kocher|Meltdown|middle
Daniel Genkin|Meltdown|middle
Yuval Yarom|Meltdown|middle
Mike Hamburg|Meltdown|last
Frank Manola|An Evaluation of Object-Oriented DBMS Developments: 1994 Edition.|first
Michael L. Brodie|DARWIN: On the Incremental Migration of Legacy Information Systems|first
Michael Stonebraker|DARWIN: On the Incremental Migration of Legacy Information Systems|last
Mark F. Hornick|Integrating Heterogeneous, Autonomous, Distributed Applications Using the DOM Prototype.|first
Joe D. Morrison|Integrating Heterogeneous, Autonomous, Distributed Applications Using the DOM Prototype.|middle
Farshad Nayeri|Integrating Heterogeneous, Autonomous, Distributed Applications Using the DOM Prototype.|last
Frank Manola|Object Model Capabilities For Distributed Object Management.|first
Frank Manola|Integrating Object-Oriented Applications and Middleware with Relational Databases.|first
Alejandro P. Buchmann|Towards a Transaction Management System for DOM.|first
M. Tamer Özsu|Towards a Transaction Management System for DOM.|middle
Dimitrios Georgakopoulos|Towards a Transaction Management System for DOM.|last
```