from tkinter import *
from random import choice, randint as rand

window = Tk()
window.title("SPACE INVADERS")

w=1000
h=700
level1=True
level2=False
level3=False
running=True
cheat=False
changing_level=False
health=100
e_x2=10
e_x3=1
list=[100,200,300,400,500,600,700,800,900]

p_ship=PhotoImage(file="player_ship.png")
p_ship=p_ship.subsample(9,9)
e_ship_1=PhotoImage(file="enemy_ship_1.png")
e_ship_1=e_ship_1.subsample(2,2)
e_ship_2=PhotoImage(file="enemy_ship_2.png")
e_ship_2=e_ship_2.subsample(2,2)
e_ship_3=PhotoImage(file="enemy_ship_3.png")
e_ship_3=e_ship_3.subsample(10,10)
fire_ball=PhotoImage(file="fireball.png")
fire_ball=fire_ball.subsample(5,5)
close=PhotoImage(file="exit_button.png")
close=close.subsample(3,3)
start=PhotoImage(file="start_button.png")
resume=PhotoImage(file="resume_button.png")
instructions=PhotoImage(file="instructions_button.png")
leaderboard=PhotoImage(file="leaderboard_button.png")
credits=PhotoImage(file="credits_button.png")
cross=PhotoImage(file="cross_button.png")
cross=cross.subsample(7,7)
instructions_page=PhotoImage(file="instructions.png")
credits_page=PhotoImage(file="credits.png")
bg=PhotoImage(file="bg.png")
boss=PhotoImage(file="boss.png")

canvas=Canvas(window,width=w,height=h,bg="black")
canvas.pack()

def left(event):
        p_coords=canvas.bbox(player_ship)
        if p_coords[0] > 10:
            canvas.move(player_ship,-10,0)

def right(event):
    global w
    p_coords=canvas.bbox(player_ship)
    if p_coords[2] < w-10:
        canvas.move(player_ship,10,0)
        
def up(event):
    p_coords=canvas.bbox(player_ship)
    if p_coords[1] > 10:
        canvas.move(player_ship,0,-10)

def down(event):
    global h
    p_coords=canvas.bbox(player_ship)
    if p_coords[3] < h-10:
        canvas.move(player_ship,0,10)

def bind_keys():
    window.bind("<Left>",left)
    window.bind("<Right>",right)
    window.bind("<Up>",up)
    window.bind("<Down>",down)
    window.bind("<space>",fire)
    window.bind("<Escape>",pause)

def unbind_keys():
    window.unbind("<Left>")
    window.unbind("<Right>")
    window.unbind("<Up>")
    window.unbind("<Down>")
    window.unbind("<space>")
    window.unbind("<Escape>")

