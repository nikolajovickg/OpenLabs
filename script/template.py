#ucitavanje potrebnih biblioteka
import Ni6008DAQ as daq #biblioteka za citanje sa A/D-D/A konvertera
import time #biblioteka za vreme
import math #biblioteka sa matematickim funkcijama (potrebno zbog sinusoide)
from skripta import * #ucitavanje programa koji je student napisao
from socketIO_client import SocketIO, BaseNamespace  #konekcija sa serverom
socket = SocketIO('127.0.0.1', 3001) #uspostavljanje konekcije sa serverom
sio = socket.define(BaseNamespace, '/python')
#sio.emit('pyConnect', '') #obavestavanje servera da je konekcija uspostavljena
i = 0 #inicijalizacija promenljivih
u = 0
prom = {}
podesavanje(prom)
def ulaz(vrednost): #skaliranje ulaza D/A konvertera
    vrednost += 2.5
    if vrednost > 5 : vrednost = 5
    if vrednost < 0 : vrednost = 0
    daq.SetAO(6,0,vrednost)
    return None
def izlaz(red):  #citanje sa A/D konvertera
  if red == 0:
    return daq.ReadAIChanal(6,0)
  elif red == 1:
    return daq.ReadAIChanal(6,1)
  else:
    return daq.ReadAIChanal(6,2)

ulaz(0) #nuliranje ulaza
time.sleep(5) #pauza od 5 sekundi
while i<20: #vreme trajanja eksperimenta 20 sekundi
        y = izlaz(prom['red'])  #citanje ulaza, invertujuce
        u = petlja(i, y, prom)   #pokretanje studentovog programa
        ulaz(u) #slanje rezultata D/A konverteru
        sio.emit('python', {'y' : y, 't' : i, 'u' : u}) #slanje podataka
        time.sleep(0.125) #pauza od 0.125 sekundi
        i+=0.125
print 'Kraj programa!'
sio.emit('kraj');
