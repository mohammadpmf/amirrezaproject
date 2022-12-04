list_of_iran_cities =['Tehran','Tabriz','Esfahan','Ahvaz','Qazvin','Shiraz','Mashehad','Hamedan','Rasht','Zanjan'  ,
                              'Karaj','Hamedan','Kashan','Khoramshar','Khozestan','Kish','Ardabil','Khalkhal','Mako','Khoy',
                              'Bandar e Abbas','Mazandaran','Golestan',' Qom']
#------------------------------------------------------------------------------------------
list_of_world_cities =['Paris','Londan','Rio','Ezmir','Amesterdam','Newyork','Madrid','Barcelona','Estanbol','Berlin'
                              ,'Brazilan','Ankara','Torento','Milan','Dubai','Frankfort']
#------------------------------------------------------------------------------------------
list_of_seat_numbers =['a01','a02','a03','a04','a05','a06','a07','a08','a09','a10','a11',
                       'b01','b02','b03','b04','b05','b06','b07','b08','b09','b10','b11',
                       'c01','c02','c03','c04','c05','c06','c07','c08','c09','c10','c11',
                       'd01','d02','d03','d04','d05','d06','d07','d08','d09','d10','d11']
#-------------------------------------------------------------------------------------------
list_of_airlines_iran =['Mahan Airline','Ata Airline','Homa Airline',
                              'Atrak Airline','Nafet Airline','Kish Airline',
                              'Zagros Airline','Iran Airline','Aseman Airline',
                              'Qeshm Airline','Varesh Airline','Caspian Airline',]
#--------------------------------------------------------------------------------------------
list_of_airlines_world =['New zealand Airline','Singapore Airline','All Nippon Airline'
                              ,'Qatar Airline','Lufthansa Airline','American Airline','Japen Airline'
                              ,'United Airline','Emirates Airline','Virgin Airline'
                              ,'Alitalia Airline','Uk International Airline']
#------------------------------------------------------------------------------------------------
list_of_hotel_iran =['H_Espinas (Tehran)','H_Esteglal(Tehran)','H_Azadi(Tehran)',
                              'H_Bozorg(Tehran)','H_Maryam(Kish)','H_Toranj(Kish)',
                              'H_Palace(Kish)','H_Vida(Kish)','H_Dinamond(Mashahad)',
                              'H_Chamran(Shiraz)','H_Elgoli Pars(Tabriz)','H_Shahryar(Tabriz)',
                              'H_Abbasi(Esfahan)','H_Aseman(Esfahan)','H_Dad(Yazd)',
                              'H_Kadus(Rasht)','H_Pars(Kerman)']
#------------------------------------------------------------------------------------------------
list_of_hotel_degree_iran =['H_Espinas = ****','H_Esteglal = ****','H_Azadi = ****','H_Bozorg = ***',
                              'H_Maryam = ***','H_Toranj = ***','H_Kadus = ****','H_Pars = **',
                              'H_Abbasi = **','H_Aseman = **','H_Palace = ****','H_Dinamond = **',
                              'H_Chamran = ****','H_Elgoli = ****','H_Shahryar = ***','H_Dad = **']
#------------------------------------------------------------------------------------------------
list_of_hotel_degree_world =['H_Norman = ****','H_Metropol = ****','H_Riters = ****','Kapla = ***',
                              'Bauer O.Lak = ****','H_Ellerman House = **','H_Seviran = ***','H_Cartesian = ***',
                              'H_Plaza = **','H_Palms = **','H_Palace = ****','H_Boulders = **',
                              'H_Westin = ****','H_Elgoli = ****','H_Burj AL Arab = ***','H_Mardan Palac = **']
#------------------------------------------------------------------------------------------------
list_of_hotel_world =['H_Norman(TelAviv)','H_Metropol(Monutcarlo)','H_Riters(Shanghai)',
                      'Kapla(Singapore)','H_Seviran(kyoto)','H_Cartesian(Puebla)',
                      'Bauer O.Lak(Zurich)','H_Ellerman House(CapeTown)','H_Ramba(Jaipur)',
                      'H_Mardan Palace(Turkey)','H_Westin(Rome)','H_Burj AL Arab(Dubai)',
                      'H_Plaza(Newyork)','H_Palms(LasVegas)','H_Boulders(Arizona)']
