import flask
import macaddress
import random_mac

# Restore (unpickle) the classifier.
classifier = random_mac.classifier.restore(
  file="./random-mac-classifier.pickled"
)

def make_app():
  """
  app factory
  """

  # Create the flask app.
  app = flask.Flask(__name__)

  # Allow multiple routes to the index.
  @app.route("/")
  @app.route("/index")
  @app.route("/index.html")
  @app.route("/mac-attrs")
  def index():
    # Check the URI's query parameters for the `address` key.
    address = flask.request.args.get("address")

    # If no `address` key exists, then assume that the user 
    # wants the index.
    if address is None:
      return flask.render_template("index.html")

    # If the `address` key exists, then assume that the user 
    # wants to evaluate a MAC address.
    else:

      # If the MAC address is in a valid format, then 
      # return the attributes page.
      try:
        mac = macaddress.MediaAccessControlAddress(address)
        is_random = random_mac.is_random_mac(classifier, address)

        attributes = {
          "normalized": mac.normalized,
          "type": mac.type,
          "has_oui": "true" if mac.has_oui else "false",
          "has_cid": "true" if mac.has_cid else "false",
          "is_broadcast": "true" if mac.is_broadcast else "false",
          "is_multicast": "true" if mac.is_multicast else "false",
          "is_unicast": "true" if mac.is_unicast else "false",
          "is_uaa": "true" if mac.is_uaa else "false",
          "is_laa": "true" if mac.is_laa else "false",
          "is_random": "true" if is_random else "false"
        }

        return flask.render_template("attributes.html", attributes=attributes)

      # If the MAC address is in an invalid format, then
      # return the error page.
      except macaddress.AddressError:
        return flask.render_template("error.html")

  return app
