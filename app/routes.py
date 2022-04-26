from mvc_flask import Router


Router.get("/", "home#main_page")
Router.get("/importar-transacoes", "home#index")
Router.post("/importar-transacoes", "home#upload_arquivo")

Router.get("/cadastro", "user#register")
Router.post("/cadastro", "user#new_register")
Router.get("/usuarios", "user#user_registered")
Router.post("/<id>/remover", "user#delete_user")
Router.get("/<id>/cadastro", "user#edit_register")
Router.post("/<id>/cadastro", "user#update_user")

Router.get("/login", "login#login")
Router.post("/authenticate", "login#authenticate")
Router.get("/logout", "login#logout")
