import tkinter,time

import pgzrun,socket
from datetime import datetime,date
from random import randint,choice
from tkinter import Tk,Label,Button,Checkbutton,Entry
WIDTH = 1000
HEIGHT = 650


nowdate = str(date.today())
info = open("inf.txt",mode='r',encoding='utf-8')
i = info.readline()
infs = info.readline().split(";")
lastOpenDate = info.readline()
lst1 = ["name","exp","feeling","money","fish","speed","health","onduty","huazi","tea",'dkt','cyt','sft','ckrm','highsc','gmt']
inf = {}# only this is avaliable
for s in range(16):
    inf[lst1[s]]=infs[s]
info.close()
del infs
savetimer = 0
ui = 0
tmtea = 0
tmcy=0
side = ''
siui5 = ""
fishSide = ''
fishSpeed = 0
fishY = 0
tmfish = 0
tmyg = 1
tmsleep = 30
ygout = 330
wait = 60
fishing = 0
gofish = 0
scoreyg = 0
shoot = False
tme = 0
name = str(inf['name'])
exp = int(inf['exp'])
feeling = int(inf['feeling'])
money = int(inf['money'])
fish = int(inf['fish'])
speed = int(inf['speed'])
health = int(inf['health'])
onduty = int(inf['onduty'])
huazi = int(inf['huazi'])
tea = int(inf['tea'])
dkt = int(inf['dkt'])
cyt = int(inf['cyt'])
sft = int(inf['sft'])
ckrm = int(inf['ckrm']) # chalk remain
highsc = int(inf['highsc'])
gmt = int(inf['gmt'])
scoreyg = highsc
if nowdate != lastOpenDate:
    dkt = 0
    cyt = 0
    sft = 0
    gmt = 0

saying1 = open('say.txt',mode='r',encoding='utf-8')
saying = saying1.readline().replace('n','\n').split('$')
#saying=saying
say = ''
getip = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
getip.connect(('8.8.8.8',80))
print("本机ip地址：",getip.getsockname()[0])
getip.close()

kuai = Actor("1",center=(30,30))
kuai.x,kuai.y = 500,320
xcb = Actor("sk")
xcb.x,xcb.y = -120,-230
jyg = Actor('yg0')
jyg.x,jyg.y = -1233,-3211

buttom1 = Actor("but")
buttom1.x,buttom1.y = 900,140
but2 = Actor("but2")
but2.x,but2.y = 900,200
bk = Actor("back")
bk.x,bk.y = -123,-321
tofish = Actor("tofish")
tofish.x,tofish.y = -2222,-2222
torun = Actor("torun")
torun.x,torun.y = -1111,-1111
tofight = Actor('tofight')
tofight.x = -1231

aim = Actor('aim')
aim.x,aim.y = -123,-321
chalk = Actor('chalk')
chalk.x,chalk.y = -123,-321

drinktea = Actor("hc")
cy = Actor('cy')
if dkt >= 7 or tea < 1:
    drinktea.x, drinktea.y = -230, -333
else:
    drinktea.x, drinktea.y = 230, 333
if cyt >= 7 or huazi < 1:
    cy.x, cy.y = -750, -333
else:
    cy.x, cy.y = 750, 333
sellTea = Actor("te")
sellTea.x,sellTea.y = -333,-222
sellY = Actor("hz")
sellY.x,sellY.y = -133,-322
sellF = Actor("fl")
sellF.x,sellF.y = -123,-321
sellck = Actor("ck")
sellck.x,sellck.y = -123,-321

j = Actor('j')
j.x,j.y = -222,-222
fishe = Actor("sfish")
fishe.x,fishe.y = -2323,-22
stop = Actor("stop")
stop.x,stop.y = -321,-123

