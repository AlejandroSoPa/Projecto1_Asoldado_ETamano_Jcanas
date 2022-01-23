use PROJECT_1;


start transaction;


INSERT ignore INTO USER (username,password,usercreate,datecreated)
VALUES ('TestUser', 'TestPassword', current_user() , current_timestamp());


savepoint users;


INSERT ignore INTO PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Dae´mon', 
'Es un orco que desde pequeño fue entrenado para la guerra de las cuatro naciones (elfos, humanos, gnomos y orcos). Fue un guerrero muy reconocido por su habilidad con las espadas grandes hasta que en una de esas batallas fue herido de gravedad. Antes de morir fue salvado por una humana que lo escondió en su mundo humano. Él le juro lealtad por salvarle la vida y ahora está aprendiendo como es una vida pacífica mientras intenta pasar desapercibido.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Ana María',
'Es una humana adolescente que estudia una doble carrera de filosofía y derecho en la mejor universidad. Siendo ella la mejor estudiante del centro se la conoce con el apodo de “NUMBER ONE” y, sabiendo esto, se hizo tradición que en cualquier evento con figuras importantes ella estuviese presente; aunque ella estuviera todavía en su segundo año de estudio.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Belfegor',
'Es un demonio de alto rango que abandonó el infierno por las responsabilidades que tenía que cumplir. Al ser tan perezoso decidió dejar el infierno y vivir en un piso en el centro de una gran ciudad. Gracias a un teléfono que encontró tirado en el suelo no sale de su casa y pide todo lo que necesita a través de servicios de delivery. Belfegor, además, tiene interés por la cultura japonesa: Anime y Manga, siendo conocido por ello como el Demonio Otaku.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Mushu',
'Es el username de un adolescente en un nuevo MMORPG. Como él no había jugado nunca a ninguno, tuvo la brillante idea de poner los 100 puntos que te dan al hacer a tu personaje en el atributo fuerza y ninguno más. Como no quería perder ningún combate, antes de equiparse ningún atuendo, y por tanto estando desnudo, se pasó 36 horas golpeando a un objeto de práctica para subir su estadística lo máximo posible. Cuando llegó a 500 destruyó el objeto de un solo golpe. Desde ese momento se le conoce como el “Pervertido más fuerte” ya que solo necesita un solo golpe para debilitar a cualquier personaje, cosa que acorta el sufrimiento de verlo desnudo.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Jared',
'Jared es un hombre ciego de mediana edad. Es católico, pobre y... nazi! Lleva años intentando unirse a grupos neonazis pero nunca le aceptan. Por ese motivo él siempre se queja diciendo que ellos no son nazis de verdad, que no tienen la pureza de la raza aria y que él defenderia a Hitler con su propia vida. Jared no ve porque no le aceptan. Jared es negro.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Aegea',
'Aegea es una mujer que vive en una pequeña casa en la antigua grecia al lado del mar. Se gana la vida vendiendo cuadros de paisajes, de los cuales la mayoría son cuadros de lo que ella llama vida, el mar mediterráneo. Su afición por el mar y su talento para pintar la hicieron famosa por toda Grecia.',
current_user() ,
current_timestamp()
);
        
