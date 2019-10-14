import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(user="daniel", passwd="123456789", database="pdf_extract")
        print("\nConectado ao banco de dados com sucesso!\n")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "create table if not exists extracao_pdf "
            "( "
            "id serial primary key"
            ", extrator varchar(500)"
            ", dt_extracao datetime"
            ", campo_01 varchar(500)"
            ", campo_02 varchar(500)"
            ", campo_03 varchar(500)"
            ", campo_04 varchar(500)"
            ", campo_05 varchar(500)"
            ", campo_06 varchar(500)"
            ", faixa_01 numeric(8,2)"
            ", faixa_02 numeric(8,2)"
            ", faixa_03 numeric(8,2)"
            ", faixa_04 numeric(8,2)"
            ", faixa_05 numeric(8,2)"
            ", faixa_06 numeric(8,2)"
            ", faixa_07 numeric(8,2)"
            ", faixa_08 numeric(8,2)"
            ", faixa_09 numeric(8,2)"
            ", faixa_10 numeric(8,2)"
            ", status char(1) default 'N'"
            ", dt_processamento datetime default null"
            ", de_falha varchar(500) default null"
            ", dt_ajuste datetime default null"
            ");"
        )             

    def insert_into_extracao_pdf(self,extracao_pdf):
        add_extracao_pdf = (
            "INSERT IGNORE INTO extracao_pdf "
            "(extrator, dt_extracao, campo_01, campo_02, campo_03, campo_04, campo_05, campo_06, faixa_01, faixa_02, faixa_03, faixa_04, faixa_05, faixa_06, faixa_07, faixa_08, faixa_09, faixa_10) "
            "VALUES (%(extrator)s, %(dt_extracao)s, %(campo_01)s, %(campo_02)s, %(campo_03)s, %(campo_04)s, %(campo_05)s, %(campo_06)s, %(faixa_01)s, %(faixa_02)s, %(faixa_03)s, %(faixa_04)s, %(faixa_05)s, %(faixa_06)s, %(faixa_07)s, %(faixa_08)s, %(faixa_09)s, %(faixa_10)s)"
        )
        self.cursor.execute(add_extracao_pdf, extracao_pdf)
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()     