PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "BasePokemon" (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	evolution VARCHAR, 
	"preEvolution" VARCHAR, 
	"baseHealth" INTEGER NOT NULL, 
	will INTEGER NOT NULL, 
	logic INTEGER, 
	instinct INTEGER, 
	primal INTEGER, 
	"primaryType" VARCHAR(8) NOT NULL, 
	"secondaryType" VARCHAR(8), 
	strength INTEGER NOT NULL, 
	"strengthPotential" INTEGER NOT NULL, 
	dexterity INTEGER NOT NULL, 
	"dexterityPotential" INTEGER NOT NULL, 
	vitality INTEGER NOT NULL, 
	"vitalityPotential" INTEGER NOT NULL, 
	special INTEGER NOT NULL, 
	"specialPotential" INTEGER NOT NULL, 
	insight INTEGER NOT NULL, 
	"insightPotential" INTEGER NOT NULL, 
	fight INTEGER NOT NULL, 
	survival INTEGER NOT NULL, 
	contest INTEGER NOT NULL, 
	brawl INTEGER NOT NULL, 
	channel INTEGER NOT NULL, 
	clash INTEGER NOT NULL, 
	evasion INTEGER NOT NULL, 
	alert INTEGER NOT NULL, 
	athletic INTEGER NOT NULL, 
	"natureStat" INTEGER NOT NULL, 
	stealth INTEGER NOT NULL, 
	allure INTEGER NOT NULL, 
	etiquette INTEGER NOT NULL, 
	intimidate INTEGER NOT NULL, 
	perform INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO BasePokemon VALUES(1,'Ralts','Kirlia',NULL,3,3,1,1,0,'PSYCHIC','FAIRY',1,3,1,3,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(2,'Jangmo-o','Hakamo-o',NULL,3,3,1,1,0,'DRAGON',NULL,2,4,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(3,'Riolu','Lucario',NULL,3,3,1,1,0,'FIGHTING',NULL,2,5,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(4,'Piplup','Prinplup',NULL,3,3,1,1,0,'WATER',NULL,2,4,1,3,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(5,'Gabite','Garchomp','Gible',4,3,1,1,0,'DRAGON','GROUND',2,5,2,5,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(6,'Nickit','Thievul',NULL,3,3,1,1,0,'DARK',NULL,1,3,2,4,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(7,'Palkia',NULL,NULL,5,3,1,1,0,'WATER','DRAGON',7,10,6,10,6,10,8,10,7,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(8,'Dialga',NULL,NULL,7,3,1,1,0,'STEEL','DRAGON',7,10,5,10,7,10,8,10,6,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(9,'Bulbasaur','IvySaur',NULL,3,3,1,1,0,'GRASS','POISON',2,4,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(10,'IvySaur','Venusaur','Bulbasaur',4,3,1,1,0,'GRASS','POISON',2,4,2,4,2,4,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(11,'Venusaur',NULL,'IvySaur',4,3,1,1,0,'GRASS','POISON',2,5,2,5,2,5,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(12,'Mega-Venusaur',NULL,'Venusaur',4,3,1,1,0,'GRASS','POISON',3,6,2,5,3,7,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(13,'Charmander','Charmeleon',NULL,3,3,1,1,0,'FIRE',NULL,2,4,2,4,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(14,'Charmeleon','Charizard','Charmander',4,3,1,1,0,'FIRE',NULL,2,4,3,5,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(15,'Charizard','Mega-Charizard','Charmeleon',5,3,1,1,0,'FIRE','FLYING',2,5,3,6,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(16,'Mega-Charizard Y',NULL,'Charizard',6,3,1,1,0,'FIRE','FLYING',3,6,3,6,2,5,4,8,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(17,'Mega-Charizard X',NULL,'Charizard',6,3,1,1,0,'FIRE','DRAGON',3,7,3,6,3,6,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(18,'Squirtle','Wartortle',NULL,3,3,1,1,0,'WATER',NULL,2,4,1,3,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(19,'Wartortle','Blastoise','Squirtle',4,3,1,1,0,'WATER',NULL,2,4,2,4,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(20,'Blastoise','Mega-Blastoise','Wartortle',5,3,1,1,0,'WATER',NULL,2,5,2,5,3,6,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(21,'Mega-Blastoise',NULL,'Blastoise',6,3,1,1,0,'WATER',NULL,3,6,2,5,3,7,3,7,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(22,'Caterpie','Metapod',NULL,3,3,1,1,0,'BUG',NULL,1,3,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(23,'Metapod','Butterfree','Caterpie',4,3,1,1,0,'BUG',NULL,1,3,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(24,'Butterfree',NULL,'Metapod',5,3,1,1,0,'BUG','FLYING',2,4,2,5,2,4,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(25,'Weedle','Kakuna',NULL,3,3,1,1,0,'BUG','POISON',1,3,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(26,'Kakuna','Beedrill','Weedle',4,3,1,1,0,'BUG','POISON',1,3,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(27,'Beedrill','Mega-Beedrill','Kakuna',5,3,1,1,0,'BUG','POISON',2,5,2,5,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(28,'Mega-Beedrill',NULL,'Beedrill',6,3,1,1,0,'BUG','POISON',4,8,4,8,1,3,1,2,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(29,'Pidgey','Pidgeotto',NULL,3,3,1,1,0,'NORMAL','FLYING',2,4,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(30,'Pidgeotto','Pidgeot','Pidgey',4,3,1,1,0,'NORMAL','FLYING',2,4,2,5,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(31,'Pidgeot','Mega-Pidgeot','Pidgeotto',5,3,1,1,0,'NORMAL','FLYING',2,5,3,6,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(32,'Mega-Pidgeot',NULL,'Pidgeot',6,3,1,1,0,'NORMAL','FLYING',2,5,3,7,2,5,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(33,'Rattata','Raticate',NULL,3,3,1,1,0,'NORMAL',NULL,2,4,2,5,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(34,'Raticate',NULL,'Rattata',4,3,1,1,0,'NORMAL',NULL,2,5,3,6,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(35,'Alolan Rattata','Alolan Raticate',NULL,3,3,1,1,0,'DARK','NORMAL',2,4,2,5,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(36,'Alolan Raticate',NULL,'Alolan Rattata',4,3,1,1,0,'DARK','NORMAL',2,5,2,5,2,5,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(37,'Spearow','Fearow',NULL,3,3,1,1,0,'NORMAL','FLYING',2,4,2,5,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(38,'Fearow',NULL,'Spearow',4,3,1,1,0,'NORMAL','FLYING',2,5,3,6,2,4,2,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(39,'Ekans','Arbok',NULL,3,3,1,1,0,'POISON',NULL,2,4,2,4,1,3,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(40,'Arbok',NULL,'Ekans',3,3,1,1,0,'POISON',NULL,3,6,2,5,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(41,'Pikachu','Raichu','Pichu',4,3,1,1,0,'ELECTRIC',NULL,2,4,2,5,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(42,'Raichu',NULL,'Pikachu',5,3,1,1,0,'ELECTRIC',NULL,2,5,3,6,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(43,'Alolan Raichu',NULL,'Pikachu',5,3,1,1,0,'ELECTRIC','PSYCHIC',2,5,3,6,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(44,'Sandshrew','Sandslash',NULL,3,3,1,1,0,'GROUND',NULL,2,5,1,3,2,5,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(45,'Sandslash',NULL,'Sandshrew',4,3,1,1,0,'GROUND',NULL,3,6,2,4,3,6,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(46,'Alolan Sandshrew','Alolan Sandslash',NULL,3,3,1,1,0,'ICE','STEEL',2,5,1,3,2,5,1,2,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(47,'Alolan Sandslash',NULL,'Alolan Sandshrew',4,3,1,1,0,'ICE','STEEL',3,6,2,4,3,7,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(48,'Nidoran F','Nidorina',NULL,3,3,1,1,0,'POISON',NULL,2,4,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(49,'Nidorina','Nidoqueen','Nidoran F',4,3,1,1,0,'POISON',NULL,2,4,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(50,'Nidoqueen',NULL,'Nidorina',5,3,1,1,0,'POISON','GROUND',3,6,2,5,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(51,'Nidoran M','Nidorino',NULL,3,3,1,1,0,'POISON',NULL,2,4,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(52,'Nidorino','Nidoking','Nidoran M',4,3,1,1,0,'POISON',NULL,2,5,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(53,'Nidoking',NULL,'Nidorino',5,3,1,1,0,'POISON','GROUND',3,6,2,5,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(54,'Clefairy','Clefable','Cleffa',4,3,1,1,0,'FAIRY',NULL,2,4,1,3,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(55,'Clefable',NULL,'Clefairy',5,3,1,1,0,'FAIRY',NULL,2,5,2,4,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(56,'Vulpix','Ninetales',NULL,3,3,1,1,0,'FIRE',NULL,1,3,2,4,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(57,'Ninetales',NULL,'Vulpix',4,3,1,1,0,'FIRE',NULL,2,5,3,6,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(58,'Alolan Vulpix','Alolan Ninetales',NULL,3,3,1,1,0,'ICE',NULL,1,3,2,4,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(59,'Alolan Ninetales',NULL,'Alolan Vulpix',4,3,1,1,0,'ICE','FAIRY',2,4,3,6,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(60,'Jigglypuff','Wigglytuff','Igglybuff',4,3,1,1,0,'NORMAL','FAIRY',2,4,1,3,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(61,'Wigglytuff',NULL,'Jigglypuff',7,3,1,1,0,'NORMAL','FAIRY',2,5,2,4,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(62,'Zubat','Golbat',NULL,3,3,1,1,0,'POISON','FLYING',2,4,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(63,'Golbat','Crobat','Zubat',4,3,1,1,0,'POISON','FLYING',2,5,2,5,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(64,'Crobat',NULL,'Golbat',5,3,1,1,0,'POISON','FLYING',2,5,3,7,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(65,'Oddish','Gloom',NULL,3,3,1,1,0,'GRASS','POISON',2,4,1,3,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(66,'Gloom','Vileplume / Bellossom','Oddish',4,3,1,1,0,'GRASS','POISON',2,4,2,3,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(67,'Vileplume',NULL,'Gloom',5,3,1,1,0,'GRASS','POISON',2,5,2,4,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(68,'Bellossom',NULL,'Gloom',5,3,1,1,0,'GRASS',NULL,2,5,2,4,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(69,'Paras','Parasect',NULL,3,3,1,1,0,'BUG','GRASS',2,5,1,3,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(70,'Parasect',NULL,'Paras',4,3,1,1,0,'BUG','GRASS',3,6,1,3,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(71,'Venonat','Venomoth',NULL,3,3,1,1,0,'BUG','POISON',2,4,1,3,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(72,'Venomoth',NULL,'Venonat',4,3,1,1,0,'BUG','POISON',2,4,2,4,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(73,'Diglett','Dugtrio',NULL,3,3,1,1,0,'GROUND',NULL,2,4,3,6,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(74,'Dugtrio',NULL,'Diglett',4,3,1,1,0,'GROUND',NULL,2,5,3,7,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(75,'Alolan Diglett','Alolan Dugtrio',NULL,3,3,1,1,0,'GROUND','STEEL',2,4,2,5,1,3,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(76,'Alolan Dugtrio',NULL,'Alolan Diglett',4,3,1,1,0,'GROUND','STEEL',3,6,3,6,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(77,'Meowth','Persian',NULL,3,3,1,1,0,'NORMAL',NULL,2,4,2,5,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(78,'Persian',NULL,'Meowth',4,3,1,1,0,'NORMAL',NULL,2,5,3,6,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(79,'Alolan Meowth','Alolan Persian',NULL,3,3,1,1,0,'DARK',NULL,1,3,2,5,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(80,'Alolan Persian',NULL,'Alolan Meowth',4,3,1,1,0,'DARK',NULL,2,4,3,6,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(81,'Psyduck','Golduck',NULL,3,3,1,1,0,'WATER',NULL,2,4,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(82,'Golduck',NULL,'Psyduck',4,3,1,1,0,'WATER',NULL,2,5,2,5,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(83,'Mankey','Primeape',NULL,3,3,1,1,0,'FIGHTING',NULL,2,5,2,5,1,3,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(84,'Primeape',NULL,'Mankey',4,3,1,1,0,'FIGHTING',NULL,3,6,3,6,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(85,'Growlithe','Arcanine',NULL,3,3,1,1,0,'FIRE',NULL,2,5,2,5,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(86,'Arcanine',NULL,'Growlithe',4,3,1,1,0,'FIRE',NULL,3,6,3,6,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(87,'Poliwag','Poliwhirl',NULL,3,3,1,1,0,'WATER',NULL,2,4,2,5,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(88,'Poliwhirl','Poliwrath / Politoed','Poliwag',4,3,1,1,0,'WATER',NULL,2,4,2,5,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(89,'Poliwrath',NULL,'Poliwhirl',5,3,1,1,0,'WATER','FIGHTING',3,6,2,5,3,6,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(90,'Politoed',NULL,'Poliwhirl',5,3,1,1,0,'WATER',NULL,2,5,2,4,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(91,'Abra','Kadabra',NULL,3,3,1,1,0,'PSYCHIC',NULL,1,3,2,5,1,2,3,6,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(92,'Kadabra','Alakazam','Abra',4,3,1,1,0,'PSYCHIC',NULL,1,3,3,6,1,3,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(93,'Alakazam','Mega-Alakazam','Kadabra',5,3,1,1,0,'PSYCHIC',NULL,2,4,3,7,2,4,3,7,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(94,'Mega-Alakazam',NULL,'Alakazam',6,3,1,1,0,'PSYCHIC',NULL,2,4,4,8,2,4,4,9,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(95,'Machop','Machoke',NULL,3,3,1,1,0,'FIGHTING',NULL,2,5,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(96,'Machoke','Machamp','Machop',4,3,1,1,0,'FIGHTING',NULL,3,6,2,4,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(97,'Machamp',NULL,'Machoke',5,3,1,1,0,'FIGHTING',NULL,3,7,2,4,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(98,'Bellsprout','Weepinbell',NULL,3,3,1,1,0,'GRASS','POISON',2,5,1,3,1,3,2,5,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(99,'Weepinbell','Victreebel','Bellsprout',4,3,1,1,0,'GRASS','POISON',2,5,2,4,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(100,'Victreebel',NULL,'Weepinbell',4,3,1,1,0,'GRASS','POISON',3,6,2,5,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(101,'Tentacool','Tentacruel',NULL,3,3,1,1,0,'WATER','POISON',1,3,2,5,1,3,2,4,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(102,'Tentacruel',NULL,'Tentacool',4,3,1,1,0,'WATER','POISON',2,5,3,6,2,4,2,5,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(103,'Geodude','Gravler',NULL,3,3,1,1,0,'ROCK','GROUND',2,5,1,3,3,6,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(104,'Gravler','Golem','Geodude',4,3,1,1,0,'ROCK','GROUND',3,6,1,3,3,6,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(105,'Golem',NULL,'Gravler',5,3,1,1,0,'ROCK','GROUND',3,8,2,4,3,7,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(106,'Alolan Geodude','Alolan Gravler',NULL,3,3,1,1,0,'ROCK','ELECTRIC',2,5,1,3,3,6,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(107,'Alolan Gravler','Alolan Golem','Alolan Geodude',4,3,1,1,0,'ROCK','ELECTRIC',3,6,1,3,3,6,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(108,'Alolan Golem',NULL,'Alolan Gravler',5,3,1,1,0,'ROCK','ELECTRIC',3,7,2,4,3,7,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(109,'Ponyta','Rapidash',NULL,3,3,1,1,0,'FIRE',NULL,2,5,2,5,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(110,'Rapidash',NULL,'Ponyta',4,3,1,1,0,'FIRE',NULL,3,6,3,6,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(111,'Slowpoke','Slowbro',NULL,3,3,1,1,0,'WATER','PSYCHIC',2,4,1,2,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(112,'Slowbro','Mega-Slowbro / Slowking','Slowpoke',4,3,1,1,0,'WATER','PSYCHIC',2,5,1,3,3,6,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(113,'Mega-Slowbro',NULL,'Slowbro',5,3,1,1,0,'WATER','PSYCHIC',2,5,1,2,4,9,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(114,'Slowking',NULL,'Slowbro',4,3,1,1,0,'WATER','PSYCHIC',2,5,1,3,2,5,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(115,'Magnemite','Magneton',NULL,3,3,1,1,0,'ELECTRIC','STEEL',2,4,2,5,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(116,'Magneton','Magnezone','Magnemite',4,3,1,1,0,'ELECTRIC','STEEL',2,4,2,5,3,6,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(117,'Magnezone',NULL,'Magneton',5,3,1,1,0,'ELECTRIC','STEEL',2,5,2,4,3,6,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(118,'Farfetch''d',NULL,NULL,4,3,1,1,0,'NORMAL','FLYING',2,5,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(119,'Doduo','Dodrio',NULL,3,3,1,1,0,'NORMAL','FLYING',2,5,2,5,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(120,'Dodrio',NULL,'Doduo',4,3,1,1,0,'NORMAL','FLYING',3,6,3,6,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(121,'Seel','Dewgong',NULL,3,3,1,1,0,'WATER',NULL,2,4,2,4,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(122,'Dewgong',NULL,'Seel',4,3,1,1,0,'WATER','ICE',2,5,2,5,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(123,'Grimer','Muk',NULL,3,3,1,1,0,'POISON',NULL,2,5,1,3,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(124,'Muk',NULL,'Grimer',3,3,1,1,0,'POISON',NULL,3,6,2,4,2,5,2,4,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(125,'Alolan Grimer','Alolan Muk',NULL,3,3,1,1,0,'POISON','DARK',2,5,1,3,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(126,'Alolan Muk',NULL,'Alolan Grimer',5,3,1,1,0,'POISON','DARK',3,6,2,4,2,5,2,4,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(127,'Shellder','Cloyster',NULL,3,3,1,1,0,'WATER',NULL,2,4,1,3,3,6,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(128,'Cloyster',NULL,'Shellder',4,3,1,1,0,'WATER','ICE',3,6,2,5,4,9,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(129,'Gastly','Haunter',NULL,4,3,1,1,0,'GHOST','POISON',1,3,2,5,1,3,3,6,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(130,'Haunter','Gengar','Gastly',4,3,1,1,0,'GHOST','POISON',2,4,3,6,2,4,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(131,'Gengar','Mega-Gengar','Haunter',5,3,1,1,0,'GHOST','POISON',2,4,3,6,2,4,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(132,'Mega-Gengar',NULL,'Gengar',6,3,1,1,0,'GHOST','POISON',2,4,3,7,2,5,3,9,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(133,'Onix','Steelix',NULL,8,3,1,1,0,'ROCK','GROUND',2,4,2,5,4,8,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(134,'Steelix','Mega-Steelix','Onix',9,3,1,1,0,'STEEL','GROUND',2,5,1,3,5,10,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(135,'Mega-Steelix',NULL,'Steelix',10,3,1,1,0,'STEEL','GROUND',3,7,1,2,5,10,2,4,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(136,'Drowzee','Hypno',NULL,3,3,1,1,0,'PSYCHIC',NULL,2,4,1,3,2,4,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(137,'Hypno',NULL,'Drowzee',4,3,1,1,0,'PSYCHIC',NULL,2,5,2,4,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(138,'Krabby','Kingler',NULL,3,3,1,1,0,'WATER',NULL,3,6,2,4,2,5,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(139,'Kingler',NULL,'Krabby',4,3,1,1,0,'WATER',NULL,3,7,2,5,3,6,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(140,'Voltorb','Electrode',NULL,3,3,1,1,0,'ELECTRIC',NULL,1,3,3,6,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(141,'Electrode',NULL,'Voltorb',4,3,1,1,0,'ELECTRIC',NULL,2,4,4,8,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(142,'Exeggcute','Exeggutor',NULL,3,3,1,1,0,'GRASS','PSYCHIC',1,3,1,3,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(143,'Exeggutor',NULL,'Exeggcute',5,3,1,1,0,'GRASS','PSYCHIC',3,6,2,4,2,5,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(144,'Alolan Exeggutor',NULL,'Exeggcute',5,3,1,1,0,'GRASS','DRAGON',3,6,2,4,2,5,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(145,'Cubone','Marowak',NULL,3,3,1,1,0,'GROUND',NULL,2,4,1,3,3,6,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(146,'Marowak',NULL,'Cubone',4,3,1,1,0,'GROUND',NULL,2,5,2,4,3,6,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(147,'Alolan Marowak',NULL,'Cubone',4,3,1,1,0,'FIRE','GHOST',2,5,2,4,3,6,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(148,'Hitmonlee',NULL,'Tyrogue',4,3,1,1,0,'FIGHTING',NULL,3,7,2,5,2,4,1,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(149,'Hitmonchan',NULL,'Tyrogue',4,3,1,1,0,'FIGHTING',NULL,3,6,2,4,3,6,1,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(150,'Hitmontop',NULL,'Tyrogue',4,3,1,1,0,'FIGHTING',NULL,3,6,2,5,3,6,1,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(151,'Tyrogue','Hitmonlee / Hitmonchan / Hitmontop',NULL,3,3,1,1,0,'FIGHTING',NULL,1,3,1,3,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(152,'Lickitung','LickiLicky',NULL,3,3,1,1,0,'NORMAL',NULL,2,4,1,3,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(153,'LickiLicky',NULL,'Lickitung',5,3,1,1,0,'NORMAL',NULL,2,5,2,4,3,6,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(154,'Koffing','Weezing',NULL,3,3,1,1,0,'POISON',NULL,2,4,1,3,3,6,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(155,'Weezing',NULL,'Koffing',4,3,1,1,0,'POISON',NULL,2,5,2,4,3,7,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(156,'Rhyhorn','Rhydon',NULL,3,3,1,1,0,'GROUND','ROCK',2,5,1,3,3,6,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(157,'Rhydon','Rhyperior','Rhyhorn',5,3,1,1,0,'GROUND','ROCK',3,7,1,3,3,7,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(158,'Rhyperior',NULL,'Rhydon',6,3,1,1,0,'GROUND','ROCK',3,7,1,3,3,7,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(159,'Chansey','Blissey','Happiny',12,3,1,1,0,'NORMAL',NULL,1,2,2,4,1,2,1,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(160,'Blissey',NULL,'Chansey',12,3,1,1,0,'NORMAL',NULL,1,2,2,4,1,2,2,5,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(161,'Happiny','Chansey',NULL,4,3,1,1,0,'NORMAL',NULL,1,2,1,3,1,2,1,2,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(162,'Tangela','Tangrowth',NULL,3,3,1,1,0,'GRASS',NULL,2,4,2,4,3,6,3,6,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(163,'Tangrowth',NULL,'Tangela',5,3,1,1,0,'GRASS',NULL,3,6,2,4,3,7,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(164,'Kangaskhan','Mega-Kangaskhan',NULL,5,3,1,1,0,'NORMAL',NULL,3,6,2,5,2,5,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(165,'Mega-Kangaskhan',NULL,'Kangaskhan',6,3,1,1,0,'NORMAL',NULL,3,7,3,6,3,6,2,4,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(166,'Horsea','Seadra',NULL,3,3,1,1,0,'WATER',NULL,2,4,2,4,2,5,2,5,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(167,'Seadra','Kingdra','Horsea',4,3,1,1,0,'WATER',NULL,2,4,2,5,3,6,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(168,'Kingdra',NULL,'Seadra',5,3,1,1,0,'DRAGON','WATER',3,6,2,5,3,6,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(169,'Goldeen','Seaking',NULL,3,3,1,1,0,'WATER',NULL,2,4,2,4,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(170,'Seaking',NULL,'Goldeen',4,3,1,1,0,'WATER',NULL,3,6,2,4,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(171,'Staryu','Starmie',NULL,3,3,1,1,0,'WATER',NULL,2,4,2,5,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(172,'Starmie',NULL,'Staryu',4,3,1,1,0,'WATER','PSYCHIC',2,5,3,6,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(173,'Mr.Mime',NULL,'Mime jr.',4,3,1,1,0,'PSYCHIC','FAIRY',2,4,2,5,2,4,3,6,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(174,'Mime jr.','Mr.Mime',NULL,3,3,1,1,0,'PSYCHIC','FAIRY',1,3,2,4,2,4,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(175,'Scyther','Scizor',NULL,3,3,1,1,0,'BUG','FLYING',3,6,3,6,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(176,'Scizor','Mega-Scizor','Scyther',4,3,1,1,0,'BUG','STEEL',3,7,2,4,3,6,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(177,'Mega-Scizor',NULL,'Scizor',5,3,1,1,0,'BUG','STEEL',4,8,2,5,3,7,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(178,'Jynx',NULL,'Smoochum',4,3,1,1,0,'ICE','PSYCHIC',2,4,3,6,1,3,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(179,'Smoochum','Jynx',NULL,3,3,1,1,0,'ICE','PSYCHIC',1,3,2,4,1,2,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(180,'Electabuzz','Electivire','Elekid',4,3,1,1,0,'ELECTRIC',NULL,2,5,3,6,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(181,'Electivire',NULL,'Electabuzz',5,3,1,1,0,'ELECTRIC',NULL,3,7,3,6,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(182,'Elekid','Electabuzz',NULL,3,3,1,1,0,'ELECTRIC',NULL,2,4,2,5,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(183,'Magmar','Magmortar','Magby',4,3,1,1,0,'FIRE',NULL,3,6,2,5,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(184,'Magmortar',NULL,'Magmar',5,3,1,1,0,'FIRE',NULL,3,6,2,5,2,4,3,7,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(185,'Magby','Magmar',NULL,3,3,1,1,0,'FIRE',NULL,2,4,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(186,'Pinsir','Mega-Pinsir',NULL,4,3,1,1,0,'BUG',NULL,3,7,2,5,3,6,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(187,'Mega-Pinsir',NULL,'Pinsir',5,3,1,1,0,'BUG','FLYING',4,8,3,6,3,7,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(188,'Tauros',NULL,NULL,4,3,1,1,0,'NORMAL',NULL,3,6,3,6,3,6,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(189,'Magikarp','Gyarados',NULL,3,3,1,1,0,'WATER',NULL,1,2,2,5,2,4,1,2,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(190,'Gyarados','Mega-Gyarados','Magikarp',7,3,1,1,0,'WATER','FLYING',3,7,2,5,2,5,2,4,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(191,'Mega-Gyarados',NULL,'Gyarados',8,3,1,1,0,'WATER','DARK',4,8,2,5,3,6,2,5,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(192,'Lapras',NULL,NULL,6,3,1,1,0,'WATER','ICE',2,5,2,4,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(193,'Ditto',NULL,NULL,4,3,1,1,0,'NORMAL',NULL,2,4,2,4,2,4,2,4,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(194,'Eevee','Vaporeon / Jolteon / Flareon / Umbreon / Glaceon / Espeon / Sylveon',NULL,3,3,1,1,0,'NORMAL',NULL,2,4,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(195,'Vaporeon',NULL,'Eevee',6,3,1,1,0,'WATER',NULL,2,4,2,4,2,4,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(196,'Jolteon',NULL,'Eevee',4,3,1,1,0,'ELECTRIC',NULL,2,4,3,7,2,4,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(197,'Flareon',NULL,'Eevee',4,3,1,1,0,'FIRE',NULL,3,7,2,4,2,4,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(198,'Umbreon',NULL,'Eevee',4,3,1,1,0,'DARK',NULL,2,4,2,4,3,6,2,4,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(199,'Espeon',NULL,'Eevee',4,3,1,1,0,'PSYCHIC',NULL,2,4,3,6,2,4,3,7,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(200,'Sylveon',NULL,'Eevee',4,3,1,1,0,'FAIRY',NULL,2,4,2,4,2,4,3,6,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(201,'Porygon','Porygon 2',NULL,3,3,1,1,0,'NORMAL',NULL,2,4,1,3,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(202,'Porygon 2','Porygon-Z','Porygon',4,3,1,1,0,'NORMAL',NULL,2,5,2,4,2,5,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(203,'Porygon-Z',NULL,'Porygon 2',5,3,1,1,0,'NORMAL',NULL,2,5,2,5,2,5,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(204,'Omanyte','Omastar',NULL,3,3,1,1,0,'ROCK','WATER',1,3,1,3,3,6,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(205,'Omastar',NULL,'Omanyte',4,3,1,1,0,'ROCK','WATER',2,4,2,4,3,7,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(206,'Kabuto','Kabutops',NULL,3,3,1,1,0,'ROCK','WATER',2,5,2,4,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(207,'Kabutops',NULL,'Kabuto',4,3,1,1,0,'ROCK','WATER',3,6,2,5,3,6,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(208,'Aerodactyl','Mega-Aerodactyl',NULL,4,3,1,1,0,'ROCK','FLYING',3,6,3,7,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(209,'Mega-Aerodactyl',NULL,'Aerodactyl',5,3,1,1,0,'ROCK','FLYING',3,7,3,7,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(210,'Snorlax',NULL,'Munchlax',8,3,1,1,0,'NORMAL',NULL,3,6,1,3,2,4,2,4,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(211,'Munchlax','Snorlax',NULL,5,3,1,1,0,'NORMAL',NULL,2,5,1,2,1,3,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(212,'Articuno',NULL,NULL,4,3,1,1,0,'ICE','FLYING',5,5,5,5,6,6,6,6,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(213,'Zapdos',NULL,NULL,4,3,1,1,0,'ELECTRIC','FLYING',5,5,6,6,5,5,7,7,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(214,'Moltres',NULL,NULL,4,3,1,1,0,'FIRE','FLYING',6,6,5,5,5,5,7,7,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(215,'Dratini','Dragonair',NULL,3,3,1,1,0,'DRAGON',NULL,2,4,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(216,'Dragonair','Dragonite','Dratini',6,3,1,1,0,'DRAGON',NULL,2,5,2,5,2,4,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(217,'Dragonite',NULL,'Dragonair',6,3,1,1,0,'DRAGON','FLYING',3,7,2,5,3,6,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(218,'Mewtwo','Mega-Mewtwo X/Y',NULL,5,3,1,1,0,'PSYCHIC',NULL,6,6,7,7,5,5,8,8,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(219,'Mega-Mewtwo Y',NULL,'Mewtwo',6,3,1,1,0,'PSYCHIC',NULL,8,8,7,7,5,5,10,10,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(220,'Mega-Mewtwo X',NULL,'Mewtwo',6,3,1,1,0,'PSYCHIC','FIGHTING',9,9,7,7,6,6,7,7,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(221,'Mew',NULL,NULL,5,3,1,1,0,'PSYCHIC',NULL,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(222,'Chikorita','Bayleef',NULL,3,3,1,1,0,'GRASS',NULL,2,4,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(223,'Bayleef','Meganium','Chikorita',4,3,1,1,0,'GRASS',NULL,2,4,2,4,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(224,'Meganium',NULL,'Bayleef',5,3,1,1,0,'GRASS',NULL,2,5,2,5,3,6,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(225,'Cyndaquil','Quilava',NULL,3,3,1,1,0,'FIRE',NULL,2,4,2,4,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(226,'Quilava','Typhlosion','Cyndaquil',4,3,1,1,0,'FIRE',NULL,2,4,2,5,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(227,'Typhlosion',NULL,'Quilava',5,3,1,1,0,'FIRE',NULL,2,5,3,6,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(228,'Totodile','Croconaw',NULL,3,3,1,1,0,'WATER',NULL,2,4,1,3,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(229,'Croconaw','Feraligatr','Totodile',4,3,1,1,0,'WATER',NULL,2,5,2,4,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(230,'Feraligatr',NULL,'Croconaw',5,3,1,1,0,'WATER',NULL,3,6,2,5,3,6,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(231,'Sentret','Furret',NULL,3,3,1,1,0,'NORMAL',NULL,2,4,1,3,1,3,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(232,'Furret',NULL,'Sentret',4,3,1,1,0,'NORMAL',NULL,2,5,2,4,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(233,'Hoothoot','Noctowl',NULL,3,3,1,1,0,'NORMAL','FLYING',1,3,1,3,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(234,'Noctowl',NULL,'Hoothoot',4,3,1,1,0,'NORMAL','FLYING',2,5,2,5,2,4,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(235,'Ledyba','Ledian',NULL,3,3,1,1,0,'BUG','FLYING',1,3,2,4,1,3,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(236,'Ledian',NULL,'Ledyba',4,3,1,1,0,'BUG','FLYING',1,3,2,5,2,4,2,4,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(237,'Spinarak','Ariados',NULL,3,3,1,1,0,'BUG','POISON',2,4,1,3,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(238,'Ariados',NULL,'Spinarak',4,3,1,1,0,'BUG','POISON',2,5,1,3,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(239,'Chinchou','Lantern',NULL,3,3,1,1,0,'WATER','ELECTRIC',1,3,2,4,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(240,'Lanturn',NULL,'Chinchou',6,3,1,1,0,'WATER','ELECTRIC',2,4,2,4,2,4,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(241,'Pichu','Pikachu',NULL,3,3,1,1,0,'ELECTRIC',NULL,1,3,2,4,1,2,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(242,'Cleffa','Clefable',NULL,3,3,1,1,0,'FAIRY',NULL,1,3,1,2,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(243,'Igglybuff','Jigglypuff',NULL,3,3,1,1,0,'NORMAL','FAIRY',1,3,1,2,1,2,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(244,'Togepi','Togetic',NULL,3,3,1,1,0,'FAIRY',NULL,1,3,1,3,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(245,'Togetic','Togekiss','Togepi',4,3,1,1,0,'FAIRY','FLYING',1,3,1,3,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(246,'Togekiss',NULL,'Togetic',5,3,1,1,0,'FAIRY','FLYING',2,4,2,5,3,6,3,7,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(247,'Natu','Xatu',NULL,3,3,1,1,0,'PSYCHIC','FLYING',2,4,2,5,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(248,'Xatu',NULL,'Natu',4,3,1,1,0,'PSYCHIC','FLYING',2,5,3,5,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(249,'Mareep','Flaafy',NULL,3,3,1,1,0,'ELECTRIC',NULL,1,3,1,3,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(250,'Flaafy','Ampharos','Mareep',4,3,1,1,0,'ELECTRIC',NULL,2,4,2,4,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(251,'Ampharos','Mega-Ampharos','Flaafy',5,3,1,1,0,'ELECTRIC',NULL,2,5,2,4,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(252,'Mega-Ampharos',NULL,'Ampharos',6,3,1,1,0,'ELECTRIC','DRAGON',3,6,2,4,3,6,4,8,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(253,'Maril','Azumaril','Azurill',4,3,1,1,0,'WATER','FAIRY',1,3,1,3,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(254,'Azumaril',NULL,'Maril',5,3,1,1,0,'WATER','FAIRY',2,4,2,4,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(255,'Azurill','Maril',NULL,3,3,1,1,0,'NORMAL','FAIRY',1,3,1,3,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(256,'Sudowoodo',NULL,'Bonsly',4,3,1,1,0,'ROCK',NULL,3,6,1,3,3,6,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(257,'Bonsly','Sudowoodo',NULL,3,3,1,1,0,'ROCK',NULL,2,5,1,2,3,6,1,2,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(258,'Hoppip','Skiploom',NULL,3,3,1,1,0,'GRASS','FLYING',1,3,2,4,1,3,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(259,'Skiploom','Jumpluff','Hoppip',4,3,1,1,0,'GRASS','FLYING',2,4,2,5,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(260,'Jumpluff',NULL,'Skiploom',5,3,1,1,0,'GRASS','FLYING',2,4,3,6,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(261,'Aipom','Ambipom',NULL,3,3,1,1,0,'NORMAL',NULL,2,5,2,5,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(262,'Ambipom',NULL,'Aipom',4,3,1,1,0,'NORMAL',NULL,3,6,3,6,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(263,'Sunkern','Sunflora',NULL,3,3,1,1,0,'GRASS',NULL,1,3,1,3,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(264,'Sunflora',NULL,'Sunkern',4,3,1,1,0,'GRASS',NULL,2,5,1,3,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(265,'Yanma','Yanmega',NULL,3,3,1,1,0,'BUG','FLYING',2,4,3,6,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(266,'Yanma','Yanmega',NULL,3,3,1,1,0,'BUG','FLYING',2,4,3,6,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(267,'Yanmega',NULL,'Yanma',4,3,1,1,0,'BUG','FLYING',2,5,3,6,2,5,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(268,'Wooper','Quagsire',NULL,3,3,1,1,0,'WATER','GROUND',2,4,1,2,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(269,'Quagsire',NULL,'Wooper',4,3,1,1,0,'WATER','GROUND',2,5,1,3,3,6,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(270,'Murkrow','Honchkrow',NULL,3,3,1,1,0,'DARK','FLYING',2,5,1,3,2,5,2,5,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(271,'Honchkrow',NULL,'Murkrow',5,3,1,1,0,'DARK','FLYING',3,7,2,5,2,4,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(272,'Misdreavus','Mismagius',NULL,3,3,1,1,0,'GHOST',NULL,2,4,2,5,2,4,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(273,'Mismagius',NULL,'Misdreavus',4,3,1,1,0,'GHOST',NULL,2,4,3,6,2,4,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(274,'Unown',NULL,NULL,4,3,1,1,0,'PSYCHIC',NULL,2,5,2,4,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(275,'Wobbuffet',NULL,'Wynaut',9,3,1,1,0,'PSYCHIC',NULL,1,3,1,3,3,6,1,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(276,'Wynaut','Wobbuffet',NULL,3,3,1,1,0,'PSYCHIC',NULL,1,3,1,3,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(277,'Girafarig',NULL,NULL,4,3,1,1,0,'PSYCHIC','NORMAL',2,5,2,5,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(278,'Pineco','Forretress',NULL,3,3,1,1,0,'BUG',NULL,2,4,1,2,2,5,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(279,'Forretress',NULL,'Pineco',3,3,1,1,0,'BUG','STEEL',2,5,1,3,3,7,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(280,'Dunsparce',NULL,NULL,5,3,1,1,0,'NORMAL',NULL,2,5,2,4,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(281,'Gligar','Gliscor',NULL,3,3,1,1,0,'GROUND','FLYING',2,5,2,5,3,6,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(282,'Gliscor',NULL,'Gligar',5,3,1,1,0,'GROUND','FLYING',3,6,3,6,3,7,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(283,'Snubbull','Granbull',NULL,3,3,1,1,0,'FAIRY',NULL,2,5,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(284,'Granbull',NULL,'Snubbull',4,3,1,1,0,'FAIRY',NULL,3,7,2,4,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(285,'Qwilfish',NULL,NULL,4,3,1,1,0,'WATER','POISON',3,6,2,5,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(286,'Shuckle',NULL,NULL,4,3,1,1,0,'BUG','ROCK',1,2,1,2,5,10,1,2,5,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(287,'Heracross','Mega-Heracross',NULL,4,3,1,1,0,'BUG','FIGHTING',3,6,2,5,2,5,1,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(288,'Mega-Heracross',NULL,'Heracross',5,3,1,1,0,'BUG','FIGHTING',4,9,2,5,3,6,1,2,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(289,'Sneasel','Weavile',NULL,3,3,1,1,0,'DARK','ICE',3,6,3,6,2,4,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(290,'Weavile',NULL,'Sneasel',4,3,1,1,0,'DARK','ICE',3,7,3,7,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(291,'Teddiursa','Ursaring',NULL,3,3,1,1,0,'NORMAL',NULL,2,5,1,3,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(292,'Ursaring',NULL,'Teddiursa',4,3,1,1,0,'NORMAL',NULL,3,7,2,4,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(293,'Slugma','Magcargo',NULL,3,3,1,1,0,'FIRE',NULL,1,3,1,3,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(294,'Magcargo',NULL,'Slugma',4,3,1,1,0,'FIRE','ROCK',2,4,1,3,3,7,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(295,'Swinub','Piloswine',NULL,3,3,1,1,0,'ICE','GROUND',2,4,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(296,'Piloswine','Mamoswine','Swinub',5,3,1,1,0,'ICE','GROUND',3,6,2,4,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(297,'Mamoswine',NULL,'Piloswine',6,3,1,1,0,'ICE','GROUND',3,7,2,5,2,5,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(298,'Corsola',NULL,NULL,4,3,1,1,0,'WATER','ROCK',2,4,1,3,3,6,2,4,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(299,'Remoraid','Octillery',NULL,3,3,1,1,0,'WATER',NULL,2,4,2,4,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(300,'Octillery',NULL,'Remoraid',4,3,1,1,0,'WATER',NULL,3,6,2,4,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(301,'Delibird',NULL,NULL,4,3,1,1,0,'ICE','FLYING',2,4,2,5,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(302,'Mantine',NULL,'Mantyke',4,3,1,1,0,'WATER','FLYING',1,3,2,5,2,5,2,5,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(303,'Mantyke','Mantine',NULL,3,3,1,1,0,'WATER','FLYING',1,3,2,4,2,4,1,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(304,'Scarmory',NULL,NULL,4,3,1,1,0,'STEEL','FLYING',2,5,2,5,3,7,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(305,'Houndour','Houndoom',NULL,3,3,1,1,0,'DARK','FIRE',2,4,2,4,1,3,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(306,'Houndoom','Mega-Houndoom','Houndour',4,3,1,1,0,'DARK','FIRE',2,5,3,6,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(307,'Mega-Houndoom',NULL,'Houndoom',5,3,1,1,0,'DARK','FIRE',2,5,3,6,2,5,4,8,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(308,'Phanpy','Donphan',NULL,3,3,1,1,0,'GROUND',NULL,2,4,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(309,'Donphan',NULL,'Phanpy',4,3,1,1,0,'GROUND',NULL,3,7,2,4,3,6,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(310,'Stantler',NULL,NULL,4,3,1,1,0,'NORMAL',NULL,3,6,2,5,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(311,'Smeargle',NULL,NULL,4,3,1,1,0,'NORMAL',NULL,1,3,3,6,2,4,1,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(312,'Miltank',NULL,NULL,4,3,1,1,0,'NORMAL',NULL,2,5,3,6,3,6,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(313,'Raikou',NULL,NULL,4,3,1,1,0,'ELECTRIC',NULL,5,5,7,7,5,5,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(314,'Entei',NULL,NULL,5,3,1,1,0,'FIRE',NULL,7,7,6,6,5,5,5,5,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(315,'Suicune',NULL,NULL,5,3,1,1,0,'WATER',NULL,5,5,5,5,6,6,5,5,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(316,'Larvitar','Pupitar',NULL,3,3,1,1,0,'ROCK','GROUND',2,4,1,3,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(317,'Pupitar','Tyranitar','Larvitar',4,3,1,1,0,'ROCK','GROUND',2,5,2,4,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(318,'Tyranitar','Mega-Tyranitar','Pupitar',6,3,1,1,0,'ROCK','DARK',3,7,2,5,3,6,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(319,'Mega-Tyranitar',NULL,'Tyranitar',6,3,1,1,0,'ROCK','DARK',4,8,2,5,4,8,3,6,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(320,'Lugia',NULL,NULL,6,3,1,1,0,'FLYING','PSYCHIC',5,5,6,6,7,7,5,5,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(321,'Ho-oh',NULL,NULL,5,3,1,1,0,'FIRE','FLYING',7,7,5,5,5,5,6,6,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(322,'Celebi',NULL,NULL,5,3,1,1,0,'GRASS','PSYCHIC',6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(323,'Treecko','Grovyle',NULL,3,3,1,1,0,'GRASS',NULL,2,4,2,5,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(324,'Grovyle','Sceptile','Treecko',4,3,1,1,0,'GRASS',NULL,2,4,3,6,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(325,'Sceptile','Mega-Sceptile','Grovyle',5,3,1,1,0,'GRASS',NULL,2,5,3,7,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(326,'Mega-Sceptile',NULL,'Sceptile',6,3,1,1,0,'GRASS','DRAGON',3,6,4,8,2,5,4,8,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(327,'Torchic','Combusken',NULL,3,3,1,1,0,'FIRE',NULL,2,4,2,4,1,3,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(328,'Combusken','Blaziken','Torchic',4,3,1,1,0,'FIRE','FIGHTING',2,5,2,4,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(329,'Blaziken','Mega-Blaziken','Combusken',5,3,1,1,0,'FIRE','FIGHTING',3,7,2,5,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(330,'Mega-Blaziken',NULL,'Blaziken',6,3,1,1,0,'FIRE','FIGHTING',4,8,3,6,2,5,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(331,'Mudkip','Marshtomp',NULL,3,3,1,1,0,'WATER',NULL,2,5,1,3,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(332,'Marshtomp','Swampert','Mudkip',4,3,1,1,0,'WATER','GROUND',2,5,2,4,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(333,'Swampert','Mega-Swampert','Marshtomp',6,3,1,1,0,'WATER','GROUND',3,6,2,4,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(334,'Mega-Swampert',NULL,'Swampert',7,3,1,1,0,'WATER','GROUND',4,8,2,5,3,6,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(335,'Poochyena','Mightyena',NULL,3,3,1,1,0,'DARK',NULL,2,4,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(336,'Mightyena',NULL,'Poochyena',4,3,1,1,0,'DARK',NULL,3,6,2,5,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(337,'Zigzagoon','Linoone',NULL,3,3,1,1,0,'NORMAL',NULL,1,3,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(338,'Linoone',NULL,'Zigzagoon',4,3,1,1,0,'NORMAL',NULL,2,5,3,6,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(339,'Wurmple','Silcoon / Cascoon',NULL,3,3,1,1,0,'BUG',NULL,2,4,1,3,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(340,'Silcoon','Beautifly','Wurmple',4,3,1,1,0,'BUG',NULL,2,4,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(341,'Cascoon','Dustox','Wurmple',4,3,1,1,0,'BUG',NULL,2,4,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(342,'Beautifly',NULL,'Silcoon',5,3,1,1,0,'BUG','FLYING',2,5,2,4,2,4,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(343,'Dustox',NULL,'Cascoon',5,3,1,1,0,'BUG','POISON',2,4,2,4,3,6,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(344,'Lotad','Lombre',NULL,3,3,1,1,0,'GRASS','WATER',1,3,1,3,1,3,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(345,'Lombre','Ludicolo','Lotad',4,3,1,1,0,'GRASS','WATER',2,4,2,4,2,4,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(346,'Ludicolo',NULL,'Lombre',5,3,1,1,0,'GRASS','WATER',2,5,2,5,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(347,'Seedot','Nuzleaf',NULL,3,3,1,1,0,'GRASS','DARK',1,3,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(348,'Nuzleaf','Shiftry','Seedot',4,3,1,1,0,'GRASS','DARK',2,5,2,4,2,4,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(349,'Shiftry',NULL,'Nuzleaf',5,3,1,1,0,'GRASS','DARK',3,6,2,5,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(350,'Tailow','Swellow',NULL,3,3,1,1,0,'FLYING','NORMAL',2,4,2,5,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(351,'Swellow',NULL,'Tailow',4,3,1,1,0,'FLYING','NORMAL',2,5,3,7,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(352,'Wingull','Pelipper',NULL,3,3,1,1,0,'WATER','FLYING',1,3,2,5,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(353,'Pelipper',NULL,'Wingull',4,3,1,1,0,'WATER','FLYING',2,4,2,4,3,6,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(354,'Kirlia','Gardevoir','Ralts',4,3,1,1,0,'PSYCHIC','FAIRY',1,3,2,4,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(355,'Gardevoir','Mega-Gardevoir','Kirlia',5,3,1,1,0,'PSYCHIC','FAIRY',2,4,2,5,2,4,3,7,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(356,'Mega-Gardevoir',NULL,'Gardevoir',6,3,1,1,0,'PSYCHIC','FAIRY',2,5,3,6,2,4,5,10,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(357,'Surskit','Masquerain',NULL,3,3,1,1,0,'BUG','WATER',1,3,2,4,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(358,'Masquerain',NULL,'Surskit',4,3,1,1,0,'BUG','FLYING',2,4,2,5,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(359,'Shroomish','Breloom',NULL,3,3,1,1,0,'GRASS',NULL,2,4,1,3,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(360,'Breloom',NULL,'Shroomish',4,3,1,1,0,'GRASS','FIGHTING',3,7,2,5,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(361,'Slakoth','Vigoroth',NULL,3,3,1,1,0,'NORMAL',NULL,2,4,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(362,'Vigoroth','Slaking','Slakoth',4,3,1,1,0,'NORMAL',NULL,2,5,2,5,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(363,'Slaking',NULL,'Vigoroth',8,3,1,1,0,'NORMAL',NULL,4,8,3,6,3,6,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(364,'Nincada','Ninjask / Shedinja',NULL,3,3,1,1,0,'BUG','GROUND',2,4,1,3,2,5,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(365,'Ninjask',NULL,'Nincada',4,3,1,1,0,'BUG','FLYING',2,5,4,8,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(366,'Shedinja',NULL,'Nincada',1,3,1,1,0,'BUG','GHOST',2,5,1,3,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(367,'Whismur','Loudred',NULL,3,3,1,1,0,'NORMAL',NULL,2,4,1,3,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(368,'Loudred','Exploud','Whismur',4,3,1,1,0,'NORMAL',NULL,2,5,2,4,1,3,2,5,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(369,'Exploud',NULL,'Loudred',6,3,1,1,0,'NORMAL',NULL,2,5,2,4,2,4,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(370,'Makuhita','Hariyama',NULL,3,3,1,1,0,'FIGHTING',NULL,2,4,1,3,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(371,'Hariyama',NULL,'Makuhita',7,3,1,1,0,'FIGHTING',NULL,3,7,2,4,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(372,'Nosepass','Probopass',NULL,3,3,1,1,0,'ROCK',NULL,2,4,1,3,3,7,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(373,'Probopass',NULL,'Nosepass',4,3,1,1,0,'ROCK','STEEL',2,4,2,5,4,8,2,5,4,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(374,'Skitty','Delcatty',NULL,3,3,1,1,0,'NORMAL',NULL,2,4,2,5,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(375,'Delcatty',NULL,'Skitty',4,3,1,1,0,'NORMAL',NULL,2,4,2,5,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(376,'Sableye','Mega-Sableye',NULL,4,3,1,1,0,'DARK','GHOST',2,5,2,4,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(377,'Mega-Sableye',NULL,'Sableye',5,3,1,1,0,'DARK','GHOST',2,5,1,2,3,7,3,6,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(378,'Mawile','Mega-Mawile',NULL,4,3,1,1,0,'STEEL','FAIRY',2,5,2,4,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(379,'Mega-Mawile',NULL,'Mawile',5,3,1,1,0,'STEEL','FAIRY',3,7,2,4,3,7,2,4,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(380,'Aron','Lairon',NULL,3,3,1,1,0,'STEEL','ROCK',2,5,1,3,3,6,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(381,'Lairon','Aggron','Aron',4,3,1,1,0,'STEEL','ROCK',2,5,1,3,3,7,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(382,'Aggron','Mega-Aggron','Lairon',5,3,1,1,0,'STEEL','ROCK',3,6,2,4,4,9,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(383,'Mega-Aggron',NULL,'Aggron',6,3,1,1,0,'STEEL',NULL,3,7,2,4,5,10,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(384,'Meditite','Medicham',NULL,3,3,1,1,0,'FIGHTING','PSYCHIC',1,3,2,4,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(385,'Medicham','Mega-Medicham','Meditite',4,3,1,1,0,'FIGHTING','PSYCHIC',2,4,2,5,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(386,'Mega-Medicham',NULL,'Medicham',5,3,1,1,0,'FIGHTING','PSYCHIC',3,6,3,6,3,6,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(387,'Electrike','Manectric',NULL,3,3,1,1,0,'ELECTRIC',NULL,2,4,2,4,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(388,'Manectric','Mega-Manectric','Electrike',4,3,1,1,0,'ELECTRIC',NULL,2,5,3,6,2,4,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(389,'Mega-Manectric',NULL,'Manectric',5,3,1,1,0,'ELECTRIC',NULL,2,5,3,7,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(390,'Plusle',NULL,NULL,4,3,1,1,0,'ELECTRIC',NULL,2,4,3,6,1,3,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(391,'Minun',NULL,NULL,4,3,1,1,0,'ELECTRIC',NULL,1,3,3,6,2,4,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(392,'Volbeat',NULL,NULL,4,3,1,1,0,'BUG',NULL,2,5,2,5,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(393,'Illumise',NULL,NULL,4,3,1,1,0,'BUG',NULL,2,4,2,5,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(394,'Roselia','Roserade','Budew',4,3,1,1,0,'GRASS','POISON',2,4,2,4,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(395,'Budew','Roselia',NULL,3,3,1,1,0,'GRASS','POISON',1,3,2,4,1,3,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(396,'Roserade',NULL,'Roselia',5,3,1,1,0,'GRASS','POISON',2,5,2,5,2,4,3,7,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(397,'Gulpin','Swalot',NULL,3,3,1,1,0,'POISON',NULL,1,3,1,3,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(398,'Swalot',NULL,'Gulpin',5,3,1,1,0,'POISON',NULL,2,5,2,4,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(399,'Carvanha','Sharpedo',NULL,3,3,1,1,0,'WATER','DARK',2,5,2,4,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(400,'Sharpedo','Mega-Sharpedo','Carvanha',4,3,1,1,0,'WATER','DARK',3,7,3,6,1,3,3,6,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(401,'Mega-Sharpedo',NULL,'Sharpedo',5,3,1,1,0,'WATER','DARK',4,8,3,6,2,5,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(402,'Wailmer','Wailord',NULL,5,3,1,1,0,'WATER',NULL,2,5,2,4,1,3,2,5,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(403,'Wailord',NULL,'Wailmer',11,3,1,1,0,'WATER',NULL,2,5,2,4,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(404,'Numel','Camerupt',NULL,3,3,1,1,0,'FIRE','GROUND',2,4,1,3,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(405,'Camerupt','Mega-Camerupt','Numel',4,3,1,1,0,'FIRE','GROUND',3,6,1,3,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(406,'Mega-Camerupt',NULL,'Camerupt',5,3,1,1,0,'FIRE','GROUND',3,7,1,2,3,6,4,8,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(407,'Torkoal',NULL,NULL,4,3,1,1,0,'FIRE',NULL,2,5,1,3,3,7,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(408,'Spoink','Grumpig',NULL,3,3,1,1,0,'PSYCHIC',NULL,1,3,2,4,1,3,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(409,'Grumpig',NULL,'Spoink',4,3,1,1,0,'PSYCHIC',NULL,2,4,2,5,2,4,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(410,'Spinda',NULL,NULL,4,3,1,1,0,'NORMAL',NULL,2,4,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(411,'Trapinch','Vibrava',NULL,3,3,1,1,0,'GROUND',NULL,3,6,1,2,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(412,'Vibrava','Flygon','Trapinch',4,3,1,1,0,'GROUND','DRAGON',3,6,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(413,'Flygon',NULL,'Vibrava',5,3,1,1,0,'GROUND','DRAGON',3,6,3,6,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(414,'Cacnea','Cacturne',NULL,3,3,1,1,0,'GRASS',NULL,2,5,1,3,1,3,2,5,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(415,'Cacturne',NULL,'Cacnea',4,3,1,1,0,'GRASS','DARK',3,6,2,4,2,4,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(416,'Swablu','Altaria',NULL,3,3,1,1,0,'NORMAL','FLYING',1,3,2,4,2,4,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(417,'Altaria','Mega-Altaria','Swablu',4,3,1,1,0,'DRAGON','FLYING',2,5,2,5,2,5,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(418,'Mega-Altaria',NULL,'Altaria',5,3,1,1,0,'DRAGON','FAIRY',3,6,2,5,3,6,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(419,'Zangoose',NULL,NULL,4,3,1,1,0,'NORMAL',NULL,3,6,2,5,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(420,'Seviper',NULL,NULL,4,3,1,1,0,'POISON',NULL,3,6,2,4,2,4,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(421,'Lunatone',NULL,NULL,4,3,1,1,0,'ROCK','PSYCHIC',1,3,2,5,2,4,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(422,'Solrock',NULL,NULL,4,3,1,1,0,'ROCK','PSYCHIC',3,6,2,5,2,5,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(423,'Barboach','Wishcash',NULL,3,3,1,1,0,'WATER','GROUND',2,4,2,4,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(424,'Wishcash',NULL,'Barboach',5,3,1,1,0,'WATER','GROUND',2,5,2,4,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(425,'Corphish','Crawdaunt',NULL,3,3,1,1,0,'WATER',NULL,2,5,1,3,2,4,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(426,'Crawdaunt',NULL,'Corphish',4,3,1,1,0,'WATER','DARK',3,7,2,4,2,5,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(427,'Baltoy','Claydol',NULL,3,3,1,1,0,'PSYCHIC','GROUND',1,3,2,4,2,4,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(428,'Claydol',NULL,'Baltoy',4,3,1,1,0,'PSYCHIC','GROUND',2,5,2,5,3,6,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(429,'Lileep','Cradily',NULL,3,3,1,1,0,'ROCK','GRASS',1,3,1,3,2,5,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(430,'Cradily',NULL,'Lileep',4,3,1,1,0,'ROCK','GRASS',2,5,1,3,3,6,2,5,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(431,'Anorith','Armaldo',NULL,3,3,1,1,0,'ROCK','BUG',3,6,2,5,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(432,'Armaldo',NULL,'Anorith',4,3,1,1,0,'ROCK','BUG',3,7,2,4,3,6,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(433,'Feebas','Milotic',NULL,3,3,1,1,0,'WATER',NULL,1,2,2,5,1,3,1,2,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(434,'Milotic',NULL,'Feebas',7,3,1,1,0,'WATER',NULL,2,4,2,5,2,5,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(435,'Castform',NULL,NULL,4,3,1,1,0,'NORMAL',NULL,2,5,2,5,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(436,'Kecleon',NULL,NULL,4,3,1,1,0,'NORMAL',NULL,2,5,1,3,2,5,2,4,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(437,'Shuppet','Banette',NULL,3,3,1,1,0,'GHOST',NULL,2,5,2,4,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(438,'Banette','Mega-Banette','Shuppet',4,3,1,1,0,'GHOST',NULL,3,6,2,4,2,4,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(439,'Mega-Banette',NULL,'Banette',5,3,1,1,0,'GHOST',NULL,4,8,2,5,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(440,'Duskull','Dusklops',NULL,3,3,1,1,0,'GHOST',NULL,1,3,1,3,2,5,1,3,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(441,'Dusklops','Dusknoir','Duskull',4,3,1,1,0,'GHOST',NULL,2,5,1,3,3,7,2,4,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(442,'Dusknoir',NULL,'Dusklops',4,3,1,1,0,'GHOST',NULL,3,6,2,4,3,7,2,4,3,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(443,'Tropius',NULL,NULL,5,3,1,1,0,'GRASS','FLYING',2,4,2,4,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(444,'Chimecho',NULL,'Chingling',4,3,1,1,0,'PSYCHIC',NULL,2,4,2,4,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(445,'Chingling','Chimecho',NULL,3,3,1,1,0,'PSYCHIC',NULL,1,3,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(446,'Absol','Mega-Absol',NULL,4,3,1,1,0,'DARK',NULL,3,7,2,5,2,4,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(447,'Mega-Absol',NULL,'Absol',5,3,1,1,0,'DARK',NULL,4,8,3,6,2,4,3,6,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(448,'Snorunt','Glalie / Froslass',NULL,3,3,1,1,0,'ICE',NULL,2,4,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(449,'Glalie','Mega-Glalie','Snorunt',4,3,1,1,0,'ICE',NULL,2,5,2,5,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(450,'Mega-Glalie',NULL,'Glalie',5,3,1,1,0,'ICE',NULL,3,7,3,6,2,5,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(451,'Froslass',NULL,'Snorunt',4,3,1,1,0,'ICE','GHOST',2,5,3,6,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(452,'Spheal','Sealeo',NULL,3,3,1,1,0,'ICE','WATER',1,3,1,3,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(453,'Sealeo','Walrein','Spheal',4,3,1,1,0,'ICE','WATER',2,4,2,4,2,5,2,5,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(454,'Walrein',NULL,'Sealeo',6,3,1,1,0,'ICE','WATER',2,5,2,4,3,6,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(455,'Clampearl','Huntail / Gorebyss',NULL,3,3,1,1,0,'WATER',NULL,2,4,1,3,2,5,2,5,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(456,'Huntail',NULL,'Clampearl',4,3,1,1,0,'WATER',NULL,3,6,2,4,3,6,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(457,'Gorebyss',NULL,'Clampearl',4,3,1,1,0,'WATER',NULL,2,5,2,4,3,6,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(458,'Relicanth',NULL,NULL,5,3,1,1,0,'ROCK','WATER',2,5,2,4,3,7,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(459,'Luvdisc',NULL,NULL,4,3,1,1,0,'WATER',NULL,1,3,3,6,2,4,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(460,'Bagon','Shelgon',NULL,3,3,1,1,0,'DRAGON',NULL,2,5,2,4,2,4,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(461,'Shelgon','Salamence','Bagon',4,3,1,1,0,'DRAGON',NULL,3,6,2,4,3,6,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(462,'Salamence','Mega-Salamence','Shelgon',5,3,1,1,0,'DRAGON','FLYING',3,7,3,6,2,5,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(463,'Mega-Salamence',NULL,'Salamence',6,3,1,1,0,'DRAGON','FLYING',4,8,3,7,3,7,3,7,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(464,'Beldum','Metang',NULL,3,3,1,1,0,'STEEL','PSYCHIC',2,4,1,3,2,5,1,3,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(465,'Metang','Metagross','Beldum',4,3,1,1,0,'STEEL','PSYCHIC',2,5,2,4,3,6,2,4,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(466,'Metagross','Mega-Metagross','Metang',5,3,1,1,0,'STEEL','PSYCHIC',3,7,2,5,3,7,3,6,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(467,'Mega-Metagross',NULL,'Metagross',6,3,1,1,0,'STEEL','PSYCHIC',4,8,3,6,4,8,3,6,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(468,'Regirock',NULL,NULL,4,3,1,1,0,'ROCK',NULL,6,6,4,4,10,10,4,4,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(469,'Regice',NULL,NULL,4,3,1,1,0,'ICE',NULL,4,4,4,4,6,6,6,6,10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(470,'Registeel',NULL,NULL,4,3,1,1,0,'STEEL',NULL,5,5,4,4,8,8,5,5,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(471,'Latias','Mega-Latias',NULL,4,3,1,1,0,'DRAGON','PSYCHIC',5,5,6,6,5,5,6,6,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(472,'Mega-Latias',NULL,'Latias',5,3,1,1,0,'DRAGON','PSYCHIC',6,6,6,6,7,7,7,7,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(473,'Latios','Mega-Latios',NULL,4,3,1,1,0,'DRAGON','PSYCHIC',5,5,6,6,5,5,7,7,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(474,'Mega-Latios',NULL,'Latios',5,3,1,1,0,'DRAGON','PSYCHIC',7,7,6,6,6,6,8,8,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(475,'Kyogre','Primal Kyogre',NULL,6,3,1,1,0,'WATER',NULL,6,6,5,5,5,5,8,8,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(476,'Primal Kyogre',NULL,'Kyogre',10,3,1,1,0,'WATER',NULL,8,8,5,5,5,5,9,9,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(477,'Groudon','Primal Groudon',NULL,5,3,1,1,0,'GROUND',NULL,8,8,5,5,7,7,6,6,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(478,'Primal Groudon',NULL,'Groudon',7,3,1,1,0,'GROUND','FIRE',9,9,5,5,8,8,8,8,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(479,'Rayquaza','Mega-Rayquaza',NULL,8,3,1,1,0,'DRAGON','FLYING',8,8,6,6,5,5,8,8,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(480,'Mega-Rayquaza',NULL,'Rayquaza',11,3,1,1,0,'DRAGON','FLYING',9,9,6,6,6,6,9,9,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(481,'Jirachi',NULL,NULL,5,3,1,1,0,'STEEL','PSYCHIC',6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(482,'Deoxys',NULL,NULL,4,3,1,1,0,'PSYCHIC',NULL,8,8,8,8,4,4,8,8,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(483,'Deoxys (Attack Form)',NULL,NULL,4,3,1,1,0,'PSYCHIC',NULL,10,10,8,8,2,2,10,10,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(484,'Deoxys (Defense Form)',NULL,NULL,4,3,1,1,0,'PSYCHIC',NULL,5,5,5,5,9,9,5,5,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(485,'Deoxys (Speed Form)',NULL,NULL,4,3,1,1,0,'PSYCHIC',NULL,5,5,10,10,5,5,6,6,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
CREATE TABLE IF NOT EXISTS "User" (
	id INTEGER NOT NULL, 
	username VARCHAR(100) NOT NULL, 
	password VARCHAR(200) NOT NULL, 
	"passwordSalt" VARCHAR(64) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);
INSERT INTO User VALUES(1,'twigdemon','scrypt:32768:8:1$XGNrTEkIGsvwPjQL$8111896a809eb30c097827f8ff715798ba9fa176e8ecc5dbd3e2df37c577d112c94d22defbd5435c8f6e3ef8684a9677bb8663c9743f90e0f65bdc69e66a157f','0956bb2e4fe083446729b2420f618be63eb113b47b61c36dab207c663d809420');
CREATE TABLE IF NOT EXISTS "Nature" (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	description TEXT NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO Nature VALUES(1,'Brave','The Brave of heart will face any situation with courage and a cool head. They wont tolerate bullying or abuse anywhere near them and will always encourage others to conquer their fears. ''Selfless'' is their second name, as they will never turn their back on their comrades even at the cost of their own safety. Others look up to them as they inspire confidence and trust. They strive to conquer their fears and wish to inspire others to do the same. They keep it together when stress begins to escalate.');
INSERT INTO Nature VALUES(2,'Quiet','Life is what happens around those with a Quiet nature. They often take a passive stance over the circumstances around them. Strong thoughts or opinions they have will rarely be expressed, so they may be afraid to make a mistake or consider it a hassle to take action. When they manage to get the attention of others they rarely know what to do with themselves.');
INSERT INTO Nature VALUES(3,'Lonely','They like to keep their distance and do everything on their own. They ofter feel its up to them and nobody else to get things done and will take the burden of a responsibility that should be shared. Interacting with others is like a chore for them but being isolate also makes them feel misunderstood. They are hard to get close to but they can be trusted to do their best even if there''s no one around to guide them.');
INSERT INTO Nature VALUES(4,'Naughty','Why should they listen to you? You are not their boss! Most of the time they''ll deliberately do the opposite from what''s expected from them. Why? Because they can, of course. They love to see others get mad and will use their clever mind and cunning to get away with their misdeeds. When they stress they put a cool facade, dont let that fool you. They need to be coaxed or put in their place to behave properly.');
CREATE TABLE IF NOT EXISTS "Ability" (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	"flavorText" TEXT NOT NULL, 
	effect TEXT NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO Ability VALUES(1,'Synchronize','The Pokemon can share its mood, feelings and sensations with whoever caused those afflictions.','If a foe inflicts a Status Condition to this Pokemon, the same condition is inflicted into the foe unless it is immune to the effect.');
INSERT INTO Ability VALUES(2,'Torrent','This Pokemon builds up pressure to shoot water streams. When that pressure cannot be held in, it is released through uncontrollable torrents.','When this Pokemon''s Health is at half or less, Pain Penalization will not reduce successes from Damage rolls of its Water-Type Moves, and they will get 1 Extra Drice to their Damage Pool.');
INSERT INTO Ability VALUES(3,'Bulletproof','The armor on this Pokemon''s body protects it from projectiles and small explosions.','Reduce all damage from Special and Ranged Physical Attacks by 1 which hit this Pokemon.');
INSERT INTO Ability VALUES(4,'Inner Focus','The Pokemon is extremely serious and focused on everything it does. It remains calm and never backs down, even if its getting severly injured.','This Pokemon does not Flinch and cannot be Intimidated (Ability).');
CREATE TABLE IF NOT EXISTS "Item" (
    id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    effect TEXT,
    effectKey VARCHAR(50),
    effectData JSON,
    "minShopTier" VARCHAR(9) DEFAULT 'BASIC',
    "itemCategory" VARCHAR(17) DEFAULT 'MISC',
    "buyPrice" INTEGER DEFAULT 0,
    "sellPrice" INTEGER DEFAULT 0,
    "isUsable" BOOLEAN NOT NULL DEFAULT FALSE,
    "isEquipable" BOOLEAN NOT NULL DEFAULT FALSE,
    "numUses" INTEGER DEFAULT NULL,
    PRIMARY KEY (id)
);
INSERT INTO Item VALUES(1,'Lum Berry','The Lum Berry is a green berry that resembles a plum. It is known for its well-balanced flavor and is often described as having a smooth, shiny appearance.','When eaten by a Pokemon, it gets cured of any non-volatile status conditions. Activates automatically when active in Held Item slot.','CURE_STATUS','{"statuses": "all_non_volatile"}','COMMON','HEALING_ITEM',25,15,1,1,1);
INSERT INTO Item VALUES(2,'Shiny Stone','An elliptical-shaped stone that is transparent with a ball of light inside it. It is known for its dazzling shine.','Its used to evolve certain Pokemon.','evolve_pokemon','{}','ELITE','EVOLUTION_ITEM',10000,7500,0,0,NULL);
INSERT INTO Item VALUES(3,'Blast Seed','A small, round seed with a distinct explosive design, often illustrated with fiery colors to indicate its explosive nature.','When eaten the user suddenly sneezes a breath of fire. Foes do not have time to react','deal_typed_damage','{"type": "FIRE", "damage": 1}','COMMON','MISC',50,30,1,0,1);
INSERT INTO Item VALUES(4,'Cherri Berry','A bright red berry that blooms with delicate, pretty flowers. It is known for its spicy flavor.','When eaten by a Pokemon, gets cured of Paralysis if it is afflicted with it.','cure_status','{"statuses": ["PARALYSIS"]}','BASIC','HEALING_ITEM',30,20,1,1,1);
INSERT INTO Item VALUES(5,'Hyper Potion','A pink spray bottle','It is used to restore a Pokémon''s health during battles or outside of them.','heal_pool','{"maxPool": 14, "usedUnits": 0}','EXPERT','HEALING_ITEM',1200,900,1,0,1);
INSERT INTO Item VALUES(6,'Razz Berry','Resembles a raspberry, featuring a red color and a slightly spicy taste. It has a firm texture and is known for its dry center, making it distinct.','When eaten, restores the users Health by 1/3 of its Maximum Health.','heal_static','{"amount": 1}','ELITE','HEALING_ITEM',900,600,1,0,1);
INSERT INTO Item VALUES(7,'Nanab Berry','A pink berry that is round and has a very hard texture. It is known for its sweet flavor and is often used in Pokémon games for various purposes, including calming wild Pokémon.','When given to an enemy, it calms them down a bit.','use_item','{}','BASIC','MISC',30,20,1,0,1);
INSERT INTO Item VALUES(8,'Magost Berry','A pink berry that is known for its finely balanced flavor and dreamy sweetness, making it a favorite among Pokémon. It is typically used in cooking and as an ingredient for making Pokéblocks and Poffins.','Not Yet Thought of Anything','','{}','BASIC','MISC',30,20,0,0,0);
INSERT INTO Item VALUES(9,'Hondew Berry','A green berry that resembles a honeydew melon, with a firm texture and a somewhat unusual taste. It is known for its rarity and is often associated with luxury, making it a favored gift item in the Pokémon world.','A Berry which is usually given to those they deem as friends.','use_item','{}','BASIC','MISC',30,20,1,0,1);
INSERT INTO Item VALUES(10,'Sleep Seed','If you throw it at an enemy and hit them, it can make them Sleep for a little while. Be careful not to use it on your teammates.','Make a Dexteriy + Fight + Channel roll to shoot these seeds into your foe''s mouth.','apply_status','{"status": "ASLEEP"}','BASIC','MISC',75,50,1,0,1);
INSERT INTO Item VALUES(11,'Stun Seed','Small, round seeds that typically have a bright yellow color, resembling a small ball. When used, they emit a sparkling effect to indicate their stunning ability on the target Pokémon.','Make a Dexterity + Fight + Channel roll to shoot these seeds into the foe''s mouth.','apply_status','{"status": "PARALYZED"}','BASIC','MISC',75,50,1,0,1);
INSERT INTO Item VALUES(12,'All-Hit Orb','As it explodes, the visibility around gets clear, no light, darkness or fog impedes your team to strike directly.',NULL,'default','{}','EXPERT','MISC',150,100,1,0,1);
INSERT INTO Item VALUES(13,'Rindo Berry','a green berry that has a medium chance of producing a Pokéblock. It has a soft texture and a disagreeable green flavor typical of vegetables, often described as having a bitter taste with a subtle spiciness.',NULL,'default','{}','COMMON','HELD_ITEM',50,35,1,1,1);
CREATE TABLE IF NOT EXISTS "Garment" (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	description TEXT, 
	effect TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS "AccuracyModifierGroup" (
	id INTEGER NOT NULL, 
	"accuracyModifier1" VARCHAR(10) NOT NULL, 
	"accuracyModifier2" VARCHAR(10), 
	"accuracyModifier3" VARCHAR(10), 
	PRIMARY KEY (id)
);
INSERT INTO AccuracyModifierGroup VALUES(1,'Dexterity','Fight','Channel');
INSERT INTO AccuracyModifierGroup VALUES(2,'Tough_Cute','Contest','Perform');
INSERT INTO AccuracyModifierGroup VALUES(3,'Dexterity','Fight','Brawl');
INSERT INTO AccuracyModifierGroup VALUES(4,'Tough','Contest','Intimidate');
INSERT INTO AccuracyModifierGroup VALUES(5,'Dexterity','Fight','Brawl');
INSERT INTO AccuracyModifierGroup VALUES(6,'Insight','Survival','ALERT');
INSERT INTO AccuracyModifierGroup VALUES(7,'Will','NONE','NONE');
INSERT INTO AccuracyModifierGroup VALUES(8,'Dexterity','Fight','Brawl');
INSERT INTO AccuracyModifierGroup VALUES(9,'Dexterity','Fight','Channel');
CREATE TABLE IF NOT EXISTS "DamageModifierGroup" (
	id INTEGER NOT NULL, 
	"damageModifier1" VARCHAR(10) NOT NULL, 
	"damageModifier2" VARCHAR(10), 
	"damageModifier3" VARCHAR(10), 
	PRIMARY KEY (id)
);
INSERT INTO DamageModifierGroup VALUES(1,'Special','NONE','NONE');
INSERT INTO DamageModifierGroup VALUES(2,'NONE','NONE','NONE');
INSERT INTO DamageModifierGroup VALUES(3,'Strength','NONE','NONE');
INSERT INTO DamageModifierGroup VALUES(4,'NONE','NONE','NONE');
INSERT INTO DamageModifierGroup VALUES(5,'Strength','NONE','NONE');
INSERT INTO DamageModifierGroup VALUES(6,'NONE','NONE','NONE');
INSERT INTO DamageModifierGroup VALUES(7,'NONE','NONE','NONE');
INSERT INTO DamageModifierGroup VALUES(8,'Strength','NONE','NONE');
INSERT INTO DamageModifierGroup VALUES(9,'Special','NONE','NONE');
CREATE TABLE IF NOT EXISTS "HealMove" (
	id INTEGER NOT NULL, 
	"healType" VARCHAR(11), 
	"healAmount" INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS "MoveEffect" (
	id INTEGER NOT NULL, 
	effect VARCHAR(18) NOT NULL, 
	"effectLevel" VARCHAR(2) NOT NULL, 
	"effectLevelDice" INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS "GamePokemon" (
	id INTEGER NOT NULL, 
	"basePokemonId" INTEGER, 
	name VARCHAR NOT NULL, 
	level INTEGER NOT NULL, 
	gender VARCHAR, 
	age INTEGER NOT NULL, 
	apples INTEGER NOT NULL, 
	"primaryType" VARCHAR(8), 
	"secondaryType" VARCHAR(8), 
	"natureId" INTEGER, 
	"abilityId" INTEGER, 
	status VARCHAR, 
	"baseHealth" INTEGER NOT NULL, 
	health INTEGER NOT NULL, 
	lethalHealth INTEGER NOT NULL,
	will INTEGER NOT NULL, 
	logic INTEGER, 
	instinct INTEGER, 
	primal INTEGER, 
	"itemId" INTEGER, 
	strength INTEGER NOT NULL, 
	"strengthPotential" INTEGER NOT NULL, 
	dexterity INTEGER NOT NULL, 
	"dexterityPotential" INTEGER NOT NULL, 
	vitality INTEGER NOT NULL, 
	"vitalityPotential" INTEGER NOT NULL, 
	special INTEGER NOT NULL, 
	"specialPotential" INTEGER NOT NULL, 
	insight INTEGER NOT NULL, 
	"insightPotential" INTEGER NOT NULL, 
	fight INTEGER NOT NULL, 
	survival INTEGER NOT NULL, 
	contest INTEGER NOT NULL, 
	brawl INTEGER NOT NULL, 
	channel INTEGER NOT NULL, 
	clash INTEGER NOT NULL, 
	evasion INTEGER NOT NULL, 
	alert INTEGER NOT NULL, 
	athletic INTEGER NOT NULL, 
	"natureStat" INTEGER NOT NULL, 
	stealth INTEGER NOT NULL, 
	allure INTEGER NOT NULL, 
	etiquette INTEGER NOT NULL, 
	intimidate INTEGER NOT NULL, 
	perform INTEGER NOT NULL, 
	"experiencePoints" INTEGER NOT NULL, 
	"isNpc" BOOLEAN NOT NULL, 
	"playerColor" VARCHAR(20) NOT NULL, 
	"Guid" VARCHAR(6) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("basePokemonId") REFERENCES "BasePokemon" (id), 
	FOREIGN KEY("natureId") REFERENCES "Nature" (id), 
	FOREIGN KEY("abilityId") REFERENCES "Ability" (id), 
	FOREIGN KEY("itemId") REFERENCES "Item" (id), 
	UNIQUE ("Guid")
);
INSERT INTO GamePokemon VALUES(1,1,'Airalin',2,'Female',21,50,'PSYCHIC','FAIRY',2,1,'Healthy',3,3,0,6,1,2,0,NULL,1,3,1,3,1,3,2,4,1,3,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,60,0,'Black','09c38c');
INSERT INTO GamePokemon VALUES(2,2,'Ja-Bo',10,'Male',22,0,'DRAGON',NULL,1,3,'Healthy',3,1,0,4,1,2,0,NULL,3,4,2,4,3,4,2,4,2,4,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,'Blue','b513fb');
INSERT INTO GamePokemon VALUES(3,3,'Cyan',12,'Female',20,45,'FIGHTING',NULL,3,4,'Healthy',3,1,0,3,2,1,0,NULL,3,5,2,4,2,3,1,3,2,3,2,3,0,0,0,0,0,0,1,0,0,0,0,0,0,4,0,'Orange','d63f99');
INSERT INTO GamePokemon VALUES(4,4,'Pluey',5,'Male',3,0,'WATER',NULL,4,2,'Healthy',3,2,0,6,1,2,0,NULL,2,4,1,3,2,4,2,4,2,4,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,25,0,'Purple','a28d51');
INSERT INTO GamePokemon VALUES(5,6,'Nickit',1,'None',0,0,'DARK',NULL,NULL,NULL,'Fainted',3,0,0,3,1,1,0,NULL,1,3,2,4,1,3,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,'None','123se2');
INSERT INTO GamePokemon VALUES(6,5,'Gabite',1,'None',0,0,'DRAGON','GROUND',NULL,NULL,'Fainted',4,0,0,3,1,1,0,NULL,2,5,2,5,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,'None','133se2');
INSERT INTO GamePokemon VALUES(7,7,'Palkia',1,'None',0,0,'WATER','DRAGON',NULL,NULL,'Healthy',5,8,0,3,1,1,0,NULL,7,10,6,10,6,10,8,10,7,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,'None','1sf304');
INSERT INTO GamePokemon VALUES(8,8,'Dialga',1,'None',0,0,'STEEL','DRAGON',NULL,NULL,'Healthy',7,6,0,3,1,1,0,NULL,7,10,5,10,7,10,8,10,6,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,'None','1sf305');
CREATE TABLE IF NOT EXISTS "Game" (
	id INTEGER NOT NULL, 
	"gameId" VARCHAR(10) NOT NULL, 
	weather VARCHAR(20) NOT NULL, 
	"shopActive" BOOLEAN NOT NULL, 
	"activeShopTier" VARCHAR(9) NOT NULL, 
	"userId" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE ("userId"), 
	FOREIGN KEY("userId") REFERENCES "User" (id)
);
INSERT INTO Game VALUES(1,'cm7m1srjp2','None',1,'BASIC',1);
CREATE TABLE IF NOT EXISTS "Move" (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	type VARCHAR(8) NOT NULL, 
	"effectText" TEXT, 
	"flavorText" TEXT, 
	"damageType" VARCHAR(8) NOT NULL, 
	"basePower" INTEGER, 
	priority VARCHAR(2), 
	target VARCHAR(21), 
    "moveRangeType" VARCHAR(17), 
	"moveGridRange" INTEGER,
	"accuracyModifiersId" INTEGER, 
	"damageModifiersId" INTEGER, 
	"reducedAccuracy" INTEGER, 
	"hasCritical" BOOLEAN NOT NULL, 
	"hasLethal" BOOLEAN NOT NULL, 
	"hasBlock" BOOLEAN NOT NULL, 
	"hasRecoil" BOOLEAN NOT NULL, 
	"hasWeatherChange" BOOLEAN NOT NULL, 
	"hasModifiedDamage" BOOLEAN NOT NULL, 
	"modifiedDamageId" INTEGER, 
	"weatherChangeTo" VARCHAR(9), 
	"alwaysHitEffect" BOOLEAN NOT NULL, 
	"alwaysFailEffect" BOOLEAN NOT NULL, 
	"isChargeMove" BOOLEAN NOT NULL, 
	"isFistBased" BOOLEAN NOT NULL, 
	"isHighCrit" BOOLEAN NOT NULL, 
	"isNeverFail" BOOLEAN NOT NULL, 
	"isHealingMove" BOOLEAN NOT NULL, 
	"isShieldMove" BOOLEAN NOT NULL, 
	"isSoundBased" BOOLEAN NOT NULL, 
	"isMultiHit" BOOLEAN NOT NULL, 
	"isSwitchMove" BOOLEAN NOT NULL, 
	"multiHitCount" VARCHAR(4), 
	"healingTypeId" INTEGER, 
	"requiresRecharge" BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("accuracyModifiersId") REFERENCES "AccuracyModifierGroup" (id), 
	FOREIGN KEY("damageModifiersId") REFERENCES "DamageModifierGroup" (id), 
	FOREIGN KEY("modifiedDamageId") REFERENCES "DamageModifierGroup" (id), 
	FOREIGN KEY("healingTypeId") REFERENCES "HealMove" (id)
);
INSERT INTO Move VALUES(1,'Confusion','PSYCHIC','Roll 1 Chance Dice to Confuse the foe','The target''s mind is hit by a weak psychic force that leaves them wondering if they were hit by an invisible enemy. Sometimes the foe is left seeing things that aren''t really there.','Special',2,'n0','SingleEnemy','RANGED_OR_SPECIAL',NULL,1,1,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(2,'Growl','NORMAL','Reduce the foe''s Strength.','Either by a menacing attitude or cute demeanor, the foe will be unsure about attacking the user with full force.','Support',0,'n0','AllEnemyInRange','ALL_IN_RANGE',2,2,2,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(3,'Tackle','NORMAL','','A basic attack that consists of charging at an enemy.','Physical',2,'n0','SingleEnemy','ADJACENT',2,3,3,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(4,'Leer','NORMAL','Recude the Defense of those affected.','A vicious glare that will make any opponent doubt its own strength in battle.','Support',0,'n0','AllEnemyInRange','ALL_IN_RANGE',2,4,4,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(5,'Quick Attack','NORMAL','Double the Pokemon''s movement speed.','An attack as fast as lightning','Physical',2,'p1','SingleEnemy','TARGET_IN_AREA',2,5,5,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(6,'Foresight','NORMAL','Ignore any increase in the foe''s Evasion. User''s Normal and Fighting Moves can affect Ghost Types and Ghost Moves can affect Normal Types','The Pokemon uses its developed senses and mental ability to forsee the immediate future','Support',0,'n0','SingleEnemy','TARGET_IN_AREA',2,6,6,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(7,'Endure','NORMAL','The user cannot be reduced to less than 1 Health by the next attack. Status ailments, recoil, or self inflicted damage will still affect it.','The user gets prepared to recieve a fatal blow. It resists the pain despite being seriously hurt.','Support',0,'p5','User',NULL,NULL,7,7,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,1,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(8,'Pound','NORMAL','','A decent hit to smash the foe','Physical',2,'n0','SingleEnemy','ADJACENT',1,8,8,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(9,'Bubble','WATER','Roll 1 Chance Dice to Reduce the foe''s Dexterity.','A spray of bubbles flies around the enemies, some of the bubbles stick to their bodies, hindering their movement.','Special',2,'n0','AllEnemyInRange','ALL_IN_RANGE',2,9,9,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
CREATE TABLE pokemon_garments (
	pokemon_id INTEGER NOT NULL, 
	garment_id INTEGER NOT NULL, 
	PRIMARY KEY (pokemon_id, garment_id), 
	FOREIGN KEY(pokemon_id) REFERENCES "GamePokemon" (id), 
	FOREIGN KEY(garment_id) REFERENCES "Garment" (id)
);
CREATE TABLE IF NOT EXISTS "BasePokemonLearnableMove" (
	id INTEGER NOT NULL, 
	"basePokemonId" INTEGER NOT NULL, 
	"moveId" INTEGER NOT NULL, 
	"unlockXpCost" INTEGER, 
	PRIMARY KEY (id), 
	CONSTRAINT uq_basepokemon_move_learn UNIQUE ("basePokemonId", "moveId", "unlockXpCost"), 
	FOREIGN KEY("basePokemonId") REFERENCES "BasePokemon" (id), 
	FOREIGN KEY("moveId") REFERENCES "Move" (id)
);
CREATE TABLE IF NOT EXISTS "GamePokemonUnlockedMove" (
	id INTEGER NOT NULL, 
	"pokemonId" INTEGER NOT NULL, 
	"moveId" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CONSTRAINT uq_pokemon_unlocked_move UNIQUE ("pokemonId", "moveId"), 
	FOREIGN KEY("pokemonId") REFERENCES "GamePokemon" (id), 
	FOREIGN KEY("moveId") REFERENCES "Move" (id)
);
CREATE TABLE IF NOT EXISTS "GameEntities" (
	id INTEGER NOT NULL, 
	"gameId" INTEGER NOT NULL, 
	"pokemonId" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("gameId") REFERENCES "Game" (id), 
	FOREIGN KEY("pokemonId") REFERENCES "GamePokemon" (id)
);
INSERT INTO GameEntities VALUES(1,1,1);
INSERT INTO GameEntities VALUES(2,1,2);
INSERT INTO GameEntities VALUES(3,1,3);
INSERT INTO GameEntities VALUES(4,1,4);
INSERT INTO GameEntities VALUES(5,1,5);
INSERT INTO GameEntities VALUES(6,1,6);
INSERT INTO GameEntities VALUES(7,1,7);
INSERT INTO GameEntities VALUES(8,1,8);
CREATE TABLE IF NOT EXISTS "PokemonBag" (
	id INTEGER NOT NULL, 
	"bagSize" VARCHAR(6) NOT NULL, 
	"pokemonId" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("pokemonId") REFERENCES "GamePokemon" (id)
);
INSERT INTO PokemonBag VALUES(1,'size5',1);
INSERT INTO PokemonBag VALUES(2,'size5',2);
INSERT INTO PokemonBag VALUES(3,'size5',3);
INSERT INTO PokemonBag VALUES(4,'size5',4);
INSERT INTO PokemonBag VALUES(5,'size5',5);
INSERT INTO PokemonBag VALUES(6,'size5',6);
INSERT INTO PokemonBag VALUES(7,'size5',7);
INSERT INTO PokemonBag VALUES(8,'size5',8);
CREATE TABLE IF NOT EXISTS "MoveEffectConnection" (
	id INTEGER NOT NULL, 
	"moveId" INTEGER NOT NULL, 
	"moveEffectId" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CONSTRAINT uq_move_moveeffect UNIQUE ("moveId", "moveEffectId"), 
	FOREIGN KEY("moveId") REFERENCES "Move" (id), 
	FOREIGN KEY("moveEffectId") REFERENCES "MoveEffect" (id)
);
CREATE TABLE IF NOT EXISTS "MoveConnection" (
	id INTEGER NOT NULL, 
	"pokemonId" INTEGER NOT NULL, 
	"moveId" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CONSTRAINT uq_pokemon_move UNIQUE ("pokemonId", "moveId"), 
	FOREIGN KEY("pokemonId") REFERENCES "GamePokemon" (id), 
	FOREIGN KEY("moveId") REFERENCES "Move" (id)
);
INSERT INTO MoveConnection VALUES(1,1,1);
INSERT INTO MoveConnection VALUES(2,1,2);
INSERT INTO MoveConnection VALUES(3,2,3);
INSERT INTO MoveConnection VALUES(4,2,4);
INSERT INTO MoveConnection VALUES(5,3,5);
INSERT INTO MoveConnection VALUES(6,3,7);
INSERT INTO MoveConnection VALUES(7,3,6);
INSERT INTO MoveConnection VALUES(8,4,9);
INSERT INTO MoveConnection VALUES(9,4,8);
INSERT INTO MoveConnection VALUES(10,5,5);
INSERT INTO MoveConnection VALUES(11,6,3);
CREATE TABLE IF NOT EXISTS "BagItem" (
	id INTEGER NOT NULL, 
	"itemId" INTEGER NOT NULL, 
	"bagId" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("itemId") REFERENCES "Item" (id), 
	FOREIGN KEY("bagId") REFERENCES "PokemonBag" (id)
);
INSERT INTO BagItem VALUES(2,2,1);
INSERT INTO BagItem VALUES(3,3,1);
INSERT INTO BagItem VALUES(4,4,2);
INSERT INTO BagItem VALUES(5,5,3);
INSERT INTO BagItem VALUES(7,9,2);
INSERT INTO BagItem VALUES(10,10,4);
INSERT INTO BagItem VALUES(13,12,3);
INSERT INTO BagItem VALUES(14,13,4);
INSERT INTO BagItem VALUES(15,1,1);
COMMIT;
