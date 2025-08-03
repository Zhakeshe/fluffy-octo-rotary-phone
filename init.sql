CREATE TABLE countries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  code TEXT NOT NULL,
  price INTEGER NOT NULL,
  flag TEXT NOT NULL
);

INSERT INTO countries (name, code, price, flag) VALUES
('Россия', '+7', 500, 'ru.png'),
('Британия', '+44', 700, 'gb.png'),
('Испания', '+34', 650, 'es.png'),
('Италия', '+39', 620, 'it.png'),
('Дания', '+45', 600, 'dk.png'),
('Нидерланды', '+31', 580, 'nl.png'),
('Франция', '+33', 660, 'fr.png'),
('Венгрия', '+36', 550, 'hu.png'),
('Швейцария', '+41', 670, 'ch.png'),
('Польша', '+48', 540, 'pl.png'),
('Швеция', '+46', 630, 'se.png'),
('Германия', '+49', 610, 'de.png');