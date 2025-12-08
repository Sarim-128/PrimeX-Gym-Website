from flask import Flask, render_template
app= Flask(__name__)

@app.route('/Home')
def Home():
    return render_template('Home.html')
    
@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Membership')
def Membership():
    return render_template('Membership.html')

@app.route('/')
def Login():
    return render_template('Login.html')

@app.route('/Register')
def Register():
    return render_template ('Register.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/Gallery')
def Gallery():
    return render_template('Gallery.html')

if __name__ == '__main__':
    app.run(debug=True) 