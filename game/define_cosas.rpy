default pr = 0
default ph = 0
default day = 1

########## Por lo del "losercore" busque como era "perdedor" en latin y salio "victus", y como tengo entendido de que us/i son los masculino y femenino asi lo puse #####
###################################### Personajes ##############################################

define mc = Character(_("Victi"), who_color="#ea40ec", image = "mc")
define mcp = Character(_("Victi (pensamiento)"), who_color="#e6a8e7", what_prefix='(', what_suffix=')', image = "mc")
define mcpn = Character(_("Victi (pensamiento)"), kind=nvl, who_color="#e6a8e7")
define he = Character(_("Hernán"), who_color="#29a000", image = "he")
define pa = Character(_("Patricia"), who_color="#00ffff", image = "pa")
define ma = Character(_("Mandy"), who_color="#ff4646", image = "ma")
define gn = Character(_("Gemelos Narrandores"), kind=nvl, who_color="#000000")
#define voces = Character(_("Voces y otros"), who_color="#ffffff")

########################## Transform ############################################

transform custom_x(x=0.0):
    xalign x
transform custom_y(y=0.0):
    yalign y

transform infinite_spin:
    linear 0.2 rotate 180
    linear 0.2 rotate 360
    rotate 0
    repeat

transform move(xend=0.0, yend=1.0, time=1.0):
    #xalign 0.0
    linear time xalign xend yalign yend
transform move_left_to_right(time=3.0):
    offscreenleft
    linear time offscreenright
transform move_right_to_left(time=3.0):
    offscreenright
    linear time offscreenleft

transform loop_h:
    animation
    offscreenleft
    linear 0.5 offscreenright
    xzoom -1.0
    linear 0.5 offscreenleft
    xzoom 1.0
    repeat

transform wakeup:
    offscreenleft
    xalign 0.0
    rotate 90  # Inicialmente acostado
    pause 1.0
    linear 1.5 rotate 0  yalign 1.0# Se levanta en 1.5 segundos

transform attack(xend=0.5, yend=0.5, move_time=0.3, sign_time=0.1):
    #xalign 0.0 yalign 0.0  # Posición inicial
    linear move_time xalign xend yalign yend  # Mover al centro
    linear sign_time rotate -30 #xalign 0.6 yalign 0.6  # Simula un impacto

transform attacked:
    linear 0.2 rotate 30  # Simula un impacto


########################## Images ############################################
image estatica_1:
    "bg/estatica_1.png"
    pause 0.01
    "bg/estatica_1_in.png"
    pause 0.01
    repeat

image estatica_2:
    "bg/estatica_2.png"
    pause 0.01
    "bg/estatica_2_in.png"
    pause 0.01
    repeat

image estatica_3:
    "bg/estatica_3.png"
    pause 0.01
    "bg/estatica_3_in.png"
    pause 0.01
    repeat

image cuarto_1:
    "bg/gamer_room.png"

image pasillo_1:
    "bg/escalera.png"

image pasillo_2:
    "bg/escalera.png"

image cocina_1:
    "bg/bg/cocina.png"



########################## Flags ############################################
default pr1_cocina = False
default pr2_ = False
default pr3_ = False
default pr4_ = False
default pr5_ = False
default pr6_ = False
default pr7_ = False
default pr8_ = False
default pr9_ = False
default pr10_ = False
default pr11_ = False
default pr12_ = False
default pr13_ = False
default pr14_ = False
default pr15_ = False

default ph1_ = False
default ph2_ = False
default ph3_ = False
default ph4_ = False
default ph5_ = False
default ph6_ = False
default ph7_ = False
default ph8_ = False
default ph9_ = False
default ph10_ = False
default ph11_ = False
default ph12_ = False
default ph13_ = False
default ph14_ = False
default ph15_ = False



