/*CREATE TABLE IF NOT EXISTS Book (
    isbn VARCHAR(30) NOT NULL,
    title VARCHAR(60) NOT NULL,
    edition VARCHAR(30) ,
    publisher VARCHAR(30) ,
    place_of_publication VARCHAR(30),
    copyright_year INT,
    is_book_on_reserve ENUM('Y','N') DEFAULT 'N',
    shelf_num INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    cost INT;
    PRIMARY KEY(isbn)
    );*/

INSERT INTO  `cs4400_Group_60`.`Book` (
`isbn`,`title`,`edition`,`publisher`,
`place_of_publication`,`copyright_year`,`is_book_on_reserve`,`shelf_num`,`name`,`cost`
)
VALUES 
('978-1780671062','Secret Garden', 'Act Clr Cs','Laurence King Publishing',
'','2013','Y','1','Children','9.57'),
('978-0545685191','Minecraft: The Complete Handbook Collection', '1st','Scholastic Inc',
'','2014','N','1','Children','18.15'),
('978-0805095159','Being Mortal: Medicine and What Matters in the End', '1st','Metropolitan Books',
'','2014','Y','1','Medical','11.70'),
('978-1591847779','Our Lost Constitution: The Willful Subversion of America Founding Document', '1st','Sentinel',
'','2015','N','1','Law','16.77'),
 ('978-0136086208',  'Fundamentals of Database Systems',  '6th',  'Addison-Wesley', NULL ,  '2010',  'N',  '2',  'Computer','137.25'
),
('978-0132856201','Computer Networking: A Top-Down Approach', '6th','Pearson',NULL, '2012', 'N', '2', 'Computer','133.21'),
('978-0374533557','Thinking, Fast and Slow', 'Reprint','Farrar, Straus and Giroux', NULL, '2013', 'N', '2', 'Science','7.26'),
('978-1476728742','The Wright Brothers', '1st', 'Simon & Schuster',NULL, '2015', 'N', '2',' Science','18'),
('978-0060555665','The Intelligent Investor: The Definitive Book on Value Investing', 'Rev Sub',' HarperBusiness',NULL, '2006', 'N', '3', 'Business','13.20'),
('978-0553585971','The Wealth of Nations ', 'Reprint','Bantam Classics', NULL, '2003', 'N', '3', 'Business','7.15');