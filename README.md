<h1>Quokkel</h1>

📜 Serviço simples e eficaz!

<div align="center">
    <img src="https://i.imgur.com/XLiIFDJ.png" alt="quokka-logo" border="0">
</div>

<p>
💡 O objetivo da nossa aplicação é facilitar o gerenciamento hoteleiro, oferecendo controle sobre reservas, hóspedes e acomodações.
</p><br>

## 🛠️ Instalação

1. Baixe o repositório utilizando o Git com o commando:<br>

utilizando HTTPS

```sh
$ https://github.com/Vinicius2m/Quokkel.git
```

ou SSh

```sh
$ git@github.com:Vinicius2m/Quokkel.git
```

Instale um ambiente virtual (<code>venv</code>) na raíz do projeto

```sh
$ python -m venv venv && source venv/bin/activate
```

2. Instale as dependências presentes no arquivo <code>requirements.txt</code>:
   <br>: no terminal :

```
$ pip install -r requirements.txt
```

2 - Em seguida, inicie a aplicação:
<br>: no terminal :

```
$ ./manage.py runserver
```

<br><hr><br>

## <b> 🌄 Inicialização da API </b>

Base Url: https://quokkel.herokuapp.com/

<br>

## 🔚 Endpoints

Existem 22 endpoints nessa aplicação: 11 para gerenciamento de usuário (admin e hóspedes), 3 para gerenciamento de quartos, 2 para gerenciamento de categorias, 6 para gerenciamento de reservas.
<br><br>

## 🧍Usuário:

### Admins:

<br>

<span>Criação de admin:</span><br>
<code>/admins/register/</code><br><br>
Exemplo de entrada

```json
{
  "email": "marmota@mail.com",
  "password": "1234",
  "first_name": "Marmota",
  "last_name": "Kel",
  "age": 32,
  "cpf": "07744455547",
  "phone": "123456789012347",
  "is_staff": true
}
```

Status: <code style="color: green; font-size: 16px;"> 201 CREATED</code>
<br>Resposta:

```json
{
  "user_id": "db8f63dc-cf00-4ba0-91cd-43ea968e73b3",
  "email": "marmota@mail.com",
  "first_name": "Marmota",
  "last_name": "Kel",
  "age": 32,
  "cpf": "07744455547",
  "phone": "1234567890123",
  "is_staff": true
}
```

<br><br>
<span>Login de admin:</span><br>
<code>/admins/login/</code><br><br>
Exemplo de entrada

```json
{
  "email": "marmota@mail.com",
  "password": "1234"
}
```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "token": "9c2db77e46128c7f612cfa7eabcbc1aa5b3bbb88"
}
```

<br><br>
<span>Retornar todos os admins:</span><br>
<code>/users/admins/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
[
  {
    "user_id": "db8f63dc-cf00-4ba0-91cd-43ea968e73b3",
    "email": "marmota@mail.com",
    "first_name": "Marmota",
    "last_name": "Kel",
    "age": 32,
    "cpf": "07744455547",
    "phone": "1234567890123",
    "is_staff": true
  },
  {
    "user_id": "db8f63dc-cf00-4ba0-91cd-43ea968e73b3",
    "email": "marmota1@mail.com",
    "first_name": "Marmota",
    "last_name": "Kel",
    "age": 32,
    "cpf": "07744455546",
    "phone": "1234567890128",
    "is_staff": true
  },
  {
    "user_id": "db8f63dc-cf00-4ba0-91cd-43ea968e73b3",
    "email": "marmota2@mail.com",
    "first_name": "Marmota",
    "last_name": "Kel",
    "age": 32,
    "cpf": "07744455545",
    "phone": "1234567890121",
    "is_staff": true
  }
]
```

<br><br>
<span>Retornar um admin pelo ID:</span><br>
<code>/users/admins/user_id</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "user_id": "db8f63dc-cf00-4ba0-91cd-43ea968e73b3",
  "email": "marmota@mail.com",
  "first_name": "Marmota",
  "last_name": "Kel",
  "age": 32,
  "cpf": "07744455547",
  "phone": "1234567890123",
  "is_staff": true
}
```

<br><br>
<span>Atualização de admin:</span><br>
<code>/admins/admin_id/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Exemplo de entrada

```json
{
  "age": 18
}
```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "user_id": "db8f63dc-cf00-4ba0-91cd-43ea968e73b3",
  "email": "marmota@mail.com",
  "first_name": "Marmota",
  "last_name": "Kel",
  "age": 18,
  "cpf": "07744455547",
  "phone": "1234567890123",
  "is_staff": true
}
```

