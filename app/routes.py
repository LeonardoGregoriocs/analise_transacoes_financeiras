from mvc_flask import Router

Router.get("/", "home#index")
Router.post("/", "home#upload_arquivo")
