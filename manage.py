from app import app


if __name__ == "__main__":
    config = dict(
        debug=False,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)

