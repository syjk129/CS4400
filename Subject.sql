/*CREATE TABLE IF NOT EXISTS Subject (
    name VARCHAR(30) NOT NULL,
    num_of_journals INT,
    floor_num INT NOT NULL,
    PRIMARY KEY (name),
    FOREIGN KEY(floor_num ) REFERENCES Floor(floor_num )
        ON DELETE CASCADE    ON UPDATE CASCADE
);*/
INSERT INTO  `cs4400_Group_60`.`Subject` (
)
VALUES 
('Children','5','1'),
('Medical','15','1'),
('Law','20','1'),
('Computer','20','2'),
('Science','30','2'),
('Business','15','3');