"""ui = 114514"""
player1 = Actor('.\\paz\\p1')
player2 = Actor('.\\paz\\p2')
w1 = Actor('.\\paz\\x1')
w2 = Actor('.\\paz\\x2')
h1 = Actor('.\\paz\\y1')
h2 = Actor('.\\paz\\y2')
# fd = Actor(".\\paz\\c")
pao1 = Actor(".\\paz\\p")
pao2 = Actor(".\\paz\\p")
player1.x = -1231
player2.x = -1231
w1.y = -1231
w2.y = -1231
h1.x = -1231
h2.x = -1231
pao1.x = -12312
pao2.x = -12313
p1,p2 = player1,player2
s1,s2 = '',''
spp1,spp2 = '',''
dp1,dp2 = 0,0
px1,px2 = 0,0
extw1 = 0
extw2 = 0
exth1 = 0
exth2 = 0
timer1 = 0
tme21 = 0
tme22 = 0
hurt1 = False
hurt2 = False
tp1 = 1500
tp2 = 1500
state = -1
sp1,sp2 = 4.5,4.5
hp1 = 100
hp2 = 100
def on_mouse_down(pos):
    global ui,say,saying,feeling,tmtea,tmfish,exp,dkt,tea,health,cyt,tmcy,huazi,money,fish,sft,shoot,X,Y,wait,\
        state,ckrm,gmt,side,hp1,hp2,s1,s2,connected,sock,host,client
    if ui == 5:
        if ckrm > 0:
            shoot = True
            ckrm -= 1
            X = int(aim.x)
            Y = int(aim.y)
        else:
            pass
    if ui == 3:
        if pos[0] < 330:
            side = 'l'
        elif pos[0] > 570:
            side = 'r'
        else:
            side = ''
        if kuai.collidepoint(pos) and tmfish <=0:
            tmfish = 1
    if kuai.collidepoint(pos):
        a = choice(saying)
        say = a
        save()
    if drinktea.collidepoint(pos):
        if dkt < 7:
            animate(drinktea, pos=(kuai.x-10, kuai.y + 100))
            tmtea = 1
            dkt += 1
            tea -= 1
            health += 9
            feeling += 10
            exp += 2
        else:
            pass
    if cy.collidepoint(pos):
        if cyt < 7:
            animate(cy,pos=(kuai.x+38,kuai.y+20))
            tmcy = 1
            cyt += 1
            huazi -= 1
            health -= 10
            feeling += 7
            exp += 3
        else:
            pass
    if buttom1.collidepoint(pos):
        ui = 1
        tofish.x,tofish.y = 125,80
        torun.x,torun.y = 375,80
        tofight.x,tofight.y = 623,80
        save()
    if but2.collidepoint(pos):
        ui = 2
        sellY.x,sellTea.x,sellTea.y,sellY.y = 460,460,90,490
        sellF.x,sellF.y = 660,280
        sellck.x,sellck.y = 480,285
        save()
    if sellY.collidepoint(pos):
        if (money-5) > 0:
            money -= 5
            feeling-=9
            huazi += 1
        save()
    if sellTea.collidepoint(pos):
        if (money - 10)>0:
            money -= 10
            feeling -= 15
            tea += 1
        save()
    if sellF.collidepoint(pos):
        if fish >= 1 and sft < 30:
            money += 4
            feeling += 4
            fish -= 1
            sft += 1
        save()
    if sellck.collidepoint(pos):
        if gmt < 2:
            if (money-30)>0:
                money -= 30
                ckrm += 10
                gmt += 1
    if tofish.collidepoint(pos) and fish <= 20:
        ui = 3
        music.stop()
        music.play('bg')
        tofish.x, tofish.y = -213, -3211
        torun.x, torun.y = -132, -1111
        tofight.x, tofight.y = -111, -231
        kuai.image = 'f2'
        j.x,j.y = 500,110
        kuai.x, kuai.y = 500, 50
    if torun.collidepoint(pos):
        ui = 5
        wait = 60
        music.stop()
        music.play('bg2')
        tofish.x, tofish.y = -213, -3211
        torun.x, torun.y = -132, -1111
        tofight.x, tofight.y = -111, -231
        kuai.image = 'f2'
        kuai.x,kuai.y = 50,400
        chalk.x,chalk.y = 80,400
        jyg.x,jyg.y = -123,-321
    if tofight.collidepoint(pos):
        ui = 114514
        set1()
        music.stop()
        music.play('bg3')
        tofish.x, tofish.y = -213, -3211
        torun.x, torun.y = -132, -1111
        tofight.x,tofight.y = -111,-231
        p1.x,p1.y = 100,100
        p2.x,p2.y = 850,500
        s1, s2 = '', ''
        spp1, spp2 = '', ''
        dp1, dp2 = 0, 0
        px1, px2 = 0, 0
        extw1 = 0
        extw2 = 0
        exth1 = 0
        exth2 = 0
        timer1 = 0
        tme21 = 0
        tme22 = 0
        hurt1 = False
        hurt2 = False
        tp1 = 1500
        tp2 = 1500
        sp1, sp2 = 4, 4
        hp1 = 100
        hp2 = 100

        #state = 0
    if bk.collidepoint(pos):
        if ui == 3 or ui == 5 or ui == 114514:
            music.stop()
            music.play('breaktime')
        if ui == 114514:
            connected = False
            try:
                sock.close()
            except:
                pass
        ui = 0
        save()
        sellY.x, sellTea.x, sellTea.y, sellY.y = -460, -460, -490, -90
        stop.x,stop.y = -321,-123
        sellF.x,sellF.y = 1333,233
        sellck.x,sellck.y = -131,-323
        tofish.x,tofish.y = -231,-1111
        torun.x,torun.y = -132,-2222
        tofight.x,tofight.y = -12314,-12
        aim.x,aim.y = -123,-321
        chalk.x,chalk.y = -123,-321
        j.x,j.y = -2312,-222
        kuai.image = "1"
        kuai.x, kuai.y = 510, 330
        jyg.x,jyg.y = -123,-321
        p1.x = -1231
        p2.x = -1231
        w1.y = -1231
        w2.y = -1231
        h1.x = -1231
        h2.x = -1231
        pao1.x = -1231
        pao2.x = -1231
        if dkt >= 7 or tea <1:
            pass
        else:
            drinktea.x, drinktea.y = 230, 333
        if cyt >= 7 or huazi < 1:
            pass
        else:
            cy.x, cy.y = 750, 333
def on_mouse_move(pos):
    global ui
    if ui == 5:
        if not shoot:
            kuai.angle = kuai.angle_to(pos)
            chalk.angle = chalk.angle_to(pos)
        aim.x,aim.y = pos
