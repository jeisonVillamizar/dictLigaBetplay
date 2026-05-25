import os


ligaBetplay = {}

def menuLigaBetplay() -> list: 
    return ['1. Agregar Equipo/s', '2. Tabla De Posiciones', '3. Otras Opciones']



def crearEquipo(ligaBetplay : dict) -> dict : 
     nombreEquipo = input('Ingrese el nombre del equipo : ')
     preparadorFisico = input('Ingrese PrepFisico : ')
     preparadorArquero =  input('Ingrese PrepArquero : ')
     directorTecnico =  input('Ingrese Director Tecnico : ')
     medico = input('Ingrese Medico : ')
     fisioterapeuta = input('Ingrese Fisioterapeuta : ')
     ciudad = input('Ingrese Ciudad : '),
     region = input('Ingrese Region : '),
     os.system('cls')
     dataEquipo = {
         "preparadorFisico" : preparadorFisico,
         "preparadorArquero" : preparadorArquero,
         "directorTecnico": directorTecnico,
         "medico" : medico,
         "fisioterapeuta" : fisioterapeuta,
         "ciudad" : ciudad,
         "region" : region,
         "dataPartidos" : {
             "partidoJugado": 0,
             "partidoGanado": 0,
             "partidoPerdido": 0,
             "partidoEmpatado": 0,
             "golesFavor": 0,
             "golesContra": 0,
             "totalPuntos": 0
            },
          "jugadores" : jugadores()

    }
     return ligaBetplay.update({nombreEquipo : dataEquipo})
    
def crearEquipos(ligaBetplay : dict) -> dict : 
    opciones_rta = ['s'.upper(), 'n'.upper()]
    while True : 
     nombreEquipo = input('Ingrese el nombre del equipo : ')
     preparadorFisico = input('Ingrese PrepFisico : ')
     preparadorArquero =  input('Ingrese PrepArquero : ')
     directorTecnico =  input('Ingrese Director Tecnico : ')
     medico = input('Ingrese Medico : ')
     fisioterapeuta = input('Ingrese Fisioterapeuta : ')
     ciudad = input('Ingrese Ciudad : '),
     region = input('Ingrese Region : ')
     dataEquipo = {
         "preparadorFisico" : preparadorFisico,
         "preparadorArquero" : preparadorArquero,
         "directorTecnico": directorTecnico,
         "medico" : medico,
         "fisioterapeuta" : fisioterapeuta,
         "ciudad" : ciudad,
         "region" : region,
         "dataPartidos" : {
             "partidoJugado": 0,
             "partidoGanado": 0,
             "partidoPerdido": 0,
             "partidoEmpatado": 0,
             "golesFavor": 0,
             "golesContra": 0,
             "totalPuntos": 0
            },
         "jugadores" : jugadores()
    }
     ligaBetplay.update({nombreEquipo : dataEquipo})
     while True :
             rta = input('¿Desea Ingresar Otro Equipo?, s(si) n(no)').upper()
             if rta in opciones_rta and rta == 's'.upper() :
              break
             elif rta in opciones_rta and rta == 'n'.upper() :
              os.system('cls')
              return
             else: print('Pendejo')  


def jugadores() -> dict: 
   
   jugadoresDeEquipo = {}

   print('--Acontinuacion Añadiras Los Jugadores--')
   cantidadJugadores = int(input('Ingrese la cantidad de jugadores que añadira : '))
   print('-----------------------------------------')
   for i in range(cantidadJugadores):
       nombre = input('NombreDelJugador : ')
       nacionalidad = input('NacionalidadDelJugador : ')
       posicionDeJuego = input('PosicionDeJuegoDelJugador : ')
       numeroDeDorsal = int(input('NumeroDeDorsalDelJugador : '))
       edad = int(input('EdadDelJugador : '))
       print('-----------------------------------------')
       print(f'Jugador {nombre} con N.Dorsal: {numeroDeDorsal} añadido')
       print('-----------------------------------------')
       jugador = {
           "nombre" : nombre,
           "nacionalidad" : nacionalidad,
           "posicionDeJuego" : posicionDeJuego,
           "numeroDeDorsal" : numeroDeDorsal,
           "edad" : edad
       }
       jugadoresDeEquipo[numeroDeDorsal] = jugador
       
       
   return(jugadoresDeEquipo) 
     
  
def respuestaPalPendejo():
   print('Selecione lo disponible')
   os.system('pause')
   os.system('cls')   


def dueloPartidoFecha() : 
   print('---Programacion Fecha---')


opcion = 0

while True : 
    print('--Bienvenido A La LigaBetplay--')
    for opciones in menuLigaBetplay() :
       print(opciones)
    opcion = int(input(':) '))
    os.system('cls')
    match opcion :
       case 1 : 
          menuCreacionDeEquipos = '1. Agregar Equipo  \n2. Agregar Equipos'
          print(menuCreacionDeEquipos)
          try :        
               opcionMenu = int(input(':) '))
               match opcionMenu:
                  case 1 : crearEquipo(ligaBetplay), 
                  case 2 : crearEquipos(ligaBetplay),
                  case _: respuestaPalPendejo() 
          except ValueError: respuestaPalPendejo()     
       case 2 :
           menuCreacionDeEquipos = '1. Agregar Equipo  \n2. Agregar Equipos'
       case 3 :
            menuDeLiga = ["1. Registro Equipos", "2. Plantilla Tecnica", "3. Registro Jugadores", "4. Registro Estadistica", "5. Programacion Fecha", "6. Buscar Info"]
            for opcion in menuDeLiga:
             print(opcion)

    try :
              opcionMenuLiga = int(input(':) '))
              match opcionMenuLiga :
                   case 1 : pass
                   case 2 : pass
                   case 3 : pass
                   case 4 :pass
                   case 5 :pass
                   case 6 : pass
                   case _ : respuestaPalPendejo()
    except ValueError : 
           respuestaPalPendejo()


   

    # os.system('cls')
    # break