--DROP TABLE IF EXISTS book;

CREATE TABLE book (
    datetime VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    count_x NUMERIC
);

INSERT INTO book (datetime, title, count_x) VALUES ('15.11.2023 15:00:25.001', 'Arya', 55);

SELECT * FROM book;