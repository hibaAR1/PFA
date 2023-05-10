import pymysql


def createTables():
    try:
        cnt = pymysql.connect(host="localhost", port=3306,
                              user="root", password="")
        cntCursor = cnt.cursor()
        queries = [
            'CREATE DATABASE IF NOT EXISTS gestion_vet',
            'USE gestion_vet',
            'create table if not exists animal(Id int(11) NOT NULL, Id_Client int(11) NOT NULL,Nom varchar(60) NOT NULL, Ref varchar(20) NOT NULL,Sexe varchar(60) NOT NULL,Date_naissance varchar(50) NOT NULL,Type varchar(50) NOT NULL,ImagePath varchar(200) NOT NULL)',
            'create table if not exists client(id int(11) NOT NULL,Cne varchar(50) NOT NULL,Nom varchar(60) NOT NULL,Prenom varchar(60) NOT NULL,Tele varchar(60) NOT NULL)',
            'create table if not exists rendezvous (Id int(11) NOT NULL,Id_Patient int(11) NOT NULL,Date_RendezVous varchar(50) NOT NULL,Time_RendezVous varchar(50) NOT NULL,Deplacement varchar(50) NOT NULL,paid varchar(20) NOT NULL DEFAULT "No")',
            'create table if not exists treatement (Id int(11) NOT NULL,Id_Animal int(11) NOT NULL,Nom varchar(60) NOT NULL,DateDebut varchar(60) NOT NULL,DateFin varchar(60) NOT NULL,DosesPerDay int(11) NOT NULL,Prix float NOT NULL,paid varchar(60) NOT NULL DEFAULT "No")',
            'create table if not exists user (id int(11) NOT NULL,Full_Name varchar(60) NOT NULL,Username varchar(60) NOT NULL,Password varchar(60) NOT NULL,Status text NOT NULL) ',
            'ALTER TABLE animal ADD PRIMARY KEY (`Id`),ADD UNIQUE KEY `un` (`Ref`),ADD KEY `Id_Client` (`Id_Client`)',
            'ALTER TABLE client ADD PRIMARY KEY (`id`),ADD UNIQUE KEY `un` (`Cne`)',
            'ALTER TABLE rendezvous ADD PRIMARY KEY (`Id`),ADD KEY `Id_Patient` (`Id_Patient`)',
            'ALTER TABLE treatement ADD PRIMARY KEY (`Id`),ADD KEY `Id_Animal` (`Id_Animal`)',
            'ALTER TABLE user ADD PRIMARY KEY (`id`)',
            'ALTER TABLE animal MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1',
            'ALTER TABLE client MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1',
            'ALTER TABLE rendezvous MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1',
            'ALTER TABLE treatement MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1',
            'ALTER TABLE user MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1',
            'ALTER TABLE animal ADD CONSTRAINT `animal_ibfk_1` FOREIGN KEY (`Id_Client`) REFERENCES `client` (`id`)',
            'ALTER TABLE rendezvous ADD CONSTRAINT `rendezvous_ibfk_1` FOREIGN KEY (`Id_Patient`) REFERENCES `client` (`id`)',
            'ALTER TABLE treatement ADD CONSTRAINT `treatement_ibfk_1` FOREIGN KEY (`Id_Animal`) REFERENCES `animal` (`Id`)']
        for q in queries:
            cntCursor.execute(q)
    except:
        pass


class gestionEmployee:
    def __init__(self):
        try:
            self.mydb = pymysql.connect(
                host="localhost", port=3306, user="root", password="", database="gestion_vet")
            self.mycursor = self.mydb.cursor()
        except:
            pass

    def selectUsername(self, str1):
        self.mycursor.execute(
            f"SELECT * from user WHERE Username = %s", (str1,))
        return self.mycursor.fetchall()

    def selectALL(self):
        self.mycursor.execute("SELECT * FROM user")
        return self.mycursor.fetchall()

    def selectId(self, id1):
        self.mycursor.execute(f"SELECT * FROM user WHERE id = {id1}")
        return self.mycursor.fetchone()

    def insertTbl(self, tpl):
        self.mycursor.execute(
            'INSERT INTO user(Full_Name,Username,Password,Status) VALUES (%s,%s,%s,%s)', tpl)
        self.mydb.commit()