<br><br>
<span>Remover um admin:</span><br>
<code>/admins/admin_id/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 204 NO CONTENT</code>
<br>Resposta:

```json

```

### Hóspedes (Guests)

<br>

<span>Criação de hóspede:</span><br>
<code>/guests/register/</code><br><br>
Exemplo de entrada

```json
{
  "email": "quokka@mail.com",
  "password": "1234",
  "first_name": "Quokka",
  "last_name": "Quita",
  "age": 30,
  "cpf": "99999999998",
  "phone": "1234567891113",
  "is_staff": false
}
```

Status: <code style="color: green; font-size: 16px;"> 201 CREATED</code>
<br>Resposta:

```json
{
  "user_id": "43908c43-0b3d-48ba-ab26-c696ca02b5df",
  "email": "quokka@mail.com",
  "first_name": "Quokka",
  "last_name": "Quita",
  "age": 30,
  "cpf": "99999999998",
  "phone": "1234567891113"
}
```

<br><br>
<span>Login de hóspede:</span><br>
<code>/guests/login/</code><br><br>
Exemplo de entrada

```json
{
  "email": "quokka@mail.com",
  "password": "1234"
}
```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "token": "ccc24e532f6079b323c3fa09f72e0a012422fc39"
}
```

<br><br>
<span>Retornar todos os hóspedes:</span><br>
<code>/users/guests/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
[
  {
    "user_id": "f80431a8-c76a-459e-9818-1c4eb7ed76d3",
    "email": "quokka@mail.com",
    "first_name": "Quokka",
    "last_name": "Quita",
    "age": 30,
    "cpf": "99999999998",
    "phone": "1234567891113",
    "is_staff": false
  },
  {
    "user_id": "7e4bd16a-7340-4089-89e3-a9071d983ce9",
    "email": "quokka2@mail.com",
    "first_name": "Quokka",
    "last_name": "Quita",
    "age": 30,
    "cpf": "99999999999",
    "phone": "1234567891112",
    "is_staff": false
  },
  {
    "user_id": "db6ef5b0-5d11-4370-9548-87488491c32d",
    "email": "quokka3@mail.com",
    "first_name": "Quokka",
    "last_name": "Quita",
    "age": 30,
    "cpf": "99999999997",
    "phone": "1234567891111",
    "is_staff": false
  }
]
```

<br><br>
<span>Retornar um hóspede pelo ID:</span><br>
<code>/users/guests/user_id</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "user_id": "f80431a8-c76a-459e-9818-1c4eb7ed76d3",
  "email": "quokka@mail.com",
  "first_name": "Quokka",
  "last_name": "Quita",
  "age": 30,
  "cpf": "99999999998",
  "phone": "1234567891113",
  "is_staff": false
}
```

<br><br>
<span>Atualização de Hóspede(Guest):</span><br>
<code>/guests/guest_id/</code><br>
<code style="color: tomato;">Requer token de Hósoede(Guest)</code><br><br>
Exemplo de entrada

```json
{
  "age": 18
}
```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "user_id": "f80431a8-c76a-459e-9818-1c4eb7ed76d3",
  "email": "quokka@mail.com",
  "first_name": "Quokka",
  "last_name": "Quita",
  "age": 18,
  "cpf": "99999999998",
  "phone": "1234567891113",
  "is_staff": false
}
```

<br><br>
<span>Remover conta de Hóspede(Guest):</span><br>
<code>/guests/guest_id/</code><br>
<code style="color: tomato;">Requer token de Hósoede(Guest)</code><br><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 204 NO CONTENT</code>
<br>Resposta:

```json

```