insert ignore into PROJECT_1.CHARACTER (name,description,usercreate,datecreated) VALUES (
'Axel',
'Axel es un escritor que se hizo famoso a través de haber escrito grandes obras de aventuras con demonios, famosas por el transfondo de estas. Tiene grandes obras como ‘Black Glove’, ‘Slayer of Demons’, ‘The Exorcist is the Devil´s Son’ o ‘The Devil has a Job in the Human World’. Obras que le hicieron ganar varios premios de literatura.',
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


savepoint adventures;


truncate CHARACTER_ADVENTURE;
start transaction;

replace into CHARACTER_ADVENTURE (ID_CHARACTER,ID_ADVENTURE,usercreate,datecreated) VALUES (
1,
2,
 current_user(),
 current_timestamp()
);

replace into CHARACTER_ADVENTURE (ID_CHARACTER,ID_ADVENTURE,usercreate,datecreated) VALUES (
2,
1,
 current_user(),
 current_timestamp()
);

replace into CHARACTER_ADVENTURE (ID_CHARACTER,ID_ADVENTURE,usercreate,datecreated) VALUES (
3,
2,
 current_user(),
 current_timestamp()
);

replace into CHARACTER_ADVENTURE (ID_CHARACTER,ID_ADVENTURE,usercreate,datecreated) VALUES (
4,
1,
 current_user(),
 current_timestamp()
);

replace into CHARACTER_ADVENTURE (ID_CHARACTER,ID_ADVENTURE,usercreate,datecreated) VALUES (
5,
1,
 current_user(),
 current_timestamp()
);

replace into CHARACTER_ADVENTURE (ID_CHARACTER,ID_ADVENTURE,usercreate,datecreated) VALUES (
5,
2,
 current_user(),
 current_timestamp()
);

replace into CHARACTER_ADVENTURE (ID_CHARACTER,ID_ADVENTURE,usercreate,datecreated) VALUES (
6,
1,
 current_user(),
 current_timestamp()
);

replace into CHARACTER_ADVENTURE (ID_CHARACTER,ID_ADVENTURE,usercreate,datecreated) VALUES (
7,
2,
 current_user(),
 current_timestamp()
);


savepoint step_adventures;


insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Después de un largo día de trabajo decides ir a casa directamente. Por el camino te das cuenta que sale un ruido de una caja tirada al lado del supermercado.',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='La caja'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Decides dejar la caja e irte a casa para poder descansar. Al día siguiente vuelves a pasar por la misma calle pero ya no está la caja, preguntas al dueño del supermercado si sabe algo de lo que ha ocurrido con la caja. El dueño te muestra el periódico. En este hay una noticia el la que se muestra como unos gatos bebes se ven víctimas de un perro callejero, muriendo todos. Te das cuenta al momento. En esa caja estaban lo gatitos. En ese momento una sensación de culpa te invade el cuerpo y te preguntas si los podias haber salvado.',
1,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='La caja'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Abres la caja y ves a 3 gatos bebes en condiciones terribles. Ves que estan encima de otro gato, pero este está muerto. Tiene pinta de que era la madre y abandonaron a los 4 en cuanto ella dió a luz. Que vas a hacer con los gatos?',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='La caja'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Decides llevarlos a una refugio de gatos. Allí te atiende una señorita llamada Marta la cual llama tu atencion favorablemente por la amabilidad y el cariño que les da a los gatos. Ella te agradece que los hayas traido y te invita a que vayas y juegues con ellos todos los dias que quieras. Os intercambiais teléfonos y quedáis para veros otro día.',
1,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='La caja'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Decides llevártelos a casa. Te tomas el día siguiente libre en tu trabajo para llevarlos al veterinario y ver en que situación están. La veterinaria te da las gracias por salvarlos y te dice que están estables, pero no en buena condiciones. Con un buen cuidado, al mes o mes y medio podrían estar en condiciones perfectas. Esas palabras te animan y te las repites una y otra vez de vuelta a casa, pero por el camino aparece un perro callejero. El perro huele a los gatos y se pone agresivo. Te ataca, pero lo contienes para que no ataque a los gatos y decides pedir ayuda. Varios vecinos te ven y van en tu auxilio. Al final del dia apareces en un telediario, donde elogian tu valiente acto.',
1,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='La caja'),
current_user(),
current_timestamp()
);



insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Eres %personaje%...
Abres los ojos tras lo que parece un largo parpadeo…
…Estás sentado en un vagón de tren, completamente vacío, que avanza por un túnel. Sientes las vibraciones del traqueteo y el ocasional parpadeo de las luces…
…Excepto por que está vacío, cosa que a veces pasa, no hay nada fuera de lo normal…
Recuerdas vagamente que estás volviendo a casa, sin embargo, no recuerdas de dónde vienes. ¿Del trabajo?...¿De la compra?...-Te preguntas. No pareces llevar nada encima que pueda darte alguna pista y decides ignorar la cuestión.
Pese a que la situación resulta cotidiana, sientes que algo está fuera de lugar…',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'-No, no me he equivocado de tren.-Piensas; sin embargo no eres capaz de recordar que ponía en el plano; Extraño…',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'-¿Serà que estoy cansado y no puedo concentrarme para leer?
-Piensas-
-¿Quizás podría esperar a que digan la pròxima parada por megafonía?
Estás cansado y confuso, aún así mantienes la calma.
',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'-Llaves…Cartera…-Piensas para ti mismo-Lo… llevo todo…
No recuerdas tener prisa por llegar a ningún compromiso tampoco.
Pese a que no pareces haber olvidado nada la sensación perdura…',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'La sensación de que algo está fuera de lugar sigue rondando en tu cabeza pero no se te ocurre que puede ser…',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'-...-
El anuncio tiene un extraño efecto sobre tí, %personaje%: por un lado te transmite una sensación de tranquilidad, por el otro, sientes que no has entendido ni una palabra de lo que decía.
Intentas recordar inútilmente el mensaje…Silencio… Un cosquilleo escalofriante te recorre el cuerpo de abajo a arriba y empiezas a lanzar miradas esquivas a todo tu alrededor. No hay nadie…no hay nada raro… Entonces… que es lo que sientes…',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Tu corazón se acelera por momentos y los movimientos del tren te hacen perder el equilibrio momentáneamente.
Ves pasar a gran velocidad un tren en sentido contrario a través de la ventana. Lo miras pero no consigues ver nada más que un borrón… Va muy ràpido.',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Con cada paso sientes que tu cuerpo se hace más pesado. La sensación de que algo va mal aumenta y se apodera de tu cuerpo. Tu visión se inunda de lágrimas, tu corazón late cual tambor y un seísmo sacude tu cuerpo. Sientes que has de salir de ahí…
Las vibraciones del tren aumentan a cada momento. Sientes que todo va demasiado rápido.',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Por más que lo intentas tus recuerdos anteriores a subirte al tren aparecen borrosos, como la estática de la televisión. Las pocas imágenes y sonidos que recuerdas son inconexos, desordenados, una mezcla de trozos de toda tu vida unos sobre otros, sin orden ni lógica.
Notas que tu corazón se acelera por momentos…
Por la ventana vislumbras pasar de reojo otro tren a gran velocidad en sentido contrario. Como metáfora de tus pensamientos lo percibes de forma borrosa, con flashes de luz y sonidos que se sobreponen entre ellos.',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Las aceleradas pulsaciones de tu corazón se transforman en lágrimas en tus ojos. Sientes que te asfixias, tu respiración se acelera, y lo que antes era una sensación al fondo de tu cabeza ahora se ha convertido en verdadero pánico.
Las vibraciones del convoy aumentan exponencialmente y se hacen indistinguibles de tus propios temblores de terror.
Sientes que has de salir, pero… ¿¡Cómo!?
Todo parece acelerarse.',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Las ahora bruscas vibraciones del tren hacen que te caigas y no puedas avanzar. Por la cabeza se te pasa la idea de que has de detener el tren y sin dejar la mirada quieta buscas la palanca de freno de emergencia. Ponerte de pié te parece imposible, tus extremidades parecen pesarte y solo consigues arrastrarte unos centímetros. Tu mirada se torna borrosa y oscura.',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Tus dedos casi parecen rozarla, sin embargo, esta parece alejarse.
De repente el movimiento del tren se para en seco. Sientes que sales disparado y tu mirada se vuelve completamente negra.
-¿He muerto?-piensas',
0,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);