def on_key_down(key):
    global money,tea,huazi,ui,tmfish,side,siui5,sellY,cy,s1,s2,spp1,spp2,extw1,extw2,exth1,exth2,px1,px2,state,\
    tp1,tp2,spp1,spp2,hp1,hp2,connected
    if key == keys.K:
        if cy.image != 'cy2':
            cy.image = 'cy2'
            sellY.image = 'hz2'
    if key == keys.P:
        music.stop()
        music.play('sf')
        sounds.tkwl.play()

    if ui == 3:
        if key == keys.RETURN and tmfish <=0:
            tmfish = 1
        if key == keys.LEFT:
            side = 'l'
        if  key == keys.RIGHT:
            side = 'r'
    if ui == 114514:
        # move
        if player_num == 0:
            if key == keys.W:
                s1 = 'w'
            elif key == keys.S:
                s1 = 's'
            elif key == keys.A:
                s1 = 'a'
            elif key == keys.D:
                s1 = 'd'
            if key == keys.UP:
                s2 = 'w'
            elif key == keys.DOWN:
                s2 = 's'
            elif key == keys.LEFT:
                s2 = 'a'
            elif key == keys.RIGHT:
                s2 = 'd'
            if key == keys.X and tp1 <= 300:
                spp1 = s1
            if key == keys.RALT and tp2 <= 300:
                spp2 = s2
            if key == keys.Q:
                if px1 == 0:
                    px1 = 1
                    print
                    p1.image = '.\\paz\\px1'
                elif px1 == 1:
                    p1.image = '.\\paz\\p1'
                    px1 = 0
            if key == keys.RCTRL:
                if px2 == 0:
                    px2 = 1
                    p2.image = '.\\paz\\px2'
                elif px2 == 1:
                    p2.image = '.\\paz\\p2'
                    px2 = 0
            if px1 == 0:
                if key == keys.E:
                    w1.y = p1.y
                    extw1 = 1
                if key == keys.C:
                    h1.x = p1.x
                    exth1 = 1
            if px2 == 0:
                if key == keys.PAGEUP:
                    w2.y = p2.y
                    extw2 = 1
                if key == keys.PAGEDOWN:
                    h2.x = p2.x
                    exth2 = 1
        elif player_num == 1 and connected:
            if pot == 0:
                if key == keys.W:
                    s1 = 'w'
                elif key == keys.S:
                    s1 = 's'
                elif key == keys.A:
                    s1 = 'a'
                elif key == keys.D:
                    s1 = 'd'
                if key == keys.Q:
                    if px1 == 0:
                        px1 = 1
                        p1.image = '.\\paz\\px1'
                    elif px1 == 1:
                        p1.image = '.\\paz\\p1'
                        px1 = 0
                if key == keys.X and tp1 <= 300:
                    spp1 = s1
                if px1 == 0:
                    if key == keys.E:
                        w1.y = p1.y
                        extw1 = 1
                    if key == keys.C:
                        h1.x = p1.x
                        exth1 = 1
            if pot == 1:
                if key == keys.UP:
                    s1 = 'w'
                elif key == keys.DOWN:
                    s1 = 's'
                elif key == keys.LEFT:
                    s1 = 'a'
                elif key == keys.RIGHT:
                    s1 = 'd'
                if key == keys.RCTRL:
                    if px1 == 0:
                        px1 = 1
                        p1.image = '.\\paz\\px1'
                    elif px1 == 1:
                        p1.image = '.\\paz\\p1'
                        px1 = 0
                if key == keys.RALT and tp1 <= 300:
                    spp1 = s1
                if px1 == 0:
                    if key == keys.PAGEUP:
                        w1.y = p1.y
                        extw1 = 1
                    if key == keys.PAGEDOWN:
                        h1.x = p1.x
                        exth1 = 1
        elif player_num == 2 and connected:
            if pot == 0:
                if key == keys.W:
                    s2 = 'w'
                elif key == keys.S:
                    s2 = 's'
                elif key == keys.A:
                    s2 = 'a'
                elif key == keys.D:
                    s2 = 'd'
                if key == keys.Q:
                    if px2 == 0:
                        px2 = 1
                        p2.image = '.\\paz\\px2'
                    elif px2 == 1:
                        p2.image = '.\\paz\\p2'
                        px2 = 0
                if px2 == 0:
                    if key == keys.E:
                        w2.y = p2.y
                        extw2 = 1
                    if key == keys.C:
                        h2.x = p2.x
                        exth2 = 1
                if key == keys.X and tp2 <= 300:
                    spp2 = s2
            if pot == 1:
                if key == keys.UP:
                    s2 = 'w'
                elif key == keys.DOWN:
                    s2 = 's'
                elif key == keys.LEFT:
                    s2 = 'a'
                elif key == keys.RIGHT:
                    s2 = 'd'
                if key == keys.RCTRL:
                    if px2 == 0:
                        px2 = 1
                        p2.image = '.\\paz\\px2'
                    elif px2 == 1:
                        p2.image = '.\\paz\\p2'
                        px2 = 0
                if key == keys.RALT and tp2 <= 300:
                    spp2 = s2
                if px2 == 0:
                    if key == keys.PAGEUP:
                        w2.y = p2.y
                        extw2 = 1
                    if key == keys.PAGEDOWN:
                        h2.x = p2.x
                        exth2 = 1
        if key == keys.RETURN:
            if player_num == 0:
                if state == 1:
                    music.stop()
                    music.play('bg3')
                    tofish.x, tofish.y = -213, -3211
                    torun.x, torun.y = -132, -1111
                    tofight.x, tofight.y = -111, -231
                    p1.x, p1.y = 100, 100
                    p2.x, p2.y = 850, 500
                    h1.x,h2.x = -123,-123
                    w1.y,w2.y = -1321,-1321
                    pao1.x,pao2.x = -13222,-31231
                    s1, s2 = '', ''
                    spp1, spp2 = '', ''
                    dp1, dp2 = 0, 0
                    px1, px2 = 0, 0
                    extw1 = 0
                    extw2 = 0
                    exth1 = 0
                    exth2 = 0
                    timer1 = 0
                    tme21 = 0
                    tme22 = 0
                    hurt1 = False
                    hurt2 = False
                    tp1 = 1500
                    tp2 = 1500
                    sp1, sp2 = 4, 4
                    hp1 = 100
                    hp2 = 100
                    state = 0
                    p1.image = '.\\paz\\p1'
                    p2.image = '.\\paz\\p2'
            else:
                if host == 0:
                    if state == 1:
                        music.stop()
                        music.play('bg3')
                        tofish.x, tofish.y = -213, -3211
                        torun.x, torun.y = -132, -1111
                        tofight.x, tofight.y = -111, -231
                        p1.x, p1.y = 100, 100
                        p2.x, p2.y = 850, 500
                        h1.x, h2.x = -123, -123
                        w1.y, w2.y = -1321, -1321
                        pao1.x, pao2.x = -13222, -31231
                        s1, s2 = '', ''
                        spp1, spp2 = '', ''
                        dp1, dp2 = 0, 0
                        px1, px2 = 0, 0
                        extw1 = 0
                        extw2 = 0
                        exth1 = 0
                        exth2 = 0
                        timer1 = 0
                        tme21 = 0
                        tme22 = 0
                        hurt1 = False
                        hurt2 = False
                        tp1 = 1500
                        tp2 = 1500
                        sp1, sp2 = 4, 4
                        hp1 = 100
                        hp2 = 100
                        state = 0
                        p1.image = '.\\paz\\p1'
                        p2.image = '.\\paz\\p2'

    if key == keys.S:
        save()
