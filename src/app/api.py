"""API que expone los métodos del servicio para monitoreo."""
from flask import Flask, jsonify, redirect, url_for


def instance_api():
    """Crea una instancia del objeto WSGI de la API.

    Usamos esta función para poder usar el objeto con pytest y gunicorn.
    """
    api = Flask("api")

    @api.route("/")
    def index():
        return redirect(url_for("alive"))

    @api.route("/alive")
    def alive():
        return jsonify({"alive": True})

    @api.route("/predict", methods=["GET"])
    def predict():
        # TODO: Add an endpoint to return the model's prediction.
        return jsonify(message="La prediccion podria ir en este endpoint!")

    return api


if __name__ == "__main__":
    api = instance_api()
    api.run(host="0.0.0.0", port="8080", debug=True, use_reloader=True)



