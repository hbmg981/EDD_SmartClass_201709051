from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def principal():
    return "Bienvenida a mi sitio web de python"

@app.route('/login')
def login():
    #return "Aqui ira la pagina de inicio"
    return  render_template('login.html')




if __name__ == '__main__':
    app.run("localhost", port=3000,debug=True)

