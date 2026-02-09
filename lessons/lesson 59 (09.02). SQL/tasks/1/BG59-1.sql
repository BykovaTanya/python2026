SELECT * from titanic;
sELECT Name from titanic WHERE age>30;
SELECT Name from titanic WHERE sex='female' and Pclass=1;
SELECT Name,Age from titanic WHERE Survived=1 ORDER by age;
SELECT Name from titanic WHERE Parch=0 or SibSp=0;
SELECT Name,Pclass from titanic WHERE fare>100;
SELECT Name,Pclass,Age from titanic WHERE Pclass !=1 and age >18;
SELECT Name from titanic WHERE Survived=0 and Parch=0 or SibSp=0;
SELECT Name,fare, Pclass from titanic WHERE fare<10 ORDER by Pclass !=3;