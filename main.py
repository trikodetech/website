from flask import Flask,render_template,request,jsonify,redirect,url_for
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html",active_page="home")

@app.route("/read-more",methods=["GET"])
def read_more():
    return render_template("read_more.html",active_page="home")

@app.route("/services",methods=["GET"])
def services():
    return render_template("service.html",active_page="services")

@app.route("/services/compliance",methods=["GET"])
def compliance():
    return render_template("compliance_service.html",active_page="services")

@app.route("/services/security",methods=["GET"])
def security():
    return render_template("security_service.html",active_page="services")

@app.route("/services/vapt",methods=["GET"])
def vapt():
    return render_template("vapt_service.html",active_page="services")

@app.route("/services/infrastructure",methods=["GET"])
def infrastructure():
    return render_template("infra_service.html",active_page="services")

@app.route("/about",methods=["GET"])
def about():
    return render_template("about.html",active_page="about")

@app.route("/contact",methods=["GET"])
def contact():
    return render_template("contact.html",active_page="contact")

# @app.route("/project",methods=["GET"])
# def project():
#     return render_template("project.html",active_page="project")

@app.route("/feature",methods=["GET"])
def feature():
    return render_template("feature.html")

@app.route("/quote",methods=["GET"])
def qyote():
    return render_template("quote.html")

@app.route("/testimonial",methods=["GET"])
def testimonial():
    return render_template("testimonial.html")

@app.route("/team",methods=["GET"])
def team():
    return render_template("team.html")

@app.route("/contact-mail",methods=["POST"])
def contact_mail():
    try:
        data=request.form
        msg=MIMEText(data["message"])
        msg["subject"]=data["subject"]
        msg["from"]=data["email"]
        msg["to"]="ripivi1957@pricegh.com"
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(os.getenv("EMAIL"),os.getenv("PASSWORD"))
        server.sendmail(msg["from"],[msg["to"]],msg.as_string())
        return redirect(url_for("contact",active_page="contact"))
    except Exception as e:
        return jsonify({"error":str(e)})
    
@app.route("/contact-quote",methods=["POST"])
def contact_quote():
    try:
        data=request.form
        msg=MIMEText(f"""
        Name: {data["name"]}
        Email: {data["email"]}
        Mobile: {data["phone"]}
        Service Intersted: {data["service"]}
        Special Note: {data["note"] if data["note"] else "N/A"}
        """)
        print(msg)
        msg["subject"]=f"New Free Quote Request from {data["name"]} for {data["service"]}"
        msg["from"]=data["email"]
        msg["to"]="ripivi1957@pricegh.com"
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(os.getenv("EMAIL"),os.getenv("PASSWORD"))
        server.sendmail(msg["from"],[msg["to"]],msg.as_string())
        return redirect(url_for("home"))
    except Exception as e:
        return jsonify({"error":str(e)})

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__=="__main__":
    app.run(debug=True)
