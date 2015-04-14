/*CREATE TABLE IF NOT EXISTS Authors(
    isbn VARCHAR(30) NOT NULL,
    authors_name VARCHAR(30) NOT NULL,
    PRIMARY KEY(isbn,authors_name),
    FOREIGN KEY (isbn) REFERENCES Book(isbn)
        ON DELETE CASCADE    ON UPDATE CASCADE
    );
*/
INSERT INTO  `cs4400_Group_60`.`Authors` (
`isbn`,`authors_name`
)
VALUES 
('978-1780671062','Basford, Johanna'),


('978-0545685191','Stephanie Milton'),
('978-0545685191','Paul Soares Jr.'),


('978-0805095159','Atul Gawande'),


('978-1591847779',' Mike Lee'),


('978-0136086208', 'Ramez Elmasri '),
('978-0136086208', 'Shamkant B. Navathe'),


('978-0132856201', 'James F. Kurose'),
('978-0132856201', 'Keith W. Ross'),


('978-0374533557','Daniel Kahneman'),


('978-1476728742','David McCullough'),


('978-0060555665','Benjamin Graham'),
('978-0060555665','Jason Zweig'),


('978-0553585971','Adam Smith'),
('978-0553585971','Alan B. Krueger');