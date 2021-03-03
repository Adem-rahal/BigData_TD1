from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@cluster0.xjgjp.mongodb.net/mydb?retryWrites=true&w=majority'

#app.config['MONGO_URI'] = 'mongodb+srv://cluster0.xjgjp.mongodb.net/mydb?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority'

mongo = PyMongo(app)

todos = mongo.db.todos

@app.route('/')
def index():
    saved_todos = todos.find()
    return render_template('index.html', todos=saved_todos)


@app.route('/add', methods=['POST'])
def add_todo():
    new_todo = request.form.get('new-todo')
    todos.insert_one({'text' : new_todo, 'complete' : False})
    # print(f"AQUNAMATATA { new_todo}")
    return redirect(url_for('index'))

@app.route('/complete/<oid>')
def complete(oid):
    todo_item = todos.find_one({'_id': ObjectId(oid)})
    todo_item['complete'] = True
    todos.save(todo_item)
    return redirect(url_for('index'))

# @app.route('/delete_completed')
# def delete_completed():
#     todos.delete_many({'complete' : True})
#     return redirect(url_for('index'))

# @app.route('/delete_all')
# def delete_all():
#     todos.delete_many({})
#     return redirect(url_for('index'))

mongo.init_app(app)
app.run(host="0.0.0.0")