def on_key_up(key):
    global side,siui5
    if key == keys.K:
        cy.image = 'cy'
        sellY.image = 'hz'
    if key == keys.LEFT or key == keys.RIGHT:
        side = ''
    if key == keys.DOWN or key == keys.UP:
        siui5 = ''
def save():
    global name,exp,feeling,money,fish,speed,health,onduty,huazi,tea,dkt,cyt,inf,nowdate,sft,ckrm,highsc,gmt
    inffile = open("inf.txt",mode = 'r',encoding='utf-8')
    line1 = inffile.readline()
    line2 = inffile.readline()
    line3 = inffile.readline()
    lst = [name,exp,feeling,money,fish,speed,health,onduty,huazi,tea,dkt,cyt,sft,ckrm,highsc,gmt]
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    wr = ';'.join(lst)
    inffile.close()
    inffile = open("inf.txt",mode = 'w',encoding='utf-8')
    inffile.write(line1+wr+"\n"+nowdate)
    inffile.close()
player_num = -1 # 0:single;  1: player1   2:player2
host = -1 # 0:host    1:guest
pot = -1 #0: wasd   1:udlr
connected = False
targetIp = ''
def set0(a):
    global player_num,host,pot,targetIp,e0,l3,B0,state,tk
    if a == 0:
        tk.destroy()
        state = 0
    if a in [1,2]:
        player_num = a
        l0['text']='选择模式：%s'%('单机' if a == 0 else '玩家%s'%(a))
        b0['state'] = tkinter.DISABLED
        b1['state'] = tkinter.DISABLED
        b2['state'] = tkinter.DISABLED
    elif a in [3,4]:
        l1['text'] = '主或客：%s' % ('主' if a-3 == 0 else '客')
        bb0['state'] = tkinter.DISABLED
        bb1['state'] = tkinter.DISABLED
        host = a - 3
    elif a in [5,6]:
        l2['text'] = '操作方式：%s'%('WASD' if a-5 == 0 else "上下左右")
        bbb0['state'] = tkinter.DISABLED
        bbb1['state'] = tkinter.DISABLED
        pot = a - 5
    elif a == -1:
        targetIp = e0.get()
    if host == 1 and pot != -1:
        l3 = Label(tk, text='房主ip:')
        e0 = Entry(tk, width=15)
        B0 = Button(tk, text='确定', width=15, height=2, command=lambda: set0(-1))
        l3.grid(column=1, row=3)
        e0.grid(column=2, row=3)
        B0.grid(column=3, row=3)
    if player_num != 0 and not connected:
        l4 = Label(tk, text='等待连接……')
        l4.grid(column=3, row=0)
    if player_num != -1 and host != -1 and pot != -1:
        online()
def set1():
    global player_num,host,pot,tk,l0,l1,l2,b0,b1,b2,bb0,bb1,bbb0,bbb1,e0,state
    tk = Tk()
    tk.title('多人设置')
    tk.wm_attributes('-topmost',1)
    player_num = 0
    host = -1
    pot = -1
    l0 = Label(tk,text='选择模式：')
    b0 = Button(tk,text='单机',width=15,height=2,command = lambda:set0(0))
    b1 = Button(tk,text='玩家1',width=15,height=2,command = lambda:set0(1))
    b2 = Button(tk,text='玩家2',width=15,height=2,command = lambda:set0(2))
    l0.grid(column=0,row=0)
    b0.grid(column=0,row=1)
    b1.grid(column=0,row=2)
    b2.grid(column=0,row=3)
    l1=Label(tk,text='主或客：')
    bb0 = Button(tk,text='主',width=15,height=2,command = lambda:set0(3))
    bb1 = Button(tk,text='客',width=15,height=2,command = lambda:set0(4))
    l1.grid(column = 1,row = 0)
    bb0.grid(column=1,row=1)
    bb1.grid(column=1,row=2)
    l2=Label(tk,text='操作方式：')
    bbb0 = Button(tk,text='WASD',width=15,height=2,command = lambda:set0(5))
    bbb1 = Button(tk,text='上下左右',width=15,height=2,command = lambda:set0(6))
    l2.grid(column = 2,row = 0)
    bbb0.grid(column=2,row=1)
    bbb1.grid(column=2,row=2)

    tk.mainloop()
def online():
    global s1, s2, px1, px2, state, hp1, hp2, extw2, extw1, exth1, exth2, timer1, sp2, \
        sp1, tme, tr, tp2, tp1, spp1, spp2, \
        dp1, dp2, tme22, tme21, hurt1, hurt2,\
        feeling,health,\
        pot,player_num,host,connected,ui,player_num,pot,host,l4,sock,client,connected,targetIp,state,tk,ui,status
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 314))
    if host==0:
        sock.listen(1)
        print("Waiting for connection to be established...")
        client,caddr = sock.accept()
        print("Connection established.")
        connected = True
        # status = 'send1'
        ui = 114514
        state = 0
        music.stop()
        music.play('bg3')
        tofish.x, tofish.y = -213, -3211
        torun.x, torun.y = -132, -1111
        tofight.x, tofight.y = -111, -231
        p1.x, p1.y = 100, 100
        p2.x, p2.y = 850, 500
        h1.x, h2.x = -123, -123
        w1.y, w2.y = -1321, -1321
        pao1.x, pao2.x = -13222, -31231
        s1, s2 = '', ''
        spp1, spp2 = '', ''
        dp1, dp2 = 0, 0
        px1, px2 = 0, 0
        extw1 = 0
        extw2 = 0
        exth1 = 0
        exth2 = 0
        timer1 = 0
        tme21 = 0
        tme22 = 0
        hurt1 = False
        hurt2 = False
        tp1 = 1500
        tp2 = 1500
        sp1, sp2 = 4, 4
        hp1 = 100
        hp2 = 100
        state = 0
        p1.image = '.\\paz\\p1'
        p2.image = '.\\paz\\p2'
        print("Starting info exchanging process...")
        tk.destroy()
    elif host == 1:
        sock.connect((targetIp,314))
        print("Connection established.")
        connected = True
        # status = 'recv1'
        ui = 114514
        state = 0
        music.stop()
        music.play('bg3')
        tofish.x, tofish.y = -213, -3211
        torun.x, torun.y = -132, -1111
        tofight.x, tofight.y = -111, -231
        p1.x, p1.y = 100, 100
        p2.x, p2.y = 850, 500
        h1.x, h2.x = -123, -123
        w1.y, w2.y = -1321, -1321
        pao1.x, pao2.x = -13222, -31231
        s1, s2 = '', ''
        spp1, spp2 = '', ''
        dp1, dp2 = 0, 0
        px1, px2 = 0, 0
        extw1 = 0
        extw2 = 0
        exth1 = 0
        exth2 = 0
        timer1 = 0
        tme21 = 0
        tme22 = 0
        hurt1 = False
        hurt2 = False
        tp1 = 1500
        tp2 = 1500
        sp1, sp2 = 4, 4
        hp1 = 100
        hp2 = 100
        state = 0
        p1.image = '.\\paz\\p1'
        p2.image = '.\\paz\\p2'
        print("Starting info exchanging process...")
        tk.destroy()
