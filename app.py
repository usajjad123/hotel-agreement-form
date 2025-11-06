from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS
import os
import tempfile
import json
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
from config import SAMPLE_AGREEMENT_FILE, FONT_FILE

app = Flask(__name__)
CORS(app)


# Serve static files
@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/<path:filename>")
def static_files(filename):
    return app.send_static_file(filename)


@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    try:
        # Get form data
        data = request.get_json()

        # Extract values in the same order as the original script
        values = [
            data.get("agreement_number", ""),
            data.get("agreement_date", ""),
            data.get("name", ""),
            data.get("nationality", ""),
            data.get("phone", ""),
            data.get("citizen", ""),
            data.get("passport", ""),
            data.get("checkin_date", ""),
            data.get("checkout_date", ""),
            data.get("rent_description", ""),
            data.get("total_rent", ""),
            data.get("received_rent", ""),
            data.get("remaining_rent", ""),
            data.get("insurance_deposit", ""),
            data.get("flat_no", ""),
        ]

        # Unpack values (same as original script)
        agreement_number, agreement_date, name, nationality, phone, citizen, passport, checkin_date, checkout_date, rent_description, total_rent, received_rent, remaining_rent, insurance_deposit, flat_no = (
            values
        )

        # Check if sample image exists
        if not os.path.exists(SAMPLE_AGREEMENT_FILE):
            return (
                jsonify(
                    {
                        "error": f"Sample agreement image not found: {SAMPLE_AGREEMENT_FILE}"
                    }
                ),
                404,
            )

        # Check if font exists
        if not os.path.exists(FONT_FILE):
            return jsonify({"error": f"Font file not found: {FONT_FILE}"}), 404

        # Open the sample image
        img = Image.open(SAMPLE_AGREEMENT_FILE)

        # Create drawing object
        draw = ImageDraw.Draw(img)

        # Load font
        try:
            font = ImageFont.truetype(FONT_FILE, 30)
        except Exception as e:
            # Fallback to default font if custom font fails
            font = ImageFont.load_default()

        # Add optional top fields if provided
        if agreement_number:
            draw.text((320, 320), agreement_number, font=font, fill=(0, 0, 0))
        if agreement_date:
            draw.text((1065, 330), agreement_date, font=font, fill=(0, 0, 0))

        # Add text to image (same coordinates as original script)
        draw.text((466, 422), name, font=font, fill=(0, 0, 0))
        draw.text((466, 472), nationality, font=font, fill=(0, 0, 0))
        draw.text((466, 513), phone, font=font, fill=(0, 0, 0))
        draw.text((466, 558), citizen, font=font, fill=(0, 0, 0))
        draw.text((466, 601), passport, font=font, fill=(0, 0, 0))

        draw.text((466, 718), checkin_date, font=font, fill=(0, 0, 0))
        draw.text((466, 768), checkout_date, font=font, fill=(0, 0, 0))
        draw.text((466, 815), rent_description, font=font, fill=(0, 0, 0))
        draw.text((466, 860), total_rent, font=font, fill=(0, 0, 0))

        draw.text((466, 910), received_rent, font=font, fill=(0, 0, 0))
        draw.text((466, 960), remaining_rent, font=font, fill=(0, 0, 0))
        draw.text((466, 1007), insurance_deposit, font=font, fill=(0, 0, 0))
        draw.text((466, 1053), flat_no, font=font, fill=(0, 0, 0))

        # Save to temporary file
        temp_dir = tempfile.gettempdir()
        filename = f"{flat_no}-agreement.pdf" if flat_no else "agreement.pdf"
        temp_path = os.path.join(temp_dir, filename)

        # Save as PDF
        img.save(temp_path, "PDF", resolution=100.0)

        # Return the file
        return send_file(
            temp_path,
            as_attachment=True,
            download_name=filename,
            mimetype="application/pdf",
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    # Create static directory structure
    os.makedirs("static", exist_ok=True)

    # Move HTML, CSS, and JS files to static directory
    static_files = ["index.html", "styles.css", "script.js"]
    for file in static_files:
        if os.path.exists(file):
            os.rename(file, f"static/{file}")

    print("Starting Hotel Agreement Form Server...")
    print("Open your browser and go to: http://localhost:5001")
    app.run(debug=True, host="0.0.0.0", port=5001)
