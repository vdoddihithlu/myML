# coments

conda create -p venv python==3.8 -y
activate venv\

git init
git config --global user.name "vidya"
git config --global user.email "myemail"
git remote add origin https://github.com/vdoddihithlu/myML.git
git remote -v

git add README.md
git commit -m "new comit"
git branch -M main
git push -u origin main
git status