#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint
from Tkinter import *
from collections import OrderedDict
from tkinter import *
import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2


# In[ ]:





# In[ ]:


#constructs a basic window, sets title, geometry
#window = Tk()
#window.title("Estudio Application") 
#window.geometry('350x200')
#main_window_geometry = [350, 200]
#center_x= (main_window_geometry[0])/2 
#print center_x
#window.mainloop()
#trying to implement foreign class for switch_frame which destroys a frame and switches to another
#edit, frame is no longer destoryed, it is replaced
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Spedish')
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("650x400")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(300, weight=1)
        container.grid_columnconfigure(300, weight=1)
        


        self.frames = {}
        for F in (MainMenu, StartPage, OptionsPage, Flashcards, BasicQuestions, Lessons, ComplexQuestions,
                 ):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    #def close_window(self, page_name):
        #'''Destroy a frame for the given page name'''
        #frame = self.frames[page_name]
        #frame.destroy()
        
class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        label = tk.Label(self, text="Main Menu", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Start",
                            command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Options",
                            command=lambda: controller.show_frame("OptionsPage"))
       
        
        button1.pack()
        button2.pack()
        
        #button that closes application
        #btn_op_exit = tk.Button(self, text="Exit", 
        #                     bg="red", 
        #                     fg="black",  
        #                     activebackground="green",
        #                     command=lambda: controller.close_window(""))
        #btn_op_exit.grid(column=center_x, row=6)
        #btn_op_exit.place(x=175, y=130, anchor="center")
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Start Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Main Menu",
                           command=lambda: controller.show_frame("MainMenu"))
        button1.pack()
        button2 = tk.Button(self, text="Flashcards",
                           command=lambda: controller.show_frame("Flashcards"))
        
        button2.pack()
        button2 = tk.Button(self, text="Basic Questions",
                           command=lambda: controller.show_frame("BasicQuestions"))
        
        button2.pack()
        button3 = tk.Button(self, text="Lessons",
                           command=lambda: controller.show_frame("Lessons"))
        
        button3.pack()
        button4 = tk.Button(self, text="Complex Questions",
                           command=lambda: controller.show_frame("ComplexQuestions"))
        
        button4.pack()


class OptionsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Options Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Main Menu",
                           command=lambda: controller.show_frame("MainMenu"))
        button.pack()

