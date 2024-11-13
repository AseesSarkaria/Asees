WITH tag_extraction AS (
	SELECT 
		film.film_id AS id,
		film.title,
		unnest(tsvector_to_array(film.fulltext)) AS tag_entry
	FROM film
), parsed_tags AS (
 	SELECT tag_extraction.id,
		tag_extraction.title,
		split_part(tag_extraction.tag_entry, ':', 1) AS tag
	FROM tag_extraction
)
SELECT parsed_tags.tag,
	array_length(array_agg(parsed_tags.id), 1) AS num_movies_with_tag,
	array_agg(parsed_tags.title) AS movies_with_tag,
	array_agg(parsed_tags.id) AS film_id_array
FROM parsed_tags
GROUP BY tag
ORDER BY tag


---top 5 rows--
"tag"	"num_movies_with_tag"	"movies_with_tag"	"film_id_array"
"abandon"	111	"{""Borrowers Bedazzled"",""Sling Luke"",""Groove Fiction"",""Argonauts Town"",""Durham Panky"",""Apocalypse Flamingos"",""Hurricane Affair"",""Mission Zoolander"",""Driving Polish"",""Strangelove Desire"",""Runaway Tenenbaums"",""Fireball Philadelphia"",""Dances None"",""Annie Identity"",""Frontier Cabin"",""Drums Dynamite"",""Packer Madigan"",""Gump Date"",""Frida Slipper"",""Treatment Jekyll"",""Dude Blindness"",""Anything Savannah"",""Comforts Rush"",""Attacks Hate"",""Trip Newton"",""Story Side"",""Hunting Musketeers"",""Sense Greek"",""Velvet Terminator"",""Baby Hall"",""Love Suicides"",""Nightmare Chill"",""Heavyweights Beast"",""Crowds Telemark"",""Beauty Grease"",""Clueless Bucket"",""Town Ark"",""Anthem Luke"",""Empire Malkovich"",""Breaking Home"",""Neighbors Charade"",""Conquerer Nuts"",""Wedding Apollo"",""Nash Chocolat"",""Illusion Amelie"",""Siege Madre"",""Hunger Roof"",""Haunting Pianist"",""Language Cowboy"",""Crooked Frogmen"",""Conspiracy Spirit"",""Bed Highball"",""Sugar Wonka"",""Motions Details"",""Apollo Teen"",""Barefoot Manchurian"",""Untouchables Sunrise"",""Party Knock"",""Spice Sorority"",""Lolita World"",""Jaws Harry"",""Bedazzled Married"",""Leathernecks Dwarfs"",""Alone Trip"",""Purple Movie"",""Moulin Wake"",""Armageddon Lost"",""Commandments Express"",""Elf Murder"",""Strictly Scarface"",""Shawshank Bubble"",""Blues Instinct"",""Crusade Honey"",""Villain Desperate"",""World Leathernecks"",""Grail Frankenstein"",""Cupboard Sinners"",""Rage Games"",""Thief Pelican"",""Uptown Young"",""Dazed Punk"",""Saddle Antitrust"",""Tadpole Park"",""Voyage Legally"",""Shanghai Tycoon"",""Indian Love"",""Egypt Tenenbaums"",""Island Exorcist"",""Flatliners Killer"",""Undefeated Dalmations"",""Candles Grapes"",""Dracula Crystal"",""Superfly Trip"",""Sun Confessions"",""Sinners Atlantis"",""Ishtar Rocketeer"",""South Wait"",""Bang Kwai"",""Divine Resurrection"",""Pilot Hoosiers"",""Texas Watch"",""Rules Human"",""Peak Forever"",""Fiction Christmas"",""Wind Phantom"",""Walls Artist"",""Masked Bubble"",""Driver Annie"",""Killer Innocent"",""Scorpion Apollo"",""Sky Miracle""}"	{89,808,383,36,263,32,443,583,255,852,751,317,205,26,340,258,651,386,337,910,260,30,169,44,911,850,442,779,938,47,535,624,412,195,61,162,900,28,280,96,619,179,966,615,452,795,440,406,509,191,180,62,859,600,33,56,926,660,827,528,478,63,513,17,705,601,39,171,278,857,785,83,197,943,990,375,199,710,887,928,217,756,874,951,784,458,275,471,322,922,117,249,868,863,800,470,823,53,236,679,885,749,668,311,976,955,562,254,498,771,802}
"academi"	2	"{""Victory Academy"",""Academy Dinosaur""}"	{940,1}
"ace"	3	"{""Million Ace"",""Dirty Ace"",""Ace Goldfinger""}"	{578,232,2}
"action"	44	"{""Dorado Notting"",""Highball Potter"",""Happiness United"",""Newsies Story"",""Hedwig Alter"",""Lord Arizona"",""Pluto Oleander"",""Factory Dragon"",""Ali Forever"",""Hawk Chill"",""Pinocchio Simon"",""Elf Murder"",""Hanging Deep"",""Matrix Snowman"",""Holy Tadpole"",""Rainbow Shock"",""Floats Garden"",""Wardrobe Phantom"",""Apollo Teen"",""Secretary Rouge"",""Tequila Past"",""Words Hunter"",""Worker Tarzan"",""King Evolution"",""Temple Attraction"",""Peach Innocent"",""Telemark Heartbreakers"",""Interview Liaisons"",""Driving Polish"",""Christmas Moonshine"",""Varsity Trip"",""Shane Darkness"",""Informer Double"",""Dazed Punk"",""Chocolat Harry"",""Arachnophobia Rollercoaster"",""Gorgeous Bingo"",""Charade Duffel"",""Reef Salute"",""Super Wyoming"",""Aladdin Calendar"",""Dirty Ace"",""Dinosaur Secretary"",""Wedding Apollo""}"	{244,416,399,622,413,530,686,299,13,407,680,278,396,565,425,713,325,958,33,777,883,987,988,499,881,667,880,465,255,149,937,783,459,217,147,35,370,137,722,867,10,232,231,966}
"action-pack"	44	"{""Driving Polish"",""Matrix Snowman"",""Informer Double"",""Varsity Trip"",""Dazed Punk"",""Pinocchio Simon"",""Secretary Rouge"",""Wardrobe Phantom"",""Lord Arizona"",""Factory Dragon"",""Christmas Moonshine"",""Gorgeous Bingo"",""Interview Liaisons"",""Holy Tadpole"",""Aladdin Calendar"",""Rainbow Shock"",""Reef Salute"",""Hanging Deep"",""Charade Duffel"",""Hawk Chill"",""Worker Tarzan"",""Chocolat Harry"",""Hedwig Alter"",""Wedding Apollo"",""Dinosaur Secretary"",""Ali Forever"",""Super Wyoming"",""Dirty Ace"",""Temple Attraction"",""Telemark Heartbreakers"",""King Evolution"",""Apollo Teen"",""Dorado Notting"",""Newsies Story"",""Shane Darkness"",""Highball Potter"",""Elf Murder"",""Happiness United"",""Arachnophobia Rollercoaster"",""Words Hunter"",""Tequila Past"",""Peach Innocent"",""Pluto Oleander"",""Floats Garden""}"	{255,565,459,937,217,680,777,958,530,299,149,370,465,425,10,713,722,396,137,407,988,147,413,966,231,13,867,232,881,880,499,33,244,622,783,416,278,399,35,987,883,667,686,325}
