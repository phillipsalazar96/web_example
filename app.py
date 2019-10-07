from flask import Flask, render_template, request

# create the application object
app = Flask(__name__)
# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html')  # render a template
@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/todolist')
# def todolist():
#         return render_template('todolist.html')

@app.route('/todolist',methods = ['POST', 'GET'])
def todolist():
   if request.method == 'POST':
        delete = request.form.get('data')
        if delete == '0':
            result = request.form.get('name')
            myfile = open("data.txt", "a")
            myfile.write(result + '\n')
            myfile.close()

        elif delete == '1':
            myfile = open("data.txt", "w").close()

        myfile = open("data.txt", "r")
        result = myfile.read()
        result = result.split('\n')
        return render_template("todolist.html",data = result)

   elif request.method == 'GET':
       myfile = open("data.txt", "r")
       result = myfile.read()
       result = result.split('\n')
       return render_template("todolist.html",data = result)

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("data.html")

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