class Flashcards(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        label = tk.Label(self, text="Flashcards", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
        
class BasicQuestions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        label = tk.Label(self, text="Basic Questions", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
class Lessons(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        label = tk.Label(self, text="Lessons", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class ComplexQuestions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        label = tk.Label(self, text="Complex Questions", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()




#lb_op = Label(window, text="Welcome to Estudio", font=("Arial Bold", 20))
#lb_op.grid(column=0, row=0)
#lb_op.place(x=175, y=20, anchor="center")

#creates button which will progress towards the secondary menu, sets position on window
#btn_op_start = Button(window, text="Start", 
#                      bg="red", 
#                      fg="black", 
#                      relief=RAISED, 
#                      activebackground="green"                    
#                     )
#btn_op_start.grid(column=center_x, row=4)
#btn_op_start.place(x=175, y=70, anchor="center")

#creates button which progresses towards a menu possessing options for the user to change
#btn_op_options = Button(window, text="Options", 
#                        bg="yellow", 
#                        fg="black", 
#                        relief=RAISED, 
#                        activebackground="green",                      
#                       )
#btn_op_options.grid(column=center_x, row=5)
#btn_op_options.place(x=175, y=100, anchor="center")

#function called by exit application buttons which will close the window
#def close_window(): 
#    window.destroy()
#button that closes application
#btn_op_exit = Button(window, text="Exit", 
#                     bg="red", 
#                     fg="black", 
#                     relief=RAISED, 
#                     activebackground="green",
#                    command=close_window)
#btn_op_exit.grid(column=center_x, row=6)
#btn_op_exit.place(x=175, y=130, anchor="center")


# In[ ]:


lessons = ('basic vocab', 'gender of words', 'demonstrative', 'word order agreement',
           'present tense & irregulars/stem changers', 'ser vs estar',
           'posessive pronouns', 'reflexive verbs', 'verbs like gustar',
           'gerund & progressive', 'adverbs', 'superlatives', 'preterite & car,gar,zar', 'imperfect',
           'hacer/past participle', 'conditional & irregulars', 'passive voice',
           'impersonal se', 'commands', 'present perfect', 'subjunctive')
           
vocabulary = ('school work', 'greetings & personal info', 'descriptions', 'numbers', 'family',
              'health', 'class subjects', 'hobbies', 'routines', 'navigation',
              'art', 'science & technology', 'medical', 'society', 'government',
              'nature', 'activities')
              
class vocabulary_Lesson():
  #Displays a list of spanish words and their english translation
  def __init__(self, subject, contents):
    self.sub = subject
    self.con = contents
    #subject refers to an entry made in the vocabulary tuple
    
  def print_Subject(self):
    print ('This unit\'s topic is: ' + self.sub)
  
  def display_Contents(self):
    for k, v in self.con.iteritems():
       print(k, v)
      
  def start_Flashcards(self):
    print ('Please enter the number of the mode of practice: \n1: Spanish to English \n2: English to Spanish \n3: Mixed')
    mode = input()
    tries = 0 #tries tracks the amount of incorrect guesses
    if ((mode != 1) and (mode != 2) and (mode != 3)):
      print ('Error: Please enter a valid number for the mode of practice:')
      self.start_Flashcards()
      
    elif (mode == 1):
      tries = 0
      words = -1
      for key in self.con:
        words = words + 1
        print (key)
        print ('Please enter the English translation of the above word: ')
        print ('To stop the exercise at any time, enter: Stop')
        response = raw_input()
        if (response.lower() == 'stop'):
          break
        elif (response.lower() != self.con[key].lower()):
          tries = tries + 1
          sec_response = raw_input('Incorrect, please try again.\n')
          if (sec_response.lower() == 'stop'):
            break
          elif (sec_response.lower() != self.con[key].lower()):
            tries = tries + 1
            print ('Incorrect, the correct answer is: ' + self.con[key])
      print ('You have passed through ' + str(words) + ' words with ' + str(tries) + ' error(s).')      
      
    elif (mode == 2):
      tries = 0
      words = -1
      for key in self.con:
        words = words + 1
        print (self.con[key])
        print ('Please enter the Spanish translation of the above word: ')
        print ('To stop the exercise at any time, enter: Stop')
        response = raw_input()
        if (response.lower() == 'stop'):
          break
        elif (response.lower() != key.lower()):
          tries = tries + 1
          sec_response = raw_input('Incorrect, please try again.\n')
          if (sec_response.lower() == 'stop'):
            break
          elif (sec_response.lower() != key.lower()):
            tries = tries + 1
            print ('Incorrect, the correct answer is: ' + key)
      print ('You have passed through ' + str(words) + ' words with ' + str(tries) + ' error(s).')  
            
    #mixed Spanish and English    
    elif (mode == 3):
      tries = 0
      words = -1
      for key in self.con:
        words = words + 1
        determiner = randint(0,1)
        if (determiner == 0):
          print (self.con[key])
        else:
          print (key)
        print ('Please enter the translation of the above word: ')
        print ('To stop the exercise at any time, enter: Stop')
        response = raw_input()
        if (response.lower() == 'stop'):
          break
        elif ( ((determiner != 0) and (sec_response.lower() != self.con[key].lower())) or ((determiner != 1) and (sec_response.lower() != key.lower())) ):
          tries = tries + 1
          sec_response = raw_input('Incorrect, please try again.\n')
        elif (sec_response.lower() == 'stop'):
            break
        if ( ((determiner != 0) and (sec_response.lower() != self.con[key].lower())) or ((determiner != 1) and (sec_response.lower() != key.lower())) ):
            tries = tries + 1
            print ('Incorrect, the correct answer is: ' + key + ' <-> ' + self.con[key])
        print ('You have passed through ' + str(words) + ' words with ' + str(tries) + ' error(s).')

        
class grammer_Lesson():
  
  def __init__(self, subject):
    self.sub = subject


# In[ ]:


#Vocabulary lesson topics and dictionaries

words_School_Work = OrderedDict([('Tarea', 'Homework'), ('Libro', 'Book'), ('Clase', 'Class'), ('Semestre', 'Semester'),
                    ('Tomar apuntes', 'To take notes'), ('Suspender', 'To fail'), ('Universidad', 'University'),
                    ('Cursos', 'Courses'), ('Director', 'Principle'), ('Estudiar', 'To study'),
                    ('Maestro', 'Teacher'), ('Profesor', 'Professor'), ('Consejero', 'Guidance counselor'),
                    ('Detalle', 'Detail'), ('Escribir', 'To write'), ('Prestar atención', 'To pay attention'),
                    ('Papel', 'Paper'), ('Ensayo', 'Essay'), ('Proyecto', 'Project'), ('Leer', 'To read'),
                    ('Periodo', 'Period'), ('Problema', 'Problem'), ('Tema', 'Subject'), ('Razón', 'Reason'),
                    ('Correcto', 'Corect'), ('Fuente', 'Source'), ('Escuela', 'School'), ('Lápiz', 'Pencil'),
                    ('Libro', 'Book'), ('Cuaderno', 'Notebook'), ('Escritorio', 'Desk'), ('Computadora', 'Computer'),
                    ('Pluma', 'Pen'), ('Examen', 'Exam'), ('Prueba', 'Quiz'), ('Lección', 'Lesson'), ('Diploma', 'Diploma'),
                    ('Título', 'Degree'), ('Diccionario', 'Dictionary')])


words_Greetings = OrderedDict([('Hola', 'Hello'), ('¿Qué tal?', 'What\'s up'), ('Buenas días', 'Good morning'),
                  ('Buenas tardes', 'Good afternoon'), ('Buenas noches', 'Good evening'),
                  ('Me llamo', 'My name is'), ('¿Y usted?', 'And you?'), ('Lo siento', 'Sorry'),
                  ('Mucho gusto', 'Nice to meet you'), ('Encantado', 'Pleased to meet you'), ('Muy bien', 'Very well'),
                  ('Sí', 'Yes'), ('No', 'No'), ('Hasta mañana', 'See you tomorrow'), ('Hasta luego', 'See you later'),
                  ('Adiós', 'Goodbye'), ('Gracias', 'Thank you'), ('Muchas gracias', 'Thank you very much'),
                  ('Bienvenidos', 'Welcome'), ('Yo soy de', 'I am from')])

words_Descriptions = OrderedDict([('Gran', 'Large'), ('Bueno', 'Good'), ('Inteligente', 'Intelligent'), ('Gracioso', 'Funny'),
                     ('Loco', 'Crazy'), ('Brillante', 'Bright'), ('Adolescente', 'Adolescent'), ('Serio', 'Serious'),
                     ('Amable', 'Pleasant'), ('Divertido', 'Fun'), ('Antipático', 'Mean'), ('Estúpido', 'Stupid'),
                     ('Genuino', 'Genuine'), ('Feliz', 'Happy'), ('Malo', 'Bad'), ('Perfecto', 'Perfect'),
                     ('Triste', 'Sad'), ('Alto', 'Tall'), ('Bajo', 'Short'), ('Grande', 'Big'), ('Pequeño', 'Small'),
                     ('Simple', 'Simple'), ('Complicado', 'Complicated'), ('Aburrido', 'Boring'), ('Nuevo', 'New'),
                     ('Viejo', 'Old'), ('Rico', 'Rich'), ('Pobre', 'Poor'), ('Caluroso', 'Hot'), ('Frió', 'Cold'),
                     ('Caro', 'Expensive'), ('Barato', 'Cheap'), ('Rápido', 'Fast'), ('Lento', 'Slow'), ('Tarde', 'Late'),
                     ('Tempraño', 'Early'), ('Fuerte', 'Strong'), ('Débil', 'Weak'), ('Enfermo', 'Sick'),
                     ('Sano', 'Healthy'), ('Limpio', 'Clean'), ('Sucio', 'Dirty'), ('Junto', 'Together'),
                     ('Solo', 'Alone'), ('Injusto', 'Unfair'), ('Justo', 'Fair')])

words_Numbers = OrderedDict([('Número', 'Number'), ('Primo', 'Prime'), ('Par', 'Even'), ('Impar', 'Odd'), ('Cero', 'Zero'),
                ('Uno', 'One'), ('Dos', 'Two'), ('Tres', 'Three'), ('Cuatro', 'Four'), ('Cinco', 'Five'),
                ('Seis', 'Six'), ('Siete', 'Seven'), ('Ocho', 'Eight'), ('Nueve', 'Nine'), ('Diez', 'Ten'),
                ('Once', 'Eleven'), ('Doce', 'Twelve'), ('Trece', 'Thirteen'), ('Catorce', 'Fourteen'),
                ('Quince', 'Fifteen'), ('Dieciséis', 'Sixteen'), ('Diecisiete', 'Seventeen'),
                ('Dieciocho', 'Eighteen'), ('Diecinueve', 'Nineteen'), ('Veinte', 'Twenty'),
                ('Veintiuno', 'Twenty one'), ('Veintidos', 'Twenty dos'), ('Treinta', 'Thirty'),
                ('Treinta y uno', 'Thirty one'), ('Cuarenta', 'Fourty'), ('Cuarenta y uno', 'Fourty one'),
                ('Cincuenta', 'Fifty'), ('Sesenta', 'Sixty'), ('Setenta', 'Seventy'), ('Ochenta', 'Eighty'),
                ('Noventa', 'Ninety'), ('Cien', 'Hundred'), ('Ciento uno', 'Hundred and one'), 
                ('Doscientos', 'Two hundred'), ('Trescientos', 'Three hundred'), ('Quincientos', 'Five hundred'),
                ('Setecientos', 'Seven hundred'), ('Novescientos', 'Nine hundred'), ('Mil', 'Thousand'),
                ('Dos mil', 'Two thousand'), ('Millón', 'Million'), ('Dos millón', 'Two million')])

words_Family = OrderedDict([('Madre', 'Mother'), ('Padre', 'Father'), ('Hermano', 'Brother'), ('Hermana', 'Sister'),
               ('Bebé', 'Baby'), ('Hijo', 'Son'), ('Hija', 'Daughter'), ('Abuela', 'Grandmother'),
               ('Abuelo', 'Grandfather'), ('Bisabuela', 'Great Grandmother'), ('Bisabuelo', 'Great Grandfather'),
               ('Tío', 'Uncle'), ('Tía', 'Aunt'), ('Tío abuelo', 'Great Uncle'), ('Tía abuela', 'Great Aunt'),
               ('Primo', 'Cousin'), ('Sobrino', 'Nephew'), ('Sobrina', 'Niece'), ('Suegro', 'Father in law'),
               ('Suegra', 'Mother in law'), ('Yerno', 'Son in law'), ('Nuera', 'Daughter in law'),
               ('Cuñado', 'Brother in law'), ('Cuñada', 'Sister in law'), ('Medio hermano', 'Half brother'),
               ('Medio hermana', 'Half sister'), ('Hermanastra', 'Stepsister'), ('Hermanastro', 'Stepbrother'),
               ('Hijastro', 'Stepson'), ('Hijastra', 'Stepdaughter'), ('Padrastro', 'Stepfather'), ('Madrastro', 'Stepmother')])

words_Health = OrderedDict([('Doctor', 'Doctor'), ('Médico', 'Medic'), ('Hospital', 'Hospital'), ('Ambulancia', 'Ambulance'),
               ('Farmacia', 'Pharmacy'), ('Inyección', 'Injection'), ('Medicina', 'Medicine'),
               ('Ejercicio', 'Exercise'), ('Dormir', 'To sleep'), ('Descanso', 'Rest'), ('Dieta', 'Diet'),
               ('Herida', 'Injury'), ('Recuperar', 'To recover'), ('Estrés', 'Stress'), ('Mental', 'Mental'),
               ('Físico', 'Physical'), ('Sanidad', 'Healthiness'), ('Hidratar', 'To hydrate'),
               ('Primeros auxilios', 'First aid'), ('Dolor', 'Pain'), ('Tratamiento', 'Treatment'),
               ('Alergia', 'Allergy'), ('Gripe', 'Flu'), ('Fiebre', 'Fever'), ('Quemadura', 'Burn'),
               ('Tos', 'Cough'), ('Cabeza', 'Head'), ('Corazón', 'Heart'), ('Estómago', 'Stomach'),
               ('Espalda', 'Back'), ('Brazo', 'Arm'), ('Mano', 'Hand'), ('Ojo', 'Eye'), ('Oreja', 'Ear'),
               ('Dolor de cabeza', 'Headache'), ('Higiene', 'Hygiene'), ('Microbios', 'Germs'),
               ('Paciente', 'Patient'), ('Sindrome', 'Syndrome'), ('Síntomas', 'Symptoms'), ('Terapia', 'Therapy')])

words_Class_Subjects = OrderedDict([('Matemáticas', 'Mathematics'), ('Físicas', 'Physics'), ('Español', 'Spanish'),
                       ('Banda', 'Band'), ('Música', 'Music'), ('Arte', 'Art'), ('Ciencias', 'Science'), ('Ciencias sociales', 'Scoial sciences'),
                       ('Economía', 'Economics'), ('Historia', 'History'), ('Informática', 'Computer science'),
                       ('Idioma extranjero', 'Foreign Language'), ('Inglés', 'English'), ('Cálculo', 'Calculus'),
                       ('Educación física', 'Physical education'), ('Biología', 'Biology'), ('Geografía', 'Geography'),
                       ('Álgebra', 'Algebra'), ('Química', 'Chemistry'), ('Asuntos', 'Subjects'),
                       ('Recreo', 'Recess'), ('Ingeniería', 'Engineering'), ('Lituratura', 'Literature'),
                       ('Almuerzo', 'Lunch'), ('Consultivo', 'Advisory')])

words_Hobbies = OrderedDict([('pasatiempo','hobby'),  ('cocina', 'cooking'), ('dibujo', 'drawing'), 
                             ('pesca', 'fishing'), ('tejer', 'crochet'), ('edificio', 'building'),
                             ('escritura', 'writing'), ('lectura', 'reading'), ('juego con videojuegos', 'gaming'),
                             ('coser', 'sewing'), ('tocando instrumentos', 'playing instruments'), ('recoger', 'collecting'),
                             
                            ])
                            
words_Routines =  OrderedDict([('rutina', 'routine'), ('horario', 'schedule'), ('ejercicio', 'exercise'), ('estriramiento', 'stretching'), 
                               ('comer desayuno', 'eating breakfast'), ('comer almuerzo', 'eating lunch'), ('comer cena', 'eating dinner'),
                               ('programación', 'scheduling'), ('cepillarse los dientes', 'brushing teeth'), ('bañarse', 'bathing'), 
                               ('ducharse', 'showering'), ('ir a la escuela', 'going to school'), ('ir a trabajar', 'going to work'), ('ir a casa', 'going home'), 
                               ('ir a dormir', 'going to sleep'), ('despertar', 'waking up')
                               
    
])
words_Navigation = OrderedDict([('navegación','navigation'),('mapa','map'),('sistema de posicionamiento global','GPS system'),
                                ('mundo','world'),('geografía','geography'),('océano','ocean'),
                                ('mar','sea'),('lago','lake'),('estanque','pond'),
                                ('río','river'),('canal','canal'),('carretera','highway'),
                                ('calle','street'),('avenida','avenue'),('ubicación','location'),
                                ('esquina','corner'),('barco','boat'),('vehiculo','vehicle'),
                                ('navío','ship'),('coche','car'),('camión','truck'),
                                ('avión','plane'),('aerolínea','airline'),('satélite','satellite'),
                                ('dirección','direction'),('adelante','forward'),
                                ('izquierda','left'),('derecho','right'),('encima','above'),
                                ('abajo','below'),('por otra parte','beside'),('cerca','near'),
                                ('milla','mile'),('metro','meter'),
                                ('pies','feet'),('viaje','commute'),('destino','destination'),
                                ('empezar','start'),('viaje','trip'),
                                ('transporte','transport'),('transporte público','public transportation'),('autobús','bus'),
                                ('tren','train'),('express','express')
                                ])

words_Art = OrderedDict([ ('arte','art'),('pintar','paint'),('suministros de arte','art supplies'),
                         ('imagen','picture'),('tejido','fabric'),('tela','canvas'),
                         ('pincel','paint brush'),('tienda de artesanías','crafts store'),('colores de aqua','water colors'),
                         ('crayones','crayons'),('marcadores','markers'),('examen','paper'),
                         ('artesanía','crafts'),('cuento','yarn'),('escultura','sculpture'),
                         ('ejemplar','model'),('material','material'),('color','color'), ('tono','hue')        
                       ])

words_Science_Tech = OrderedDict([ ('química','chemistry'),('elementos','elements'),('energía','energy'),('molécula','molecule'),
                                  ('compuesto','compound'),('gas','gas'),('líquido','liquid'),('sólido','solid'),
                                  ('átomo','atom'),('químico','chemical'),('reacción','reaction'),('biología','biology'),
                                  ('evolución','evolution'),('población','population'),('genes','genes'),('hereditario','hereditary'),
                                  ('biológico','biological'),('especies','species'),('organo','organ'),('sistema de órganos','organ system'),
                                  ('tejido','tissue'),('células','cells'),('orgánulos','organelles'),('física','physics'),
                                  ('partícula','particle'),('repartido','speed'),('velocidad','velocity'),
                                  ('fuerza','force'),('electricidad','electricty'),('magetismo','magnetism'),('atracción','attraction'),
                                  ('gravedad','gravity'),('atracción','acceleration'),('bioquímica','biochemistry'),
                                  ('química orgánica','organic chemistry'),('ciencias de la computación','computer science'),
                                  ('computadora','computer'),('tecnología','technoloy'),('conexión a internet','internet connection'),
                                  ('datos','data'),('programa de computadora','computer program'),('ingeniero','enginner'),('software','software')

])

words_Medical = OrderedDict([('Adolorido', 'In Pain'), ('Cirugia', 'Surgery'), ('Contagioso', 'Contagious'),
                             ('Diagnosticar', 'To diagnose'), ('Efectos adversos', 'Adverse effects'),
                             ('Embarazo', 'Pregnancy'), ('Fiebre', 'Fever'), ('Epidemia', 'Epidemic'),
                             ('Gripe', 'Flu'), ('Hierbas medicionales', 'Medicinal herbs'), ('higiene', 'Hygene'),
                             ('Hinchar', 'To swell'), ('influenza', 'Influenza'), ('Insomnio', 'Insomnia'),
                             ('Medicinas alternativas', 'Alternative medicines'), ('Microbios', 'Germs'),
                             ('Obesida', 'Obesity'), ('Paciente', 'Patient'), ('Padecer de', 'To suffer from'),
                             ('Pastillas', 'Pills'), ('Receta', 'Prescription'), ('Resfriado', 'A cold'),
                             ('saludable', 'Healthy(for you)'), ('Sano', 'Healthy'), ('Sindrome', 'Syndrome'),
                             ('Sobrepeso', 'Overweight'), ('terapia', 'therapy'), ('tratamientos', 'treatments')])

words_Government = OrderedDict([('', ''), ('', ''), ('', ''), ('', '')])




words_Society = OrderedDict([('Amistad', 'Friendship'), ('Ancianos', 'Elderly'), ('Avances', 'Advamcements'),
                             ('Calidad de vida', 'Quality of life'), ('Caridad', 'Charoty'), ('Crimen', 'Crime'),
                             ('Derechos humanos', 'Human rights'), ('Desigualdad', 'Inequality'),
                             ('Desplazados', 'Desplaced'), ('Discapacidad', 'Disabled'), ('Pobreza', 'Poverty'),
                             ('Refugio politico', 'Political asylum'), ('Sanidad', 'Health'), ('Seguridad', 'Security'),
                             ('Viuda', 'Widow')])



words_Nature = OrderedDict([('Ambiente', 'Atmosphere'), ('Calentamiento global', 'Global warming'),
                            ('Capa de ozono', 'Ozone layer'), ('Combustibles', 'Fuel'), ('Derretimiento', 'Melting'),
                            ('Desechos', 'Wastes'), ('Efecto invernadero', 'Greenhouse effect'), ('Entorno', 'Environment'),
                            ('Extinguirse', 'To become extinct'), ('Glaciar', 'glacier'), ('Huella de carbono', 'Carbon footprint'),
                            ('Masa polar', 'Polar ice cap'), ('Petroleo', 'Oil'), ('Placas', 'Plates'), ('Reciclaje', 'Recycling'),
                            ('Reciclar', 'to recycle'), ('Recursos', 'Resources'), ('Recursos renovables', 'Renewable resources')])

words_Activities = OrderedDict([('debate', 'debate'), ('deportes', 'sports'), ('tiro con arco', 'archery'), ('caminata con mochila','backpacking'), 
                             ('bádminton', 'badminton'), ('béisbol', 'baseball'), ('basquetbol', 'basketball'), ('ciclismo', 'biking'),
                             ('billar', 'billiards'), ('pasep en bote', 'boating'), ('paseo en lancha', 'bobsledding'),
                             ('halterofilia', 'bodybuilding'), ('juego de bolos', 'bowling'), ('boxeo', 'boxing'),
                             ('acampar, camping'), ('piragüismo', 'canoeing'), ('cricquet', 'cricket'), ('croquet, croquet'),
                             ('juego de flechillas', 'darts'), ('ejercicios', 'exercise'), ('esgrima', 'fencing'),
                             ('pesca', 'fishing'), ('futbol americano', 'football'), ('disco volante'), ('golf', 'golf'), 
                             ('gimnástica', 'gymnastics'), ('ala delta', 'hang gliding'), ('caminata', 'hiking'), 
                             ('jockey', 'hockey'), ('caza', 'hunting'), ('kárate', 'karate'), ('boxeo a patadas', 'kickboxing'),
                             ('elacrosse', 'lacrosse'), ('artes marciales', 'martial arts'), ('motociclismo', 'motocycle racing'), 
                             ('paintball', 'paintball'), ('parapente', 'paragliding'), ('tenis de mesa', 'ping-pong'), ('polo', 'polo'),
                             ('racquetball', 'racquetball'), ('alpinismo', 'rock climbing'), ('rugby', 'rugby'), ('deporte de vela', 'sailing'), 
                             ('buceo', 'scuba diving'), ('tiro al blanco', 'sharpshooting'), ('skateboarding', 'skateboarding'),
                             ('patinaje', 'skating'), ('salto a paracaídas'), ('snokeling', 'snorkeling'), ('snowboarding', 'snowboarding'),
                             ('esquiar', 'snow skiing'), ('fútbol', 'soccer'), ('sofbol', 'softball'), ('squash', 'squash'),
                             ('surfing', 'surfing'), ('natación', 'swimming'), ('tenis', 'tennis'), ('atletismo', 'track and field'),
                             ('voleibol', 'volleyball'), ('polo acático', 'water polo'), ('esqui acuático'), ('rafting en aguas bravas'), 
                             ('windsurfing', 'windsurfing'), ('lucha libre', 'wrestling')])


# In[ ]:



school = vocabulary_Lesson('School Work', words_School_Work)
school.display_Contents()
school.print_Subject()
greetings = vocabulary_Lesson('Greetings & Personal information', words_Greetings)
school.start_Flashcards()


# In[ ]:





# In[ ]:




