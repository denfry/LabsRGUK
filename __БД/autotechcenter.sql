
CREATE TABLE autotechcenter.AutoMobile (
                CodeModel INTEGER NOT NULL,
                NameModel VARCHAR NOT NULL,
                CONSTRAINT automobile_pk PRIMARY KEY (CodeModel)
);


CREATE TABLE autotechcenter.Client (
                CodeClient INTEGER NOT NULL,
                ClientType VARCHAR NOT NULL,
                FIO VARCHAR NOT NULL,
                NumberClient VARCHAR NOT NULL,
                CONSTRAINT client_pk PRIMARY KEY (CodeClient)
);


CREATE SEQUENCE autotechcenter.zakaznaryad_idzakaznaryad_seq;

CREATE TABLE autotechcenter.ZakazNaryad (
                IDZakazNaryad INTEGER NOT NULL DEFAULT nextval('autotechcenter.zakaznaryad_idzakaznaryad_seq'),
                NumberZakaz INTEGER NOT NULL,
                DateOformlenie DATE NOT NULL,
                SrokIspolneniya DATE NOT NULL,
                CodeClient INTEGER NOT NULL,
                GosnomerAuto VARCHAR NOT NULL,
                StoimostRabot NUMERIC(10,2) DEFAULT 0 NOT NULL,
                CodeModel INTEGER NOT NULL,
                CONSTRAINT zakaznaryad_pk PRIMARY KEY (IDZakazNaryad)
);


ALTER SEQUENCE autotechcenter.zakaznaryad_idzakaznaryad_seq OWNED BY autotechcenter.ZakazNaryad.IDZakazNaryad;

CREATE TABLE autotechcenter.TypeOfWork (
                WorkTypeCode INTEGER NOT NULL,
                NameTypeWork VARCHAR NOT NULL,
                CONSTRAINT typeofwork_pk PRIMARY KEY (WorkTypeCode)
);


CREATE TABLE autotechcenter.Work (
                WorkCode INTEGER NOT NULL,
                WorkTypeCode INTEGER NOT NULL,
                NameWork VARCHAR NOT NULL,
                StoimostOdinNCH NUMERIC(10,2) DEFAULT 0 NOT NULL,
                CONSTRAINT work_pk PRIMARY KEY (WorkCode)
);


CREATE SEQUENCE autotechcenter.donework_iddonework_seq;

CREATE TABLE autotechcenter.DoneWork (
                IDDoneWork INTEGER NOT NULL DEFAULT nextval('autotechcenter.donework_iddonework_seq'),
                WorkCode INTEGER NOT NULL,
                TrudoemkostVnch NUMERIC(5,1) NOT NULL,
                StoimostVnch NUMERIC(10,2) DEFAULT 0 NOT NULL,
                IDZakazNaryad INTEGER NOT NULL,
                CONSTRAINT donework_pk PRIMARY KEY (IDDoneWork)
);


ALTER SEQUENCE autotechcenter.donework_iddonework_seq OWNED BY autotechcenter.DoneWork.IDDoneWork;

ALTER TABLE autotechcenter.ZakazNaryad ADD CONSTRAINT automobile_zakaznaryad_fk
FOREIGN KEY (CodeModel)
REFERENCES autotechcenter.AutoMobile (CodeModel)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE autotechcenter.ZakazNaryad ADD CONSTRAINT client_zakaznaryad_fk
FOREIGN KEY (CodeClient)
REFERENCES autotechcenter.Client (CodeClient)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE autotechcenter.DoneWork ADD CONSTRAINT zakaznaryad_donework_fk
FOREIGN KEY (IDZakazNaryad)
REFERENCES autotechcenter.ZakazNaryad (IDZakazNaryad)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE autotechcenter.Work ADD CONSTRAINT typeofwork_work_fk
FOREIGN KEY (WorkTypeCode)
REFERENCES autotechcenter.TypeOfWork (WorkTypeCode)
ON DELETE RESTRICT
ON UPDATE RESTRICT
NOT DEFERRABLE;

ALTER TABLE autotechcenter.DoneWork ADD CONSTRAINT work_donework_fk
FOREIGN KEY (WorkCode)
REFERENCES autotechcenter.Work (WorkCode)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
