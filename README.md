# Web
Проект представляет собой сервис ответов на вопросы. Пользователь сервиса имеет возможность зарегистрироваться, задать вопрос, ответить на вопросы других пользователей.

# Основные сущности проекта
1. Пользователь - email, имя, пароль
2. Вопрос - заголовок, текст, автор, рейтинг вопроса
3. Ответ - текст, вопрос, автор

# Формы и страницы проекта

## Главная страница

URL: /

Представляет из себя список "популярных" вопросов. В списке выводятся вопросы в порядке убывания рейтинга.

## Список новых вопросов

URL: /new/

Список вопросов по дате их добавления начиная с самого свежего.

## Страница одного вопроса

URL: /question/123/

На этой странице можно прочитать текст вопроса и список ответов к нему. Авторизованные пользователи могут добавить свой ответ.

## Страница регистрации

URL: /signup/

Пользователь может ввести свой email, пароль, имя и зарегистрироваться в проекте

## Страница авторизации

URL: /login/

Пользователь может ввести email и пароль и авторизоваться в проекте.

## Страница добавления вопроса

URL: /ask/

Авторизованный пользователь может задать вопрос, после чего перейдет на страницу этого вопроса.