def start_game():
    global canvas,score,level,lives,health,score_label,lives_label,ready_label,health_label,level1,level2,level3,p_coords,e_coords,b_coords,changing_level
    score=0
    lives=3
    health=100
    level=1
    level1=True
    level2=False
    level3=False
    changing_level=False
    p_coords=None
    e_coords=None
    b_coords=None
    canvas.destroy()
    canvas=Canvas(window,width=w,height=h,bg="black")
    canvas.pack()
    score_label=Label(canvas,bg="gray",width=8,height=1,text="Score: "+str(score),font=(50),fg="yellow")
    lives_label=Label(canvas,bg="gray",width=8,height=1,text="Lives: "+str(lives),font=(50),fg="yellow")
    bind_keys()
    c=["white","#fefefe","#fdfdfd"]
    for i in range(400):
        a=rand(1,w-1)
        b=rand(1,h-1)
        size=rand(2,5)
        f=rand(0,2)
        ab=(a,b,a+size,b+size)
        tmp_star=canvas.create_oval(ab,fill=c[f])
    ready_label=Label(canvas,bg="black",text="R E A D Y . . .",font=50,fg="yellow")
    ready_label.place(x=w//2-50,y=h//2)
    window.after(2000,gameloop)

def submit():
        global enter_name,score,file
        username=enter_name.get()
        file=open("leaderboard.txt","a")
        file.write(username)
        file.close()

def save_in_leaderboard():
    global file,score,username
    file=open("leaderboard.txt","a")
    file.write(":"+str(score)+",")
    file.close()

def display_leaderboard():
        global file,canvas_lb
        file=open("leaderboard.txt","r")
        c=[]
        l1=[]
        l2=[]
        p1=''
        s1=''
        p2=''
        s2=''
        p3=''
        s3=''
        for line in file:
                a=line.split(",")
                for i in a:
                    b=i.split(":")
                    c.append(b)
        file.close()
        try:
                if c[-1]==['']:
                    c.pop()
                for i in c:
                    l1.append(i[0])
                    l2.append(int(i[1]))

                s1=max(l2)
                for i in range(len(l2)):
                    if l2[i]==s1:
                        p1=l1[i]
                l1.remove(p1)
                l2.remove(s1)
                s2=max(l2)
                for i in range(len(l2)):
                    if l2[i]==s2:
                        p2=l1[i]
                l1.remove(p2)
                l2.remove(s2)
                s3=max(l2)
                for i in range(len(l2)):
                    if l2[i]==s3:
                        p3=l1[i]
                l1.remove(p3)
                l2.remove(s3)
        except:
                pass
        canvas_lb=Canvas(canvas,width=300,height=400,bg="black")
        canvas_lb.place(x=350,y=170)
        cross_button=Button(canvas_lb,image=cross,command=close_canvas)
        cross_button.place(x=260,y=10,anchor=NW)
        canvas_lb.create_image(47,30,image=leaderboard,anchor=NW)
        canvas_lb.create_text(80,140,text=str(p1),font=("Arial Bold",20),fill="white")
        canvas_lb.create_text(80,240,text=str(p2),font=("Arial Bold",20),fill="white")
        canvas_lb.create_text(80,340,text=str(p3),font=("Arial Bold",20),fill="white")
        canvas_lb.create_text(240,140,text=str(s1),font=("Arial Bold",20),fill="white")
        canvas_lb.create_text(240,240,text=str(s2),font=("Arial Bold",20),fill="white")
        canvas_lb.create_text(240,340,text=str(s3),font=("Arial Bold",20),fill="white")

def display_credits():
    global canvas_credits
    canvas_credits=Canvas(canvas,width=800,height=450,bg="black")
    canvas_credits.place(x=100,y=170)
    cross_button=Button(canvas_credits,image=cross,command=close_canvas)
    cross_button.place(x=760,y=10,anchor=NW)
    canvas_credits.create_image(47,30,image=credits_page,anchor=NW)

def display_instructions():
    global canvas_instructions
    canvas_instructions=Canvas(canvas,width=650,height=700,bg="black")
    canvas_instructions.place(x=175,y=0)
    cross_button=Button(canvas_instructions,image=cross,command=close_canvas)
    cross_button.place(x=610,y=10,anchor=NW)
    canvas_instructions.create_image(47,30,image=instructions_page,anchor=NW)

def close_canvas():
    global canvas_lb,canvas_instructions,canvas_credits
    try:
        canvas_lb.destroy()
    except:
        pass
    try:
        canvas_instructions.destroy()
    except:
        pass
    try:
        canvas_credits.destroy()
    except:
        pass
    try:
        canvas_lb.destroy()
    except:
        pass

def start_screen():
    global start_button,exit_button,w,h,enter_name,submit_button,credits_button,instructions_button,lb_button
    canvas.create_image(0,0,anchor=NW,image=bg)
    start_button=Button(canvas,image=start,command=start_game)
    start_button.place(x=450,y=300)
    exit_button=Button(canvas,image=close,command=window.destroy)
    exit_button.place(x=575,y=300)
    lb_button=Button(canvas,image=leaderboard,command=display_leaderboard)
    lb_button.place(x=210,y=300)
    credits_button=Button(canvas,image=credits,command=display_credits)
    credits_button.place(x=70,y=300)
    instructions_button=Button(canvas,image=instructions,command=display_instructions)
    instructions_button.place(x=680,y=300)
    enter_name=Entry(canvas,width=15,font=10,bg="#B4B4B4")
    enter_name.place(x=390,y=200)
    submit_button=Button(canvas,text="Enter",font=("Arial Bold",10),bg="#B4B4B4",command=submit)
    submit_button.place(x=565,y=200)

def initial_state():
    global player_ship,changing_level,running
    changing_level=False
    running=True
    bind_keys()
    try:
        canvas.delete(level_text)
    except:
        pass
    try:
        ready_label.destroy()
    except:
        pass
    try:
        life_label.destroy()
    except:
        pass
    canvas.create_window(w-55,25,window=score_label)
    canvas.create_window(55,25,window=lives_label)
    player_ship=canvas.create_image(w/2-10,h-100,anchor=NW,image=p_ship)
    
def lose_message():
    global w,h,start_button,exit_button
    save_in_leaderboard()
    lose_label=Label(canvas,text="YOU LOST!",bg="grey",font=(100))
    canvas.create_window(w//2,h//2,window=lose_label)
    start_button=Button(canvas,image=start,command=start_game)
    start_button.place(x=400,y=400)
    exit_button=Button(canvas,image=close,command=window.destroy)
    exit_button.place(x=550,y=400)
    
def collision():
    global p_coords,e_coords
    p_coords=canvas.bbox(player_ship)
    e_coords=canvas.bbox(enemy_ship)
    if (e_coords[2] >= p_coords[2] >= e_coords[0] or e_coords[2] >= p_coords[0] >= e_coords[0]) and (e_coords[1] <= p_coords[1] <= e_coords[3] or e_coords[1] <= p_coords[3] <= e_coords[3]):
        return True
    else:
        return False

def enemy_motion():
    global enemy_ship,e_coords,h,motion,lives,w,running,changing_level,life_label,e_x2,e_x3
    window.bind("<f>",freeze)
    window.bind("<r>",revive)
    if not level3:
        window.bind("<s>",straight_to_the_final)
    if running==True and changing_level==False:
            bind_keys()
            e_coords=canvas.bbox(enemy_ship)
            if collision() or e_coords[3]>=h:
                unbind_keys()
                canvas.delete(player_ship)
                canvas.delete(enemy_ship)
                try:
                    canvas.delete(bullet)
                except:
                    pass
                lives-=1
                lives_label.config(text="Lives: "+str(lives))
                if lives==0:
                    lose_message()
                else:
                    life_label=Label(canvas,bg="black",text=str(lives)+"  L I V E S   R E M A I N I N G",font=50,fg="yellow")
                    life_label.place(x=w//2-120,y=h//2)
                    if lives==1:
                        life_label.config(text="1   L I F E   R E M A I N I N G")
                    window.after(3000,gameloop)
            else:
                if level1:
                    canvas.move(enemy_ship,0,3)
                elif level2:
                    if e_coords[2]>=w:
                        e_x2=-10
                    elif e_coords[0]<=0:
                        e_x2=10
                    canvas.move(enemy_ship,e_x2,2)
                elif level3:
                    if e_coords[2]>=w:
                        e_x3=-1
                    elif e_coords[0]<=0:
                        e_x3=1
                    canvas.move(enemy_ship,e_x3,0)
                window.after(15,enemy_motion)

def shoot_fireball():
    global running,fireball,lives,h,lives_label,b_coords,bullet,score,score_label,cheat
    if running==True and cheat==False:
            f_coords=canvas.bbox(fireball)
            b_coords=canvas.bbox(bullet)
            try:
                    if (f_coords[2] >= p_coords[2] >= f_coords[0] or f_coords[2] >= p_coords[0] >= f_coords[0]) and (f_coords[1] <= p_coords[1] <= f_coords[3] or f_coords[1] <= p_coords[3] <= f_coords[3]):
                        unbind_keys()
                        canvas.delete(player_ship)
                        canvas.delete(fireball)
                        lives=0
                        lives_label.config(text="Lives: "+str(lives))
                        running=False
                        lose_message()
            except:
                    pass
                
            else:
                try:
                        if (f_coords[2] >= b_coords[2] >= f_coords[0] or f_coords[2] >= b_coords[0] >= f_coords[0]) and (f_coords[1] <= b_coords[1] <= f_coords[3] or f_coords[1] <= b_coords[3] <= f_coords[3]):
                            score+=3
                            score_label.config(text="Score: "+str(score))
                            canvas.delete(fireball)
                            canvas.delete(bullet)
                            generate_fireball()
                except:
                        pass
                if f_coords[3]>=h:
                    canvas.delete(fireball)
                    generate_fireball()
                else:
                    canvas.move(fireball,0,3)
                    window.after(50,shoot_fireball)
        
def generate_fireball():
    global fireball,e_coords,lives,cheat
    if running==True and level3==True and cheat==False:
        e_coords=canvas.bbox(enemy_ship)
        fireball=canvas.create_image((e_coords[0]+e_coords[2])/2-50,e_coords[3],anchor=NW,image=fire_ball)
        shoot_fireball()    
        
    
def generate_enemy_ship():
    global enemy_ship,level1,level2,level3,health,w,health_label
    e_x=choice(list)
    if level1:
        enemy_ship=canvas.create_image(e_x,50,anchor=NW,image=e_ship_1)
    elif level2:
        enemy_ship=canvas.create_image(e_x,50,anchor=NW,image=e_ship_2)
    elif level3:
        health_label=Label(canvas,bg="cyan",width=10,height=1,text="Health: "+str(health),font=(50),fg="red")
        health_label.place(x=w//2,y=25)
        enemy_ship=canvas.create_image(e_x,50,anchor=NW,image=e_ship_3)
        window.after(5000,generate_fireball)


def change_level():
    global level1,level2,level3,level_text
    if level1==True:
        level1=False
        level2=True
        level=2
    elif level2==True:
        level2=False
        level3=True
        level=3
    running=False
    unbind_keys()
    canvas.delete(player_ship)
    level_text=canvas.create_text(w//2,h//2,text="L E V E L   "+str(level),font=50,fill="yellow")
    window.after(3000,gameloop)

def win():
    global w,h,start_button,exit_button
    running=False
    unbind_keys()
    canvas.delete(enemy_ship)
    win_label=Label(canvas,text="YOU WIN!",bg="grey",font=(100))
    canvas.create_window(w//2,h//2,window=win_label)
    start_button=Button(canvas,image=start,command=start_game)
    start_button.place(x=500,y=200)
    exit_button=Button(canvas,image=close,command=window.destroy)
    exit_button.place(x=440,y=390)
        
def bullet_motion(bullet):
    global score,running,level2,changing_level,health,health_label,cheat
    if (running==True and cheat==False) or (running==False and cheat==True):
        try:
            if hit(bullet):
                canvas.delete(bullet)
                score+=1
                score_label.config(text="Score: "+str(score))
                if score==5 or score==10:
                    changing_level=True
                    change_level()
                else:
                    if level3:
                        health-=5
                        health_label.config(text="Health: "+str(health))
                        if health==0:
                            win()
                    else:
                        generate_enemy_ship()
            else:
                if b_coords[1]<=0:
                    canvas.delete(bullet)
                else:
                    canvas.move(bullet,0,-5)
                    window.after(5,lambda :bullet_motion(bullet))
        except:
            pass
        
def fire(event):
    global p_coords,bullet
    p_coords=canvas.bbox(player_ship)
    bullet=canvas.create_oval((p_coords[0]+p_coords[2])/2-2.5,p_coords[1]-20,(p_coords[0]+p_coords[2])/2+2.5,p_coords[1],fill="yellow")
    bullet_motion(bullet)

def hit(bullet):
    global b_coords
    b_coords=canvas.bbox(bullet)
    if (e_coords[2] >= b_coords[2] >= e_coords[0] or e_coords[2] >= b_coords[0] >= e_coords[0]) and (e_coords[1] <= b_coords[1] <= e_coords[3] or e_coords[1] <= b_coords[3] <= e_coords[3]):
        if not level3:
            canvas.delete(enemy_ship)
        return True
    else:
        return False

def restart():
    global running
    running=True
    resume_button.destroy()
    exit_button.destroy()
    start_game()

def unpause():
    try:
        enemy_motion()
    except:
        pass
    try:
        bullet_motion(bullet)
    except:
        pass
    try:
        shoot_fireball()
    except:
        pass
    
def countdown(count,counter):
    global running
    running=True
    counter.config(text=str(count))
    if count>0:
        window.after(1000,lambda :countdown(count-1,counter))
    elif count==0:
        counter.config(text="GO!")
        window.after(1000,lambda :countdown(count-1,counter))
    elif count<0:
        counter.destroy()
        unpause()
    
def pause(event):
    global running,resume_button,exit_button,timer
    running=not running
    if running:
        resume_button.destroy()
        exit_button.destroy()
        timer=Label(canvas,bg="black",fg="yellow",font=50)
        timer.place(x=w//2,y=h//2)
        countdown(3,timer)        
    else:
        unbind_keys()
        window.bind("<Escape>",pause)
        resume_button=Button(canvas,image=resume,highlightbackground="black",command=lambda :pause(event))
        resume_button.place(x=440,y=300)
        exit_button=Button(canvas,image=close,highlightbackground="black",command=window.destroy)
        exit_button.place(x=440,y=390)

def boss_key(event):
    global running,bullet,canvas2
    running=not running
    if running:
        canvas2.destroy()
        timer=Label(canvas,bg="black",fg="yellow",font=50)
        timer.place(x=w//2,y=h//2)
        countdown(3,timer)
    else:
        unbind_keys()
        canvas2=Canvas(window,width=1000,height=700)
        boss_label=Label(canvas2,image=boss)
        canvas2.create_window(0,0,anchor=NW,window=boss_label)
        canvas2.place(relx=0,rely=0)

def unfreeze():
    global running,cheat
    running=True
    cheat=False
    enemy_motion()
    try:
        shoot_fireball()
    except:
        pass

def freeze(event):
    global running,cheat
    running=False
    cheat=True
    window.unbind("<f>")
    window.after(5000,unfreeze)

def straight_to_the_final(event):
    global level1,level2,level3,level,enemy_ship
    level=3
    level1=False
    level2=False
    level3=True
    canvas.delete(enemy_ship)
    generate_enemy_ship()

def revive(event):
    global lives,lives_label
    lives=3
    lives_label.config(text="Lives: "+str(lives))

def gameloop():
    initial_state()
    generate_enemy_ship()
    enemy_motion()

start_screen()
window.bind("<b>",boss_key)

window.mainloop()
