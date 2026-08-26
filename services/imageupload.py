import boto3

from botocore.client import Config
from flask import Blueprint, current_app, request
from werkzeug.utils import secure_filename

image_bp = Blueprint("image", __name__)


@image_bp.route("/img-upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")

    if not file or not file.filename:
        return "No file selected", 400

    filename = secure_filename(file.filename)

    s3 = boto3.client(
        "s3",
        aws_access_key_id=current_app.config["S3_ACCESS_KEY"],
        aws_secret_access_key=current_app.config["S3_SECRET_KEY"],
        config=Config(signature_version="s3v4"),
    )

    s3.upload_fileobj(
        file,
        current_app.config["S3_BUCKET"],
        filename,
    )

    return "File upload successfully", 200