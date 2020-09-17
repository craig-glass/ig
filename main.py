from flask import Flask, render_template, url_for, request, session



app = Flask(__name__)


@app.route ('/')
def index():
    return render_template('index.html')


@app.route ('/formSuccess', methods=["POST"])
def formSuccess():
    if request.method=="POST":
        email = request.form.get('email')
        if not emails.__contains__(email):
            emails.append(email)
    return render_template('formSuccess.html', emails=emails)
    

@app.route ('/whyus')
def whyus():
    return render_template('whyus.html')


@app.route ('/about')
def about():
    return render_template('about.html')


@app.route ('/testimonials')
def testimonials():
    return render_template('testimonials.html')


@app.route ('/contact')
def contact():
    return render_template('contact.html')


@app.route ('/mealprep')
def mealprep():
    return render_template('mealprep.html')

if __name__ == "__main__":
    app.run()
