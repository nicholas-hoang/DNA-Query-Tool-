import psycopg2
import csv
import os

# connect to the PostgreSQL database 'ex1' and return the connection object.


def init_db():
    """ This function connects to the PostgreSQL database 'ex1'
        and returns the connection object.

    Returns:
        _type_: psycopg2.extensions.connection
    """
    conn = psycopg2.connect(
        database="ex1",
        user="postgres",
        password='passwordtaco',
        host="localhost",
        port='5432'
    )
    return conn


# retrieve information about the gene from the genes table
def get_gene_info(conn, gene_id):
    """
    This function retrieves information about the gene from the genes table.
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM genes WHERE geneid = %s", (gene_id,))
    gene_info = cur.fetchone()

    print("geneid:", gene_info[0])
    print("gene_name:", gene_info[1])
    print("proteinid:", gene_info[2])
    print("protein_size:", gene_info[3])
    print("protein_desc:", gene_info[4])

    # write gene information to csv file
    with open('gene_info.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["geneid", "gene_name", "proteinid",
                        "protein_size", "protein_desc"])
        writer.writerow([gene_info[0], gene_info[1],
                        gene_info[2], gene_info[3], gene_info[4]])


def get_rsid_info(conn, gene_id, model_weight):
    """
    This function retrieves information about the rsids with weight
    higher than the input weight for the given gene.
    """
    cur = conn.cursor()
    cur.execute("SELECT rsid, geneid, weight FROM weights WHERE geneid = %s AND weight > %s ORDER BY weight ASC",
                (gene_id, model_weight))

    rsid_info = cur.fetchall()

    print("\nRSIDs with weight higher than",
          model_weight, "for gene", gene_id + ":")

    # write rsid information to csv file
    with open('rsid_info.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["rsid", "geneid", "weight"])
        for rsid in rsid_info:
            writer.writerow([rsid[0], rsid[1], rsid[2]])
            print(" ---------------------------------")
            print("rsid:", rsid[0])
            print("geneid:", rsid[1])
            print("weight:", rsid[2])


def close_db(conn):
    """
    This function closes the communication with the PostgreSQL database.
    """
    conn.close()


def main():
    print("Welcome to the gene information database!")
    ex1_conn = init_db()
    gene_id = input("Please enter a gene id: ")
    model_weight = input("Please enter a model weight: ")
    get_gene_info(ex1_conn, gene_id)
    get_rsid_info(ex1_conn, gene_id, model_weight)
    close_db(ex1_conn)


if __name__ == '__main__':
    main()
    start = input('Would you like to query another gene? (y/n): ')

    if start == 'y':
        os.system('cls')
        main()
    else:
        print('Thank you for using the gene information database!')
