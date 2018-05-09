"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def index():
    """Renders a sample page."""
        
    return render_template ('index.html') 

@app.route('/form', methods=['GET', 'POST'])
def form():
    """Form page"""
     
    if request.method == 'POST':
        name = str(request.form['name'])
        age = int(request.form['age'])
        if age >= int('36') :
            result = str('OLD as fuck')
        else:
            result = str('YOUNG')

        return render_template('age.html', name=name, age=age , result=result)

    return render_template('index.html')

if __name__ == '__main__':
  app.run()
