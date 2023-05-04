import mysql.connector

class Boutique:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="boutique"
        )
        self.mycursor = self.mydb.cursor()


    def table_product(self):
        self.mycursor.execute("CREATE TABLE produit(id int AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), "
                              "prix int, quantité int, id_categorie int, description TEXT)")
        self.mydb.commit()

    def table_category(self):
        self.mycursor.execute("CREATE TABLE categorie(id int AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255))")
        self.mydb.commit()

    def add_product(self):
        produit = ("INSERT INTO produit(nom, prix, quantité, id_categorie, description) VALUES (%s, %s, %s, %s, %s)")
        val = (input("entrez le nom du produit :"), input("entrez le prix du produit :"),
               input("entrez la quantité du produit :"), input("entrez l'id de catégorie du produit :"),
               input("entrez la description du produit :"))
        self.mycursor.execute(produit, val)
        self.mydb.commit()

    def read_product(self, id):
        query = "SELECT * FROM produit WHERE id=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        return self.mycursor.fetchone()


    def update_product(self, id, nom, prix, quantite, id_categorie, description):
        query = "UPDATE produit SET nom=%s, prix=%s, quantite=%s, id_categorie=%s, description=%s WHERE id=%s"
        val = (nom, prix, quantite, id_categorie, description, id)
        self.mycursor.execute(query, val)
        self.mydb.commit()

    def delete_product(self, id):
        query = "DELETE FROM produit WHERE id=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        self.mydb.commit()

    def add_category(self):
        categorie = ("INSERT INTO categorie (nom) VALUES (%s)")
        val = (input("entrez le nom de la catégorie :"),)
        self.mycursor.execute(categorie, val)
        self.mydb.commit()

    def read_category(self, id):
        query = "SELECT * FROM categorie WHERE id=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        return self.mycursor.fetchone()

    def update_category(self, id, nom):
        query = "UPDATE categorie SET nom=%s WHERE id=%s"
        val = (nom, id)
        self.mycursor.execute(query, val)
        self.mydb.commit()

    def delete_category(self, id):
        query = "DELETE FROM categorie WHERE id=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        self.mydb.commit()


boutique = Boutique()
#boutique.table_product()
#boutique.table_category()
boutique.add_product()
#boutique.add_category()