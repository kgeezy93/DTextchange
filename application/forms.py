from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField, SelectField, validators
from wtforms.widgets import TextArea

class LoginForm(Form):
	username = TextField('username', [validators.Required()])
	password = PasswordField('password', [validators.Required()])
	remember_me = BooleanField('remember_me', default = False)
	submit = SubmitField('Log In')

class ContactForm(Form):
	name = TextField('name', [validators.Required()])
	subject = TextField('subject', [validators.Required()])
	message = TextField('message', [validators.Required()], widget = TextArea())
	submit = SubmitField('submission')

class InfoForm(Form):
	first_name = TextField('first_name', [validators.Required()])
	last_name = TextField('last_name', [validators.Required()])
	dartID = TextField('dartID')
	email = TextField('email', [validators.Required(), validators.Email(message=u'invalid email address')])
	username = TextField('username', [validators.Required()])
	password = PasswordField('password', [validators.Required()])
	confirm_password = PasswordField('confirm_password', [validators.Required(), validators.EqualTo('password', message=u'Passwords don\'t match')])
	submit = SubmitField('submission')

class QueryEngine(Form):
	query = TextField('query')
	query_parameter = SelectField(u'Search by: ', [validators.Required()])