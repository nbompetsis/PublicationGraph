# DBLP Parser

This project is a python parser for [DBLP dataset](https://dblp.uni-trier.de/), the XML format dumped file can be downloaded [here](http://dblp.org/xml/) from [DBLP Homepage](https://dblp.org/). 

DBLP parser focuses on the following essential entities.
```
• Article: An article published in a journal. Mandatory fields: author, title, year, journal.

• Inproceedings: Article that appeared in the proceedings of a conference. Mandatory fields: author, title, booktitle, year.

• Incollection: Part of a book having its own title. Mandatory fields: author, title, booktitle, publisher, year.

```

DBLP Parser collects and transforms data of each category in a way to be imported into csv files. The final csv files include data related to authors, publications, relationships between authors and publications (author-[PUBLISHED]->publication), journals, publication issued on journals, conferences and publication issued on conferences (publication-[ISSUED]->(journal, conference)).

**Import step before parser execution**

Parser requires `dtd` file, so make sure you have both `dblp-XXX.xml` and `dblp-XXX.dtd` located under **dataset** directory. Note that you also should guarantee that both `xml` and `dtd` files are in **dataset** directory, and the name of `dtd` file should same as the name given in the `<!DOCTYPE>` tag of the `xml` file.

## Run parser 
```
# Create Virtual environment
$ python3 -m pip install -r requirements.txt

# Execute parser
$ python3 src/parser.py -number <Number of publication>

# OR Execute parser with default argument (1000000 publication to be parsed)
$ python3 src/parser.py

# Copy extracted csv files into neo4j import directory 
$ cp ./dataset/*.csv ../docker-compose-setup/neo4j/import
```

## CSV files

* Authors csv file
```
author_name
Martín García
Yuxuan Shen
Yazhou Wang
Hüseyin Acan
...
...
```

* Publications csv file
```
id|title|year|pages
https://spectreattack.com/spectre.pdf|Spectre Attacks: Exploiting Speculative Execution.|2018|0
https://doi.org/10.1007/978-1-4419-5906-5_738|Ear Shape for Biometric Identification.|2011|7
http://www.mitre.org/support/swee/rosenthal.html|The Future of Classic Data Administration: Objects + Databases + CASE|1998|0
...
```

* author-[PUBLISHED]->publication csv file
```
author_name|id|author_order
Paul Kocher|https://spectreattack.com/spectre.pdf|first
Daniel Genkin|https://spectreattack.com/spectre.pdf|middle
Daniel Gruss|https://spectreattack.com/spectre.pdf|middle
Werner Haas 0004|https://spectreattack.com/spectre.pdf|middle
Mike Hamburg|https://spectreattack.com/spectre.pdf|middle
Moritz Lipp|https://spectreattack.com/spectre.pdf|middle
Stefan Mangard|https://spectreattack.com/spectre.pdf|middle
Thomas Prescher 0002|https://spectreattack.com/spectre.pdf|middle
Michael Schwarz 0001|https://spectreattack.com/spectre.pdf|middle
Yuval Yarom|https://spectreattack.com/spectre.pdf|last
```

* Journals csv file
```
name
meltdownattack.com
...
```

* publication-[ISSUED]->(journal) csv file
```
id|name
https://spectreattack.com/spectre.pdf|meltdownattack.com
...
```

* Conference csv file
```
name
SWEE
...
```

* publication-[ISSUED]->(conference) csv file
```
id|name
http://www.mitre.org/support/swee/rosenthal.html|SWEE
...
```