INSERT INTO user_types(name)
VALUES("Менеджер"),
      ("Автомеханик"),
      ("Оператор"),
      ("Заказчик");

INSERT INTO users (fio, phone, login, password, type_id)
VALUES("Белов Александр Давидович",	"89210563128", "login1", "pass1", 1),
("Харитонова Мария Павловна", "89535078985", "login2", "pass2", 2),
("Марков Давид Иванович", "89210673849", "login3", "pass3", 2),
("Громова Анна Семёновна", "89990563748", "login4",	"pass4", 3),
("Карташова Мария Данииловна", "89994563847", "login5",	"pass5", 3),
("Касаткин Егор Львович", "89219567849", "login11",	"pass11", 4),
("Ильина Тамара Даниловна",	"89219567841", "login12", "pass12", 4),
("Елисеева Юлиана Алексеевна", "89219567842", "login13", "pass13", 4),
("Никифорова Алиса Тимофеевна", "89219567843", "login14", "pass14", 4),
("Васильев Али Евгеньевич", "89219567844", "login15", "pass15", 2);

INSERT INTO car_types(name)
VALUES("Легковая"), ("Грузовая");

INSERT INTO car_brands(name)
VALUES("Hyundai"), ("Nissan"), ("Toyota"), ("Citroen"), ("УАЗ");

INSERT INTO car_models(name)
VALUES("Avante (CN7)"), ("180SX"), ("2000GT"), ("Berlingo (B9)"), (" 2360 ");

INSERT INTO cars(type_id, brand_id, model_id)
VALUES(1, 1, 1), (1, 2, 2), (1, 3, 3), (2, 4, 4), (2, 5, 5);

INSERT INTO status(name)
VALUES("Новая заявка"), ("В процессе ремонта"), ("Готова к выдаче");

INSERT INTO requests(start_date, complete_date, car_id, client_id, description, status_id,master_id)
VALUES
("2023-06-06", "", 1, 7, "Отказали тормоза.", 2, 2),
("2023-05-05", "",2, 8, "Отказали тормоза.", 2, 3),
("2022-07-07", "2023-01-01",3, 9, "В салоне пахнет бензином.", 3, 3),
("2023-08-02", "", 4, 8, "Руль плохо крутится.", 1, 2),
("2023-08-02", "", 5, 9, "Руль плохо крутится.", 1, 2);

INSERT INTO comments(message, master_id, request_id)
VALUES("Очень странно.", 2, 1), ("Будем разбираться!", 3, 2), ("Очень странно.", 3, 3)