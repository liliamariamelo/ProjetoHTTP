from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

users_data = {
    1:{
        "id":1,
        "nome":"Joyce",
        "idade":15
    }
}

def response_users():
    return{"users": list(users_data.values())}



#Criar
@app.route('/users',methods=['POST'])
def CriarCliente():
    body= request.json
    ids = list(users_data.keys())
    
    if ids:
        new id = ids[-1] + 1
    else: 
        new id = 1
        
   users_data[new_id] = {
       "id": new_id,
       "name" : body["name"],
       "idade" : body["idade"]
   }
    return response_users()

#Listar
@app.route('/users',methods=['GET'])
def ListarClientes():
    body = request.json
    return response_users()

#Atualizar
@app.route('/users/<int:user_id>',methods=['UPDATE'])
def AtualizarCliente(user id: int):
    body = request.json
    name = body.get["name"]
    
    if user_id in users_data:
        users_data[user_id]["name"] = name
    return response_users()

#Deletar
@app.route('/users/<int:user_id>',methods=['DELETE'])
def DeletarCliente(user id: int):
    user = users_data.get(user_id)
    if user:
        del users_data[user_id]
    return response_users()