def sendD():
    global s1, s2, px1, px2, state, hp1, hp2, \
        extw2, extw1, exth1, exth2, timer1, sp2, \
        sp1, tme, tp2, tp1, spp1, spp2, \
        dp1, dp2, tme22, tme21, hurt1, hurt2, \
        pot, player_num, host, connected,sock,client,\
        status
    if connected:
        msg1 = ';'.join('%s'%i for i in [
            state,
            px1,px2,
            hurt1,hurt2,
            dp1, dp2,
            sp1,sp2,
            hp1,hp2
        ])# 状态变量
        msg2=';'.join('%s'%i for i in [
            exth2,exth1,extw2,extw1,
            timer1,
            tme21,tme22,
            tp1,tp2
        ])#计时变量
        msg3=';'.join('%s'%i for i in [
            s1,s2,spp1,spp2
        ])#方向变量
        msg4 = ';'.join('%s'%i for i in [
            p1.x, p2.x,
            p1.y, p2.y,
            pao1.x, pao2.x,
            pao1.y,pao2.y,
            w1.x, w2.x,
            w1.y,w2.y,
            h1.x, h2.x,
            h1.y,h2.y
        ])#坐标变量
        msg0 = ';'.join([msg1,msg2,msg3,msg4])
        #print(msg0)
        if host == 0:
            client.send(msg0.encode('gbk'))
        elif host == 1:
            sock.send(msg0.encode('gbk'))
        status = 'send1'
def recvD():
    global s1, s2, px1, px2, state, hp1, hp2, \
        extw2, extw1, exth1, exth2, timer1, sp2, \
        sp1, tme, tp2, tp1, spp1, spp2, \
        dp1, dp2, tme22, tme21, hurt1, hurt2, \
        pot, player_num, host, connected,sock,client,\
        status
    if connected:
        if host == 0:
            recv=(client.recv(2048)).decode('gbk').split(';')#[:26]
        elif host == 1:
            recv = (sock.recv(2048)).decode('gbk').split(';')#[:26]
        msg1 = recv[0:11]
        msg2=recv[11:20]
        msg3=recv[20:24]
        msg4=recv[24:]

        if int(msg1[0]) != state:  # state change
            if host == 0:
                pass
            if host == 1:
                state = int(msg1[0])
        #host
        if host == 0:
            pass
        if host == 1:
            #exth2,exth1,extw2,extw1,\
            timer1,\
            tme21,tme22,\
            tp1,tp2 = int(msg2[4]),\
            int(msg2[5]),int(msg2[6]),\
            int(msg2[7]),int(msg2[8])
            hp1,hp2 = int(msg1[-2]),int(msg1[-1])
        exth2,exth1,extw2,extw1=int(msg2[0]), int(msg2[1]), int(msg2[2]), int(msg2[3]),
            #playernum
        if player_num == 1:
            px2 = int(msg1[2])
            hurt2 = bool(msg1[4])
            dp2 = int(msg1[6])
            w2.x,w2.y,h2.x,h2.y = float(msg4[9]),float(msg4[11]),float(msg4[13]),float(msg4[15])
            if host == 0:
                pass
            if host == 1:
                sp2 = float(msg1[8])
                hp2 = int(msg1[10])
            if msg3[1] != s2:
                s2 = msg3[1]
                p2.x,p2.y = float(msg4[1]),float(msg4[3])
            if msg3[3] != spp2:
                spp2 = msg3[3]
                pao2.x,pao2.y = float(msg4[5]),float(msg4[7])

        if player_num == 2:
            px1 = int(msg1[1])
            hurt1 = bool(msg1[3])
            dp1 = int(msg1[5])
            w1.x, w1.y, h1.x, h1.y = float(msg4[8]), float(msg4[10]), float(msg4[12]), float(msg4[14])
            if host == 0:
                pass
            if host == 1:
                sp1 = float(msg1[7])
                hp1 = int(msg1[9])
            if msg3[0] != s1:
                s1 = msg3[0]
                p1.x, p1.y = float(msg4[0]), float(msg4[2])
            if msg3[2] != spp1:
                spp1 = msg3[2]
                pao1.x, pao1.y = float(msg4[4]), float(msg4[6])
