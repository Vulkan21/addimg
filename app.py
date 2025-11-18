from flask import Flask, request, Response
from PIL import Image
import io
import os

app = Flask(__name__)

MOODLE_LOGIN = os.environ.get("MOODLE_LOGIN", "vulkan21")


@app.route("/login")
def login() -> str:
    """Return the configured Moodle login string."""
    return MOODLE_LOGIN


@app.route("/makeimage")
def make_image() -> Response:
    """Return a PNG image with the requested dimensions."""
    width_arg = request.args.get("width")
    height_arg = request.args.get("height")

    try:
        width = int(width_arg)
        height = int(height_arg)
        if width <= 0 or height <= 0:
            raise ValueError
    except (TypeError, ValueError):
        return "width and height must be positive integers", 400

    image = Image.new("RGB", (width, height), color=(255, 255, 255))
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")

    return Response(buffer.getvalue(), mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
