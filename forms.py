from wtforms import Form
from wtforms import FloatField, IntegerField, PasswordField, StringField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
  matricula = IntegerField("Matricula", [
    validators.DataRequired(message="El campo es requerido"),
    validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
  ])
  nombre = StringField("Nombre", [
    validators.DataRequired(message="El campo es requerido"),
    validators.length(min=3, max=10, message="Ingrese valor valido")
  ])
  apaterno = StringField("Apaterno", [
    validators.DataRequired(message="El campo es requerido"),
    validators.length(min=3, max=10, message="Ingrese valor valido")
  ])
  amaterno = StringField("Amaterno", [
    validators.DataRequired(message="El campo es requerido"),
    validators.length(min=3, max=10, message="Ingrese valor valido")
  ])
  correo = EmailField("Correo", [
    validators.DataRequired(message="El campo es requerido"),
    validators.Email(message="Ingresa correo valido"),
  ])
  