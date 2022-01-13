from vpython import *
# GlowScript 3.0 VPython



scene.range=20                  #mittakaava
scene.center=vec(0,5,0)
scene.title='Aloita klikkaamalla ikkunaa'

#luodaan grafiikkaobjektit pallo, lattia ja seina
pallo = sphere(pos=vec(-10,10,0), radius=0.5,color=color.orange, make_trail = True)  
taulu = label(pos=vec(-20,15,0), text = 'korkeus: ') 
lattia=box(pos=vec(0,-0.5,0),size=vec(40,1,20),colot=color.white)
seina = box(pos=vec(13,6,0), size=vec(0.2,12,12), texture=textures.rough) 
g = 9.81
#alustetaan nopeus- ja kiihtyvyysvektorit
pallo.velocity = vec(1.5,0,0)   #alkunopeus
pallo.acc=vec(0,-g,0)      #painovoiman kiihtyvyys

#tarvittavia vakioita
e=0.9           #kimmoisuuskerroin tormayksissa
dt = 0.01       #aikaaskelen pituus
 
scene.pause()   #ohjelma odottaa hiiren klikkausta

while  -12 < pallo.pos.x<20:
    rate(100)
    pallo.pos+=pallo.velocity*dt+0.5*pallo.acc*dt**2
    pallo.velocity+=pallo.acc*dt
    taulu.text = 'Korkeus:'+round(pallo.pos.y)
    if pallo.pos.y<0:
        pallo.velocity.y=-e*pallo.velocity.y  #e = elastisuus
    if pallo.pos.x >13:
        pallo.velocity.x=-e*pallo.velocity.x