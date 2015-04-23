from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Home Page</title>
        </head>
        <body>
            <h3>Hi! This is the home page.</h3>
            <a href="/hello">Go to Hello page</a>
        </body>
    </html>
    """

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label>What's your name? <input type="text" name="person"></label>
                    <br><br>
                <label>Choose Compliment:
                    <br>
                    <input type="radio" name="compliment" value="awesome">awesome
                    <br>              
                    <input type="radio" name="compliment" value="terrific">terrific
                    <br>
                    <input type="radio" name="compliment" value="fantastic">fantastic
                    <br>
                    <input type="radio" name="compliment" value="neato">neato
                    <br>
                    <input type="radio" name="compliment" value="fantabulous">fantabulous
                    <br>
                    <input type="radio" name="compliment" value="wowza">wowza
                    <br>
                    <input type="radio" name="compliment" value="oh-so-not-meh">oh-so-not-meh
                    <br>
                    <input type="radio" name="compliment" value="brilliant">brilliant
                    <br>
                    <input type="radio" name="compliment" value="ducky">ducky
                    <br>
                    <input type="radio" name="compliment" value="coolio">coolio
                    <br>
                    <input type="radio" name="compliment" value="incredible">incredible
                    <br>
                    <input type="radio" name="compliment" value="wonderful">wonderful
                    <br>
                    <input type="radio" name="compliment" value="smashing">smashing
                    <br>
                    <input type="radio" name="compliment" value="lovely">lovely
                </label>
                    <br><br>
                <label>Choose your power animal:
                    <br>
                    <select name="animal">
                        <option value="balloonicorn">Balloonicorn</option>
                        <option value="pegasus">Pegasus</option>
                        <option value="hippogriff">Hippogriff</option>
                        <option value="kirby">Kirby</option>
                    </select>
                </label>
                <input type="submit">
            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    animal_dictionary = { "balloonicorn": "http://th03.deviantart.net/fs70/PRE/i/2012/186/3/4/balloonicorn_by_hokutto-d564r4n.png", 
                        "pegasus": "https://s-media-cache-ak0.pinimg.com/736x/a0/71/30/a07130ac0f2e7f4577f7caafce459228.jpg", 
                        "hippogriff": "http://i215.photobucket.com/albums/cc158/susansargies07/hippogriff.jpg", 
                        "kirby": "http://vignette4.wikia.nocookie.net/kirby/images/0/01/KDCol_Kirby_K64.png/revision/latest?cb=20120627075127&path-prefix=en"}

    compliment = request.args.get("compliment")

    animal_key = request.args.get("animal")
    animal_src = animal_dictionary[animal_key]


    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
            <br>
            <img src="%s" height=100/>
        </body>
    </html>""" % (player, compliment, animal_src)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
