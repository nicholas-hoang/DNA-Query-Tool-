# DNA Query Tool 

## Description
This is a Python program that retrieves information about genes and their corresponding rsids from a PostgreSQL database. The program takes user input for a gene id and a model weight, and then outputs information about the gene and rsids with weights higher than the input weight.

## Getting Started

### Installing
Before running the program, make sure you have the following installed:

Python 3.6 or later
psycopg2 module (you can install it using pip install psycopg2)
PostgreSQL database
Once you have installed these dependencies, you can download the program and run it using the command python gene_info_db.py.

### Executing program
When you run the program, you will be prompted to enter a gene id and a model weight. The program will then retrieve information about the gene from the genes table in the PostgreSQL database, and rsids with weights higher than the input weight from the weights table. The gene information and rsid information will be printed to the console, and also written to separate CSV files (gene_info.csv and rsid_info.csv, respectively).

If you want to query another gene, you can enter 'y' when prompted, and the program will start over.

### Database schema
The program assumes that the PostgreSQL database has the following schema:

genes table
Column name	Data type
geneid	text
gene_name	text
proteinid	text
protein_size	integer
protein_desc	text
weights table
Column name	Data type
rsid	text
geneid	text
weight	numeric

Version History
[Insert a list of the project's version history here]

### License
This program is licensed under the MIT License. Feel free to modify and distribute it as you see fit.

