INSERT INTO PhoneModel(ModelNumber, manufacturer, phoneName)
	VALUES('0001', 'Apple', 'iPhone');
INSERT INTO Accessories(ModelNumber, HasCase, ScreenProtector)
	VALUES('0001', 'False', 'False');
INSERT INTO ScreenType(ModelNumber, screenType, resolution, aspectRatio)
	VALUES('0001', 'LCD', '320x480', '1.5:1');
INSERT INTO Specs(ModelNumber, CPU, color, weight, batteryLife, dimensions, Storage)
	VALUES('0001', 'ARM11', 'Black', '135g', '8h', '115x61x11.6mm', '4GB');

INSERT INTO PhoneModel(ModelNumber, manufacturer, phoneName)
	VALUES('0002', 'Samsung', 'Galaxy S6');
INSERT INTO Accessories(ModelNumber, HasCase, ScreenProtector)
	VALUES('0002', 'True', 'False');
INSERT INTO ScreenType(ModelNumber, screenType, resolution, aspectRatio)
	VALUES('0002', 'OLED', '1440x2560', '16:9');
INSERT INTO Specs(ModelNumber, CPU, color, weight, batteryLife, dimensions, Storage)
	VALUES('0002', '7420 Octa', 'Black', '138g', '17h', '143x71x7mm', '64GB');
	
INSERT INTO PhoneModel(ModelNumber, manufacturer, phoneName)
	VALUES('0003', 'OnePlus', '8T');
INSERT INTO Accessories(ModelNumber, HasCase, ScreenProtector)
	VALUES('0003', 'True', 'True');
INSERT INTO ScreenType(ModelNumber, screenType, resolution, aspectRatio)
	VALUES('0003', 'OLED 120Hz', '1080x2400', '20:9');
INSERT INTO Specs(ModelNumber, CPU, color, weight, batteryLife, dimensions, Storage)
	VALUES('0003', 'Snapdragon 865', 'Aqua', '188g', '104h', '160x74x8mm', '128GB');
	
INSERT INTO PhoneModel(ModelNumber, manufacturer, phoneName)
	VALUES('0004', 'Google', 'Pixel 6 Pro');
INSERT INTO Accessories(ModelNumber, HasCase, ScreenProtector)
	VALUES('0004', 'False', 'False');
INSERT INTO ScreenType(ModelNumber, screenType, resolution, aspectRatio)
	VALUES('0004', 'OLED 120Hz', '1440x3120', '19.5:9');
INSERT INTO Specs(ModelNumber, CPU, color, weight, batteryLife, dimensions, Storage)
	VALUES('0004', 'Google Tensor', 'White', '210g', '84h', '164x76x9mm', '256GB');
	
INSERT INTO PhoneModel(ModelNumber, manufacturer, phoneName)
	VALUES('0005', 'Apple', 'iPhone SE');
INSERT INTO Accessories(ModelNumber, HasCase, ScreenProtector)
	VALUES('0005', 'True', 'False');
INSERT INTO ScreenType(ModelNumber, screenType, resolution, aspectRatio)
	VALUES('0005', 'LCD', '750x1334', '16:9');
INSERT INTO Specs(ModelNumber, CPU, color, weight, batteryLife, dimensions, Storage)
	VALUES('0005', 'A15 Bionic', 'Red', '144g', '62h', '138x67x7mm', '64GB');

INSERT INTO Store(StoreNameID, StoreName, Address, City, State, Price)
	VALUES('01253', 'Best Buy', '500 E University', 'Tempe', 'Arizona', 1000.0);
INSERT INTO Store(StoreNameID, StoreName, Address, City, State, Price)
	VALUES('83042', 'T-Mobile', '777 S Mill Ave', 'Tempe', 'Arizona', 900.0);
INSERT INTO Store(StoreNameID, StoreName, Address, City, State, Price)
	VALUES('77272', 'Target', '1800 E Rio Salado', 'Tempe', 'Arizona', 750.0);
INSERT INTO Store(StoreNameID, StoreName, Address, City, State, Price)
	VALUES('13954', 'Costco', '4502 E Oak St', 'Phoenix', 'Arizona', 820.0);
INSERT INTO Store(StoreNameID, StoreName, Address, City, State, Price)
	VALUES('99999', 'Apple Store', '7014 E Camelback', 'Scottsdale', 'Arizona', 940.0);
	
INSERT INTO SoldAt(SoldAtModelNumber, StoreNameID)
	VALUES('0001', '01253');
INSERT INTO SoldAt(SoldAtModelNumber, StoreNameID)
	VALUES('0001', '99999');
INSERT INTO SoldAt(SoldAtModelNumber, StoreNameID)
	VALUES('0002', '77272');
INSERT INTO SoldAt(SoldAtModelNumber, StoreNameID)
	VALUES('0003', '01253');
INSERT INTO SoldAt(SoldAtModelNumber, StoreNameID)
	VALUES('0003', '83042');
INSERT INTO SoldAt(SoldAtModelNumber, StoreNameID)
	VALUES('0003', '13954');
INSERT INTO SoldAt(SoldAtModelNumber, StoreNameID)
	VALUES('0003', '77272');
INSERT INTO SoldAt(SoldAtModelNumber, StoreNameID)
	VALUES('0004', '13954');
INSERT INTO SoldAt(SoldAtModelNumber, StoreNameID)
	VALUES('0005', '99999');
INSERT INTO SoldAt(SoldAtModelNumber, StoreNameID)
	VALUES('0005', '13954');

INSERT INTO PhoneFinder(UserID, UserName, Password)
	VALUES(1, 'User1', 'pwd');
INSERT INTO PhoneFinder(UserID, UserName, Password)
	VALUES(2, 'testing', 'pwd');
INSERT INTO Finds(ModelNumber, UserID)
	VALUES('0001', 1);
