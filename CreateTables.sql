CREATE TABLE PhoneFinder (
	UserID INT PRIMARY KEY,
	UserName VARCHAR(32) UNIQUE,
	Password VARCHAR(16)
);
CREATE TABLE PhoneModel (
	ModelNumber VARCHAR(15),
	Manufacturer VARCHAR(15),
	PhoneName VARCHAR(15),
	PRIMARY KEY(ModelNumber)
);
CREATE TABLE Finds (
	ModelNumber VARCHAR(15) REFERENCES PhoneModel(ModelNumber) ON DELETE CASCADE,
	UserID INT REFERENCES PhoneFinder(UserID) ON DELETE CASCADE,
	PRIMARY KEY(ModelNumber, UserID)
);
CREATE TABLE Store (
	StoreNameID CHAR(15) PRIMARY KEY,
	StoreName VARCHAR(32),
	Address VARCHAR(64),
	City VARCHAR(15),
	State VARCHAR(15),
	Price FLOAT
);
CREATE TABLE SoldAt (
	ModelNumber CHAR(15) REFERENCES PhoneModel(ModelNumber) ON DELETE CASCADE,
	StoreNameID CHAR(15) REFERENCES Store(StoreNameID) ON DELETE CASCADE,
	PRIMARY KEY(ModelNumber, StoreNameID)
);
CREATE TABLE Accessories (
	ModelNumber CHAR(15),
	HasCase VARCHAR(32),
	ScreenProtector VARCHAR(32),
	PRIMARY KEY(ModelNumber, HasCase),
	FOREIGN KEY(ModelNumber) REFERENCES PhoneModel ON DELETE CASCADE
);
CREATE TABLE ScreenType (
	ModelNumber CHAR(15),
	ScreenType VARCHAR(15),
	Resolution VARCHAR(32),
	AspectRatio VARCHAR(32),
	PRIMARY KEY(ModelNumber, ScreenType),
	FOREIGN KEY(ModelNumber) REFERENCES PhoneModel ON DELETE CASCADE
);
CREATE TABLE Specs (
	ModelNumber CHAR(15),
	Cpu VARCHAR(32),
	Color VARCHAR(15),
	Weight VARCHAR(6),
	BatteryLife VARCHAR(6),
	Dimensions VARCHAR(32),
	Storage VARCHAR(6),
	PRIMARY KEY(ModelNumber, CPU),
	FOREIGN KEY(ModelNumber) REFERENCES PhoneModel ON DELETE CASCADE
);
