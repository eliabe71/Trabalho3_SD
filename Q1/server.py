from importlib.metadata import requires
from turtle import pos
from urllib import request
from flask import Flask
from flask import jsonify
from flask import request

import json
class Aluno:
    nome=""
    idade=0
    matricula=0

class Professor:
    nome=""
    idade=0
    matricula=0

class Turma:
    materia =""
    alunos =[]
    professores =[]

class School:
    diretor = []
    turmas  = []

scholl = School()

b = Professor()
b.idade = 15
b.matricula= 470820
b.nome = "eliabe"
jsonStr = json.dumps(b.__dict__)
app = Flask(__name__)
@app.route('/professor', methods=['POST'])
def registerProfessor():
    a = json.loads(request.data)
    for i in range (0, len(scholl.turmas)):
        if( scholl.turmas[i].materia == a["materia"]):
            al = Professor()
            al.nome = a["name"]
            al.matricula = a["matricula"] 
            for j in range (0,len(scholl.turmas[i].professores)):
                if(scholl.turmas[i].professores[j].matricula == al.matricula ):
                    return "Professor Já Existente"
            al.idade = a["idade"]
            scholl.turmas[i].professores.append(al)
    return "Sucess"

@app.route('/allmaterias', methods=['GET'])
def allmaterias():
    materias = []
    for i in scholl.turmas:
        materias.append(i.materia)
    resp = {
        "materias": materias
    }
    return json.loads(json.dumps(resp))

@app.route('/alunos', methods=['POST'])
def registerAlunos():
    a = json.loads(request.data)
    for i in range (0, len(scholl.turmas)):
        if( scholl.turmas[i].materia == a["materia"]):
            al = Aluno()
            al.nome = a["name"]
            al.matricula = a["matricula"] 
            for j in range (0,len(scholl.turmas[i].alunos)):
                if(scholl.turmas[i].alunos[j].matricula == al.matricula ):
                    return "Aluno Já Existente"
            al.idade = a["idade"]
            scholl.turmas[i].alunos.append(al)
    return "Sucess"

@app.route('/materia', methods=['POST'])
def registerMateria():
    a = json.loads(request.data)
    for i in range (0, len(scholl.turmas)):
        if( scholl.turmas[i].materia == a["materia"]):
            return "Materia Já Existente"
    t = Turma()
    t.materia = a["materia"]
    scholl.turmas.append(t)
    return "Sucess"

@app.route('/alunos/<username>/<materia>', methods=['GET', 'POST'])
def getAluno(username, materia):
    if request.method == "GET" :
        for i in scholl.turmas:
            if( i.materia == materia):
                for j in i.alunos:
                    if j.nome == username:
                        resp = {
                            "matricula":j.matricula,
                            "idade":j.idade,
                            "nome": j.nome
                        }
                        js = json.dumps(resp)           
                        return json.loads(js)
                    return "Aluno não existe"
            return "Materia Nao Existe"            
            
@app.route('/m/<materia>', methods=['GET'])
def getMateria(materia):
    if request.method == "GET" :
        for i in scholl.turmas:
            if( i.materia == materia):
                alunos=[]
                for k in i.alunos:
                    alunos.append(k.matricula)
                professor = []
                for k in i.professores:
                    professor.append(k.matricula)
                resp= {
                    "materia": i.materia,
                    "alunos": alunos,
                    "professores": professor
                }
                return json.loads(json.dumps(resp))

@app.route('/r/<materia>', methods=['GET'])
def removeMateria(materia):
    if request.method == "GET" :
        for i in scholl.turmas:
            if( i.materia == materia):
                scholl.turmas.remove(i)
                return "Sucesso"
    return "materia inexistente"
@app.route('/alunos/<username>/<materia>', methods=['GET', 'POST'])
def removeAluno(username, materia):
    if request.method == "GET" :
        for i in scholl.turmas:
            if( i.materia == materia):
                for j in i.alunos:
                    if j.nome == username:
                        i.alunos.remove(j)
                        return "Aluno Removido Com Sucesso"
    return "Aluno inexistente"                        