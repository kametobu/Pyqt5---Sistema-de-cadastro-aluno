import mysql.connector
from mysql.connector import errorcode
import socket

class Banco:
    def __init__(self):
        
        banco = {
            'host':'127.0.0.1',
            'user':'root',
            'password': '',
            'database':'lbsumare',
            'port': '3306',
        }
        conn = mysql.connector.connect(**banco)
        cursor= conn.cursor() 
        cursor= conn.cursor(buffered=True)
        conn.commit()
        self.conn = conn
        self.cursor = cursor
  
    def criar_tabelas(self):
        cur = self.cursor
        try:
            cur.execute("CREATE TABLE user(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,login VARCHAR(250) NOT NULL,password VARCHAR(50) NOT NULL,admin BOOLEAN);")
            cur.execute("CREATE TABLE atividades(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,Atividade VARCHAR(250) NOT NULL);")
            cur.execute("CREATE TABLE Cursos(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,curso VARCHAR(250) NOT NULL);")
            cur.execute("CREATE TABLE unidades(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,NomeUnidade VARCHAR(250) NOT NULL,Endereço VARCHAR(250) NOT NULL,CNPJ VARCHAR(250) NOT NULL,CEP VARCHAR(250) NOT NULL,Regiao VARCHAR(250) NOT NULL);")
            cur.execute("CREATE TABLE cadastroprincipal(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,Nome VARCHAR(250) NOT NULL,CPF VARCHAR(50) NOT NULL,email VARCHAR(250) NOT NULL,login VARCHAR(50) NOT NULL,senha VARCHAR(50) NOT NULL,atividade INT(6) UNSIGNED, CONSTRAINT atividade_id FOREIGN KEY(atividade) REFERENCES atividades(id),curso INT(6) UNSIGNED, CONSTRAINT curso_id FOREIGN KEY(curso) REFERENCES Cursos(id),unidade INT(6) UNSIGNED, CONSTRAINT unidade_id FOREIGN KEY(unidade) REFERENCES unidades(id), IMG MEDIUMBLOB);")
        except:
            pass
    
    def pegar_dados(self,query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall() 

    def inserir_apaga_atualizar(self,query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()

    def add(self,Nome,CPF,Email,Login,Senha,Atividade,Curso,Unidade,blob):
        cur = self.cursor
        sql = "INSERT INTO cadastroprincipal (Nome, CPF, email, login, senha, atividade, curso, unidade , IMG) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql, (Nome,CPF,Email,Login,Senha,Atividade,Curso,Unidade,blob))
        self.conn.commit()

    
    def upgrade(self,Nome,CPF,Email,Login,Senha,Atividade,Curso,Unidade,ImgSrc,AtId):
        cur = self.cursor
        sql = "UPDATE cadastroprincipal SET nome=%s,cpf=%s,email=%s,login = %s, senha=%s,atividade=%s,curso=%s,unidade=%s,IMG = %s WHERE cadastroprincipal.id=%s;"
        cur.execute(sql, (Nome,CPF,Email,Login,Senha,Atividade,Curso,Unidade,ImgSrc,AtId))
        self.conn.commit()

    def upgradeS(self,Nome,CPF,Email,Login,Atividade,Curso,Unidade,ImgSrc,AtId):
        cur = self.cursor
        sql = "UPDATE cadastroprincipal SET nome= %s,cpf= %s,email= %s,login = %s, atividade= %s,curso= %s,unidade= %s,IMG = %s WHERE cadastroprincipal.id=%s;"
        cur.execute(sql, (Nome,CPF,Email,Login,Atividade,Curso,Unidade,ImgSrc,AtId))
        self.conn.commit()

    def crirAdmin(self):
        cur = self.cursor
        try:
            cur.execute("INSERT INTO user(login, password) VALUES('admin','21232f297a57a5a743894a0e4a801fc3')")
        except:
            pass
        self.conn.commit()
    

        

db = Banco()

#db.criar_tabelas()

#db.crirAdmin()



      
