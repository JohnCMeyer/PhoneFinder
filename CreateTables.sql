CREATE TABLE PhoneFinder (
	UserID INT PRIMARY KEY,
	UserName VARCHAR(32) UNIQUE,
	Password VARCHAR(16)
);
CREATE TABLE PhoneModel (
	ModelNumber CHAR(4),
	Manufacturer VARCHAR(32),
	PhoneName VARCHAR(32),
	PRIMARY KEY(ModelNumber)
);
CREATE TABLE Finds (
	ModelNumber CHAR(4) REFERENCES PhoneModel(ModelNumber) ON DELETE CASCADE,
	UserID INT REFERENCES PhoneFinder(UserID) ON DELETE CASCADE,
	PRIMARY KEY(ModelNumber, UserID)
);
CREATE TABLE Store (
	StoreNameID CHAR(5) PRIMARY KEY,
	StoreName VARCHAR(32),
	Address VARCHAR(64),
	City VARCHAR(16),
	State VARCHAR(16),
	Price FLOAT
);
CREATE TABLE SoldAt (
	SoldAtModelNumber CHAR(4) REFERENCES PhoneModel(ModelNumber) ON DELETE CASCADE,
	StoreNameID CHAR(5) REFERENCES Store(StoreNameID) ON DELETE CASCADE,
	PRIMARY KEY(SoldAtModelNumber, StoreNameID)
);
CREATE TABLE Accessories (
	ModelNumber CHAR(4),
	HasCase VARCHAR(32),
	ScreenProtector VARCHAR(32),
	PRIMARY KEY(ModelNumber, HasCase),
	FOREIGN KEY(ModelNumber) REFERENCES PhoneModel ON DELETE CASCADE
);
CREATE TABLE ScreenType (
	ModelNumber CHAR(4),
	ScreenType VARCHAR(16),
	Resolution VARCHAR(32),
	AspectRatio VARCHAR(32),
	PRIMARY KEY(ModelNumber, ScreenType),
	FOREIGN KEY(ModelNumber) REFERENCES PhoneModel ON DELETE CASCADE
);
CREATE TABLE Specs (
	ModelNumber CHAR(4),
	Cpu VARCHAR(32),
	Color VARCHAR(16),
	Weight VARCHAR(16),
	BatteryLife VARCHAR(16),
	Dimensions VARCHAR(32),
	Storage VARCHAR(16),
	PRIMARY KEY(ModelNumber, CPU),
	FOREIGN KEY(ModelNumber) REFERENCES PhoneModel ON DELETE CASCADE
);
