DROP TABLE IF EXISTS book;

CREATE TABLE book (
    datetime VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    count_x NUMERIC
);

SELECT * FROM book;