# Sapo Alimentícios

## Ambiente com Docker Compose

### Pré-requisitos

-   [Docker Compose](http://https://docs.docker.com/compose/install/ "Install Docker Compose")
-   [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "Git")

### Executando os ambientes

```sh
$ docker-compose build
$ docker-compose up
```

### Criar super usuário

```sh
$ docker-compose run --rm api python manage.py createsuperuser
```

### Carga inicial dos dados

```sh
$ docker exec -it api-sapo-alimenticios bash -c "cd /app/initial_data && python initial_data_import.py"
```

### Executando os testes do frontend

```sh
$ docker-compose run --rm app npm run test
```

### Executando os testes do backend

```sh
$ docker-compose run --rm api python manage.py test
```

## Acessando os ambientes

### API

**ENDPOINTS**

-   http://localhost:9000/api/foods/
-   http://localhost:9000/api/food/

**Admin**

-   http://localhost:9000/admin/

### APP

-   http://localhost:3000
