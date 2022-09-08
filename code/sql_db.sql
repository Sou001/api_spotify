-- a lancer seulement pour supprimer les tables et les recréer
DROP TABLE IF EXISTS artistes_popularity;
DROP TABLE IF EXISTS histo_playlist;

CREATE TABLE IF NOT EXISTS artistes_popularity (
	id_artiste VARCHAR PRIMARY KEY,
	nom_artiste VARCHAR,
    popularite INTEGER,
    date_effet DATE
);

CREATE TABLE IF NOT EXISTS histo_playlist (
	id_playlist VARCHAR PRIMARY KEY,
	id_artiste VARCHAR,
	date_entree DATE,
	date_sortie DATE,
	FOREIGN KEY (id_artiste) REFERENCES artistes_popularity(id_artiste)
);
