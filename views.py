from flask import Flask, Blueprint, render_template, request
from favsongs import fav_songs
from mb_menu import drink_menu
from mb_menu import food_menu


my_view = Blueprint("my_view", __name__) # you then tell it in app.py where to look for this and pull info back


@my_view.route("/")
def index(): # 1st would usually be Home or Index - first page it takes you too
    return render_template("index.html")


@my_view.route("/page2")
def page2():
    return render_template("page2.html")

@my_view.route("/page3")
def page3():
    my_name = "Louisa"
    return render_template("page3.html", my_name=my_name) #you need to pass it the info eg my name = my name

@my_view.route("/page4", methods = ["GET", "POST"])
def page4():
    if request.method == "POST":
        new_song = request.form["add_song"]
        fav_songs.append(new_song)

    return render_template("page4form.html", fav_songs=fav_songs)

@my_view.route("/page5")
def page5():
    return render_template("page5MB.html", drink_menu=drink_menu, food_menu=food_menu)

@my_view.route("/page6", methods = ["GET", "POST"])
def page6():
    if request.method == "POST":
        name = request.form.get("Name")
        comment = request.form.get("Comment")
        rating = request.form.get("Rating")
    return render_template("page6MBform.html")