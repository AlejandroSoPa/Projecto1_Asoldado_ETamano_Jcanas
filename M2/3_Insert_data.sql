start transaction;


INSERT ignore INTO USER (username,password,usercreate,datecreated)
VALUES ('TestUser', 'TestPassword', current_user() , current_timestamp());


savepoint users;


INSERT ignore INTO PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Dae´mon', 
'Es un orco que desde pequeño fue entrenado para la guerra de las cuatro naciones (elfos, humanos, gnomos y orcos). Fue un guerrero muy reconocido por su habilidad con las espadas grandes hasta que en una de esas batallas fue herido de gravedad. Antes de morir fue salvado por una humana y lo escondió en el mundo humano. Él le juro lealtad por salvarle la vida y ahora está aprendiendo como es una vida pacifica mientras intenta pasar desapercibido.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Ana María',
'Es una humana adolescente que estudia una doble carrera de filosofía con derecho en la mejor universidad, siendo ella la mejor estudiante dando le el apodo de “NUMBER ONE”. Sabiendo esto se hizo tradición que en cualquier caso con figuras 	importantes ella estuviera presente aunque ella estuviera todavía en su segundo año de estudio.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Belfegor',
'Es un demonio de alto rango que abandono el infierno por las responsabilidades que tenía que cumplir. Al ser tan perezoso decidió dejar el infierno y vivir en un piso en el centro de una gran ciudad. Gracias a un teléfono que encontró tirado en el suelo no sale de su casa y pide todo lo que necesite. Ademas se intereso en la cultura japonesa: Anime y Manga (Demonio Otaku).',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Mushu',
'Es el username de un adolescente en un nuevo MMORPG, él no ha jugado nunca uno así que tuvo la brillante idea de poner los 100 puntos, que te dan al hacer a tu personaje, en el atributo fuerza. Como no quería perder ningún combate, antes de 	equiparse ningún atuendo (desnudo), se pasó 36 horas golpeando un objeto de práctica para subir su estadística lo máximo que pueda. Cuando llego a 500 destruyo el objeto de un solo golpe. Desde ese momento se le conoce como el “Pervertido mas fuerte” ya que solo necesita un solo golpe para debilitar a cualquier personaje.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Jared',
'Jared es un hombre ciego de mediana edad. Es católico, pobre y... nazi! Lleva años intentando unirse a los grupos neonazis pero nunca le aceptan. Por ese motivo él siempre se queja diciendo que ellos no son nazis de verdad o que no tienen la pureza de la raza aria o que el defenderia a Hitler con su propia vida. Jared no ve porque no le aceptan. Jared es negro.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Aegea',
'Aegea es una mujer que vive en una pequeña casa en la antigua grecia al lado del mar. Se gana la vida vendiendo cuadros de paisajes, los cuales la mayoria son cuadros de lo que ella llama vida, el mar mediterranio. Su aficion por el mar y su talento para pintar la hicieron famosa por toda Grecia.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Axel',
'Axel es un escritor que se hizo famoso através de haber escrito grandes obras de aventuras con demonios, haciendose famoso por el transfondo de estos. Tiene grandes obras como ‘Black Glove’, ‘Slayer of Demons’, ‘The Exorcist is the Devil´s Son’ o ‘The Devil has a Job in the Human World’. Obras que le hicieron ganar varios premios de literatura.',
current_user() ,
current_timestamp()
);


savepoint characters;


INSERT ignore INTO ADVENTURE (name,description,usercreate,datecreated) VALUES (
 'La caja',
 'Una caja cuyos contenidos dependen de ti; ¿te haces responsable?',
 current_user(),
 current_timestamp());