<br><br>
<span>Retornar todos os usuários:</span><br>
<code>/users/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
[
  {
    "user_id": "f80431a8-c76a-459e-9818-1c4eb7ed76d3",
    "email": "quokka@mail.com",
    "first_name": "Quokka",
    "last_name": "Quita",
    "age": 30,
    "cpf": "99999999998",
    "phone": "1234567891113",
    "is_staff": false
  },
  {
    "user_id": "7e4bd16a-7340-4089-89e3-a9071d983ce9",
    "email": "quokka2@mail.com",
    "first_name": "Quokka",
    "last_name": "Quita",
    "age": 30,
    "cpf": "99999999999",
    "phone": "1234567891112",
    "is_staff": false
  },
  {
    "user_id": "db6ef5b0-5d11-4370-9548-87488491c32d",
    "email": "quokka3@mail.com",
    "first_name": "Quokka",
    "last_name": "Quita",
    "age": 30,
    "cpf": "99999999997",
    "phone": "1234567891111",
    "is_staff": false
  },
  {
    "user_id": "db8f63dc-cf00-4ba0-91cd-43ea968e73b3",
    "email": "marmota@mail.com",
    "first_name": "Marmota",
    "last_name": "Kel",
    "age": 32,
    "cpf": "07744455547",
    "phone": "1234567890123",
    "is_staff": true
  },
  {
    "user_id": "db8f63dc-cf00-4ba0-91cd-43ea968e73b3",
    "email": "marmota1@mail.com",
    "first_name": "Marmota",
    "last_name": "Kel",
    "age": 32,
    "cpf": "07744455546",
    "phone": "1234567890128",
    "is_staff": true
  },
  {
    "user_id": "db8f63dc-cf00-4ba0-91cd-43ea968e73b3",
    "email": "marmota2@mail.com",
    "first_name": "Marmota",
    "last_name": "Kel",
    "age": 32,
    "cpf": "07744455545",
    "phone": "1234567890121",
    "is_staff": true
  }
]
```

<hr>

## 🧍Categorias:

<br>

<span>Criação de categoria:</span><br>
<code>/rooms_categories/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Exemplo de entrada

```json
{
  "category_name": "Standard",
  "price": 100.0,
  "max_guest_number": 1
}
```

Status: <code style="color: green; font-size: 16px;"> 201 CREATED</code>
<br>Resposta:

```json
{
  "room_category_id": "764dfc4c-9549-433b-9f6a-8b973fd6aa27",
  "category_name": "Standard",
  "price": 100.0,
  "max_guest_number": 1
}
```

<br><br>
<span>Retornar todos as categorias:</span><br>
<code>/rooms_categories/</code><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
[
  {
    "room_category_id": "ec1ee616-2974-4bec-b049-7e95ac6daddb",
    "category_name": "Standart master",
    "price": 300.0,
    "max_guest_number": 4,
    "number_of_rooms": 0,
    "rooms_available": 0,
    "rooms_occupy": 0
  },
  {
    "room_category_id": "764dfc4c-9549-433b-9f6a-8b973fd6aa27",
    "category_name": "Standard",
    "price": 100.0,
    "max_guest_number": 1,
    "number_of_rooms": 0,
    "rooms_available": 0,
    "rooms_occupy": 0
  }
]
```

<br><br>
<span>Retornar uma categoria pelo ID:</span><br>
<code>/rooms_categories/room_category_id</code><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "room_category_id": "764dfc4c-9549-433b-9f6a-8b973fd6aa27",
  "category_name": "Standard",
  "price": 100.0,
  "max_guest_number": 1,
  "number_of_rooms": 0
}
```

<br><br>
<span>Atualização de uma categoria:</span><br>
<code>/rooms_categories/room_category_id/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Exemplo de entrada

```json
{
  "price": 400.0
}
```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "room_category_id": "764dfc4c-9549-433b-9f6a-8b973fd6aa27",
  "category_name": "Standard",
  "price": 400.0,
  "max_guest_number": 1
}
```

<br><br>
<span>Remover conta de uma categoria:</span><br>
<code>/rooms_categories/room_category_id/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 204 NO CONTENT</code>
<br>Resposta:

```json

```

## 🧍Quartos:

<br>

<span>Criação de quartos:</span><br>
<code>/rooms/room_category/room_category_id/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Exemplo de entrada

```json
{
  "number": "101"
}
```

Status: <code style="color: green; font-size: 16px;"> 201 CREATED</code>
<br>Resposta:

```json
{
  "room_id": "8fa041bc-db67-4e9b-b38d-49901e7ae0bd",
  "number": 101,
  "available": true,
  "room_category": {
    "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
    "category_name": "Suite",
    "price": 200.0,
    "max_guest_number": 2
  }
}
```

<br><br>
<span>Retornar todos os quartos:</span><br>
<code>/rooms/</code><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
[
  {
    "room_id": "d8e7a5fa-147a-481a-ba6f-a5772d09c34b",
    "number": 107,
    "available": true,
    "room_category": {
      "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
      "category_name": "Suite",
      "price": 200.0,
      "max_guest_number": 2
    }
  },
  {
    "room_id": "07b6e3c7-54c6-40c8-8233-aaddb08a5fbd",
    "number": 108,
    "available": false,
    "room_category": {
      "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
      "category_name": "Suite",
      "price": 200.0,
      "max_guest_number": 2
    }
  },
  {
    "room_id": "8fa041bc-db67-4e9b-b38d-49901e7ae0bd",
    "number": 101,
    "available": true,
    "room_category": {
      "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
      "category_name": "Suite",
      "price": 200.0,
      "max_guest_number": 2
    }
  }
]
```

<br><br>
<span>Retornar uma reserva pelo usuário:</span><br>
<code>/rooms/room/room_id</code><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "room_id": "8fa041bc-db67-4e9b-b38d-49901e7ae0bd",
  "number": 101,
  "available": true,
  "room_category": {
    "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
    "category_name": "Suite",
    "price": 200.0,
    "max_guest_number": 2
  }
}
```

