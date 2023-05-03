
from flask import Flask, render_template, redirect,url_for, request

app = Flask (__name__)

    
@app.route ('/')
def Inicio ():
    
    return render_template('Inicio.html')

@app.route ('/Servicios')
def Servicios ():
    
    return render_template('Servicios.html')

@app.route ('/Nosotros')
def Nosotros ():
    
    return render_template('Nosotros.html')

@app.route ('/Equipo')
def Equipo ():
    
    return render_template('Equipo.html')

@app.route ('/Contactanos')
def Contactanos ():
    
    return render_template('Contactanos.html')

@app.route ('/Mision')
def Mision ():
    return render_template('Mision.html')
@app.route ('/Vision')
def Vision ():
    return render_template('Vision.html')

@app.route ('/Valores')
def Valores ():
    
    return render_template('Valores.html')

if __name__ == '__main__':
    app.run (debug = True)