class gestClients:
    def __init__(self):
        try:
            self.mydb = pymysql.connect(
                host="localhost", port=3306, user="root", password="", database="gestion_vet")
            self.mycursor = self.mydb.cursor()
        except:
            pass

    def selectTreat(self, cne):
        self.mycursor.execute(
            f"SELECT treatement.* FROM treatement JOIN animal ON treatement.Id_Animal = animal.Id JOIN client ON animal.Id_Client = client.id WHERE treatement.paid='No' and client.Cne = %s", (cne,))
        return self.mycursor.fetchall()

    def selectRdv(self, cne):
        self.mycursor.execute(
            f"SELECT rendezvous.* FROM rendezvous JOIN client ON rendezvous.Id_Patient = client.id WHERE rendezvous.paid='No' and client.Cne = %s", (cne,))
        return self.mycursor.fetchall()

    def selectNom(self, str1):
        self.mycursor.execute(
            "SELECT * from client WHERE Nom LIKE %s", (str1+'%',))
        return self.mycursor.fetchall()

    def selectCne(self, str1):
        self.mycursor.execute(f"SELECT * from client WHERE Cne = %s", (str1,))
        return self.mycursor.fetchall()

    def selectALL(self):
        self.mycursor.execute("SELECT * FROM client")
        return self.mycursor.fetchall()

    def selectId(self, id1):
        self.mycursor.execute(f"SELECT * FROM client WHERE id = {id1}")
        return self.mycursor.fetchone()

    def insertTbl(self, tpl):
        self.mycursor.execute(
            'INSERT INTO client(id,Cne,Nom,Prenom,Tele) VALUES (%s,%s,%s,%s,%s)', tpl)
        self.mydb.commit()

    def updateTbl(self, tpl):
        self.mycursor.execute(
            'UPDATE client SET Cne=%s,Nom = %s,Prenom = %s,Tele = %s WHERE id = %s', tpl)
        self.mydb.commit()


class gestanimaux:

    def __init__(self):
        try:
            self.mydb = pymysql.connect(
                host="localhost", port=3306, user="root", password="", database="gestion_vet")
            self.mycursor = self.mydb.cursor()
        except:
            pass

    def selectRef(self, str1):
        self.mycursor.execute(
            f"SELECT * from animal WHERE Ref LIKE %s", (str1+"%",))
        return self.mycursor.fetchall()

    def selectALL(self):
        self.mycursor.execute("SELECT * FROM animal")
        return self.mycursor.fetchall()

    def selectId(self, id1):
        self.mycursor.execute(f"SELECT * FROM animal WHERE Id = {id1}")
        return self.mycursor.fetchone()

    def insertTbl(self, tpl):
        self.mycursor.execute(
            'INSERT INTO animal(Id_Client,Nom,Ref,Sexe,Date_naissance,Type,ImagePath) VALUES (%s,%s,%s,%s,%s,%s,%s)', tpl)
        self.mydb.commit()

    def updateTbl(self, tpl):
        self.mycursor.execute(
            'UPDATE animal SET Nom=%s,Sexe = %s,Date_naissance = %s WHERE Id = %s', tpl)
        self.mydb.commit()


class gestrendezvous:
    def __init__(self):
        try:
            self.mydb = pymysql.connect(
                host="localhost", port=3306, user="root", password="", database="gestion_vet")
            self.mycursor = self.mydb.cursor()
        except:
            pass

    def selectDateTime(self, dte, tme):
        self.mycursor.execute(
            f"SELECT * from rendezvous WHERE Date_RendezVous = %s and Time_RendezVous = %s", (dte, tme,))
        return self.mycursor.fetchall()

    def selectALL(self):
        self.mycursor.execute("SELECT * FROM rendezvous")
        return self.mycursor.fetchall()

    def selectId(self, id1):
        self.mycursor.execute(f"SELECT * FROM rendezvous WHERE Id = {id1}")
        return self.mycursor.fetchone()

    def insertTbl(self, tpl):
        self.mycursor.execute(
            'INSERT INTO rendezvous(Id_Patient,Date_RendezVous,Time_RendezVous,Deplacement) VALUES (%s,%s,%s,%s)', tpl)
        self.mydb.commit()

    def updateTbl(self, tpl):
        self.mycursor.execute(
            'UPDATE rendezvous SET Date_RendezVous=%s,Time_RendezVous = %s,Deplacement = %s WHERE Id = %s', tpl)
        self.mydb.commit()

    def paid(self, id):
        self.mycursor.execute(
            f"UPDATE rendezvous SET paid='Yes' WHERE Id = {id}")
        self.mydb.commit()


class gesttreatement:
    def __init__(self):
        try:
            self.mydb = pymysql.connect(
                host="localhost", port=3306, user="root", password="", database="gestion_vet")
            self.mycursor = self.mydb.cursor()
        except:
            pass

    def selectALL(self):
        self.mycursor.execute("SELECT * FROM treatement")
        return self.mycursor.fetchall()

    def selectId(self, id1):
        self.mycursor.execute(f"SELECT * FROM treatement WHERE Id = {id1}")
        return self.mycursor.fetchone()

    def insertTbl(self, tpl):
        self.mycursor.execute(
            'INSERT INTO treatement(Id_Animal,Nom,DateDebut,DateFin,DosesPerDay,Prix) VALUES (%s,%s,%s,%s,%s,%s)', tpl)
        self.mydb.commit()

    def updateTbl(self, tpl):
        self.mycursor.execute(
            'UPDATE treatement SET Nom=%s,DateDebut = %s,DateFin = %s,DosesPerDay=%s,Prix=%s WHERE Id = %s', tpl)
        self.mydb.commit()

    def paid(self, id):
        self.mycursor.execute(
            f"UPDATE treatement SET paid='Yes' WHERE Id = {id}")
        self.mydb.commit()
