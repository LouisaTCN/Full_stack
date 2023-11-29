from flask import Flask, render_template
from views import my_view


app = Flask (__name__) # creates app object
app.register_blueprint(my_view) # tells where to look to copy blueprint

if __name__ == "__main__":
    app.run(debug = True, port=8000)

## this turns my computer into a server & then sends and recieves requests made to it