<br><br>
<span>Atualização de um quarto:</span><br>
<code>/rooms/room/room_id/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Exemplo de entrada

```json
{
  "number": "104"
}
```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "room_id": "8fa041bc-db67-4e9b-b38d-49901e7ae0bd",
  "number": 104,
  "available": true,
  "room_category": {
    "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
    "category_name": "Suite",
    "price": 200.0,
    "max_guest_number": 2
  }
}
```

<br><br>
<span>Remover um quarto:</span><br>
<code>/rooms/room/room_id/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 204 NO CONTENT</code>
<br>Resposta:

```json

```

<br><br>
<span>Retornar quartos disponíveis:</span><br>
<code>/rooms/room_category_id?available=true</code><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "room_id": "8fa041bc-db67-4e9b-b38d-49901e7ae0bd",
  "number": 101,
  "available": true,
  "room_category": {
    "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
    "category_name": "Suite",
    "price": 200.0,
    "max_guest_number": 2
  }
}
```

<br><br>
<span>Retornar quartos indisponíveis:</span><br>
<code>/rooms/room_category_id?available=false</code><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "room_id": "8fa041bc-db67-4e9b-b38d-49901e7ae0bd",
  "number": 101,
  "available": false,
  "room_category": {
    "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
    "category_name": "Suite",
    "price": 200.0,
    "max_guest_number": 2
  }
}
```

<br><br>

## 🧍Reservas:

<br>

<span>Criação de reserva:</span><br>
<code>/reservations/register/room_category_id/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Exemplo de entrada

```json
{
  "in_reservation_date": "2022-07-29",
  "out_reservation_date": "2022-09-26",
  "guest": "quokka@mail.com"
}
```

Status: <code style="color: green; font-size: 16px;"> 201 CREATED</code>
<br>Resposta:

```json
{
  "reservation_id": "caa03add-fd63-41ec-8260-8cda0611570d",
  "in_reservation_date": "2022-07-25",
  "out_reservation_date": "2022-09-26",
  "checkin_date": null,
  "checkout_date": null,
  "status": "available",
  "total_value": null,
  "room_category": {
    "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
    "category_name": "Suite",
    "price": 200.0,
    "max_guest_number": 2
  },
  "room": null
}
```

<br><br>
<span>Retornar todas as reservas:</span><br>
<code>/reservations/</code><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
[
  {
    "reservation_id": "69803eea-9d43-425c-a5b3-7e406545d6c8",
    "in_reservation_date": "2022-07-29",
    "out_reservation_date": "2022-09-26",
    "checkin_date": null,
    "checkout_date": null,
    "status": "available",
    "total_value": null,
    "guest": {
      "user_id": "43908c43-0b3d-48ba-ab26-c696ca02b5df",
      "email": "quokka@mail.com",
      "first_name": "Quokka",
      "last_name": "Quita",
      "age": 30,
      "cpf": "99999999998",
      "phone": "1234567891113"
    },
    "room": null,
    "room_category": {
      "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
      "category_name": "Suite",
      "price": 200.0,
      "max_guest_number": 2
    }
  },
  {
    "reservation_id": "caa03add-fd63-41ec-8260-8cda0611570d",
    "in_reservation_date": "2022-07-25",
    "out_reservation_date": "2022-09-26",
    "checkin_date": null,
    "checkout_date": null,
    "status": "available",
    "total_value": null,
    "guest": {
      "user_id": "43908c43-0b3d-48ba-ab26-c696ca02b5df",
      "email": "quokka@mail.com",
      "first_name": "Quokka",
      "last_name": "Quita",
      "age": 30,
      "cpf": "99999999998",
      "phone": "1234567891113"
    },
    "room": null,
    "room_category": {
      "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
      "category_name": "Suite",
      "price": 200.0,
      "max_guest_number": 2
    }
  }
]
```

