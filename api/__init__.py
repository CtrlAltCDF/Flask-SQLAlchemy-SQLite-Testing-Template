from flask import Flask


def create_app(testing=False):
    app = Flask("flaskApi")

    if testing:
        from api.config import TestingConfig
        app.config.from_object(TestingConfig())
    elif app.config.get("ENV") == "production":
        from api.config import ProductionConfig
        app.config.from_object(ProductionConfig())
    elif app.config.get("DEBUG") == True:
        from api.config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig())

    print(app.config)


    @app.get("/")
    def reply():
        return {"hello": "world"}

    return app