# jlp_pytools
This project is based on Python Pro module pytools

A ideia neste projeto é fazer um projeto iniciando do zero com fork de um instituição 
no github para uma conta pessoal depois o clone para IDLE Pycharm

## 1- Commit action after README file modification
   - in the personal github account a second commit is going to be created
     - Commit for file README modification
     - Initial commit

## 2- Pull requests can be created in the github personal account
   - just to send this modification to original file jlplautz/jlp_pytools -> pythonprgbr/jlp_pytools

![](static/images/pullrequest1.png)

## 3- We can verify the branch that we have created
```
Comandos úteis:
    git branch : lista todas branches locais
    git branch --all : listas todas branches, incluindo remotas
    git remote -v: lista todos repositórios remotos conectados
    git remote add <apelido> <link do repositório> : conecta um repositório remoto
    git remote rm <apelido> : desconecta um repositório remoto
    git fetch --all: atualizada todas branchs remotas de todos repositórios remotos
    git fetch <repositorio>: atualizada todas branchs remotas de determinado respositório remoto
    git branch <nome-da-branch>: cria uma branch local
    git checkout <nome-da-branch>: carrega os arquivos de uma branch especifica
```

## 4- We can send the local branch to remote via CMD
   - git push origin master  -> send the local master branch to remote origin

## 5- We need to create upstream remote
   - git remote add upstream git@github.com:pythonprgbr/jlp_pytools.git
```
jlp_pytools $ git remote -v
origin  git@github.com:jlplautz/jlp_pytools.git (fetch)
origin  git@github.com:jlplautz/jlp_pytools.git (push)
upstream        git@github.com:pythonprgbr/jlp_pytools.git (fetch)
upstream        git@github.com:pythonprgbr/jlp_pytools.git (push)
```

## 6-  we can have this modification available in our local branch in Pycharm IDLE
   - project jlp_pytools --> GIT --> Fetch --> the information comes from remotes branch to update the local one.
   - now we can see that upstream branch appeared in the Pycharm IDLE

## 7- We can execute a commit with force push when we did no follow the correct branch steps
   - project jlp_pytools --> GIT --> Commit Directory --> Commit and Push --> Force Push
   - jlp_pytools $ git push origin master -f  --> (-f force)

## 8- Create a virtual environment
   - jlp_pytools $ pyenv local 3.8.1
   - jlp_pytools $ pipenv shell
   - (jlp_pytools) jlp_pytools $ pipenv install flake8 --dev
   - (jlp_pytools) jlp_pytools $ pip freeze > requirements.txt
   - create file ->.flake8
```
[flake8]
max-line-length = 120
exclude = .venv
```
  - create file -> .pyup.yml
```
requirements:
  - Pipfile
  - Pipfile.lock
```

