from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'PorfolioAlmonacidCammarata111200'

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
        msg = Message('Nuevo mensaje de contacto', sender=form.email.data, recipients=['antu.almonacid@alu.ing.unlp.edu.ar'])
        msg.body = f"Nombre: {form.name.data}\nEmail: {form.email.data}\nMensaje: {form.message.data}"
        mail.send(msg)
        return redirect(url_for('index'))

    return render_template('index.html', name=name, status=status, fields=fields, tech=tech, loves=loves, experiences=experiences, educations=educations, form=form)

# Ruta para servir el archivo PDF del currículum
@app.route('/get_cv_pdf')
def get_cv_pdf():
    return send_from_directory('static', 'Almonacid.Francisco.Developer.pdf')

experiences = [
        {
            'id': 1,
            'date': 'July 2023',
            'title': 'Antu Shop',
            'repository': 'https://github.com/antu2809/antushop',
            'website': 'https://antudev.pythonanywhere.com/',
            'company': '@antu.beats',
            'description_part1': 'A sophisticated online platform designed as a virtual retail hub, allowing producer @antu.beats to display and showcase his extensive inventory of instrumentals.',
            'description_part2': 'In the backend configuration, I addressed the management of authentication, registration, password change, and payments in Django, integrating MercadoPago API configuration for secure and efficient payment processing. I addressed model management to allow the publication of different products. Furthermore, I configured the cart for its proper functioning in the store.',
            'description_part3': 'On the frontend I created an intuitive design, secure access, easy registration, interactive store with integrated payment experience using html5 and css3.',
            'description': 'A sophisticated online platform designed as a virtual retail hub, allowing producer @antu.beats to display and showcase his extensive inventory of instrumentals.',
            'image1_path': 'img/tienda1.png',
            'image2_path': 'img/tienda2.png',
            'image3_path': 'img/tienda3.png',
            'skills': [
                'Front End: HTML, CSS and Javascript',
                'Back-End: Python 3.2.0; Django 4.2.1'
            ],
            "image_path": "img/newfriends.png"
        },
        {
            'id': 2,
            'date': 'August 2023',
            'title': '@trenzas.laplata Online Catlog',
            'repository': 'https://github.com/antudev/trenzas-laplata',
            'website': 'https://trenzaslaplata.onrender.com/',
            'company': 'Trenzas La Plata',
            'description_part1': 'Online catalog that allows the brand @trenzas.laplata to share the price list of its different services and share valuable information about their work',
            'description_part2': 'In FLask I configured a postgresql database connection, defined braiding and price models, routes to display prices and braiding types, and a chatbot function to answer questions.',
            'description_part3': 'The frontend uses HTML, CSS and JavaScript to create a responsive web page with a drop-down menu, informational sections and an integrated chatbot. ',
            'description':  'Online catalog that allows the brand @trenza.laplata to share the price list of its different services and share valuable information about their work',
            'image1_path': 'img/trenzas (1).png',
            'image2_path': 'img/trenzas (2).png',
            'image3_path': 'img/trenzas (3).png',
            'skills': [
                'Front End: HTML, CSS and Javascript',
                'Back-End: Python 3.2.0; Flask'
            ],
            'gif1_path': 'img/trenzas_laplata.gif',
            'gif2_path': 'img/trenzas_laplata_mobile[1].gif'
        },
        {
            'id': 3,
            'date': 'March - June 2023',
            'title': 'La galería rosa',
            'repository': 'https://github.com/antudev/trenzas-laplata',
            'website': 'not yet',
            'company': 'La galería rosa',
            'description_part1': 'A platform allowing users to showcase, acquire, and exchange available artistic creations through an interactive web interface.',
            'description_part2': 'The backend provides functions for adding customers, managing an online store, processing purchases, displaying images, and getting information from Instagram.',
            'description_part3': 'The frontend features an elegant interface with personalized greetings, an art gallery, store and social links, and search functionalities.',
            'description': 'My first project. A platform allowing users to showcase, acquire, and exchange available artistic creations through an interactive web interface.',
            'image1_path': 'img/lagaleriarosapresentacion.gif',
            'image2_path': 'img/lagaleriarosahome.gif',
            'image3_path': 'img/galeria.png',
            'skills': [
                'Front End: HTML, CSS and Javascript',
                'Back-End: Python 3.2.0; Django 4.2.1'
            ],

            'gif1_path': 'img/lagaleriarosapresentacion.gif',
            'gif2_path': 'img/lagaleriarosahome.gif'

        }
    ]

@app.route('/experience')
def experience():


    return render_template('experience.html', experiences=experiences)

@app.route('/project/<int:project_id>')
def project_details(project_id):
    # Lógica para obtener los detalles del proyecto con el ID especificado
    # Se asume que tienes una lista de proyectos llamada "experiences"
    project = None
    for experience in experiences:
        if experience['id'] == project_id:
            project = experience
            break

    if project is None:
        # Manejar el caso en que no se encuentre el proyecto con el ID especificado
        return "Proyecto no encontrado", 404

    return render_template('project_details.html', project=project)

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
                      sender=form.email.data, # Correo elecctronico del remitente
                      recipients=['antu.almonacid@alu.ing.unlp.edu.ar'])  # Tu dirección de correo destinatario
        msg.body = f"Nombre: {form.name.data}\nEmail: {form.email.data}\nMensaje: {form.message.data}"
        mail.send(msg)

        return redirect(url_for('index'))

    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run()