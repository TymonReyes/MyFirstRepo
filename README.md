### LEARNING TO USE GIT AND GITHUB
>In this repository, I will create a simple guide of my progress learning about Git and GitHub. I will include syntax, key concepts and other important things about the use these platforms. 
*This repository is actually in progress.

**Content List**
- How to install and configure git in a Windows device.
- How to use Git Bash and Virtual Studio Code
- How to administrate files in git
- How to connect Git with GitHub
- Git sintax 

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdd25hyNQOMs4Xx1Cv_A_oaT0zagfSWlXMBA&s)![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuYIprEvJ5lj-58xOPTE1xD_DBgdbrNhicyg&s)

**Topics**
 1. How to install and configure Git.
# How to install and configure Git
First, you have to go to the Official Git Website. 
(https://git-scm.com/install/)
And install the aplication on your laptop.

# Git sintax

**git --version**  = View de Git Version
**git config --global user.name "(username)" ** = Create an user in Git
**git config --global user.email (gmail)** = Log your email in Git
**git config --global -e** / View the git configuration on your text editor (VS Code in this case)
**git config -h** / ver opciones de configuración.

---
**git config --global core.autocrlf true** = For Windows
**git config --global core.autocrlf input**  =For MAC 
These syntax is so necesary when we have to work with other in the same repository. If your teammates use different Operating Systems, such as Windows and Mac, this systax helps to configurate Git for all devices.

---
**ls** / ver directorios
**ls -a** / ver directorios ocultos
**cd** / moverme a otro directorio
**cd .. **/ salirme de un directorio
**cd .** / directorio actual
**pwd** / ver mi ubicación actual
**mkdir (nombrecarpeta)** / crear un nuevo directorio
**rm (nombrearchivo)** / eliminar un archivo
**mv (origen) (destino)** / mover o cambiar nombre de archivo
**cat (filename)** / mostrar contenido del archivo

CTRL + L / Limpiar terminal de git

---

git init / iniciar git en el directorio actual
git status / ver el estado de el git, stage, commit
	git status -s / Se visualiza el estado pero resumido.
git diff / muestra exactamente que cambios se están realizando dentro del archivo.
	git diff --staged / cambios pero en la etapa stage
git add . / añadir todos los archivos a stage (no se debe utilizar debido a que se pueden subir archivos que no debería subirse)
git add (nombre del archivo) (archivo dos en caso de que se requiera)

git commit -m "(description)" / realizar un commit con descripción
	git commit / se agrega la descripcion en un archivo en VS Code
git restore --staged (filename) / restaurar archivo eliminado en stage
git restore (filename) / restaurar archivo borrado

git log / mostrar historial de commits
git log --oneline / mostrar historial de commits resumido

git branch / ver en que rama estoy
git checkout -b (branchname) / crear una nueva rama
git merge (branchname) / tiene que estar en la rama master.

GITHUB
git remote add origin (url repo)
git push -u origin master / aquí es importante donde va master se agrega el nombre del branch, puede ser master, main, etc.
git push / subir todos los commits realizados a GitHub
git push -u origin (branchname) / agregar o subir branch al repositorio de github

git pull / traer los archivos que estan alojados en GitHub y hacerles un merge automatico con el branch actual. Es importante no tener archivo o datos esperando en stage o commit (utilizar git status y ver que este limpio) y entender que todos los cambios que esten realizado en github se sobrepondran sobre lo realizado en local

---
crear archivo en VS Code llamado ".gitignore" y adentro se agrega archivos o carpetas que se desean ignorar.  