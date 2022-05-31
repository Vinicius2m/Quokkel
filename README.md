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
	"email": "johndoe@mail.com",
	"password": "1234",
	"first_name": "John",
	"last_name": "Doe",
	"age": 21,
	"cpf": "07744455547",
	"phone": "123456789012347",
	"is_staff": true
}
```

Status: <code style="color: green; font-size: 16px;"> 201 CREATED</code>
<br>Resposta:

```json
{
	"user_id": "01d6ecba-3c57-4718-abd7-986c24484139",
	"email": "johndoe@mail.com",
	"first_name": "John",
	"last_name": "Doe",
	"age": 21,
	"cpf": "07744455547",
	"phone": "123456789012347",
	"is_staff": true
}
```

<br><br>
<span>Login de admin:</span><br>
<code>/admins/login/</code><br><br>
Exemplo de entrada

```json
{
	"email": "johndoe@mail.com",
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
		"user_id": "605c40e1-8df5-4441-9f66-f137fba703ff",
		"email": "johndoe02@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 21,
		"cpf": "13734455547",
		"phone": "2434967890123",
		"is_staff": true
	},
	{
		"user_id": "01d6ecba-3c57-4718-abd7-986c24484139",
		"email": "johndoe03@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 21,
		"cpf": "13734455542",
		"phone": "2434967897123",
		"is_staff": true
	},
	{
		"user_id": "f63e90d7-ca10-4b70-9c34-5de19df3b666",
		"email": "john@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 29,
		"cpf": "08709783903",
		"phone": "1234567891111",
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
	"user_id": "f63e90d7-ca10-4b70-9c34-5de19df3b666",
	"email": "john@mail.com",
	"first_name": "John",
	"last_name": "Doe",
	"age": 29,
	"cpf": "08709783903",
	"phone": "1234567891111",
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
	"user_id": "c6cdde8f-12da-4517-82aa-951a5ddcee7c",
	"email": "johndoe@mail.com",
	"first_name": "John",
	"last_name": "Doe",
	"age": 18,
	"cpf": "07744455547",
	"phone": "123456789012347",
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
	"email": "guest@mail.com",
	"password": "1234",
	"first_name": "Vinícius",
	"last_name": "de Freitas",
	"age": 72,
	"cpf": "99999999999",
	"phone": "1234567891112",
	"is_staff": false
}
```

Status: <code style="color: green; font-size: 16px;"> 201 CREATED</code>
<br>Resposta:

```json
{
	"user_id": "541a5f78-04ac-43ea-9aca-516e9c181d36",
	"email": "guest@mail.com",
	"first_name": "Vinícius",
	"last_name": "de Freitas",
	"age": 72,
	"cpf": "99999999999",
	"phone": "1234567891112"
}
```

<br><br>
<span>Login de hóspede:</span><br>
<code>/guests/login/</code><br><br>
Exemplo de entrada

```json
{
	"email": "guest@mail.com",
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
		"email": "johndoe@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 21,
		"cpf": "07744455547",
		"phone": "1234567890123",
		"is_staff": false
	},
	{
		"user_id": "7e4bd16a-7340-4089-89e3-a9071d983ce9",
		"email": "johndoe00@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 21,
		"cpf": "03744455547",
		"phone": "2234567890123",
		"is_staff": false
	},
	{
		"user_id": "db6ef5b0-5d11-4370-9548-87488491c32d",
		"email": "johndoe01@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 21,
		"cpf": "13744455547",
		"phone": "2434567890123",
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
	"user_id": "541a5f78-04ac-43ea-9aca-516e9c181d36",
	"email": "guest@mail.com",
	"first_name": "Vinícius",
	"last_name": "de Freitas",
	"age": 72,
	"cpf": "99999999999",
	"phone": "1234567891112",
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
	"user_id": "541a5f78-04ac-43ea-9aca-516e9c181d36",
	"email": "guest@mail.com",
	"first_name": "Vinícius",
	"last_name": "de Freitas",
	"age": 18,
	"cpf": "99999999999",
	"phone": "1234567891112"
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
		"email": "johndoe@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 21,
		"cpf": "07744455547",
		"phone": "1234567890123",
		"is_staff": false
	},
	{
		"user_id": "7e4bd16a-7340-4089-89e3-a9071d983ce9",
		"email": "johndoe00@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 21,
		"cpf": "03744455547",
		"phone": "2234567890123",
		"is_staff": false
	},
	{
		"user_id": "db6ef5b0-5d11-4370-9548-87488491c32d",
		"email": "johndoe01@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 21,
		"cpf": "13744455547",
		"phone": "2434567890123",
		"is_staff": false
	},
	{
		"user_id": "605c40e1-8df5-4441-9f66-f137fba703ff",
		"email": "johndoe02@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 21,
		"cpf": "13734455547",
		"phone": "2434967890123",
		"is_staff": true
	},
	{
		"user_id": "01d6ecba-3c57-4718-abd7-986c24484139",
		"email": "johndoe03@mail.com",
		"first_name": "John",
		"last_name": "Doe",
		"age": 21,
		"cpf": "13734455542",
		"phone": "2434967897123",
		"is_staff": true
	},
	{
		"user_id": "f63e90d7-ca10-4b70-9c34-5de19df3b666",
		"email": "victor@mail.com",
		"first_name": "Victor",
		"last_name": "Scherer",
		"age": 29,
		"cpf": "08709783903",
		"phone": "1234567891111",
		"is_staff": true
	},
	{
		"user_id": "541a5f78-04ac-43ea-9aca-516e9c181d36",
		"email": "ravi@mail.com",
		"first_name": "Ravi",
		"last_name": "Scherer",
		"age": 3,
		"cpf": "99999999999",
		"phone": "1234567891112",
		"is_staff": false
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
