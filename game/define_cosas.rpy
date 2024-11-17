default pr = 0
default ph = 0

###################################### Personajes ##############################################

define mc = Character(_("Protagonista"), who_color="#ea40ec", image = "mc")
define mcp = Character(_("Protagonista (pensamiento)"), who_color="#e6a8e7", what_prefix='(', what_suffix=')', image = "mc")
define mcpn = Character(_("Protagonista (pensamiento)"), kind=nvl, who_color="#e6a8e7")
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

transform move_x(time=5.0, xend=1.0):
    #xalign 0.0
    linear time xalign xend
transform move_left_to_right(time=5.0):
    offscreenleft
    linear time offscreenright

transform loop_h(xstar=0.0, xend=1.0):
    animation
    xalign xstar
    linear 0.5 xalign xend
    xzoom -1.0
    linear 0.5 xalign xstar
    xzoom 1.0
    repeat

transform wakeup:
    rotate 90  # Inicialmente acostado
    linear 1.5 rotate 0  # Se levanta en 1.5 segundos

transform attack(xend=0.5, yend=0.5, move_time=0.3, sign_time=0.1):
    #xalign 0.0 yalign 0.0  # Posición inicial
    linear move_time xalign xend yalign yend  # Mover al centro
    linear sign_time rotate -30 #xalign 0.6 yalign 0.6  # Simula un impacto

transform attacked:
    linear 0.2 rotate 30  # Simula un impacto


########################## Images ############################################
image estatica_1:
    "bg/estatica_1.png"
    pause 0.1
    "bg/estatica_1_in.png"
    pause 0.1
    repeat

image estatica_2:
    "bg/estatica_2.png"
    pause 0.1
    "bg/estatica_2_in.png"
    pause 0.1
    repeat

image estatica_3:
    "bg/estatica_3.png"
    pause 0.1
    "bg/estatica_3_in.png"
    pause 0.1
    repeat

image cuarto_1:
    "bg/gamer_room.png"

image pasillo_1:
    "bg/escalera.png"

image pasillo_2:
    "bg/escalera.png"

image cocina_1:
    "bg/bg/cocina.png"








