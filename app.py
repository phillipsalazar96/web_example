from flask import Flask, render_template

# create the application object
app = Flask(__name__)
# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html')  # render a template
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/todolist')
def todolist():
    return render_template('todolist.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
