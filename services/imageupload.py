import uuid

import boto3
from botocore.client import Config
from flask import Blueprint, current_app, jsonify, request
from werkzeug.utils import secure_filename


image_bp = Blueprint("image", __name__)


def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=current_app.config["S3_ACCESS_KEY"],
        aws_secret_access_key=current_app.config["S3_SECRET_KEY"],
        config=Config(signature_version="s3v4"),
        region_name='ap-northeast-2'
    )


def upload_file(file):

    if not file or not file.filename:
        return jsonify({
            "success": False,
            "message": "No file selected"
        }), 400

    filename = secure_filename(file.filename)
    extension = filename.rsplit(".", 1)[-1].lower()

    object_key = f"capsules/{uuid.uuid4()}.{extension}"

    s3 = get_s3_client()

    s3.upload_fileobj(
        file,
        current_app.config["S3_BUCKET"],
        object_key,
        ExtraArgs={
            "ContentType": file.content_type
        }
    )

    return {
        "success": True,
        "objectKey": object_key
    }


def view_file(object_key):
    s3 = get_s3_client()

    presigned_url = s3.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": current_app.config["S3_BUCKET"],
            "Key": object_key
        },
        ExpiresIn=3600
    )

    return presigned_url