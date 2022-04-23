from mvc_flask import Router


Router.get("/", "home#index")
Router.post("/", "home#upload_arquivo")

Router.get("/cadastro", "user#register")
Router.post("/cadastro", "user#new_register")

Router.get("/usuarios", "user#user_registered")
Router.post("/<id>/remover", "user#delete_user")
Router.get("/<id>/cadastro", "user#cadastro")
Router.post("/<id>/cadastro", "user#update_user")
