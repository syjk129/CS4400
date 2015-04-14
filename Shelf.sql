/*CREATE TABLE IF NOT EXISTS Shelf (
    shelf_num INT NOT NULL,
    aisle_num INT NOT NULL,
    floor_num INT NOT NULL,
    PRIMARY KEY (shelf_num),
    FOREIGN KEY(floor_num ) REFERENCES Floor(floor_num )
        ON DELETE CASCADE    ON UPDATE CASCADE

);*/
INSERT INTO  `cs4400_Group_60`.`Shelf` (
)
VALUES 
('1','1','1'),
('2','1','2'),
('3','1','3');