def ui114514():
    global s1, s2, px1, px2, state, hp1, hp2, extw2, extw1, exth1, exth2, timer1, sp2, \
        sp1, tme, tr, tp2, tp1, spp1, spp2, \
        dp1, dp2, tme22, tme21, hurt1, hurt2,\
        feeling,health,\
        pot,player_num,host,connected,ui
    #print(sp1,sp2,hurt1,hurt2)
    if player_num !=0:
        hurt1,hurt2=False,False
    if player_num == 0 or connected:
        if state == 1:
            p1.image = '.\\paz\\vic1'
            p2.image = '.\\paz\\vic2'
        if state != -1 and state != 1:
            if hurt1:
                tme21 += 1
                if tme21 >= 201:
                    hurt1 = False
            if hurt2:
                tme22 += 1
                if tme22 >= 201:
                    hurt2 = False
            if tp1 >= 300:
                tp1 -= 1
            else:
                if spp1 != '':
                    tp1 = 1500
            if tp2 >= 300:
                tp2 -= 1
            else:
                if spp2 != '':
                    tp2 = 1500 # timers
        if state == 0: # Gaming
            if px1 == 0 and p1.image != '.\\paz\\p1':
                p1.image = '.\\paz\\p1'
            if px2 == 0 and p2.image != '.\\paz\\p2':
                p2.image = '.\\paz\\p2'
            if px1 == 1 and p1.image != '.\\paz\\px1':
                p1.image = '.\\paz\\px1'
            if px2 == 1 and p2.image != '.\\paz\\px2':
                p2.image = '.\\paz\\px2'

            """Moving normally"""
            if px1 == 0:
                if not hurt1:
                    if px2 == 1:
                        sp1 = 6.5
                    else:
                        sp1 = 4
                else:
                    if px1 == 0:
                        if px2 == 1:
                            sp1 = 4
                        else:
                            sp1 = 1.5
                if s1 == 'w' and p1.top > 3:
                    p1.y -= sp1
                elif s1 == 's' and p1.bottom < 637:
                    p1.y += sp1
                elif s1 == 'a' and p1.left > 3:
                    p1.x -= sp1
                elif s1 == 'd' and p1.right < 977:
                    p1.x += sp1
            if px2 == 0:
                if not hurt2:
                    if px1 == 1:
                        sp2 = 6.5
                    else:
                        sp2 = 4
                else:
                    if px2 == 0:
                        if px1 == 1:
                            sp2 = 4
                        else:
                            sp2 = 1.5
                if s2 == 'w' and p2.top > 3:
                    p2.y -= sp2
                elif s2 == 's' and p2.bottom < 637:
                    p2.y += sp2
                elif s2 == 'a' and p2.left > 3:
                    p2.x -= sp2
                elif s2 == 'd' and p2.right < 977:
                    p2.x += sp2
            """hurt"""
            if px1 == 1:
                if not hurt2:
                    sp2 = 4.5
                else:
                    sp2 = 2.5
            if px2 == 1:
                if not hurt1:
                    sp1 = 4.5
                else:
                    sp1 = 2.5
            """fire"""
            if spp1 != '':
                if dp1 == 0:
                    sounds.kp.play()
                    pao1.x, pao1.y = p1.x, p1.y
                    dp1 = 1
                if spp1 == 'w':
                    pao1.y -= 17
                elif spp1 == 's':
                    pao1.y += 17
                elif spp1 == 'a':
                    pao1.x -= 17
                elif spp1 == 'd':
                    pao1.x += 17
                if pao1.top <= -50 or pao1.left <= -50 or pao1.right >= 1050 or pao1.bottom >= 700:
                    spp1 = ''
                    dp1 = 0
            if spp2 != '':
                if dp2 == 0:
                    sounds.kp.play()
                    pao2.x, pao2.y = p2.x, p2.y
                    dp2 = 1
                if spp2 == 'w':
                    pao2.y -= 17
                elif spp2 == 's':
                    pao2.y += 17
                elif spp2 == 'a':
                    pao2.x -= 17
                elif spp2 == 'd':
                    pao2.x += 17
                if pao2.top <= -50 or pao2.left <= -50 or pao2.right >= 1050 or pao2.bottom >= 700:
                    spp2 = ''
                    dp2 = 0
            """death"""
            # px1,px2 = 0, or say normal
            if px2 == 0:
                """pao"""
                if pao1.colliderect(p2):
                    hp2 -= 21
                    sounds.aaa.stop()
                    sounds.aaa.play()
                    hurt2 = True #if player_num == 0 else print()
                    state = 2
                """Light"""
                if p2.colliderect(w1) or p2.colliderect(h1):
                    hp2 -= 14
                    state = 2
                    sounds.awc.stop()
                    sounds.awc.play()
            if px1 == 0:
                """pao"""
                if pao2.colliderect(p1):
                    hp1 -= 21
                    sounds.aaa.stop()
                    sounds.aaa.play()
                    hurt1 = True #if player_num == 0 else print()
                    state = 2
                """light"""
                if p1.colliderect(w2) or p1.colliderect(h2):
                    hp1 -= 14
                    state = 2
                    sounds.awc.stop()
                    sounds.awc.play()
            # px1,px2 = 1, or say defending
            if px2 == 1:
                if p1.colliderect(p2):
                    hp2 -= 17
                    sounds.aaa2.play()
                    state = 2
                if p2.colliderect(w1) or p2.colliderect(h1):
                    hp1 -= 14
                    state = 2
                    sounds.awc.play()
            if px1 == 1:
                if p2.colliderect(p1):
                    hp1 -= 17
                    sounds.aaa2.play()
                    state = 2
                if p1.colliderect(w2) or p1.colliderect(h2):
                    hp2 -= 14
                    state = 2
                    sounds.awc.play()
            """walls disappearing"""
            if extw2 != 0:
                extw2 += 1
            if exth2 != 0:
                exth2 += 1
            if extw1 != 0:
                extw1 += 1
            if exth1 != 0:
                exth1 += 1
            if extw2 >= 121:
                extw2 = 0
                w2.y = -100
            if exth2 >= 121:
                exth2 = 0
                h2.x = -100
            if extw1 >= 121:
                extw1 = 0
                w1.y = -100
            if exth1 >= 121:
                exth1 = 0
                h1.x = -100
            """none of pxs business"""
            if hp1 <= 0 or hp2 <= 0:
                state = 1
                sounds.aaa.play()
                feeling += 7
                health += 7
                if hp1 <= 0:
                    p1.x, p1.y = -100, -100
                if hp2 <= 0:
                    p2.x, p2.y = -200, -200
        if state == 2:
            timer1 += 1
            if timer1 >= 30:
                state = 0
                timer1 = 0
                w1.y, w2.y, h1.x, h2.x = -100, -100, -100, -100
                pao1.x, pao1.y, pao2.x, pao2.y = -12432, -12324, -1422, -43242
                p1.x, p1.y, p2.x, p2.y = 100, 100, 700, 500# hit
