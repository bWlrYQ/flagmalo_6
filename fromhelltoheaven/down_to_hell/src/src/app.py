from flask import Flask, request, render_template, session, redirect
from json import load, dump
from django.utils.html import escape
from re import match
import jinja2

app = Flask(__name__)
app.secret_key = "8>sLFsw1C3<N.d$'h+Wi4B3$>;m@W|"

@app.route("/", methods=["GET", "POST"])
def index():
    if (session.get('loggedIn') == True):
        return redirect('/notes', code=302)
    else:
        return redirect('/login', code=302)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        error = "Error, invalid credentials. Please try again"
        if request.form['user'] == "Max3nce_Y0d4" and request.form['pass'] == "spongebob":
            session["loggedIn"] = True
            return redirect('/notes', code=302)
        else:
            return render_template('login.html', error=error)

@app.route("/notes", methods=['POST', 'GET'])
def notes():
    if request.method == "GET":
        if session.get('loggedIn') == True:
            f = open('4358b5009c67d0e31d7fbf1663fcd3bf/notes.json')
            data = load(f)
            for i in range(len(data)):
                del data[i]['content']
            return render_template('notes.html', notes_list=data, showButtons=True)
        else:
            return redirect('/login', code=302)

@app.route("/viewNote", methods=['GET'])
def viewNote():
    if session.get('loggedIn') == True:
        if request.method == "GET":
            foundNote = False
            try:
                idNote = int(request.args.get('idNote'))
            except Exception as e:
                error = "Either you haven't specified any ID or you haven't put an int number, please try again"
                return render_template('viewNotes.html', redir=True, error=error)
            with open('4358b5009c67d0e31d7fbf1663fcd3bf/notes.json', 'r') as f:
                data = load(f)
                for i in range(len(data)):
                    if data[i]['id'] == idNote:
                        author = data[i]['author']
                        title = data[i]['title']
                        content = data[i]['content']
                        foundNote=True
                        break
            f.close()
            if(not foundNote):
                error="Note ID not found, please try again..."
                return render_template('viewNotes.html', redir=True,error=error)
            else:
                showNote_template  ="""
                    <div class="d-flex justify-content-center ">
                        <div class="card bg-secondary" style="width: 18rem;">
                            <div class="card-body">
                                <h4 class="card-title">{{ noteTitle }}</h4>
                                <h6 class="card-subtitle mb-2">Author: {{ noteAuthor }}</h6>
                                <hr>
                                <p class="card-text">%s</p>
                            </div>
                        </div>
                    </div>
                """
                showNote_template = showNote_template % content
                note = jinja2.Template(showNote_template).render(
                    noteTitle=title,
                    noteAuthor=author,
                    noteContent=content
                )
                return render_template('viewNotes.html', render=True, noteToRender=note)
    else:
        return redirect('/login', code=302)

@app.route("/delNote", methods=['POST'])
def delNote():
    if session.get('loggedIn') == True:
        if request.method == "POST":
            try:
                idNote = int(request.form['idNote'])
            except Exception as e:
                error = "Error, id should be a number"
                return render_template('notes.html', error=error, redir=True)
            with open('4358b5009c67d0e31d7fbf1663fcd3bf/notes.json', 'r') as f:
                data = load(f)
                f.close()
            if idNote == 0:
                error = "Hey, you can't delete that note, sorry !"
                for i in range(len(data)):
                    del data[i]['content']
                return render_template('notes.html', error=error, redir=True, notes_list=data)
            with open('4358b5009c67d0e31d7fbf1663fcd3bf/notes.json', 'w') as f:
                for i in range(len(data)):
                    if data[i]['id'] == idNote:
                        del data[i]
                        break
                dump(data, f, indent=4)
            f.close()
            for i in range(len(data)):
                del data[i]['content']
            success = "Note has been deleted"
            return render_template('notes.html', success=success, notes_list=data, redir=True)
    else:
        return redirect('/login', code=302)

@app.route("/addNote", methods=["POST"])
def addNote():
    if session.get('loggedIn') == True:
        if request.method == "POST":
            if "title" in request.form.keys() and request.form['title'] != 'null' and "author" in request.form.keys() and request.form['author'] != 'null' and "content" in request.form.keys() and request.form['content'] != 'null':
                title = request.form['title']
                author = request.form['author']
                content = request.form['content']
                if len(title)>15:
                    error="Title length shouldn't exceed 15 chars"
                    return render_template('viewNotes.html', error=error, redir=True)
                if len(author)>20:
                    error="Author length shouldn't exceed 20 chars"
                    return render_template('viewNotes.html', error=error, redir=True)
                for i in range(len(title)):
                    if(match("[a-zA-Z0-9_ ]",title[i])):
                        pass
                    else:
                       error="Title should match the following : [a-zA-Z0-9_ ]" 
                       return render_template('viewNotes.html', error=error, redir=True)
                for i in range(len(author)):
                    if(match("[a-zA-Z0-9_ ]",author[i])):
                        pass
                    else:
                        error="Title should match the following : [a-zA-Z0-9_ ]" 
                        return render_template('viewNotes.html', error=error, redir=True)
                for i in range(len(content)):
                    if(match("[<>]",content[i])):
                        error="Did you really think you could get an XSS twice ? Go out !" 
                        return render_template('viewNotes.html', error=error, redir=True)
                existingIds = []
                id = 0
                foundId = False
                with open('4358b5009c67d0e31d7fbf1663fcd3bf/notes.json', 'r+') as f:
                    data = load(f)
                    for i in range(len(data)):
                        existingIds.append(data[i]['id'])
                    existingIds.sort()
                    for i in range(len(existingIds)):
                        if (i in existingIds):
                            pass
                        else:
                            id = i
                            foundId = True
                            break
                    if not foundId:
                        id = existingIds[len(existingIds) - 1] + 1
                    newNote = {
                        "id": id,
                        "title": title,
                        "content": content,
                        "author": author,
                    }
                    data.append(newNote)
                f.close()
                with open('4358b5009c67d0e31d7fbf1663fcd3bf/notes.json', 'w+') as f:
                    dump(data, f, indent=4)
                f.close()
                for i in range(len(data)):
                    del data[i]['content']
                success = "Note has been added with id " + str(id)
                return render_template('notes.html', notes_list=data, redir=True, success=success)
            else:
                error = "You must fill in all the fields to add a note"
                return render_template('notes.html', error=error, redir=True)
    else:
        return redirect('/login', code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, threaded=True)