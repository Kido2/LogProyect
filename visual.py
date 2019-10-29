from PIL import Image,ImageDraw,ImageFont

def checkSquare(draw,fontobject,square,name,color):
    '''a DrawImage.Draw object to draw on,font object,
    Receives a number from 1-20, name and color (RRR,GGG,BBB)
    and checks square with that
    color and sets name on it '''
    if square < 11: #Before Lunch
        square_y = (square-1)//5
        square_x = (square-1)%5

        if color != (255,255,255):
            draw.rectangle([(square_x*100+100,square_y*70+70),(square_x*100+200,square_y*70+140)],fill=color)

        x = square_x*100+100
        y = square_y*70+70


    else: #Post-Lunch
        square_y = (square-1)//5
        square_x = (square-1)%5

        square_y += 1#We skipping lunch so y+1

        if color != (255,255,255):
            draw.rectangle([(square_x*100+100,square_y*70+70),(square_x*100+200,square_y*70+140)],fill=color)

        x = square_x*100+100
        y = square_y*70+70


    draw.text((x+20,y+20),name,(0,0,0),font=fontobject) #black text

def checkSignature(draw,fontobject,number,color):
    '''Same as checkSquare but for square 41, 42, 43 and 44 '''
    number -= 41 #Number is now 0,1,2,3
    square_y = (number)//2
    square_x = (number)%2

    if color != (255,255,255):
        draw.rectangle([(square_x*100+700,square_y*70+210),(square_x*100+800,square_y*70+280)],fill=color)

    x = square_x*100+700
    y = square_y*70+210

    draw.text((x+30,y+15),'X',(0,0,0),font=fontobject)




'''Changeable Variables '''
signature1 = 'Kurt'
signature2 = 'Bernand'
professor1 = 'Lógica I'
professor2 = 'Lógica II'
filename = 'test' #nombre de .jpg a salir


def export_horario(diccionario,professor1,professor2,signature1,signature2,filename):

    filename += '.jpg' #Para que sea una imagen
    '''Se crea la base del horario, es decir el horario vacío '''

    '''Define Some const'''
    width = 900
    height = 420

    smallfont = ImageFont.truetype('Arial.ttf',20)
    mediumfont = ImageFont.truetype('Arial.ttf',30)
    bigfont = ImageFont.truetype('Arial.ttf',40)

    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)

    lightblue = (46, 167, 198)
    lightgreen = (155, 203, 72)
    lightred = (232, 58, 42)

    red = (255, 0, 0)
    green = (0,128,0)

    '''Actual Colors '''

    image = Image.new('RGB',(width,height),white)
    draw = ImageDraw.Draw(image) #Allows us to draw

    #5 initial horizontal lines
    for i in range(1,6):
        draw.line([55,i*70,600,i*70],black,width=3)

    #draw horizontal last line
    draw.line([55,417,600,417],black,width=3)

    #draw schedule vertical lines
    for i in range(1,7):
        draw.line([100*i,30,100*i,417],black,width=3)


    #draw signature vertical lines
    for i in range(2):
        draw.line([700+100*i,170,700+100*i,350],black,width=3)

    #draw signature last line
    draw.line([897,170,897,350],black,width=3)

    #draw signature horizontal lines
    for i in range(1,4):
        draw.line([640,140+70*i,900,140+70*i],black,width=3)

    #Draw Mon Tue Wed... text

    draw.text((125,35),"Lunes",black,font=smallfont)
    draw.text((220,35),"Martes",black,font=smallfont)
    draw.text((310,35),"Miércoles",black,font=smallfont)
    draw.text((420,35),"Jueves",black,font=smallfont)
    draw.text((515,35),"Viernes",black,font=smallfont)

    counter = 0
    for time in ['7AM','9AM','11AM','1PM','3PM']:

        draw.text( (0,70*(counter+1)-10),time,black,font=smallfont)
        counter+=1

    #draw last 5pm
    draw.text((0,400),'5PM',black,font=smallfont)


    #draw professor names and signature names
    draw.text((705,175),professor1,black,font=smallfont)
    draw.text((805,175),professor2,black,font=smallfont)

    draw.text((605,230),signature1,black,font=smallfont)
    draw.text((605,300),signature2,black,font=smallfont)

    #Do Lunch Line
    draw.rectangle([(100,210),(600,280)],fill=lightred)
    draw.text((280,220),'Almuerzo',font=bigfont,fill=black)

    ''' Se ha creado la base del Horario, Lineas nombres, horas, pero vacio '''

    # ----- Código que Añade las horas respectivas Carlos, Aqui. ---NO TOCAR otras secciones de codigo

    for x in diccionario.keys():
        if diccionario[x]==1:
            if x<=20:
                checkSquare(draw,smallfont,   x , professor1, lightblue)
            elif x>20 and x<41:
                x=x-20
                checkSquare(draw,smallfont,   x , professor2, lightblue)
            else:
                checkSignature(draw,bigfont,     x    ,lightblue)









    #Se guarda la imagen
    image.save(filename)








