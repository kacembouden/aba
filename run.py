from flask import Flask, render_template


app = Flask(__name__)  

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/index.html')
def index1():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html') 

@app.route('/services.html')
def services():
    return render_template('services.html') 

@app.route('/preformance.html')
def preformance():
    return render_template('preformance.html') 

@app.route('/contact.html')
def contact():
    return render_template('contact.html') 




if __name__ == '__main__':
    app.run(debug = True)  