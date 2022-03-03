from flask import Flask

app = Flask(__name__)

#Listar
@app.route('/todo/getall',methods=['GET'])
def ListarClientes():
    return "Listar Clientes"

#Criar
@app.route('/todo/create',methods=['POST'])
def CriarCliente():
    return 'Criar novo Cliente'

#Atualizar
@app.route('/todo/update',methods=['UPDATE'])
def AtualizarCliente():
    return 'Atualizar Dados do Cliente'

#Deletar
@app.route('/todo/delete',methods=['DELETE'])
def DeletarCliente():
    return 'Deletar Cliente'
