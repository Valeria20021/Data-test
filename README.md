# app 

```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

# read_csv.py

El proceso de lectura y revision del archivo coordenates.csv se encuentra en este modulo. Este se puede llamar desde otro archivo o ejecutar como script con las siguientes instrucciones

```sh
import read_csv
python3 read_csv.py
```
# Git Flow

El flujo de trabajo consta de 3 ramas; master, develop y feature/send_bd. 
En la rama feature/send_db se realizan pequeños cambios sobre esta caractiristica para después unirlos a la rama de desarrollo
```sh
git checkout feature/send_bd
git add .
git commit -m ""
git push origin feature/send_bd
```
Unir los cambios de feature/send_bd con la rama develop
```sh
git checkout develop
git merge feature/
```
Finalmente pasar los cambios de develop a la rama master
```sh
git checkout master
git merge develop
```