insert ignore into STEP (description,adventure_end,ID_ADVENTURE,usercreate,datecreated) values (
'Abres los ojos de nuevo y, para tu sorpresa, te encuentras en lo que parece ser un húmedo mar de telas. No hay fuego, no hay gritos…
Estiras ambos brazos hacia arriba con la intención de nadar pero, en vez de impulsarte, la tela se desliza por ellos revelando lo que parece ser una luz de techo.
De un salto levantas el torso y observas el lugar en penumbra… Es tu habitación.
¿Era…un sueño?
Observas a tu alrededor aún confundido, deseando que sea verdad…',
1,
(select ID_ADVENTURE from ADVENTURE where ADVENTURE.NAME='Tren a casa'),
current_user(),
current_timestamp()
);


savepoint steps;


insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Abres la caja para comprobar que hay dentro.',
'¿Que será?',
3,
1,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Dejas la caja cerrada porque no es de tu incumbencia.',
'No es mi problema',
2,
1,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Decides llevartelos a casa y cuidarlos tu mismo.',
'No puedo dejarlos aquí',
4,
3,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Decides llevarlos a algún lugar en el que se puedan hacerse cargo de ellos.',
'No puedo dejarlos aquí, pero tampoco llevármelos',
5,
3,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Cierras la caja y te vas a casa.',
'Problema de otro',
2,
3,
current_user(),
current_timestamp()
);



insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'¿Me he equivocado de tren?',
'Diriges tu mirada al plano de ruta en la pared del vagón.',
7,
6,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'¿Me he olvidado algo?',
'Rebuscas en tus bolsillos con ambas manos con tal de ver si lo llevas todo.',
9,
6,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'No pasa nada…',
'Te echas para atràs en tu asiento y suspiras mirando el techo del vagón.',
10,
6,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Vuelves a mirar el plano',
'-Vamos %personaje%, concéntrate.-
Una vez más vuelves a observar el plano de ruta con el mismo resultado.',
8,
7,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'¿Serà que me he olvidado de algo?',
'Rebuscas en tus bolsillos con ambas manos con tal de ver si te falta algo.',
9,
7,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'¿Serà que me he equivocado de tren?',
'Diriges tu mirada al plano de la ruta en la pared del vagón.',
7,
9,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Ignoras la perturbadora sensación y continuas sentado. ',
'Te echas para atrás en tu asiento y suspiras, mirando el techo del vagón.',
10,
9,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Vuelves la mirada y agudizas tus oídos a la espera de que suene el anuncio',
'Te echas para atràs en tu asiento y suspiras profundamente mirando el techo del vagón.  ',
10,
8,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Ignoras la perturbadora sensación y continuas sentado.',
'Te echas para atràs en tu asiento y suspiras mirando el cercano techo del vagón.',
10,
7,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Continuas esperando',
'Se oyen las interferèncias de la megafonía y suena el anuncio de próxima parada. Escuchas atentamente…',
11,
10,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Intentas tranquilizarte y decides hacer recapitulación de lo que habías hecho antes en el día.',
'Sentado, intentas tranquilizarte y decides hacer recapitulación de lo que habías hecho antes en el día.',
14,
11,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Decides investigar el tren',
'Como quién se levanta para cambiar de vagón caminas por el pasillo entre los asientos, esquivando las barandillas.',
12,
11,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Continúas avanzando',
'Caminas paso a paso',
13,
12,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Te levantas en busca de una salida ',
'Irracionalmente le haces caso a tus instintos y desesperadamente buscas una salida a esta situación. ',
16,
13,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Continúas sentado',
'Continúas sentado, la intrigante sensación aumenta',
15,
14,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Te levantas en busca de una salida',
'Irracionalmente le haces caso a tus instintos y desesperadamente buscas una salida a esta situación.',
16,
15,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'Levantas la mano hacia la palanca',
'Alzas la mano y estiras los dedos',
17,
16,
current_user(),
current_timestamp()
);

insert ignore into PROJECT_1.OPTION (description,answer,next_step,ID_STEP,usercreate,datecreated) values (
'...',
'...',
18,
17,
current_user(),
current_timestamp()
);


savepoint options;


COMMIT;