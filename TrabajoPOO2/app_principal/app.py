from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "clave_secreta_segura"  # Necesaria para manejar sesiones
bcrypt = Bcrypt(app)

# Simulación de usuarios (en producción usarías una base de datos)
usuarios = {
    "admin": bcrypt.generate_password_hash("1234").decode('utf-8')
}


@app.route("/")
def home():
    if "usuario" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    usuario = request.form["usuario"]
    password = request.form["password"]

    if usuario in usuarios and bcrypt.check_password_hash(usuarios[usuario], password):
        session["usuario"] = usuario
        return redirect(url_for("dashboard"))
    else:
        return "Credenciales inválidas, intenta de nuevo."


@app.route("/dashboard")
def dashboard():
    if "usuario" in session:
        return f"Bienvenido {session['usuario']} a tu panel privado!"
    return redirect(url_for("home"))


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
