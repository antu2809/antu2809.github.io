from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message 
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'PorfolioAlmonacidCammarata111200'

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')


mail = Mail(app)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')
    
    
@app.route('/error')
def error():
    form = ContactForm()
    return render_template('error.html', message="Bad Request", form=form) 


@app.errorhandler(Exception)
def handle_exception(e):
    form = ContactForm()
    return render_template('error.html', message="Bad Request", form=form), 400  


@app.errorhandler(404)
def err_404(e):
    form = ContactForm()
    return render_template('error.html', message='404 Page Not Found', form=form), 404  

@app.route('/', methods=['GET', 'POST'])
def index():
    name = "Francisco Antu Almonacid Cammarata"
    status = "Student of Computer Engineering, Universidad Nacional de La Plata"
    fields = "Web Development, Technical Research and Writing"
    tech = "Python (Django and Flask), HTML, CSS, Javascript, Bootstrap, Git (GitHub, GitLab)"
    loves = "Writing; Sharing knowledge with interested persons; Sports; Music Production"

    experiences = [
        {
            'date': 'March - June 2023',
            'title': 'Website Development',
            'company': 'La galería Rosa',
            'description': 'My first project. A platform allowing users to showcase, acquire, and exchange available artistic creations through an interactive web interface.',
            'skills': [
                'Front End: HTML, CSS and Javascript',
                'Back-End: Python 3.2.0; Django 4.2.1'
            ],
            
            'gif1_path': 'img/lagaleriarosapresentacion.gif',
            'gif2_path': 'img/lagaleriarosahome.gif'
            
        },
        {
            'date': 'July 2023',
            'title': 'E-commerce Website Development',
            'company': 'New Friends  ',
            'description': 'A sophisticated online platform designed as a virtual retail hub, allowing the New Friends brand to showcase and exhibit its extensive inventory of merchandise, thereby paving the way for seamless and streamlined sales transactions.',
            'skills': [
                'Front End: HTML, CSS and Javascript',
                'Back-End: Python 3.2.0; Django 4.2.1'
            ],
            "image_path": "img/newfriends.png"
        },
        {
            'date': 'August 2023',
            'title': '@trenzas.laplata Website Developer',
            'company': 'Trenzas La Plata',
            'description': 'Online catalog that allows the brand @trenza.laplata to share the price list of its different services.',
            'skills': [
                'Front End: HTML, CSS and Javascript',
                'Back-End: Python 3.2.0; Flask'
            ],
            'gif1_path': 'img/trenzas_laplata.gif'
        }
    ]

    educations = [
        {'date': '2012 / 2018',
            'degree': 'Technical degree in agricultural production corresponding to completed secondary education',
            'institution': 'Secondary School of Technical and Professional Education No. 733 "Benito Owen"',
            'location': 'Gaiman, Chubut, Argentina'    
        },
        {'date': 'July 2017',
            'degree': 'English',
            'institution': 'Gateway School of English',
            'location': 'La Valeta, Malta'    
        },
        {
            'date': '2019 / Present',
            'degree': 'Computer Engineering',
            'institution': 'UNLP, La Plata',
            'location': 'La Plata, Buenos Aires, Argentina'
        },
        {
            'date': '2023',
            'degree': 'Python',
            'institution': 'Coderhouse',
            'location': 'Online'
        }
    ]
    form = ContactForm()

    if form.validate_on_submit():
        msg = Message('Nuevo mensaje de contacto', sender='tu_correo@gmail.com', recipients=['antualmonacid@gmail.com'])
        msg.body = f"Nombre: {form.name.data}\nEmail: {form.email.data}\nMensaje: {form.message.data}"
        mail.send(msg)
        return redirect(url_for('index'))

    return render_template('index.html', name=name, status=status, fields=fields, tech=tech, loves=loves, experiences=experiences, educations=educations, form=form)



@app.route('/experience')
def experience():
    experiences = [
        {
            'date': 'March - June 2023',
            'title': 'Website Developer',
            'company': 'La galería Rosa',
            'description': 'My first project. A platform allowing users to showcase, acquire, and exchange available artistic creations through an interactive web interface.',
            'skills': [
                'Front End: HTML, CSS and Javascript',
                'Back-End: Python 3.2.0; Django 4.2.1'
            ],
            'gif1_path': 'img/lagaleriarosapresentacion.gif',
            'gif2_path': 'img/lagaleriarosahome.gif'
            
        },
        {
            'date': 'July 2023',
            'title': 'Website Developer',
            'company': 'New Friends  ',
            'description': 'A sophisticated online platform designed as a virtual retail hub, allowing the New Friends brand to showcase and exhibit its extensive inventory of merchandise, thereby paving the way for seamless and streamlined sales transactions.',
            'skills': [
                'Front End: HTML, CSS and Javascript',
                'Back-End: Python 3.2.0; Django 4.2.1'
            ],
            "image_path": "img/newfriends.png"
        },
        {
            'date': 'August 2023',
            'title': 'Website Developer',
            'company': 'Trenzas La Plata',
            'description': 'Online catalog that allows the brand @trenza.laplata to share the price list of its different services.',
            'skills': [
                'Front End: HTML, CSS and Javascript',
                'Back-End: Python 3.2.0; Flask'
            ],
            'gif1_path': 'img/trenzas_laplata.gif',
        }
    ]

    return render_template('experience.html', experiences=experiences)


@app.route('/education')
def education():
    educations = [
        {
            'date': '2019 / Present',
            'degree': 'Computer Engineering',
            'institution': 'UNLP, La Plata',
            'location': 'Buenos Aires, Argentina'
        },
        {
            'date': '2023',
            'degree': 'Python web development',
            'institution': 'Coderhouse',
            'location': 'Online'
        }
    ]

    return render_template('education.html', educations=educations)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Envío de correo electrónico
        msg = Message('Nuevo mensaje de contacto',  # Asunto del correo
                      sender='tu_correo@gmail.com',  # Cambia a tu dirección de correo
                      recipients=['antualmonacid@gmail.com'])  # Tu dirección de correo destinatario
        msg.body = f"Nombre: {form.name.data}\nEmail: {form.email.data}\nMensaje: {form.message.data}"
        mail.send(msg)

        return redirect(url_for('index'))

    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run()