INSERT ignore INTO ADVENTURE (name,description,usercreate,datecreated) VALUES (
 'Tren a casa',
 'Un viaje en tren aparentemente normal da un giro inesperado que te hará cuestionar hasta que punto las cosas són reales o una ilusión',
 current_user() ,
 current_timestamp());
 
 INSERT ignore INTO ADVENTURE (name,description,usercreate,datecreated) VALUES (
 'Among us',
 'Todos los personajes han decidido pasar la tarde jugando una partida al Among Us. Tienes que adivinar quien es el impostor y sacarlo de la nave antes de que mate a 4 personas.',
 current_user(),
 current_timestamp());


savepoint adventures;


insert ignore into CHARACTER_ADVENTURE (ID_CHARACTER,ID_ADVENTURE,usercreate,datecreated) values (
1,
1,
current_user(),
current_timestamp()
);


savepoint adventure_characters;


insert into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Despues de un largo dia de trabajo decides ir a casa directamente. Por el camino te das cuenta que sale un ruido de una caja al lado de un supermercado.',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='La caja'),
current_user(),
current_timestamp()
);

insert into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Decides dejar la caja e irte a casa para poder descansar. Al dia siguiente vuelves a pasar por la misma calle pero ya no esta la caja, preguntas al dueño de la tienda si sabe algo de lo que ha ocurrido con esa caja. El dueño le muestra el periódico. En este hay una noticia el la que se muestra como unos gatos bebes se enfrentan a un perro callejero muriendo todos. Te das cuenta al momento. En esa caja estaban lo gatitos. En ese momento una sensacion de culpa e invade el cuerpo y te preguntas se los podias haber salvado.',
1,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='La caja'),
current_user(),
current_timestamp()
);

insert into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Abres la caja y ves a 3 gatos bebes en condiciones terribles. Ves que estan encima de otro gato, però este esta muerto. Tiene pinta de que era la madre y abandonaron a los 4 en cuanto ella dio a luz. Un sentimiento de rabia te invade. Que vas a hacer con los gatos?',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='La caja'),
current_user(),
current_timestamp()
);

insert into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Decides llevarlo a una refugio de gatos. Alli te atiende una señorita llamada Marta la cual llama tu atencion favorablemente por la amabilidad y el cariño que les da a los gatos. Ella te mucho agradece que los hayas traido y te invita a que vayas y juegues con ellos todos los dias que quieras. Os intercambiais telefonos y quedais para veros otro dia.',
1,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='La caja'),
current_user(),
current_timestamp()
);

insert into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Decides llevatelos a casa. Te tomas el dia siguiente libre en tu trabajo para llevarlos al veterinario y ver en que situacion estan. La veterinaria te da las gracias por salvarlos y te dice que estan estables però no en buena condiciones, con un buen cuidado al mes o mes y medio podrian estar en condiciones perfectas. Esas palabras te animan y te las repites una y otra vez de vuelta a casa. Pero por el camino aparece un perro callejero. El perro huele a los gatos y se pone agresivo. El perro te ataca però lo contienes para que no ataque a los gatos. Decides parar al perro y pedir ayuda. Varios vecinos te ven y van al auxilio. Al final del dia apareces en un telediario elogiandote por tu valiente acto.',
1,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='La caja'),
current_user(),
current_timestamp()
);


savepoint steps;


insert into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Abres la caja para comprobar que hay dentro.',
'¿Que será?',
3,
1,
current_user(),
current_timestamp()
);

insert into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Dejas la caja cerrada porque no es de tu incumbencia.',
'No es mi problema',
2,
1,
current_user(),
current_timestamp()
);

insert into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Decides llevartelos a casa y cuidarlos tu mismo.',
'No puedo dejarlos aquí',
4,
3,
current_user(),
current_timestamp()
);

insert into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Decides llevarlos a algun lugar en el que se puedan hacer cargo de ellos.',
'No puedo dejarlos aquí, pero tampoco llevármelos',
5,
3,
current_user(),
current_timestamp()
);

insert into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Cierras la caja y te vas a casa.',
'Problema de otro',
2,
3,
current_user(),
current_timestamp()
);


savepoint options;


COMMIT;
