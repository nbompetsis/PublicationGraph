# PublicationGraph
This repository holds a Restful API implementation that uses data provided by a graph database ([Neo4j DB](https://neo4j.com)) and exposes information on various queries related to computer science publication. All data used by this project were extracted from the [DBLP](https://dblp.uni-trier.de/) (Online Computer Science Bibliography) website.

Publication Graph project consists of three essential parts:

* DBLP dataset Parser
* Neo4j (Graph Database) setup
* RestFul API

## DBLP Parser
DBLP Parser project aims to perform the ETL process leveraging dataset of computer science publications by DBLP data source. More specifically, DBLP provides a large xml dataset containing articles, proceedings, incollection, etc.

### Extract phase 
In our use case we focused only on the following three categories of publication.
* Article: An article published in a journal.
* Inproceedings: Article that appeared in the proceedings of a conference.
* Incollection: Part of a book having its own title.

### Transform phase
Based on the graph schema we chose (see below the Labeled Property Graph model) we collected and transformed the data of each category in a way to serve us for the final step of load phase.

### Load phase
The transformed data used to create the final csv files. These files contain the suitable information for the needs of publication graph project such as authors, publications, relationships between authors and publications (author-[PUBLISHED]->publication), journals, conferences and publication issued on conferences and journal (publication-[ISSUED]->(journal, conference)). 

Finally, you must copy the csv files under the **docker-compose-setup/neo4j/import** directory to be ready for the insertion in Neo4j.

More information about DBLP Parser can be found [here](./DBLPParser/README.md).

## Neo4j setup

### Neo4j Graph Schema
The schema of Neo4j consists of the following nodes and relationships:

* Nodes

    1.    Author: Properties: name
    2.    Publication: Properties: id, title, year, pages
    3.    Journal: Properties: name
    4.    Conference: Properties: name


* Relationship

    1.    PUBLISHED: Author-[PUBLISHED]->Publication, Properties: order (values: first, middle and last)
    2.    ISSUED: Publication -[ISSUED]-> Conference or Journal

![Screenshot 2021-06-10 at 3 54 31 AM](https://user-images.githubusercontent.com/11991105/121448088-a202af00-c99f-11eb-892e-c3c9d9a65574.png)


### Data insertion
When you execute the ```docker up``` command that you can find in **Run Project** section, you can execute the [script](./docker-compose-setup/neo4j/script/README.md) to import data into Neo4j by using the following process.

Execution of script:
* Open browser
* Go to http://localhost:7474/browser/
* Login to Neo4j DB
* Run script.

## Rest API
A Rest API was created on top of Neo4j exposing results on various queries related to nodes and relationships of graph schema. For the needs of the project implemented 18 [cypher queries](./Neo4jQueries/README.md) which indicate the powerful features and efficiency of a graph database like Neo4j on heavy queries.

All curl requests from the endpoints of Rest API are collected and can be found [here](./RestAPI/CurlRequests/README.md). 

The Rest API of project was implemented by the [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework.

## Run Project

To run project you have to install on your local environment the following prerequisite services.
```
Install docker and docker-compose services

1.  https://docs.docker.com/get-docker/
2.  https://docs.docker.com/compose/install/
```

After installation of docker and docker-compose services, you are ready to run the PublicationGraph project using the following commands

```
# Go to docker-compose-setup directory
$ cd docker-compose-setup/

# Build Rest API image
$ docker-compose build

# Start Neo4j and Rest API containers
$ docker-compose up

# Stop Neo4j and Rest API containers
$ docker-compose stop

# Destroy Neo4j and Rest API containers
$ docker-compose down
```
