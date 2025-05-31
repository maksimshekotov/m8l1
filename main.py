from flask import Flask, render_template, request


app = Flask(__name__)

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/list')
def list():
    return render_template('list.html')
@app.route('/find')
def find():
    return render_template('find.html')
@app.route('/after', methods=['POST'])
def after():
    name = request.form['name']
    wh = request.form['wh']
    print(name)
    print(wh)
    with open('form.txt', 'a', encoding='utf-8') as f:
        f.write(name + ' ' + wh + '\n') 
    return render_template('index.html') 


@app.route('/p')
def p():
    return render_template('p.html')

app.run(debug=True)

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa