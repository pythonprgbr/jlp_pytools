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
jlp_pytools $ git branch
* master
jlp_pytools $ git branch --all
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
jlp_pytools $ git remote -v
origin  git@github.com:jlplautz/jlp_pytools.git (fetch)
origin  git@github.com:jlplautz/jlp_pytools.git (push)
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
   - project jlp_pytools --> GIT --> Commit Directory