#-----------------------------------------------------------------------------------------
list_of_countries =['Afghanistan','Albania','Algeria','Andorra','Angola','Argentina','Armenia','Australia','Austria','Azarbijan','Bahamas',
                    'Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia','Botswana','Brazil',
                    'Britain','Brunei','Bulgaria','Burkina Faso','Burma','Cambodia','Cameroon','Canada','Cape Verde','Chad','Chile','China',
                    'Colombia','Congo','Costa Rica','Croatia','Cuba','Cypurs','Czech Republic','Denmark','Djibouti','Dominica','Dominican',
                    'Ecuador','Egypt','El Salvador','England','Eritera','Estonia','Ethiopia','Fiji','Finland','France','Gabon','Gambia',
                    'Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guyana','Haiti','Netherlands','Honduras','Hungray',
                    'Iceland','India','Indonesia','Iran','Iraq','Ireland Republic','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya',
                    'Kuwait','Laos','Lebanon','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi',
                    'Malaysia','Maldives','Mali','Malta','Mauritania','Mauritius','Mexico','Moldova','Monaco','Mongolia','Montenegro',
                    'Morocco','Mozambique','Namibia','Nepal','New Zealand','Nicaragua','Niger','Nigeria','North Korea','Norway','Oman',
                    'Pakistan','Panama','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saudi Arabic',
                    'Scotland','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenai','Solomon','Somalia','South Africa',
                    'South Korea','Spain','Sri Lanka','Sudan','Suriname','Swaziland','Sweden','Syria','Taiwan','Tajikastan','Tanzania',
                    'Thailand','Togo','Tuniasa','Turkey','Turkamanestan','Tuvalu','Uganda','Ukranie','UAE','UK','USA','Uruguay','Uzbekistan',
                    'Vanutau','Vatican','Venezuela','Vietnam','Wales','Samoa','Yeman','Yugoslavia','Zaire','Zambia','Zimbawe']

list_of_db_queries = [
  "CREATE SCHEMA IF NOT EXISTS `travel`;", # این ویرگول یادت نره. مهمه. بیرون از کوتیشن هم باید باشه.


  "CREATE TABLE IF NOT EXISTS `travel`.`signup` (\
  `id` INT NOT NULL AUTO_INCREMENT,\
  `firstname` VARCHAR(45) NOT NULL,\
  `lastname` VARCHAR(45) NOT NULL,\
  `age` INT NOT NULL,\
  `nationality` VARCHAR(45) NOT NULL,\
  `gender` VARCHAR(10) NOT NULL,\
  `email` VARCHAR(45) NOT NULL,\
  `username` VARCHAR(45) NOT NULL,\
  `password` VARCHAR(45) NOT NULL,\
  `datebirthday` DATE NOT NULL,\
  PRIMARY KEY (`id`),\
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,\
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);", # این ویرگول یادت نره. مهمه. بیرون از کوتیشن هم باید باشه.


  "CREATE TABLE IF NOT EXISTS `travel`.`airplane` (\
  `id` INT NOT NULL AUTO_INCREMENT,\
  `cmb_origin` VARCHAR(45) NOT NULL,\
  `cmb_destination` VARCHAR(45) NOT NULL,\
  `dt_flight` DATE NOT NULL,\
  `num_passengers` VARCHAR(45) NOT NULL,\
  `air_companey` VARCHAR(45) NOT NULL,\
  `type_flight` VARCHAR(45) NOT NULL,\
  `time_flight_h` VARCHAR(2) NOT NULL,\
  `time_flight_m` VARCHAR(2) NOT NULL,\
  `seat_number` VARCHAR(45) NOT NULL,\
  `price` INT NULL,\
  `iran_or_world` VARCHAR(5) NOT NULL,\
  PRIMARY KEY (`id`));", # این ویرگول یادت نره. مهمه. بیرون از کوتیشن هم باید باشه.


  "CREATE TABLE IF NOT EXISTS `travel`.`hotel` (\
  `id` INT NOT NULL AUTO_INCREMENT,\
  `desired_hotel` VARCHAR(45) NOT NULL,\
  `quality_degree` VARCHAR(45) NOT NULL,\
  `departure_dt` DATE NOT NULL,\
  `avrrival_t_h` INT NOT NULL,\
  `avrrival_t_m` INT NOT NULL,\
  `departure_t_h` INT NOT NULL,\
  `departure_t_m` INT NOT NULL,\
  `num_person_adult` INT NOT NULL,\
  `num_person_child` INT NOT NULL,\
  `num_rooms` INT NOT NULL,\
  `price` INT NOT NULL,\
  `iran_or_world` VARCHAR(5) NOT NULL,\
  PRIMARY KEY (`id`));", # این ویرگول یادت نره. مهمه. بیرون از کوتیشن هم باید باشه.


  "CREATE TABLE IF NOT EXISTS `travel`.`bus_train` (\
  `id` INT NOT NULL AUTO_INCREMENT,\
  `cmb_origin` VARCHAR(45) NOT NULL,\
  `cmb_destination` VARCHAR(45) NOT NULL,\
  `dt_deprature` DATE NOT NULL,\
  `num_passengers` VARCHAR(45) NOT NULL,\
  `time_deprature_h` VARCHAR(45) NOT NULL,\
  `time_deprature_m` VARCHAR(45) NOT NULL,\
  `seat_number` VARCHAR(45) NOT NULL,\
  `price` INT NULL,\
  `bus_or_train` VARCHAR(5) NOT NULL,\
  PRIMARY KEY (`id`));", # این ویرگول یادت نره. مهمه. بیرون از کوتیشن هم باید باشه.
]
COLOR1 = '#292826'
COLOR2 = '#3D155F'
COLOR3 = '#DF678C'
COLOR4 = '#047760'
COLOR5 = '#FF001B'
COLOR6 = '#0004FF'
COLOR7 = '#00E0FF'
COLOR8 = '#00FF04'
COLOR9 = '#F7FF00'
COLOR10 = '#D100FF'
