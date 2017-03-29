from bottle import run, get, post, request, redirect # or route

mensagens = []
nomes = []

@get('/home') # or @route('/login')
def login():
    return '''
        <form action="/send" method="post">
            Nome: <input name="nome" type="text" />
            Mensagem: <input name="mensagem" type="text" />
            <input value="Send" type="submit" />
        </form>
    '''+'Nomes: '+str(nomes)+' Mensagens: '+str(mensagens)

@post('/send') # or @route('/login', method='POST')
def do_login():
    nome = request.forms.get('nome')
    mensagem = request.forms.get('mensagem')
    #if check_login(username, password):
    #    return "<p>Your login information was correct.</p>"
    #else:
    #    return "<p>Login failed.</p>"
    mensagens.append(mensagem)
    nomes.append(nome)
    redirect('/home')

run(host='localhost', port=8080)
