/*CREATE TABLE IF NOT EXISTS Student_Faculty (
    username VARCHAR(30) NOT NULL,
    name VARCHAR(30) NOT NULL,
    email  VARCHAR(30),
    address VARCHAR(30),
    dob DATE,
    gender ENUM('M', 'F'),
    faculty ENUM('Y','N') DEFAULT 'N',
    debarred ENUM('Y','N') DEFAULT 'N',
    penalty FLOAT(6,2) DEFAULT 0,
    department VARCHAR(30),
    PRIMARY KEY (username),
    FOREIGN KEY (username) REFERENCES User(username)
        ON DELETE CASCADE    ON UPDATE CASCADE
    );*/

INSERT INTO  `cs4400_Group_60`.`Student_Faculty` (

)
VALUES 

('student1',  'Stu1','stu1@gatech.edu','Atlanta','1992-2-21','M','N','Y','100.5',''),
('student2',  'Stu2','stu2@gatech.edu','Atlanta','1993-5-4','M','N','Y','103',''),
('student3',  'Stu3','stu3@gatech.edu','New York','1991-9-13','F','N','N','1',''),
('student4',  'Stu4','stu4@gatech.edu','Decatur','1994-6-09','M','N','N','5',''),
('student5',  'Stu5','stu5@gatech.edu','Seattle','1997-5-1','M','N','N','0.5',''),
('student6',  'Stu6','stu6@gatech.edu','Atlanta','1993-8-3','F','N','N','0',''),
('student7',  'Stu7','stu7@gatech.edu','Miami','1995-1-1','M','N','N','',''),
('student8',  'Stu8','stu8@gatech.edu','Orlando','1996-3-17','F','N','N','15',''),
('student9',  'Stu9','stu9@gatech.edu','Atlanta','1992-7-7','F','N','N','95',''),
('student10',  'Stu10','stu10@gatech.edu','Columbus','1993-5-26','M','N','N','10',''),
('student11',  'Stu11','stu11@gatech.edu','Atlanta','1988-4-19','F','N','N','2',''),
('student12',  'Stu12','stu12@gatech.edu','Marietta','1994-12-20','M','N','N','',''),
('student13',  'Stu13','stu13@gatech.edu','Atlanta','1993-11-4','M','N','N','',''),
('student14',  'Stu14','stu14@gatech.edu','Savannah','1996-2-12','M','N','N','20',''),
('student15',  'Stu15','stu15@gatech.edu','Atlanta','1995-10-9','F','N','N','70',''),
('faculty1',  'Fct1','Fct1@gatech.edu','Atlanta','1965-2-9','F','Y','N','70','CS'),
('faculty2',  'Fct2','Fct2@gatech.edu','Miami','1955-8-12','M','Y','N','0','Math'),
('faculty3',  'Fct3','Fct3@gatech.edu','Atlanta','1971-11-28','F','Y','N','20','Physics'),
('faculty4',  'Fct4','Fct4@gatech.edu','Savannah','1958-4-29','M','Y','N','5','CS'),
('faculty5',  'Fct5','Fct5@gatech.edu','Atlanta','1969-5-17','M','Y','N','','Chem');