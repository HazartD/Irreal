label start:
    ################## Acto 1 (Sueño) ###########################

    scene estatica_1 with dissolve ##deberia ser un espacio negro pero con estatica empezando

    show mc_normal at left##Protagonista a la izquierda
    mc ".............."
    mc "....................."
    mc "..............................."
    mcp "¿Dónde estoy? No... veo... nada........ Tal vez, sea que no estoy despierta."
    mcp "¿Es un sueño? Me pellizcaré a ver si siento algo."


    ""
    #play sound pellizco

    mcp "...Es un sueño."
    mcp "¡Es un sueño!"
    mcp "Finalmente, después de tantas notas, rutinas y mierdas, logre tener un sueño lucido.{w}\n¡Es hora de volverlo húmedo!"
    mcp "¡Aquí te voy, Linus de stardew valley! Ahora sí veré que paso cuando me «enseño a hacer cebo silvestre»."
    mcp "Ay... mi viejito, tan sabio, maduro, casto, determinado y libre..."

    scene estatica_2 #que se nota mas la estatica
    show mc_normal at left
    show ma_normal at right with dissolve

    mcp "Ya quiero despertar en el deseos carnales y que me... Un momento, esa es [ma], no Linus."
    mcp "¡Menteeee, te equivocaste de archivo! \nBusca en la carpeta de husbandos, no en la de familia, que eso mal visto y además no le voy a la tijera."
    mcp "Bueno, igual el sueño es el subconsciente. Los tiempos y la gente cambian. Probemos."

    ma "{cps=2}...{/cps}"

    mc "Bueno, cuñada, ¿es esto un manga yuri?, ¿le vas a mi hermano para en realidad pasar tiempo conmigo?"

    ma "{cps=2}...{/cps}"

    mc "¿Qué pasa, [ma]? ¿Mucho calor? ¿La ropa incómoda?"
    show mc_normal at move(0.4,1.0,0.1)
    mc "¿Te ayudo a arreglarlo?"
    show mc_normal at move(0.7,1.0,0.1)
    #hacercar personajes

    "[mc] acerca su brazo al cuello de [ma]."
    show pa_normal at center, custom_x(0.8)#center
    with zoomin
    "Y de la nada, apareció una niña entre ellas, agitando los brazos y negando con la cabeza." ###la prota la sueña así porque como ella es la que actúa extraña contra Mandy, le relaciona que sabe cosas que no dice.

    pa "N-No."
    pa "Peligrosa."

    mc "¿Qué?"
    mc "¿Qué se mete la pinche niña aquí? Okay, esto sí no puede ser el tipo de sueño que quiero que sea."
    mc "¿No se suponía que al darme cuenta lo controlaría?{fast} \nO es que... ¿No estoy soñando?"

    "[ma] toco el hombro de [pa]."

    pa "¡AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!"
    hide pa_normal
    with pixellate#dissolve

    mc "¿¡Qué verga!?"

    "Y al fondo, [mc] nota a quienes también sufrían el mismo destino que su primita."
    "Familiares, amigos que tenía de niña, amigos de internet, artistas que le gustaban, y demás personas y rostros que guardaba su memoria. \nTodos agonizando."

    "{color=#ffffff}Multitud{/color}" "¡AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!"

    mc "¡Dios mío, ¿qué es esto?!"#lagrimea, quizas como la Mel de ese episodio de ATA del ladrón

    "[ma] se abalanza sobre [mc] y le entierra las uñas en el rostro."

    ma "La niña siempre tuvo razón"

    mc "¡¿Eh?!"
    mc "¡AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!{nw}"

    ### todos los sprite se glichean. el volum de la estatica aumenta y de golpe termina.
    scene estatica_3

    ###Suena un pitito.
    scene cuarto_1
    "..."
    show mc_normal at offscreenleft,wakeup

    mc "¡¡AHHHH!!"
    mc "Ah... ah... ah..."
    mc "...Creo que desperté."
    mc "..."
    mc "¿Qué... significa todo eso?"

    ### aqui la intro si acaso
    jump day1
