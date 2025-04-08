from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

contact_data = []

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        message = request.form.get('message')
        subject = request.form.get('subject')
        other_subject = request.form.get('other_subject')
        contactmethod = request.form.get('contactmethod')
        agreement = request.form.get('agreement')

        if not name or not email or not number or not message:
            flash('Please fill out all fields!', 'error')
            return redirect(url_for('confirmation'))

        if not phone.isdigit():
            errors.append("phone number must be numeric.")
            
        if subject == other and not other_subject:
            errors.append("please specify the subject.")
        
        if agreement != "on":
            errors.append("you must agree to the terms and conditions.")

        if errors:
            for errors in errors:
                flask(errors)
            return redirecion(url_for("contact_form"))

        final_subject
        contact_data.append({
            'name': name,
            'email': email,
            'number': number,
            'message': message
        })

        flash('Thank you for your filling!', 'success')
        return redirect(url_for('confirmation.html', contact=contact_data))

    return render_template('contact_form.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html', contact=contact_data)

if __name__ == '__main__':
    app.run()