PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "BasePokemon" (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
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
INSERT INTO BasePokemon VALUES(1,'Ralts',3,3,1,1,0,'PSYCHIC',NULL,1,3,1,3,1,3,2,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(2,'Jangmo-o',3,3,1,1,0,'DRAGON',NULL,2,4,2,4,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(3,'Riolu',3,3,1,1,0,'FIGHTING',NULL,2,5,2,4,1,3,1,3,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
INSERT INTO BasePokemon VALUES(4,'Piplup',3,3,1,1,0,'WATER',NULL,2,4,1,3,2,4,2,4,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
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
INSERT INTO Item VALUES (
    1,
    'Lum Berry',
    'The Lum Berry is a green berry that resembles a plum. It is known for its well-balanced flavor and is often described as having a smooth, shiny appearance.',
    'When eaten by a Pokemon, it gets cured of any non-volatile status conditions. Activates automatically when active in Held Item slot.',
    'CURE_STATUS',
    '{"statuses": "all_non_volatile"}',
    'COMMON',
    'HEALING_ITEM',
    25,
    15,
    TRUE,
    FALSE,
    1
);

INSERT INTO Item VALUES (
    2,
    'Shiny Stone',
    'An elliptical-shaped stone that is transparent with a ball of light inside it. It is known for its dazzling shine.',
    'Its used to evolve certain Pokemon.',
    'evolve_pokemon',
    '{}',
    'ELITE',
    'EVOLUTION_ITEM',
    10000,
    7500,
    FALSE,
    FALSE,
    NULL
);

INSERT INTO Item VALUES (
    3,
    'Blast Seed',
    'A small, round seed with a distinct explosive design, often illustrated with fiery colors to indicate its explosive nature.',
    'When eaten the user suddenly sneezes a breath of fire. Foes do not have time to react',
    'deal_typed_damage',
    '{"type": "FIRE", "damage": 1}',
    'COMMON',
    'MISC',
    50,
    30,
    TRUE,
    FALSE,
    1
);

INSERT INTO Item VALUES (
    4,
    'Cherri Berry',
    'A bright red berry that blooms with delicate, pretty flowers. It is known for its spicy flavor.',
    'When eaten by a Pokemon, gets cured of Paralysis if it is afflicted with it.',
    'cure_status',
    '{"statuses": ["PARALYSIS"]}',
    'BASIC',
    'HEALING_ITEM',
    30,
    20,
    TRUE,
    FALSE,
    1
);

INSERT INTO Item VALUES (
    5,
    'Hyper Potion',
    'A pink spray bottle',
    'It is used to restore a Pokémon''s health during battles or outside of them.',
    'heal_pool',
    '{"maxPool": 14, "usedUnits": 0}',
    'EXPERT',
    'HEALING_ITEM',
    1200,
    900,
    TRUE,
    FALSE,
    1
);

INSERT INTO Item VALUES (
    6,
    'Razz Berry',
    'Resembles a raspberry, featuring a red color and a slightly spicy taste. It has a firm texture and is known for its dry center, making it distinct.',
    'When eaten, restores the users Health by 1/3 of its Maximum Health.',
    'heal_static',
    '{"amount": 1}',
    'ELITE',
    'HEALING_ITEM',
    900,
    600,
    TRUE,
    FALSE,
    1
);
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
INSERT INTO GamePokemon VALUES(1,1,'Airalin',2,'Female',21,0,'PSYCHIC',NULL,2,1,'Healthy',3,4,0,6,1,2,0,NULL,1,3,1,3,1,3,2,4,1,3,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,38,0,'Black','09c38c');
INSERT INTO GamePokemon VALUES(2,2,'Ja-Bo',5,'Male',22,0,'DRAGON',NULL,1,3,'Healthy',3,5,0,4,1,2,0,NULL,3,4,2,4,2,4,2,4,2,4,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,13,0,'Blue','b513fb');
INSERT INTO GamePokemon VALUES(3,3,'Cyan',6,'Female',20,45,'FIGHTING',NULL,3,4,'Healthy',3,4,0,3,2,1,0,NULL,2,5,2,4,1,3,1,3,2,3,2,3,0,0,0,0,0,0,1,0,0,0,0,0,0,12,0,'Orange','d63f99');
INSERT INTO GamePokemon VALUES(4,4,'Pluey',2,'Male',3,0,'WATER',NULL,4,2,'Healthy',3,5,0,6,1,2,0,NULL,2,4,1,3,2,4,2,4,2,4,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,17,0,'Purple','a28d51');
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
INSERT INTO Game VALUES(1,'cm7m1srjp2','None',0,'BASIC',1);
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
INSERT INTO Move VALUES(1,'Confusion','PSYCHIC','Roll 1 Chance Dice to Confuse the foe','The target''s mind is hit by a weak psychic force that leaves them wondering if they were hit by an invisible enemy. Sometimes the foe is left seeing things that aren''t really there.','Special',2,'n0','SingleEnemy',1,1,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(2,'Growl','NORMAL','Reduce the foe''s Strength.','Either by a menacing attitude or cute demeanor, the foe will be unsure about attacking the user with full force.','Support',0,'n0','AllEnemyInRange',2,2,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(3,'Tackle','NORMAL','','A basic attack that consists of charging at an enemy.','Physical',2,'n0','SingleEnemy',3,3,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(4,'Leer','NORMAL','Recude the Defense of those affected.','A vicious glare that will make any opponent doubt its own strength in battle.','Support',0,'n0','AllEnemyInRange',4,4,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(5,'Quick Attack','NORMAL','Double the Pokemon''s movement speed.','An attack as fast as lightning','Physical',2,'p1','SingleEnemy',5,5,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(6,'Foresight','NORMAL','Ignore any increase in the foe''s Evasion. User''s Normal and Fighting Moves can affect Ghost Types and Ghost Moves can affect Normal Types','The Pokemon uses its developed senses and mental ability to forsee the immediate future','Support',0,'n0','SingleEnemy',6,6,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(7,'Endure','NORMAL','The user cannot be reduced to less than 1 Health by the next attack. Status ailments, recoil, or self inflicted damage will still affect it.','The user gets prepared to recieve a fatal blow. It resists the pain despite being seriously hurt.','Support',0,'p5','User',7,7,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,1,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(8,'Pound','NORMAL','','A decent hit to smash the foe','Physical',2,'n0','SingleEnemy',8,8,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
INSERT INTO Move VALUES(9,'Bubble','WATER','Roll 1 Chance Dice to Reduce the foe''s Dexterity.','A spray of bubbles flies around the enemies, some of the bubbles stick to their bodies, hindering their movement.','Special',2,'n0','AllEnemyInRange',9,9,0,0,0,0,0,0,0,NULL,NULL,0,0,0,0,0,0,0,0,0,0,0,'ONE',NULL,0);
CREATE TABLE IF NOT EXISTS pokemon_garments (
	pokemon_id INTEGER NOT NULL, 
	garment_id INTEGER NOT NULL, 
	PRIMARY KEY (pokemon_id, garment_id), 
	FOREIGN KEY(pokemon_id) REFERENCES "GamePokemon" (id), 
	FOREIGN KEY(garment_id) REFERENCES "Garment" (id)
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
CREATE TABLE IF NOT EXISTS "BagItem" (
	id INTEGER NOT NULL, 
	"itemId" INTEGER NOT NULL, 
	"bagId" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("itemId") REFERENCES "Item" (id), 
	FOREIGN KEY("bagId") REFERENCES "PokemonBag" (id)
);
INSERT INTO BagItem VALUES(1,1,1);
INSERT INTO BagItem VALUES(2,2,1);
INSERT INTO BagItem VALUES(3,3,1);
INSERT INTO BagItem VALUES(4,4,2);
INSERT INTO BagItem VALUES(5,5,3);
INSERT INTO BagItem VALUES(6,6,3);
COMMIT;
