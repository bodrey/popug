Это учебный проект системы управления попугами PopugJira UberPopug Inc

Андрей Мартынов, AA6

КОММЕНТ week 3:

В этом реквесте я исправляю свой кривой PR из прошлого раза, в который вошли компоненты pycache.

Я отстаю от графика домашек, но поланирую догонять. Что сделано в этот раз:

Здесь у нас заработала авторизация. Пока что у нас все еще два сервиса - auth и task.

Сервис task смотрит токен в куках и либо проверяет его (запрашивая у auth), либо сразу перекидывает на страничку логина сервиса auth, если токена нет.

У сервиса auth заработал listener, который отвечает сервису task. Если он вернул токен, то task прописывает его в куки и дальше пускает по нему.

В оба сервиса добавлена валидация схемы сообщений через python jsonschema, однако схемы пока не вынесены в отдельное хранилище.

Доска Miro:
    https://miro.com/app/board/uXjVNtbEVlI=/?share_link_id=436752171344
