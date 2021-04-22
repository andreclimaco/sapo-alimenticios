$ docker-compose build

sudo ss -lptn 'sport = :5432
sudo kill -9 2030

$ docker-compose run --rm app python manage.py migrate
$ docker-compose run --rm app python manage.py createsuperuser --username teste --password dfsa

python manage.py drf_create_token
$ docker-compose up -d
$ docker exec -i -t app_sapo_alimenticios bash -c "cd /app/initial_data && python initial_data_import.py"

http://localhost:9000/api/foods/?macronutrients=proteins&ordering=-proteins,name
http://localhost:9000/api/foods/?macronutrients=carbohydrates&ordering=-carbohydrates,name
http://localhost:9000/api/foods/?macronutrients=fats&ordering=-fats,name

$ docker exec -i -t app_sapo_alimenticios bash -c "./manage.py drf_create_token admin"

1 - Se existir algum serviço postgres rodando localmente na porta 5432, pare o serviço.
$ sudo ss -lptn 'sport = :5432'
$ sudo kill -9 <PID>

2 - Execute os seguinte sequência de comandos:
$ docker-compose build
$ docker-compose run --rm app python manage.py migrate
$ docker-compose run --rm app python manage.py createsuperuser
$ docker-compose up -d
$ docker exec -i -t app_sapo_alimenticios bash -c "cd /app/initial_data && python initial_data_import.py"
