INSERT INTO PhoneModel(ModelNumber, manufacturer, phoneName)
	VALUES('0001', 'Apple', 'iPhone');
INSERT INTO Accessories(ModelNumber, HasCase, ScreenProtector)
	VALUES('0001', 'False', 'False');
INSERT INTO ScreenType(ModelNumber, screenType, resolution, aspectRatio)
	VALUES('0001', 'LCD', '320x480', '1.5:1');
INSERT INTO Specs(ModelNumber, CPU, color, weight, batteryLife, dimensions, Storage)
	VALUES('0001', 'ARM11', 'Black', '135g', '8h', '115x61x11.6mm', '4GB');
INSERT INTO Store(StoreNameID, StoreName, City, State, Price)
	VALUES('01253', 'Best Buy', 'Tempe', 'Arizona', 1000);
INSERT INTO SoldAt(ModelNumber, StoreNameID)
	VALUES('0001', '01253');
INSERT INTO PhoneFinder(UserID, UserName, Password)
	VALUES(1, 'User1', 'pwd');
INSERT INTO Finds(ModelNumber, UserID)
	VALUES('0001', 1);