<br><br>
<span>Retornar uma reserva pelo id do hóspede:</span><br>
<code>/reservations/guest/guest_id</code><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  {
		"reservation_id": "69803eea-9d43-425c-a5b3-7e406545d6c8",
		"in_reservation_date": "2022-07-29",
		"out_reservation_date": "2022-09-26",
		"checkin_date": null,
		"checkout_date": null,
		"status": "available",
		"total_value": null,
		"room_category": {
			"room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
			"category_name": "Suite",
			"price": 200.0,
			"max_guest_number": 2
		},
		"room": null
	},
	{
		"reservation_id": "caa03add-fd63-41ec-8260-8cda0611570d",
		"in_reservation_date": "2022-07-25",
		"out_reservation_date": "2022-09-26",
		"checkin_date": null,
		"checkout_date": null,
		"status": "available",
		"total_value": null,
		"room_category": {
			"room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
			"category_name": "Suite",
			"price": 200.0,
			"max_guest_number": 2
		},
		"room": null
	}
}
```

<br><br>
<span>Retornar uma reserva pelo id da reserva:</span><br>
<code>/reservations/retrieve/reservation_id</code><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "reservation_id": "caa03add-fd63-41ec-8260-8cda0611570d",
  "in_reservation_date": "2022-07-25",
  "out_reservation_date": "2022-09-27",
  "checkin_date": null,
  "checkout_date": null,
  "status": "available",
  "total_value": null,
  "guest": {
    "user_id": "43908c43-0b3d-48ba-ab26-c696ca02b5df",
    "email": "quokka@mail.com",
    "first_name": "Quokka",
    "last_name": "Quita",
    "age": 30,
    "cpf": "99999999998",
    "phone": "1234567891113"
  },
  "room": null,
  "room_category": {
    "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
    "category_name": "Suite",
    "price": 200.0,
    "max_guest_number": 2
  }
}
```

<br><br>
<span>Atualização de uma reserva:</span><br>
<code>/reservations/reservation_id/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Exemplo de entrada

```json
{
  "out_reservation_date": "2022-09-27"
}
```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "reservation_id": "caa03add-fd63-41ec-8260-8cda0611570d",
  "in_reservation_date": "2022-07-25",
  "out_reservation_date": "2022-09-27",
  "checkin_date": null,
  "checkout_date": null,
  "status": "available",
  "total_value": null,
  "room_category": {
    "room_category_id": "9ef10e70-391c-4bde-adef-2bd68b66eb6a",
    "category_name": "Suite",
    "price": 200.0,
    "max_guest_number": 2
  },
  "room": null
}
```

<br><br>
<span>Checkin de uma reserva:</span><br>
<code>/reservations/reservation_id/checkin/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Exemplo de entrada

```json
{
  "checkin_date": "2022-07-26"
}
```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "reservation_id": "bd12b4c5-9240-4aff-9901-4abdcbf02cde",
  "in_reservation_date": "2022-07-26",
  "out_reservation_date": "2022-09-26",
  "checkin_date": "2022-07-26",
  "checkout_date": null,
  "status": "available",
  "total_value": null,
  "guest": {
    "user_id": "8757bbd4-c88e-4599-88d7-320ee891974c",
    "email": "ravi@mail.com",
    "first_name": "Ravi",
    "last_name": "Scherer",
    "age": 3,
    "cpf": "99999999999",
    "phone": "1234567891112"
  }
}
```

<br><br>
<span>checkout de uma reserva:</span><br>
<code>/reservations/reservation_id/checkout/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Exemplo de entrada

```json
{
  "checkout_date": "2022-09-26"
}
```

Status: <code style="color: green; font-size: 16px;"> 200 OK</code>
<br>Resposta:

```json
{
  "reservation_id": "bd12b4c5-9240-4aff-9901-4abdcbf02cde",
  "in_reservation_date": "2022-07-26",
  "out_reservation_date": "2022-09-26",
  "checkin_date": "2022-07-26",
  "checkout_date": "2022-09-26",
  "status": "available",
  "total_value": 12400.0,
  "guest": {
    "user_id": "8757bbd4-c88e-4599-88d7-320ee891974c",
    "email": "ravi@mail.com",
    "first_name": "Ravi",
    "last_name": "Scherer",
    "age": 3,
    "cpf": "99999999999",
    "phone": "1234567891112"
  }
}
```

<br><br>
<span>Remover uma reserva:</span><br>
<code>/reservations/delete/reservation_id/</code><br>
<code style="color: tomato;">Requer token de ADMIN</code><br><br>
Sem corpo de requisição

```json

```

Status: <code style="color: green; font-size: 16px;"> 204 NO CONTENT</code>
<br>Resposta:

```json

```