def update():
    global ui,tmtea,tea,tmcy,huazi,tmfish,tmyg,dkt,cyt,savetimer,fishSide,fishSpeed,fishY,fishing,shoot,\
        X,Y,gofish,fish,side,health,feeling,exp,siui5,ygout,scoreyg,money,tmsleep,highsc,wait,ckrm,gmt#,\
    if feeling >= 140:
        feeling = 70
        exp += 25
    if feeling <= 15:
        feeling = 30
        exp -= 35
    if health <= 25:
        health = 40
        exp -= 45
        save()
    if health >= 140:
        health = 100
        exp += 25
        save()
    if savetimer < 61:
        savetimer+=1
        if savetimer//60==1:
            save()
            savetimer = 0
    else:
        savetimer = 0
    if ui == 3:
        if fish > 20:
            ui = 0
            music.stop()
            music.play('breaktime')
            sounds.tkwl.play()
        if tmfish == 0:
            if side == 'r' and kuai.right < 950:
                kuai.x += 3
                j.x += 3
            elif side == 'l' and kuai.left > 50:
                kuai.x -= 3
                j.x -= 3
        if not j.colliderect(fishe):
            if kuai.image != 'f2':
                kuai.image = 'f2'
            if tmfish > 0 and tmfish <= 540 // 6:
                tmfish += 1
                j.y += 6
            if tmfish > 540 // 6 and tmfish <= 540 // 6 * 2:
                j.y -= 6
                tmfish += 1
            if tmfish > 540 // 6 * 2:
                tmfish = 0
            if fishe.x in range(-46,1100):
                if fishing > gofish:
                    if fishSide == 'r':
                        fishe.x += fishSpeed
                    elif fishSide == 'l':
                        fishe.x -= fishSpeed
                else:
                    fishing += 1
            else:
                fishing = 0
                gofish = randint(60*3,60*8)
                fishSide = choice(['l','r'])
                fishSpeed = randint(4,12)
                fishY = randint(280,585)
                fishe.y = fishY
                if fishSide == 'r':
                    fishe.image = 'fishs'
                    fishe.x = -45
                else:
                    fishe.image = 'sfish'
                    fishe.x = 1095
        else:

            if j.y != 110:
                j.y -= 6
                tmfish = 0
                if kuai.image != 'f3':
                    kuai.image = 'f3'
                fishe.x,fishe.y = j.x,j.y
                fishing = 0
            else:
                fishe.x,fishe.y = -425,500
                gofish = randint(60 * 3, 60 * 8)
                fish += 1
                health += 5
                feeling += 5
                exp += 5
                fishing = 0
    if ui == 5:
        if ckrm ==0:
            aim.image = 'stop'
        if shoot:
            if chalk.colliderect(jyg):
                tmyg = 1
                ygout = randint(69-(scoreyg//15),219-(scoreyg//15))
                jyg.x, jyg.y = -123, -321
                if jyg.image == 'yg1':
                    scoreyg -= 10
                    if money > 10:
                        money -= 10
                        feeling -= 3
                        sounds.tkwl.play()
                    tmsleep = 0
                elif jyg.image == 'yg4':
                    scoreyg += 5
                    feeling += 2
                    sounds.b.play()
                    money += 15
                else:
                    scoreyg += 1
                    feeling += 3
                    sounds.a.play()
            if chalk.x<X+5 and chalk.x > X -5:
                shoot = False
                chalk.x,chalk.y = kuai.x+40,kuai.y
            else:
                chalk.x += (X + 19 - chalk.x) / (10+(120-wait)//30)
            if chalk.y<Y+5 and chalk.y > Y -5:
                shoot = False
                chalk.x, chalk.y = kuai.x+40,kuai.y
            else:
                chalk.y += (Y + 19 - chalk.y) / (10+(120-wait)//30)
        if tmsleep < 22:
            tmsleep += 1
        if ygout >= tmyg:
            tmyg += 1
        else:
            jyg.x,jyg.y = randint(150,800),randint(50,600)
            ygout = ygout + wait+25
            if wait > 20:
                wait -= (scoreyg//50)/2
            jyg.image = choice(['yg0','yg1','yg2','yg3','yg4','yg1','yg2','yg0','yg3'])
        if scoreyg%10==0:
            money += 12
            scoreyg += 1
    if ui == 114514:
        # manage()
        # sendD()
        # recvD()
        try:
            sendD()
            recvD()
        except Exception as err:
            connected = False
            print("Connection lost. Returning to home page..")
            print("The reason of connection loss:", err) if err != OSError else print(
                "Connection was closed by the user.")
            sock.close()
            ui = 0
            state = -1
            save()
            sellY.x, sellTea.x, sellTea.y, sellY.y = -460, -460, -490, -90
            stop.x, stop.y = -321, -123
            sellF.x, sellF.y = 1333, 233
            sellck.x, sellck.y = -131, -323
            tofish.x, tofish.y = -231, -1111
            torun.x, torun.y = -132, -2222
            tofight.x, tofight.y = -12314, -12
            aim.x, aim.y = -123, -321
            chalk.x, chalk.y = -123, -321
            j.x, j.y = -2312, -222
            kuai.image = "1"
            kuai.x, kuai.y = 510, 330
            jyg.x, jyg.y = -123, -321
            p1.x = -1231
            p2.x = -1231
            w1.y = -1231
            w2.y = -1231
            h1.x = -1231
            h2.x = -1231
            pao1.x = -1231
            pao2.x = -1231
            if dkt >= 7 or tea < 1:
                pass
            else:
                drinktea.x, drinktea.y = 230, 333
            if cyt >= 7 or huazi < 1:
                pass
            else:
                cy.x, cy.y = 750, 333
        ui114514()
        # time.sleep(0.5)
    if tmtea > 0:
        tmtea += 1
        if tmtea >= 81:
            tmtea = 0
            drinktea.x,drinktea.y = 230,333
            if dkt >= 7 or tea < 1:
                drinktea.x, drinktea.y = -123, -321
    if tmcy > 0:
        tmcy += 1
        if tmcy >= 81:
            tmcy = 0
            cy.x,cy.y = 750, 333
            if cyt >= 7 or huazi < 1:
                cy.x, cy.y = -123, -321
    if ui == 0:
        bk.x, bk.y = -900, 600
        kuai.x, kuai.y = 510, 330
        buttom1.x, buttom1.y = 900, 140
        but2.x, but2.y = 900, 200
    elif ui == 1 or ui == 2:
        kuai.x, kuai.y = -500, -320
        buttom1.x, buttom1.y = -900, -140
        but2.x, but2.y = -900, -200
        drinktea.x,drinktea.y = -123,-321
        cy.x, cy.y = -123, -321
        if ui == 1:
            pass
        else:
            xcb.x,xcb.y = 120,290
    if ui != 0:
        bk.x,bk.y = 920,615
    if ui != 2:
        xcb.x, xcb.y = -120, -230
    if ui != 3 and ui != 5:
        fishe.x = -3333
        j.x,j.y = -123,-333
        kuai.image = '1'
    if scoreyg > highsc:
        highsc = scoreyg
def draw():
    global ui,name,say,exp,scoreyg,tmsleep,highsc,ckrm,state
    buttom1.draw()
    but2.draw()
    screen.fill((12,13,14))
    if ui == 0:
        screen.draw.text(name, pos=(10, 0), fontname='a',color='blue')
        screen.draw.text("经验值：%s"%(exp), pos=(10, 27), fontname='a')
        screen.draw.text("心情：%s" % (feeling), pos=(10, 54), fontname='a')
        screen.draw.text(say,(300,500),fontname='a',fontsize=30,color='red')
        screen.draw.text("钱：%s" % (money), pos=(10, 81), fontname='a')
        screen.draw.text("健康：%s" % (health), pos=(10, 108), fontname='a')
    if ui == 2:
        screen.draw.text('娲石百货', (750, 30), fontname='a',fontsize=60,color='red')
        screen.draw.text("豆浆：10",(290,100),fontname='a')
        screen.draw.text("巧克力棒：5", (290, 500), fontname='a')
        screen.draw.text("娲石757：30", (257, 300), fontname='a')
        screen.draw.text("卖鱼：4",(720,280), fontname='a',color='grey')
        screen.draw.text("钱：%s" % (money), pos=(10, 100), fontname='a')
        screen.draw.text("还有%s杯茶" % (tea), pos=(10, 2), fontname='a')
        screen.draw.text("还有%s根巧克力棒" % (huazi), pos=(10, 27), fontname='a')
        screen.draw.text('还有%s条鱼'%(fish),(10,54),fontname='a')
        screen.draw.text('还有%s架飞机'%(ckrm),(10,79),fontname='a')
    if ui == 3:
        screen.draw.text(r"鱼：%s/21 条"%(fish),(10,1),fontname='a',color='orange')
        screen.draw.text("经验值：%s" % (exp), pos=(10, 27), fontname='a')
        screen.draw.text("健康：%s" % (health), pos=(10, 54), fontname='a')
        screen.draw.text("心情：%s" % (feeling), pos=(10, 79), fontname='a')
    if ui == 5:
        if tmsleep < 22:
            screen.fill((222,6,5))
        else:
            screen.fill((12,13,14))
        screen.draw.text("命中次数：%s" % (scoreyg), (10, 1), fontname='a', color='skyblue')
        screen.draw.text("剩余飞机数：%s" % (ckrm), (10, 28), fontname='a', color='darkgreen')
        screen.draw.text("钱：%s" % (money), pos=(10, 55), fontname='a')
        screen.draw.text("经验值：%s" % (exp), pos=(10, 80), fontname='a')
        screen.draw.text("心情：%s" % (feeling), pos=(10, 101), fontname='a')
    if ui == 114514:
        if state == 0:
            screen.fill((89, 189, 192))
            if tp1 <= 300:
                screen.draw.text("LOADED", (p1.x - 27, p1.y - 50), fontname='a', fontsize=18, color='orange',
                                 gcolor='black')
            if tp2 <= 300:
                screen.draw.text("LOADED", (p2.x - 27, p2.y - 50), fontname='a', fontsize=18, color='#18D7B8',
                                 gcolor='black')
        screen.draw.text("Player 1: %s" % (hp1), (895, 8), fontname='a', fontsize=16)
        screen.draw.text("Player 2: %s" % (hp2), (895, 28), fontname='a', fontsize=16)
        if state == 1:
            screen.fill((255 - 109, 255 - 109, 255 - 102))
            screen.draw.text("Press Enter to start again...", (259, 240), fontname='a', fontsize=40)
            screen.draw.text("Winner", (p1.x - 27, p1.y - 50), fontname='a', fontsize=18, color='orange',
                             gcolor='black')
            screen.draw.text("Winner", (p2.x - 27, p2.y - 50), fontname='a', fontsize=18, color='#18D7B8',
                             gcolor='black')
        if state == 2:
            screen.fill((225, 25, 25))
    screen.draw.text("官网：https://github.com/NuclearBiologica",(732,635),fontname='a',fontsize=12)
    screen.draw.text("v3.1.4 Copyright (c) Micropuppy Corp. All right reserved.", (5, 635), fontname='a', fontsize=12)
    kuai.draw()
    buttom1.draw()
    but2.draw()
    bk.draw()
    xcb.draw()
    drinktea.draw()
    cy.draw()
    sellY.draw()
    sellF.draw()
    sellTea.draw()
    j.draw()
    fishe.draw()
    tofish.draw()
    torun.draw()
    tofight.draw()
    stop.draw()
    aim.draw()
    chalk.draw()
    jyg.draw()
    sellck.draw()
    p1.draw()
    p2.draw()
    w1.draw()
    w2.draw()
    h1.draw()
    h2.draw()
    pao1.draw()
    pao2.draw()
music.play("sf")
pgzrun.go()
