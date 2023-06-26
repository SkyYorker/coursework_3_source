import base64
import hashlib

from flask import current_app


def generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(generate_password_digest(password)).decode('utf-8')


def decode_password_hash(password):
    base64_bytes = password.encode('utf-8')
    return base64.b64decode(base64_bytes)
# TODO: [security] Описать функцию compose_passwords(password_hash: Union[str, bytes], password: str)
