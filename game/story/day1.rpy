label day1:
    ################## Acto 2 (Desayuno) ###########################

    #scene cuarto_1##Ella igual en el costado izquierdo, un poco abajo, apenas despegada del cuadro de diálogo
    #show mc_normal at left

    mcp "..."
    mcp "Bueno, los sueños son solo sueños. Olvidemos esa mierda turbia y comamos ya."
    mcp "..."
    mcp "...A lo mejor soñé eso por la actitud que tiene [pa] desde hace unos días. Debería olvidarlo, es solo una niña. Además de que con el autismo que tiene, suele ser rara siempre."
    mcp "..."
    mcp "Puya, es que son solo locuras, vos."
    mcp "..."
    mcp "...Aunque, más de una relación habrá terminado porque la morra sonó que su morro le era infiel. \n¿Qué me niega a mí el derecho de clandestinamente abrirle carpeta de investigación a la novia de mi hermano porque soñé que nos mataba?"
    mcp "¡De inmediato empezaré, \nno parar \nhasta el misterio acabaré!"
    "Y la joven de un brinco se levantó de la cama, con una nueva cruzada."
    mcp "¡Finalmente me pasa algo interesante!"
    #ruido de tripa
    "Pero su estómago tenía otra, la usual."
    mcp "...Pues ...mejor comeré primero."
    mcp "Man, soy patética. Mucha emoción al inicio y a la mínima dejo todo. Jajaja."
    #algo debe pasar aqui, quizas solo que se oscurezca todo o algo asi
    gn "Lo que esta joven ignora, es que esta vez no podrá abandonar el problema en que se metió."
    gn "Oh, los jóvenes. \nSiempre igual de vagos, en toda época, en todo universo. Siempre igual de estúpidos."
    mcp "¿Qué debería hacer?"
    menu:
        "Primero ir a comer":
            jump cocina
        "Primero revisar el PC e investigar":
            jump pc1


    mcp "Oh, espera. \nMi streamer favorito esta transmitiendo."
    mcp "¡Tengo que preguntarle que opina sobre la polémica de hace 2 horas sobre otros streamers que de seguro ni conoce!"

    ##pantalla hace fade-in y fade-out

    mcp "Y así pase 4 horas de mi vida. Viendo a cuatro comediantes jugar a ser goblinas que limpian una mazmorra."

    mc "sdxfcgvhbjnlkm"
    mc "sdfcgvhbjn"
    mc "cv bnmhjb"
    mc "ghmb uigbn ighn "





label cocina:
    $pr+=1
    $pr1_cocina = True
    scene pasillo_1
    show mc_normal at move_left_to_right
    #play sound caminar
    "Como ya estaba de pie, [mc] caminó hacia la cocina"
    scene pasillo_2
    show mc_normal at left

    mcp "A prepararme el manjar de hoy."##*sprite moviéndose al otro costado, desaparece*
    
    show mc_normal at move_left_to_right
    pause
    scene cocina
    show mc_normal at move_left_to_right
    ##*vuelve a aparecer a la izquierda ahora en la cocina*

    mcp "A ver que le meto a la maruchan."

    ##Se mueve a la derecha y a la izquierda aparece Hernán
    show he_normal at left
    with dissolve
    he "¡Miren quién salió de su cueva hoy! {w} \nDrácula en persona."

    mc "¡Miren quién encontró su casa hoy! {w} \nEl señor vagabundo."

    show pa_normal#entra por la izquierda y se acerca a mc
    pa "¿Me haces comilla?"

    mc "¿E-Eh? ¿Como qué?"
    mcp "Mierda, yo solo sé hacer maruchan. Putos niños, siempre solo molestar saben."

    he "Huevo con queso le gusta comer."
    he "Continúan las sorpresas, ¡Miren quien habla con desconocidos!"
    #he se hacerca a pa
    "[he] se acercó a la cipotilla extendiendo los brazos con intención de cargarla, como suele hacer."

    pa "¡Ño!"

    "Pero esta se refugió detrás de [mc], agarrándola de los muslos."

    mc "Ahhh."

    he "¿Eh? \n¿Qué paso, mija? ¿Te gustan más los góticos ahora? jajaja"

    pa "Ño es ehsho."
    pa "E´ que ella te puede habel contagiayo."

    #Hernan con exprecion seria
    he "..."
    he "Tenés razón."
    he "Mandy en secreto siempre fue un alien que quería extinguir la humanidad. \n¡Y ahora te contagiaré la enfermedad letal que diseño para ello: {w}las cosquillas!"

    "[he], riendo, empezó a corretear a [pa] por la sala, la cual huía con visible preocupación"
    hide he_normal
    hide pa_normal
    show he_chase_pa at loop_h
    ##deberia haber modo de hacer un bucle en que se esten moviendo y desapareciendo para aparecer del otro lado
    pa "¡Ñoooooooooooooooooo!"

    he "Uyuyuy, que te contagio que te mueres."

    mcp "Ask, esta gente. \n¿Cómo siquiera tienen energía tan temprano? Yo me pongo a correr ahora y caigo en coma."
    mcp "Además haciendo tanto ruido..."
    mcp "Bueno, mejor me llevaré la maruchan al cuarto y le meteré coca cola. \n¿Con que sea un líquido sirve, no?"
    mcp "A ver si no me botan en lo que salgo."

    #
    "Así se echó sal. Su prima corrió directo hacia ella."

    mcp "{fast}¡Mierda si me van a chocar!"

    ##el bucle se para, pa] esta un poco mas arriba, estan los 2 frente a mc]

    "Pero su hermano le salva de una contusión, causada por su propia mal condición física."
    hide he_chase_pa
    show he_normal at left
    show pa_normal at custom_x(0.1),custom_y(0.6)
    he "Espérate, mija."
    he "Ahí ibas a chocar con [mc], a los anémicos les tardan mucho en curar las heridas. \nJajaja"

    mc "¡Ja!...No sé si agradecerte o pegarte."
    ##se va el sprite y pa voltea a ver a he

    "[mc] se va de la sala."
    "[he] y [pa] se miran en silencio unos minutos. [he] sonríe y [pa] muestra preocupación."

    he "..."

    pa "..."
    pa "¿Me vas a matai?"

    he "Chi."

    "Y en infantil juego, [he] empezó a hacerle cosquillas a la chiquitina."

    pa "¡Ñoo! {fast}jajajdjjjsdj."
    pa "{fast}Jajajsjisajsjija ¡Par..! jsjajjsid."

    he "Jejeje."

    "Los dos no sabían que, desde su espionaje a un lado de la puerta, pusieron a [mc] a pensar."

    mcp "Ahora que lo pienso..., se ve muy entretenido jugar así."
    mcp "..."
    mcp "Iré yendo a mi cuarto."
    scene pasillo_2
    show mc_normal at move_right_to_left
    pause
    scene pasillo_1
    show mc_normal at move_right_to_left
    pause
    scene cuarto
    show mc_normal at left

    jump pr1

    "[mc] toma su maruchan, y se sienta frente al vértice de LEDs tricolores."



label pc1:
    "..."








###########################################################la "meta crítica" es que a veces somos muy huevones, como la tipa al inicio que va a hacer algo pero lo deja porque le da hambre