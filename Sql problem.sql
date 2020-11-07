CREATE TABLE colleges(
College_id varchar(18) primary key  UNIQUE,
College_Name varchar(100) not null,
College_code Varchar(18) not Null);

Create Table Departments(
Department_id varchar(18) Primary key Unique,
Name_of_Department Varchar(50),
N_of_Students Integer Default(50),
College_id varchar(18), foreign key(College_id) references colleges(College_id));


Insert into colleges values('C-1','Adithya Engineering College','AE-101');
Insert into colleges values('C-2','Jawaharlal Nehru Technical University','JN-243');
Insert into colleges values('C-3','Geetham University','GTM-22');
Insert into colleges values('C-4','Koneru Lakshmaiah University','KL-23');
Insert into colleges values('C-5','Vishnu Engineering College','VE-44');
Insert into colleges values('C-6', 'VFSTR Foundation','VFT-66');

Insert into departments values('Dpt-CS01','Computer Science',200,'C-4');
Insert into departments values('Dpt-ME02','Mechanical',65,'C-5');
Insert into departments values('Dpt-EC01','Electronics',110,'C-3');
Insert into departments values('Dpt-EL04','Electrical',700,'C-3');
Insert into departments values('Dpt-EC02','Electronics',80,'C-2');
Insert into departments values('Dpt-FT06','Food Technology',90,'C-6');
Insert into departments values('Dpt-AE07','Automobile',35,'C-6');
Insert into departments values('Dpt-CV03','Civil',85,'C-1');
Insert into departments values('Dpt-CV01','Civil',110,'C-2');
Insert into departments values('Dpt-EC05','Electronics',90,'C-3');
Insert into departments values('Dpt-Av01','Aviation',35,'C-5');
Insert into departments values('Dpt-AT11','Aeronautical',65,'C-1');
Insert into departments values('Dpt-BI65','BioInformatics',86,'C-1');
Insert into departments values('Dpt-BT77','Biotechnology',130,'C-2');
Insert into departments values('Dpt-CS34','Computer Science',210,'C-2');
Insert into departments values('Dpt-ME77','Mechanical',140,'C-6');
Insert into departments values('Dpt-EL77','Electrical',95,'C-4');
Insert into departments values('Dpt-BT45','Biotechnology',75,'C-4');
Insert into departments values('Dpt-AE33','Automobile',130,'C-5');
Insert into departments values('Dpt-CS22','Computer Science',240,'C-3');
Insert into departments values('Dpt-BI56','BioInformatics',73,'C-2');
Insert into departments values('Dpt-CS99','Computer Science',180,'C-5');
Insert into departments values('Dpt-ME56','Mechanical',66,'C-3');
Insert into departments values('Dpt-AT33','Aeronautical',85,'C-4');
Insert into departments values('Dpt-CV44','Civil',95,'C-6');

