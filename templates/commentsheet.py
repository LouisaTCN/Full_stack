{% extends 'base.html' %}

 {% block content %}

 <h1>Welcome to the 4th page of my Website</h1>
 <p>Hello, these are my favourite songs</p>

#------- THIS CREATES A FOR LOOP TO GIVE EACH SONG IN THE LIST -------#
 <ul>
    {% for song in fav_songs %}
    <li> {{song}}</li> # song is just like the index position & return each song in a list seperately
{% endfor %}
 </ul>
 {% endblock %}

#---------------- END OF FOR LOOP -----------#

# -------- THIS CREATES USER INPUT -----------------#
<hr>
<form>
    <input type="text" name="Add Favourite Song", placeholder="Enter your favourite song"
    <button>Submit favourite song</button>
</form>

{% endblock %}
#THIS JUST ALLOWS THE USER TO INUT BUT DOESN'T RETURN THEIR ANSWER

@my_view.route("/page4", methods = ["GET", "POST"]) # adding methods allows only those methods 
def page4():
    If request.method == "POST": # makes it run if it is a post!
    new_song = request.form["add_song"]
    fav_songs.append(new_song)
    
    return render_template("page4form.html", fav_songs=fav_songs)

#***** THIS DOES RETURN THE USER INFO BUT DOESN'T SAVE IT TO SITE!!!! THIS IS DONE SEPERATELY*****
#--------------- END -----------------------#