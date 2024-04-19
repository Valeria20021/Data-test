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

El flujo de trabajo consta de 3 ramas; master, develop y feature/send_bd. En la rama feature/send_db se realizan pequeños cambios sobre esta caractiristica para después unirlos a la rama de desarrollo mediante git merge para después unirla con la master.

# Docker
Para la construccion del contenedor, luego lanzarlo para que se cree y se inicie, luego revisar el estado, ingresar al ambiente
```sh
sudo docker-compose build
sudo docker-compose up -d
sudo docker-compose ps
sudo docker-compose exec app-csv bash
uvicorn main:app --reload
```
