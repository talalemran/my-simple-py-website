from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # In a real application, you'd probably store this in a database
        # or send an email. For this example, we'll just print it.
        print(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        return render_template("contact.html", message="Message sent!") #Confirmation message
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

