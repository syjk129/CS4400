/*CREATE TABLE IF NOT EXISTS Keywords(
    name VARCHAR(30) NOT NULL,
    keywords VARCHAR(30) NOT NULL,
    PRIMARY KEY (name, keywords),
    FOREIGN KEY(name) REFERENCES Subject(name)
        ON DELETE CASCADE    ON UPDATE CASCADE
);*/
INSERT INTO  `cs4400_Group_60`.`Keywords` (
)
VALUES 
('Children','kids'),
('Children','boys'),
('Children','girls'),
('Medical','medicine'),
('Medical','surgery'),
('Law','lawyer'),
('Law','law'),
('Computer','computer'),
('Science','math'),
('Science','chemical'),
('Business','market'),
('Business','finance');