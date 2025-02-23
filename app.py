from flask import Flask, render_template, request, redirect, url_for  # Import redirect and url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])  # Important: Specify both GET and POST
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Process the form data (e.g., store in a database, send an email)
        print(f"Name: {name}\nEmail: {email}\nMessage: {message}")  # Placeholder

        # Redirect to a success page or back to the contact form (better UX)
        return redirect(url_for('contact', message="Message sent!"))  # Redirect after POST

    # If it's a GET request (initial page load or redirect after POST),
    # render the contact form.  The 'message' will be None on the first visit
    message = request.args.get('message') # Get message from query string
    return render_template("contact.html", message=message)  # Pass message to template


if __name__ == "__main__":
    app.run(debug=True)
