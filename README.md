# table_reservation
Сервис позволяет создавать, просматривать и удалять брони, а также управлять столиками и временными слотами

1) склонируйте себе проект, например
git clone git@github.com:vawy/table_reservation.git
2) после создайте в app/settings файл .env, куда поместите данные о бд
```bazaar
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=test_db
```
3) запустите
```bazaar
docker-compose up --build
```
