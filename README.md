# PublicationGraph
This repository holds a Restful API implementation that uses data provided by a graph database ([Neo4j DB](https://neo4j.com)) and exposes information on various queries related to computer science publication. All data used by this project was extracted from the [DBLP](https://dblp.uni-trier.de/) (Online Computer Science Bibliography) website.

Publication Graph project consists of three essential parts:

* DBLP dataset Parser
* Neo4j (Graph Database) setup
* RestFul API

## DBLP Parser
DBLP Parser project aims to perform the ETL process for the extracted dataset of computer science publications by DBLP data source. More specifically, DBLP data source provides a large xml dataset containing articles, proceedings, incollection and a lot of other stuff that are documented on the [dtd](https://dblp.org/xml/dblp.dtd) file. 

### Extract phase 
In our use case we focused only on the following three categories of publication.
• Article: An article published in a journal.
• Inproceedings: Article that appeared in the proceedings of a conference.
• Incollection: Part of a book having its own title.

### Transform phase
After retrieving the specific entities of xml dataset the next step is the transformation. Based on the graph schema we chose (see below the Labeled Property Graph model) we collected and transformed the data of each category in a way to serve us for the final step of load phase.

### Load phase
The final step is to create csv files using the transformed data and after that to insert them in Neo4j. The final csv files include data related to authors, publications, relationships between authors and publications (author-[PUBLISHED]->publication), journals, publication issued on journals, conferences and publication issued on conferences (publication-[ISSUED]->(journal, conference)).

### Extra info
Extra information about DBLP Parser implementation and execution instructions can be found [here](./DBLPParser/README.md).

## Neo4j setup
After the creation of csv files that covered in the latest section, the data are ready for the insertion in Neo4j DB. As you will see in one of the following sections, Neo4j DB is configured as docker container, so the final csv files must be copied under the docker-compose-setup/neo4j/import directory.

After successful instantiation of Neo4j the developer must perform manual import data by using insertion [script](./docker-compose-setup/neo4j/script/README.md).

Execute insertion script process:
* Open browser
* Go to http://localhost:7474/browser/
* Login to Neo4j DB
* Execute insertion script.

## Neo4j Graph Schema
The schema of Neo4j consists of the following nodes and relationships:

* Nodes

    1.    Author: Properties: name
    2.    Publication: Properties: id, title, year, pages
    3.    Journal: Properties: name
    4.    Conference: Properties: name


* Relationhhip

    1.    PUBLISHED: Author-[PUBLISHED]->Publication, Properties: order (values: first, middle and last)
    2.    ISSUED: Publication -[ISSUED]-> Conference or Journal

![Screenshot 2021-06-10 at 3 54 31 AM](https://user-images.githubusercontent.com/11991105/121448088-a202af00-c99f-11eb-892e-c3c9d9a65574.png)


## Rest API
A Rest API was created on top of Neo4j exposing results on various queries related to nodes and relationships of graph schema. For the needs of the project implemented 18 [cypher queries](./Neo4jQueries/README.md) which indicate the powerful features and efficiency of a graph database like Neo4j on heavy queries.

The curl commands of the Rest API requests can be found [here](./RestAPI/CurlRequests/README.md). 

The Rest API of project was implemented by the use of [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework.

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
