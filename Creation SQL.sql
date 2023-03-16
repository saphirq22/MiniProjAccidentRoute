CREATE SCHEMA IF NOT EXISTS `accidentologie` ;
USE accidentologie;

/*luminosite*/
 CREATE TABLE IF NOT EXISTS lum(
	id_lum INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	lib_lum VARCHAR(40) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  lum(id_lum, lib_lum)
VALUES (1, 'Plein jour');
INSERT IGNORE INTO  lum(id_lum, lib_lum)
VALUES (2, 'Crépuscule ou aube');
INSERT IGNORE INTO  lum(id_lum, lib_lum)
VALUES (3, 'Nuit sans éclairage public');
INSERT IGNORE INTO  lum(id_lum, lib_lum)
VALUES (4, 'Nuit avec éclairage public non allumé');
INSERT IGNORE INTO  lum(id_lum, lib_lum)
VALUES (5, 'Nuit avec éclairage public allumé');

/* CREATE TABLE IF NOT EXISTS t1 (
    c1 INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    c2 VARCHAR(100),
    c3 VARCHAR(100) )
ENGINE=InnoDB
*/
/*agglomeration*/
 CREATE TABLE IF NOT EXISTS agg(
	id_agg INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	lib_agg VARCHAR(20) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  agg (id_agg, lib_agg)
VALUES (1, 'Hors agglomération');
INSERT IGNORE INTO  agg (id_agg, lib_agg)
VALUES (2, 'En agglomération');

/*type intersection*/
 CREATE TABLE IF NOT EXISTS inter(
	id_inter INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	lib_inter VARCHAR(35) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  inter (id_inter, lib_inter)
VALUES (1, 'Hors intersection');
INSERT IGNORE INTO  inter (id_inter, lib_inter)
VALUES (2, 'Intersection en X');
INSERT IGNORE INTO  inter (id_inter, lib_inter)
VALUES (3, 'Intersection en T');
INSERT IGNORE INTO  inter (id_inter, lib_inter)
VALUES (4, 'Intersection en Y');
INSERT IGNORE INTO  inter (id_inter, lib_inter)
VALUES (5, 'Intersection à plus de 4 branches');
INSERT IGNORE INTO  inter (id_inter, lib_inter)
VALUES (6, 'Giratoire');
INSERT IGNORE INTO  inter (id_inter, lib_inter)
VALUES (7, 'Place');
INSERT IGNORE INTO  inter (id_inter, lib_inter)
VALUES (8, 'Passage à niveau');
INSERT IGNORE INTO  inter (id_inter, lib_inter)
VALUES (9, 'Autre intersection');

/*condition atmo*/
 CREATE TABLE IF NOT EXISTS atm(
	id_atm INT NOT NULL PRIMARY KEY,
	lib_atm VARCHAR(25) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  atm (id_atm, lib_atm)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  atm (id_atm, lib_atm)
VALUES (1, 'Normale');
INSERT IGNORE INTO  atm (id_atm, lib_atm)
VALUES (2, 'Normale');
INSERT IGNORE INTO  atm (id_atm, lib_atm)
VALUES (3, 'Pluie forte');
INSERT IGNORE INTO  atm (id_atm, lib_atm)
VALUES (4, 'Neige - grêle');
INSERT IGNORE INTO  atm (id_atm, lib_atm)
VALUES (5, 'Brouillard - fumée');
INSERT IGNORE INTO  atm (id_atm, lib_atm)
VALUES (6, 'Vent fort - tempête');
INSERT IGNORE INTO  atm (id_atm, lib_atm)
VALUES (7, 'Temps éblouissant');
INSERT IGNORE INTO  atm (id_atm, lib_atm)
VALUES (8, 'Temps couvert');
INSERT IGNORE INTO  atm (id_atm, lib_atm)
VALUES (9, 'Autre');

/*type collision*/
 CREATE TABLE IF NOT EXISTS col(
	id_col INT NOT NULL PRIMARY KEY,
	lib_col VARCHAR(50) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  col (id_col, lib_col)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  col (id_col, lib_col)
VALUES (1,'Deux véhicules - frontale');
INSERT IGNORE INTO  col (id_col, lib_col)
VALUES (2, 'Deux véhicules – par l’arrière');
INSERT IGNORE INTO  col (id_col, lib_col)
VALUES (3,'Deux véhicules – par le coté');
INSERT IGNORE INTO  col (id_col, lib_col)
VALUES (4,'Trois véhicules et plus – en chaîne');
INSERT IGNORE INTO  col (id_col, lib_col)
VALUES (5,'Trois véhicules et plus - collisions multiples');
INSERT IGNORE INTO  col (id_col, lib_col)
VALUES (6, 'Autre collision');
INSERT IGNORE INTO  col (id_col, lib_col)
VALUES (7, 'Sans collision');

/*catégorie de route*/
 CREATE TABLE IF NOT EXISTS catr(
	id_catr INT NOT NULL PRIMARY KEY,
	lib_catr VARCHAR(60) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  catr (id_catr, lib_catr)
VALUES (1,'Autoroute');
INSERT IGNORE INTO  catr (id_catr, lib_catr)
VALUES (2,'Route nationale');
INSERT IGNORE INTO  catr (id_catr, lib_catr)
VALUES (3,'Route Départementale');
INSERT IGNORE INTO  catr (id_catr, lib_catr)
VALUES (4,'Voie Communales');
INSERT IGNORE INTO  catr (id_catr, lib_catr)
VALUES (5,'Hors réseau public');
INSERT IGNORE INTO  catr (id_catr, lib_catr)
VALUES (6,'Parc de stationnement ouvert à la circulation publique');
INSERT IGNORE INTO  catr (id_catr, lib_catr)
VALUES (7,'Routes de métropole urbaine');
INSERT IGNORE INTO  catr (id_catr, lib_catr)
VALUES (9,'autre');

/*regime de circulation*/
 CREATE TABLE IF NOT EXISTS circ(
	id_circ INT NOT NULL PRIMARY KEY,
	lib_circ VARCHAR(35) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  circ (id_circ, lib_circ)
VALUES (-1,'Non renseigné');
INSERT IGNORE INTO  circ (id_circ, lib_circ)
VALUES (1,'A sens unique');
INSERT IGNORE INTO  circ (id_circ, lib_circ)
VALUES (2,'Bidirectionnelle');
INSERT IGNORE INTO  circ (id_circ, lib_circ)
VALUES (3,'A chaussées séparées');
INSERT IGNORE INTO  circ (id_circ, lib_circ)
VALUES (4,'Avec voies d’affectation variable');

/*existence voie reservé a proximité*/
 CREATE TABLE IF NOT EXISTS vosp(
	id_vosp INT NOT NULL PRIMARY KEY,
	lib_vosp VARCHAR(25) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  vosp (id_vosp, lib_vosp)
VALUES (-1,'Non renseigné');
INSERT IGNORE INTO  vosp (id_vosp, lib_vosp)
VALUES (0,'Sans objet');
INSERT IGNORE INTO  vosp (id_vosp, lib_vosp)
VALUES (1,'Piste cyclable');
INSERT IGNORE INTO  vosp (id_vosp, lib_vosp)
VALUES (2,'Bande cyclable');
INSERT IGNORE INTO  vosp (id_vosp, lib_vosp)
VALUES (3,'Voie réservée');

/*profil de déclivité terrain*/
 CREATE TABLE IF NOT EXISTS prof(
	id_prof INT NOT NULL PRIMARY KEY,
	lib_prof VARCHAR(25) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  prof (id_prof, lib_prof)
VALUES (-1,'Non renseigné');
INSERT IGNORE INTO  prof (id_prof, lib_prof)
VALUES (1, 'Plat');
INSERT IGNORE INTO  prof (id_prof, lib_prof)
VALUES (2, 'Pebte');
INSERT IGNORE INTO  prof (id_prof, lib_prof)
VALUES (3, 'Sommet de côte');
INSERT IGNORE INTO  prof (id_prof, lib_prof)
VALUES (4, 'Bas de côte');

/*tracé en plan*/
 CREATE TABLE IF NOT EXISTS plan(
	id_plan INT NOT NULL PRIMARY KEY,
	lib_plan VARCHAR(25) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  plan (id_plan, lib_plan)
VALUES(-1, 'Non renseigné' );
INSERT IGNORE INTO  plan (id_plan, lib_plan)
VALUES(1, 'Partie rectiligne' );
INSERT IGNORE INTO  plan (id_plan, lib_plan)
VALUES(2, 'En courbe à gauche' );
INSERT IGNORE INTO  plan (id_plan, lib_plan)
VALUES(3, 'En courbe à droite' );
INSERT IGNORE INTO  plan (id_plan, lib_plan)
VALUES(4, 'En « S »' );

/*etat de la surface*/
 CREATE TABLE IF NOT EXISTS surf(
	id_surf INT NOT NULL PRIMARY KEY,
	lib_surf VARCHAR(35) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  surf (id_surf, lib_surf)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  surf (id_surf, lib_surf)
VALUES (1,'Normale');
INSERT IGNORE INTO  surf (id_surf, lib_surf)
VALUES (2,'Mouillée');
INSERT IGNORE INTO  surf (id_surf, lib_surf)
VALUES (3,'Flaques');
INSERT IGNORE INTO  surf (id_surf, lib_surf)
VALUES (4,'Inondée');
INSERT IGNORE INTO  surf (id_surf, lib_surf)
VALUES (5,'Enneigée');
INSERT IGNORE INTO  surf (id_surf, lib_surf)
VALUES (6,'Boue');
INSERT IGNORE INTO  surf (id_surf, lib_surf)
VALUES (7,'Verglacée');
INSERT IGNORE INTO  surf (id_surf, lib_surf)
VALUES (8,'Corps gras – huile');
INSERT IGNORE INTO  surf (id_surf, lib_surf)
VALUES (9,'Autre');

/*amenagement et infrastrucure*/
 CREATE TABLE IF NOT EXISTS infra (
	id_infra INT NOT NULL PRIMARY KEY,
	lib_infra VARCHAR(45) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  infra (id_infra, lib_infra)
VALUES (0,'Aucun');
INSERT IGNORE INTO  infra (id_infra, lib_infra)
VALUES (1,'Souterrain - tunnel');
INSERT IGNORE INTO  infra (id_infra, lib_infra)
VALUES (2,'Pont - autopont');
INSERT IGNORE INTO  infra (id_infra, lib_infra)
VALUES (3,'Bretelle d’échangeur ou de raccordement');
INSERT IGNORE INTO  infra (id_infra, lib_infra)
VALUES (4,'Voie ferrée');
INSERT IGNORE INTO  infra (id_infra, lib_infra)
VALUES (5,'Carrefour aménagé');
INSERT IGNORE INTO  infra (id_infra, lib_infra)
VALUES (6,'Zone piétonne');
INSERT IGNORE INTO  infra (id_infra, lib_infra)
VALUES (7,'Zone de péage');
INSERT IGNORE INTO  infra (id_infra, lib_infra)
VALUES (8,'Chantier');
INSERT IGNORE INTO  infra (id_infra, lib_infra)
VALUES (9,'Autres');

/*situation de l accident*/
 CREATE TABLE IF NOT EXISTS situ (
	id_situ INT NOT NULL PRIMARY KEY,
	lib_situ VARCHAR(30) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  situ (id_situ, lib_situ)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  situ (id_situ, lib_situ)
VALUES (0, 'Aucun' );
INSERT IGNORE INTO  situ (id_situ, lib_situ)
VALUES (1, 'Sur chaussée' );
INSERT IGNORE INTO  situ (id_situ, lib_situ)
VALUES (2, 'Sur bande d’arrêt d’urgence' );
INSERT IGNORE INTO  situ (id_situ, lib_situ)
VALUES (3, 'Sur accotement' );
INSERT IGNORE INTO  situ (id_situ, lib_situ)
VALUES (4, 'Sur trottoir' );
INSERT IGNORE INTO  situ (id_situ, lib_situ)
VALUES (5, 'Sur piste cyclable' );
INSERT IGNORE INTO  situ (id_situ, lib_situ)
VALUES (6, 'Sur autre voie spéciale' );
INSERT IGNORE INTO  situ (id_situ, lib_situ)
VALUES (8, 'Autres' );

/*sens de circulation*/
 CREATE TABLE IF NOT EXISTS senc (
	id_senc INT NOT NULL PRIMARY KEY,
	lib_senc VARCHAR(55) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  senc (id_senc, lib_senc)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  senc (id_senc, lib_senc)
VALUES (0, 'Inconnu');
INSERT IGNORE INTO  senc (id_senc, lib_senc)
VALUES (1, 'PK ou PR ou numéro d’adresse postale croissant');
INSERT IGNORE INTO  senc (id_senc, lib_senc)
VALUES (2, 'PK ou PR ou numéro d’adresse postale décroissant');
INSERT IGNORE INTO  senc (id_senc, lib_senc)
VALUES (3, 'Absence de repère');

/*catégorie du véhicules*/
 CREATE TABLE IF NOT EXISTS catv (
	id_catv INT NOT NULL PRIMARY KEY,
	lib_catv VARCHAR(100) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (0, 'Indéterminable');		/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (1, 'Bicyclette');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (2, 'Cyclomoteur <50cm3');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (3, 'Voiturette (Quadricycle à moteur carrossé) (anciennement "voiturette ou tricycle à moteur")');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (4, 'Référence inutilisée depuis 2006 (scooter immatriculé)');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (5, 'Référence inutilisée depuis 2006 (motocyclette)');
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (6, 'Référence inutilisée depuis 2006 (side-car)'); /**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (7, 'VL seul');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (8, 'Référence inutilisée depuis 2006 (VL + caravane)');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (9, 'Référence inutilisée depuis 2006 (VL + remorque)');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (10, 'VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC<= 3,5T)');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (11, 'Référence inutilisée depuis 2006 (VU (10) + caravane)');
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (12, 'Référence inutilisée depuis 2006 (VU (10) + remorque)');
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (13, 'PL seul 3,5T <PTCA <= 7,5T');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (14, 'PL seul > 7,5T');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (15, 'PL > 3,5T + remorque');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (16, 'Tracteur routier seul');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (17, 'Tracteur routier + semi-remorque');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (18, 'Référence inutilisée depuis 2006 (transport en commun)');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (19, 'Référence inutilisée depuis 2006 (tramway)');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (20, 'Engin spécial');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (21, 'Tracteur agricole');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (30, 'Scooter < 50 cm3');
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (31, 'Motocyclette > 50 cm3 et <= 125 cm3');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (32, 'Scooter > 50 cm3 et <= 125 cm3');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (33, 'Motocyclette > 125 cm3');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (34, 'Scooter > 125 cm3');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (35, 'Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (36, 'Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (37, 'Autobus');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (38, 'Autocar');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (39, 'Train');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (40, 'Tramway');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (41, '3RM <= 50 cm3');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (42, '3RM > 50 cm3 <= 125 cm3');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (43, '3RM > 125 cm3');/**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (50, 'EDP à moteur');	/*troti*/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (60, 'EDP sans moteur'); 
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (80, 'VAE');	/*vélo elec*//**/
INSERT IGNORE INTO  catv (id_catv, lib_catv)
VALUES (99, 'Autre véhicule');	/**/

/*obstacle fixe*/
 CREATE TABLE IF NOT EXISTS obs (
	id_obs INT NOT NULL PRIMARY KEY,
	lib_obs VARCHAR(65) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (0, 'Sans objet');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (1, 'Véhicule en stationnement');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (2, 'Arbre');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (3, 'Glissière métallique');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (4, 'Glissière béton');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (5, 'Autre glissière');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (6, 'Bâtiment, mur, pile de pont');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (7, 'Support de signalisation verticale ou poste d’appel d’urgence');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (8, 'Poteau');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (9, 'Mobilier urbain');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (10, 'Parapet');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (11, 'Ilot, refuge, borne haute');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (12, 'Bordure de trottoir');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (13, 'Fossé, talus, paroi rocheuse');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (14, 'Autre obstacle fixe sur chaussée');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (15, 'Autre obstacle fixe sur trottoir ou accotement');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (16, 'Sortie de chaussée sans obstacle');
INSERT IGNORE INTO  obs (id_obs, lib_obs)
VALUES (17, 'Buse – tête d’aqueduc');

/*obstacle Mobile*/
 CREATE TABLE IF NOT EXISTS obsm (
	id_obsm INT NOT NULL PRIMARY KEY,
	lib_obsm VARCHAR(20) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  obsm (id_obsm, lib_obsm)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  obsm (id_obsm, lib_obsm)
VALUES (0, 'Aucun');
INSERT IGNORE INTO  obsm (id_obsm, lib_obsm)
VALUES (1, 'Piéton');
INSERT IGNORE INTO  obsm (id_obsm, lib_obsm)
VALUES (2, 'Véhicule');
INSERT IGNORE INTO  obsm (id_obsm, lib_obsm)
VALUES (4, 'Véhicule sur rail');
INSERT IGNORE INTO  obsm (id_obsm, lib_obsm)
VALUES (5, 'Animal domestique');
INSERT IGNORE INTO  obsm (id_obsm, lib_obsm)
VALUES (6, 'Animal sauvage');
INSERT IGNORE INTO  obsm (id_obsm, lib_obsm)
VALUES (7, '');
INSERT IGNORE INTO  obsm (id_obsm, lib_obsm)
VALUES (8, '');
INSERT IGNORE INTO  obsm (id_obsm, lib_obsm)
VALUES (9, 'Autre');

/*point de choc initial*/
 CREATE TABLE IF NOT EXISTS choc (
	id_choc INT NOT NULL PRIMARY KEY,
	lib_choc VARCHAR(30) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (11, 'Non renseigné');
INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (0, 'Aucun');
INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (1, 'Avant');
INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (2, 'Avant droit');
INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (3, 'Avant gauche');
INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (4, 'Arrière');
INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (5, 'Arrière droit');
INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (6, 'Arrière gauche');
INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (7, 'Côté droit');
INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (8, 'Côté gauche');
INSERT IGNORE INTO  choc (id_choc, lib_choc)
VALUES (9, 'Chocs multiples (tonneaux)');

/*manoeuvre avant l accident*/
 CREATE TABLE IF NOT EXISTS manv (
	id_manv INT NOT NULL PRIMARY KEY,
	lib_manv VARCHAR(45) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (0, 'Inconnue');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (1, 'Sans changement de direction');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (2, 'Même sens, même file');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (3, 'Entre 2 files');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (4, 'En marche arrière');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (5, 'A contresens');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (6, 'En franchissant le terre-plein central');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (7, 'Dans le couloir bus, dans le même sens');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (8, 'Dans le couloir bus, dans le sens inverse');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (9, 'En s’insérant');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (10, 'En faisant demi-tour sur la chaussée');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (11, 'Changeant de file : A gauche');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (12, 'Changeant de file : A droite');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (13, 'Déporté : A gauche');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (14, 'Déporté : A droite');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (15, 'Tournant : A gauche');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (16, 'Tournant : A droite');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (17, 'Dépassant : A gauche');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (18, 'Dépassant : A droite');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (19, 'Traversant la chaussée');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (20, 'Manœuvre de stationnement');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (21, 'Manœuvre d’évitement');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (22, 'Ouverture de porte');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (23, 'Arrêté (hors stationnement)');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (24, 'En stationnement (avec occupants)');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (25, 'Circulant sur trottoir');
INSERT IGNORE INTO  manv (id_manv, lib_manv)
VALUES (26, 'Autres manœuvres');

/*type motorisation*/
 CREATE TABLE IF NOT EXISTS motor (
	id_motor INT NOT NULL PRIMARY KEY,
	lib_motor VARCHAR(20) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  motor (id_motor, lib_motor)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  motor (id_motor, lib_motor)
VALUES (0, 'Inconnue');
INSERT IGNORE INTO  motor (id_motor, lib_motor)
VALUES (1, 'Hydrocarbures');
INSERT IGNORE INTO  motor (id_motor, lib_motor)
VALUES (2, 'Hybride électrique');
INSERT IGNORE INTO  motor (id_motor, lib_motor)
VALUES (3, 'Electrique');
INSERT IGNORE INTO  motor (id_motor, lib_motor)
VALUES (4, 'Hydrogène');
INSERT IGNORE INTO  motor (id_motor, lib_motor)
VALUES (5, 'Humaine');
INSERT IGNORE INTO  motor (id_motor, lib_motor)
VALUES (6, 'Autre');

/*catégorie usager*/
 CREATE TABLE IF NOT EXISTS catu (
	id_catu INT NOT NULL PRIMARY KEY,
	lib_catu VARCHAR(15) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  catu (id_catu, lib_catu)
VALUES (1, 'Conducteur');
INSERT IGNORE INTO  catu (id_catu, lib_catu)
VALUES (2, 'Passager');
INSERT IGNORE INTO  catu (id_catu, lib_catu)
VALUES (3, 'Piéton');

/*gravité de l usager*/
 CREATE TABLE IF NOT EXISTS grav (
	id_grav INT NOT NULL PRIMARY KEY,
	lib_grav VARCHAR(20) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  grav (id_grav, lib_grav)
VALUES (1, 'Indemne');
INSERT IGNORE INTO  grav (id_grav, lib_grav)
VALUES (2, 'Tué');
INSERT IGNORE INTO  grav (id_grav, lib_grav)
VALUES (3, 'Blessé hospitalisé');
INSERT IGNORE INTO  grav (id_grav, lib_grav)
VALUES (4, 'Blessé léger');

/*sexe*/
 CREATE TABLE IF NOT EXISTS sexe (
	id_sexe INT NOT NULL PRIMARY KEY,
	lib_sexe VARCHAR(10) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  sexe (id_sexe, lib_sexe)
VALUES (1, 'Masculin');
INSERT IGNORE INTO  sexe (id_sexe, lib_sexe)
VALUES (2, 'Féminin');

/*motif de déplacement*/
 CREATE TABLE IF NOT EXISTS trajet (
	id_trajet INT NOT NULL PRIMARY KEY,
	lib_trajet VARCHAR(30) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  trajet (id_trajet, lib_trajet)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  trajet (id_trajet, lib_trajet)
VALUES (0, 'Non renseigné');
INSERT IGNORE INTO  trajet (id_trajet, lib_trajet)
VALUES (1, 'Domicile – travail');
INSERT IGNORE INTO  trajet (id_trajet, lib_trajet)
VALUES (2, 'Domicile – école');
INSERT IGNORE INTO  trajet (id_trajet, lib_trajet)
VALUES (3, 'Courses – achats');
INSERT IGNORE INTO  trajet (id_trajet, lib_trajet)
VALUES (4, 'Utilisation professionnelle');
INSERT IGNORE INTO  trajet (id_trajet, lib_trajet)
VALUES (5, 'Promenade – loisirs');
INSERT IGNORE INTO  trajet (id_trajet, lib_trajet)
VALUES (9, 'Autre');

/*equipement de securité*/
 CREATE TABLE IF NOT EXISTS secu1 (
	id_secu1 INT NOT NULL PRIMARY KEY,
	lib_secu1 VARCHAR(25) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (0, 'Aucun équipement');
INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (1, 'Ceinture');
INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (2, 'Casque');
INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (3, 'Dispositif enfants');
INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (4, 'Gilet réfléchissant');
INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (5, 'Airbag (2RM/3RM)');
INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (6, 'Gants (2RM/3RM)');
INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (7, 'Gants + Airbag (2RM/3RM)');
INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (8, 'Non déterminable');
INSERT IGNORE INTO  secu1 (id_secu1, lib_secu1)
VALUES (9, 'Autre');

 CREATE TABLE IF NOT EXISTS secu2 (
	id_secu2 INT NOT NULL PRIMARY KEY,
	lib_secu2 VARCHAR(25) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (0, 'Aucun équipement');
INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (1, 'Ceinture');
INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (2, 'Casque');
INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (3, 'Dispositif enfants');
INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (4, 'Gilet réfléchissant');
INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (5, 'Airbag (2RM/3RM)');
INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (6, 'Gants (2RM/3RM)');
INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (7, 'Gants + Airbag (2RM/3RM)');
INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (8, 'Non déterminable');
INSERT IGNORE INTO  secu2 (id_secu2, lib_secu2)
VALUES (9, 'Autre');

 CREATE TABLE IF NOT EXISTS secu3 (
	id_secu3 INT NOT NULL PRIMARY KEY,
	lib_secu3 VARCHAR(25) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (0, 'Aucun équipement');
INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (1, 'Ceinture');
INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (2, 'Casque');
INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (3, 'Dispositif enfants');
INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (4, 'Gilet réfléchissant');
INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (5, 'Airbag (2RM/3RM)');
INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (6, 'Gants (2RM/3RM)');
INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (7, 'Gants + Airbag (2RM/3RM)');
INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (8, 'Non déterminable');
INSERT IGNORE INTO  secu3 (id_secu3, lib_secu3)
VALUES (9, 'Autre');

/*localisation du pieton*/
 CREATE TABLE IF NOT EXISTS locp (
	id_locp INT NOT NULL PRIMARY KEY,
	lib_locp VARCHAR(55) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (0, 'Sans objet');
INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (1, 'Sur chaussée : A + 50 m du passage piéton');
INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (2, 'Sur chaussée : A – 50 m du passage piéton');
INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (3, 'Sur passage piéton : Sans signalisation lumineuse');
INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (4, 'Sur passage piéton : Avec signalisation lumineuse');
INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (5, 'Sur trottoir');
INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (6, 'Sur accotement');
INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (7, 'Sur refuge ou BAU');
INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (8, 'Sur contre allée');
INSERT IGNORE INTO  locp (id_locp, lib_locp)
VALUES (9, 'Inconnue');

/*action du pieton*/
 CREATE TABLE IF NOT EXISTS actp (
	id_actp INT NOT NULL PRIMARY KEY,
	lib_actp VARCHAR(45) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  actp (id_actp, lib_actp)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  actp (id_actp, lib_actp)
VALUES (0, 'Se déplaçant : Non renseigné ou sans objet');
INSERT IGNORE INTO  actp (id_actp, lib_actp)
VALUES (1, 'Se déplaçant : Sens véhicule heurtant');
INSERT IGNORE INTO  actp (id_actp, lib_actp)
VALUES (2, 'Se déplaçant : Sens inverse du véhicule');
INSERT IGNORE INTO  actp (id_actp, lib_actp)
VALUES (3, 'Traversant');
INSERT IGNORE INTO  actp (id_actp, lib_actp)
VALUES (4, 'Masqué');
INSERT IGNORE INTO  actp (id_actp, lib_actp)
VALUES (5, 'Jouant – courant');
INSERT IGNORE INTO  actp (id_actp, lib_actp)
VALUES (6, 'Avec animal');
INSERT IGNORE INTO  actp (id_actp, lib_actp)
VALUES (9, 'Autre');

/*pieton seul ou en groupe*/
 CREATE TABLE IF NOT EXISTS etatp (
	id_etatp INT NOT NULL PRIMARY KEY,
	lib_etatp VARCHAR(15) NULL
)ENGINE=InnoDB;

INSERT IGNORE INTO  etatp (id_etatp, lib_etatp)
VALUES (-1, 'Non renseigné');
INSERT IGNORE INTO  etatp (id_etatp, lib_etatp)
VALUES (1, 'Seul');
INSERT IGNORE INTO  etatp (id_etatp, lib_etatp)
VALUES (2, 'Accompagné');
INSERT IGNORE INTO  etatp (id_etatp, lib_etatp)
VALUES (3, 'En groupe');


/*USAGER
Num_Acc	varchar(13) 202100000002
id_vehicule varchar(8)	201Â 764
num_veh varchar(4)	B01
place int	1
catu int	1
grav int	3
sexe int	1
an_nais date	2000
trajet int	1
secu1 int		1
secu2 int	1
secu3 int	1
locp int	1
actp int	1
etatp int   1

/*VH
Num_Acc	varchar(13) 202100000002
id_vehicule varchar(8)	201Â 764
num_veh varchar(4)	B01
senc int
catv int
obs int
obsm int
choc int
manv	int
motor	int
occutc int

/*lieu
Num_Acc	
catr	
voie	
v1	
v2	
circ	
nbv	
vosp	
prof	
pr	
pr1	
plan	
lartpc	
larrout	
surf	
infra	
situ	
vma

/*carac
Num_Acc	
jour	
mois	
an	
hrmn	
lum	
dep	
com	
agg	
int	
atm	
col	
adr	
lat	
long
