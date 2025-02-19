import sqlite3 as sql

def criarTabela():
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS apicep')

    comando = '''CREATE TABLE "apicep" (
        cep VAR(150) NOT NULL,
        logradouro TEXT,
        complemento TEXT,
        unidade TEXT,
        bairro TEXT,
        localidade TEXT,
        uf TEXT,
        estado TEXT,
        regiao TEXT,
        ibge TEXT,
        gia TEXT,
        ddd TEXT,
        siafi TEXT
        )'''

    cur.execute(comando)
    con.close()

def verTabela():
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute("select * from apicep")
    dados = cur.fetchall()
    con.close()
    return dados

def inserirInfo(cepApi, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafi):
    con = sql.connect('banco.db')
    cur = con.cursor()
    cur.execute('insert into apicep (cep, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafi) values(?,?,?,?,?,?,?,?,?,?,?,?,?)', (cepApi, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafi))
    con.commit()
    con.close()

criarTabela()