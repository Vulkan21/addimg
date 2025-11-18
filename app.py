from flask import Flask, request, Response
from PIL import Image
import io

app = Flask(__name__)

MOODLE_LOGIN = "vulkan21"

@app.route("/login")
def login():
    return MOODLE_LOGIN

@app.route("/makeimage")
def make_image():
      try:
        width = int(request.args.get("width", "0"))
        height = int(request.args.get("height", "0"))
        if width <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        return "Invalid width or height", 400

       image = Image.new("RGB", (width, height), (255, 255, 255))
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    png_bytes = buf.getvalue()

    return Response(png_bytes, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
