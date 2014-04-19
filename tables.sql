CREATE TABLE flight(
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(5)  NOT NULL,
    flight_price       INT    NOT NULL,
    country_from VARCHAR(15)  NOT NULL,
    country_to   VARCHAR(15)  NOT NULL,
    city_from    VARCHAR(15)  NOT NULL,
    city_to      VARCHAR(15)  NOT NULL,
    tr_type VARCHAR(1)        NOT NULL,
    tr_pos INT                NOT NULL,
    tr_pos_type VARCHAR(15)   NOT NULL
) CHARACTER SET utf8 COLLATE utf8_unicode_ci ENGINE INNODB;

CREATE TABLE hotel(
    id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_name VARCHAR(20) NOT NULL,
    country VARCHAR(15)    NOT NULL,
    city VARCHAR(15)       NOT NULL,
    address VARCHAR(25)    NOT NULL,
    hotel_type VARCHAR(20) NOT NULL,
    room_type  VARCHAR(15) NOT NULL,
    room_num   INT         NOT NULL,
    room_price INT         NOT NULL
) CHARACTER SET utf8 COLLATE utf8_unicode_ci ENGINE INNODB;


CREATE TABLE permit(
    id INT AUTO_INCREMENT PRIMARY KEY,
    departure_date DATETIME NOT NULL,
    arrival_date DATETIME   NOT NULL,
    permit_type VARCHAR(25) DEFAULT NULL,
    permit_price INT        NOT NULL
) CHARACTER SET utf8 COLLATE utf8_unicode_ci ENGINE INNODB;