# Loading the Flask Framework
from flask import Flask, render_template, request ,redirect,url_for

# Loading the ML Models for cr's
from ML_Model import crs_model

#loading chat-bot
import ML_Model.agri_bot as Bot

#loading the fertilisers
import ML_Model.fertiliser_model as fer_model

#defining the app name
app=Flask(__name__)

#Home Page
@app.route("/")
def home():
    return render_template("home.html")

#about page
@app.route("/about")
def about():
    return render_template("about.html")

#agri_bot page
@app.route("/agri_bot",methods=["POST","GET"])
def agri_bot():
    if request.method=="POST":
        query=str(request.form.get('user_query'))#gathering the user query from ui
        response=Bot.Agri_Bot_System(query)#passing the uq to model and reciving the reponse
        return render_template("agribot.html",response=response)#passing the response to ui 
    return render_template("agribot.html")

#fertilisers recommendation system
@app.route("/fertiliser_recom",methods=["POST","GET"])
def fertiliser_recom():
    if request.method=="POST":
        #gathering the user details
        crop_name=str(request.form.get("crop"))
        N=request.form.get("N")
        P=request.form.get("P")
        K=request.form.get("K")
        ph=request.form.get("ph")
        symtoms=request.form.get("symptoms")

        #posting to the model
        result=fer_model.get_fertilizers_recommendations(crop_name,N,P,K,ph,symtoms)
        return render_template("fertilisers.html",result=result)

    return render_template("fertilisers.html")

#weather page
@app.route("/weather")
def weather():
    return render_template("weathers.html")

#organic farming
@app.route("/organic_farming")
def organic_farming():
    return render_template("organics.html")

#soil test page
@app.route("/soil_test")
def soil_test():
    return render_template("soiltest.html")

#govt websites 
@app.route("/govt_webs")
def govt_webs():
    return render_template("govt_websites.html")

#crop recommendation page
@app.route("/crs",methods=["POST","GET"])
def crs():
    if request.method=="POST":
        n=float(request.form.get("N"))
        p=float(request.form.get("P"))
        k=float(request.form.get("K"))
        temp=float(request.form.get("temp"))
        hum=float(request.form.get("hum"))
        ph=float(request.form.get("ph"))
        rain=float(request.form.get("rain"))
        result=crs_model.Crop_Recommendation_System(n,p,k,temp,hum,ph,rain)
        
        return redirect(url_for("crs_result",result=result))
    return render_template("crs.html")
    

#crs result page
@app.route("/crs_result",methods=["POST","GET"])
def crs_result():
    result=request.args.get('result','')
    return render_template("crs_result.html",result=result)

    

#main function
if __name__=="__main__":
    app.run(debug=True)#activating the debug flag for showing the errors in deployment server
    
