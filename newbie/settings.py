from decouple import config


CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")
CLIENT_URI = config("CLIENT_URI")
CLIENT_CALLBACK_URL = config("AUTH0_CALLBACK_URL")
CLIENT_AUDIENCE = config('CLIENT_AUDIENCE')
CLIENT_GRANT_TYPE = config('CLIENT_GRANT_TYPE')
SLACK_BOT_TOKEN = config('SLACK_BOT_TOKEN')
SLACK_VERIFICATION_TOKEN = config('SLACK_VERIFICATION_TOKEN')
# SLACK_WEBHOOK_SECRET = config('SLACK_WEBHOOK_SECRET')
MONGODB_SECRET = config('MONGODB_SECRET')
AUTH0_DOMAIN = config('AUTH0_DOMAIN')
AUTH_ID = config('AUTH_ID')
AUTH_SECRET = config('AUTH_SECRET')
AUTH_HOST = config('AUTH_HOST')
AUTH_SECRET_KEY = config('AUTH_SECRET_KEY')
AUTH_AUDIENCE = config('AUTH_AUDIENCE')
AUTH_ISSUER = config('AUTH_ISSUER')
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/newbie'
SQLALCHEMY_TRACK_MODIFICATIONS = False

all_timezones = [
    {'zone': 'Africa/Abidjan', 'name': 'Africa/Abidjan'},
    {'zone': 'Africa/Accra', 'name': 'Africa/Accra'},
    {'zone': 'Africa/Addis_Ababa', 'name': 'Africa/Addis_Ababa'},
    {'zone': 'Africa/Algiers', 'name': 'Africa/Algiers'},
    {'zone': 'Africa/Asmara', 'name': 'Africa/Asmara'},
    {'zone': 'Africa/Asmera', 'name': 'Africa/Asmera'},
    {'zone': 'Africa/Bamako', 'name': 'Africa/Bamako'},
    {'zone': 'Africa/Bangui', 'name': 'Africa/Bangui'},
    {'zone': 'Africa/Banjul', 'name': 'Africa/Banjul'},
    {'zone': 'Africa/Bissau', 'name': 'Africa/Bissau'},
    {'zone': 'Africa/Blantyre', 'name': 'Africa/Blantyre'},
    {'zone': 'Africa/Brazzaville', 'name': 'Africa/Brazzaville'},
    {'zone': 'Africa/Bujumbura', 'name': 'Africa/Bujumbura'},
    {'zone': 'Africa/Cairo', 'name': 'Africa/Cairo'},
    {'zone': 'Africa/Casablanca', 'name': 'Africa/Casablanca'},
    {'zone': 'Africa/Ceuta', 'name': 'Africa/Ceuta'},
    {'zone': 'Africa/Conakry', 'name': 'Africa/Conakry'},
    {'zone': 'Africa/Dakar', 'name': 'Africa/Dakar'},
    {'zone': 'Africa/Dar_es_Salaam', 'name': 'Africa/Dar_es_Salaam'},
    {'zone': 'Africa/Djibouti', 'name': 'Africa/Djibouti'},
    {'zone': 'Africa/Douala', 'name': 'Africa/Douala'},
    {'zone': 'Africa/El_Aaiun', 'name': 'Africa/El_Aaiun'},
    {'zone': 'Africa/Freetown', 'name': 'Africa/Freetown'},
    {'zone': 'Africa/Gaborone', 'name': 'Africa/Gaborone'},
    {'zone': 'Africa/Harare', 'name': 'Africa/Harare'},
    {'zone': 'Africa/Johannesburg', 'name': 'Africa/Johannesburg'},
    {'zone': 'Africa/Juba', 'name': 'Africa/Juba'},
    {'zone': 'Africa/Kampala', 'name': 'Africa/Kampala'},
    {'zone': 'Africa/Khartoum', 'name': 'Africa/Khartoum'},
    {'zone': 'Africa/Kigali', 'name': 'Africa/Kigali'},
    {'zone': 'Africa/Kinshasa', 'name': 'Africa/Kinshasa'},
    {'zone': 'Africa/Lagos', 'name': 'Africa/Lagos'},
    {'zone': 'Africa/Libreville', 'name': 'Africa/Libreville'},
    {'zone': 'Africa/Lome', 'name': 'Africa/Lome'},
    {'zone': 'Africa/Luanda', 'name': 'Africa/Luanda'},
    {'zone': 'Africa/Lubumbashi', 'name': 'Africa/Lubumbashi'},
    {'zone': 'Africa/Lusaka', 'name': 'Africa/Lusaka'}, {'zone': 'Africa/Malabo', 'name': 'Africa/Malabo'}, {'zone': 'Africa/Maputo', 'name': 'Africa/Maputo'}, {'zone': 'Africa/Maseru', 'name': 'Africa/Maseru'}, {'zone': 'Africa/Mbabane', 'name': 'Africa/Mbabane'}, {'zone': 'Africa/Mogadishu', 'name': 'Africa/Mogadishu'}, {'zone': 'Africa/Monrovia', 'name': 'Africa/Monrovia'}, {'zone': 'Africa/Nairobi', 'name': 'Africa/Nairobi'}, {'zone': 'Africa/Ndjamena', 'name': 'Africa/Ndjamena'}, {'zone': 'Africa/Niamey', 'name': 'Africa/Niamey'}, {'zone': 'Africa/Nouakchott', 'name': 'Africa/Nouakchott'}, {'zone': 'Africa/Ouagadougou', 'name': 'Africa/Ouagadougou'}, {'zone': 'Africa/Porto-Novo', 'name': 'Africa/Porto-Novo'}, {'zone': 'Africa/Sao_Tome', 'name': 'Africa/Sao_Tome'}, {'zone': 'Africa/Timbuktu', 'name': 'Africa/Timbuktu'}, {'zone': 'Africa/Tripoli', 'name': 'Africa/Tripoli'}, {'zone': 'Africa/Tunis', 'name': 'Africa/Tunis'}, {'zone': 'Africa/Windhoek', 'name': 'Africa/Windhoek'}, {'zone': 'America/Adak', 'name': 'America/Adak'}, {'zone': 'America/Anchorage', 'name': 'America/Anchorage'}, {'zone': 'America/Anguilla', 'name': 'America/Anguilla'}, {'zone': 'America/Antigua', 'name': 'America/Antigua'}, {'zone': 'America/Araguaina', 'name': 'America/Araguaina'}, {'zone': 'America/Argentina/Buenos_Aires', 'name': 'America/Argentina/Buenos_Aires'}, {'zone': 'America/Argentina/Catamarca', 'name': 'America/Argentina/Catamarca'}, {'zone': 'America/Argentina/ComodRivadavia', 'name': 'America/Argentina/ComodRivadavia'}, {'zone': 'America/Argentina/Cordoba', 'name': 'America/Argentina/Cordoba'}, {'zone': 'America/Argentina/Jujuy', 'name': 'America/Argentina/Jujuy'}, {'zone': 'America/Argentina/La_Rioja', 'name': 'America/Argentina/La_Rioja'}, {'zone': 'America/Argentina/Mendoza', 'name': 'America/Argentina/Mendoza'}, {'zone': 'America/Argentina/Rio_Gallegos', 'name': 'America/Argentina/Rio_Gallegos'}, {'zone': 'America/Argentina/Salta', 'name': 'America/Argentina/Salta'}, {'zone': 'America/Argentina/San_Juan', 'name': 'America/Argentina/San_Juan'}, {'zone': 'America/Argentina/San_Luis', 'name': 'America/Argentina/San_Luis'}, {'zone': 'America/Argentina/Tucuman', 'name': 'America/Argentina/Tucuman'}, {'zone': 'America/Argentina/Ushuaia', 'name': 'America/Argentina/Ushuaia'}, {'zone': 'America/Aruba', 'name': 'America/Aruba'}, {'zone': 'America/Asuncion', 'name': 'America/Asuncion'}, {'zone': 'America/Atikokan', 'name': 'America/Atikokan'}, {'zone': 'America/Atka', 'name': 'America/Atka'}, {'zone': 'America/Bahia', 'name': 'America/Bahia'}, {'zone': 'America/Bahia_Banderas', 'name': 'America/Bahia_Banderas'}, {'zone': 'America/Barbados', 'name': 'America/Barbados'}, {'zone': 'America/Belem', 'name': 'America/Belem'}, {'zone': 'America/Belize', 'name': 'America/Belize'}, {'zone': 'America/Blanc-Sablon', 'name': 'America/Blanc-Sablon'}, {'zone': 'America/Boa_Vista', 'name': 'America/Boa_Vista'}, {'zone': 'America/Bogota', 'name': 'America/Bogota'}, {'zone': 'America/Boise', 'name': 'America/Boise'}, {'zone': 'America/Buenos_Aires', 'name': 'America/Buenos_Aires'}, {'zone': 'America/Cambridge_Bay', 'name': 'America/Cambridge_Bay'}, {'zone': 'America/Campo_Grande', 'name': 'America/Campo_Grande'}, {'zone': 'America/Cancun', 'name': 'America/Cancun'}, {'zone': 'America/Caracas', 'name': 'America/Caracas'}, {'zone': 'America/Catamarca', 'name': 'America/Catamarca'}, {'zone': 'America/Cayenne', 'name': 'America/Cayenne'}, {'zone': 'America/Cayman', 'name': 'America/Cayman'}, {'zone': 'America/Chicago', 'name': 'America/Chicago'}, {'zone': 'America/Chihuahua', 'name': 'America/Chihuahua'}, {'zone': 'America/Coral_Harbour', 'name': 'America/Coral_Harbour'}, {'zone': 'America/Cordoba', 'name': 'America/Cordoba'}, {'zone': 'America/Costa_Rica', 'name': 'America/Costa_Rica'}, {'zone': 'America/Creston', 'name': 'America/Creston'}, {'zone': 'America/Cuiaba', 'name': 'America/Cuiaba'}, {'zone': 'America/Curacao', 'name': 'America/Curacao'}, {'zone': 'America/Danmarkshavn', 'name': 'America/Danmarkshavn'}, {'zone': 'America/Dawson', 'name': 'America/Dawson'}, {'zone': 'America/Dawson_Creek', 'name': 'America/Dawson_Creek'}, {'zone': 'America/Denver', 'name': 'America/Denver'}, {'zone': 'America/Detroit', 'name': 'America/Detroit'}, {'zone': 'America/Dominica', 'name': 'America/Dominica'}, {'zone': 'America/Edmonton', 'name': 'America/Edmonton'}, {'zone': 'America/Eirunepe', 'name': 'America/Eirunepe'}, {'zone': 'America/El_Salvador', 'name': 'America/El_Salvador'}, {'zone': 'America/Ensenada', 'name': 'America/Ensenada'}, {'zone': 'America/Fort_Nelson', 'name': 'America/Fort_Nelson'}, {'zone': 'America/Fort_Wayne', 'name': 'America/Fort_Wayne'}, {'zone': 'America/Fortaleza', 'name': 'America/Fortaleza'}, {'zone': 'America/Glace_Bay', 'name': 'America/Glace_Bay'}, {'zone': 'America/Godthab', 'name': 'America/Godthab'}, {'zone': 'America/Goose_Bay', 'name': 'America/Goose_Bay'}, {'zone': 'America/Grand_Turk', 'name': 'America/Grand_Turk'}, {'zone': 'America/Grenada', 'name': 'America/Grenada'}, {'zone': 'America/Guadeloupe', 'name': 'America/Guadeloupe'}, {'zone': 'America/Guatemala', 'name': 'America/Guatemala'}, {'zone': 'America/Guayaquil', 'name': 'America/Guayaquil'}, {'zone': 'America/Guyana', 'name': 'America/Guyana'}, {'zone': 'America/Halifax', 'name': 'America/Halifax'}, {'zone': 'America/Havana', 'name': 'America/Havana'}, {'zone': 'America/Hermosillo', 'name': 'America/Hermosillo'}, {'zone': 'America/Indiana/Indianapolis', 'name': 'America/Indiana/Indianapolis'}, {'zone': 'America/Indiana/Knox', 'name': 'America/Indiana/Knox'}, {'zone': 'America/Indiana/Marengo', 'name': 'America/Indiana/Marengo'}, {'zone': 'America/Indiana/Petersburg', 'name': 'America/Indiana/Petersburg'}, {'zone': 'America/Indiana/Tell_City', 'name': 'America/Indiana/Tell_City'}, {'zone': 'America/Indiana/Vevay', 'name': 'America/Indiana/Vevay'}, {'zone': 'America/Indiana/Vincennes', 'name': 'America/Indiana/Vincennes'}, {'zone': 'America/Indiana/Winamac', 'name': 'America/Indiana/Winamac'}, {'zone': 'America/Indianapolis', 'name': 'America/Indianapolis'}, {'zone': 'America/Inuvik', 'name': 'America/Inuvik'}, {'zone': 'America/Iqaluit', 'name': 'America/Iqaluit'}, {'zone': 'America/Jamaica', 'name': 'America/Jamaica'}, {'zone': 'America/Jujuy', 'name': 'America/Jujuy'}, {'zone': 'America/Juneau', 'name': 'America/Juneau'}, {'zone': 'America/Kentucky/Louisville', 'name': 'America/Kentucky/Louisville'}, {'zone': 'America/Kentucky/Monticello', 'name': 'America/Kentucky/Monticello'}, {'zone': 'America/Knox_IN', 'name': 'America/Knox_IN'}, {'zone': 'America/Kralendijk', 'name': 'America/Kralendijk'}, {'zone': 'America/La_Paz', 'name': 'America/La_Paz'}, {'zone': 'America/Lima', 'name': 'America/Lima'}, {'zone': 'America/Los_Angeles', 'name': 'America/Los_Angeles'}, {'zone': 'America/Louisville', 'name': 'America/Louisville'}, {'zone': 'America/Lower_Princes', 'name': 'America/Lower_Princes'}, {'zone': 'America/Maceio', 'name': 'America/Maceio'}, {'zone': 'America/Managua', 'name': 'America/Managua'}, {'zone': 'America/Manaus', 'name': 'America/Manaus'}, {'zone': 'America/Marigot', 'name': 'America/Marigot'}, {'zone': 'America/Martinique', 'name': 'America/Martinique'}, {'zone': 'America/Matamoros', 'name': 'America/Matamoros'}, {'zone': 'America/Mazatlan', 'name': 'America/Mazatlan'}, {'zone': 'America/Mendoza', 'name': 'America/Mendoza'}, {'zone': 'America/Menominee', 'name': 'America/Menominee'}, {'zone': 'America/Merida', 'name': 'America/Merida'}, {'zone': 'America/Metlakatla', 'name': 'America/Metlakatla'}, {'zone': 'America/Mexico_City', 'name': 'America/Mexico_City'}, {'zone': 'America/Miquelon', 'name': 'America/Miquelon'}, {'zone': 'America/Moncton', 'name': 'America/Moncton'}, {'zone': 'America/Monterrey', 'name': 'America/Monterrey'}, {'zone': 'America/Montevideo', 'name': 'America/Montevideo'}, {'zone': 'America/Montreal', 'name': 'America/Montreal'}, {'zone': 'America/Montserrat', 'name': 'America/Montserrat'}, {'zone': 'America/Nassau', 'name': 'America/Nassau'}, {'zone': 'America/New_York', 'name': 'America/New_York'}, {'zone': 'America/Nipigon', 'name': 'America/Nipigon'}, {'zone': 'America/Nome', 'name': 'America/Nome'}, {'zone': 'America/Noronha', 'name': 'America/Noronha'}, {'zone': 'America/North_Dakota/Beulah', 'name': 'America/North_Dakota/Beulah'}, {'zone': 'America/North_Dakota/Center', 'name': 'America/North_Dakota/Center'}, {'zone': 'America/North_Dakota/New_Salem', 'name': 'America/North_Dakota/New_Salem'}, {'zone': 'America/Ojinaga', 'name': 'America/Ojinaga'}, {'zone': 'America/Panama', 'name': 'America/Panama'}, {'zone': 'America/Pangnirtung', 'name': 'America/Pangnirtung'}, {'zone': 'America/Paramaribo', 'name': 'America/Paramaribo'}, {'zone': 'America/Phoenix', 'name': 'America/Phoenix'}, {'zone': 'America/Port-au-Prince', 'name': 'America/Port-au-Prince'}, {'zone': 'America/Port_of_Spain', 'name': 'America/Port_of_Spain'}, {'zone': 'America/Porto_Acre', 'name': 'America/Porto_Acre'}, {'zone': 'America/Porto_Velho', 'name': 'America/Porto_Velho'}, {'zone': 'America/Puerto_Rico', 'name': 'America/Puerto_Rico'}, {'zone': 'America/Punta_Arenas', 'name': 'America/Punta_Arenas'}, {'zone': 'America/Rainy_River', 'name': 'America/Rainy_River'}, {'zone': 'America/Rankin_Inlet', 'name': 'America/Rankin_Inlet'}, {'zone': 'America/Recife', 'name': 'America/Recife'}, {'zone': 'America/Regina', 'name': 'America/Regina'}, {'zone': 'America/Resolute', 'name': 'America/Resolute'}, {'zone': 'America/Rio_Branco', 'name': 'America/Rio_Branco'}, {'zone': 'America/Rosario', 'name': 'America/Rosario'}, {'zone': 'America/Santa_Isabel', 'name': 'America/Santa_Isabel'}, {'zone': 'America/Santarem', 'name': 'America/Santarem'}, {'zone': 'America/Santiago', 'name': 'America/Santiago'}, {'zone': 'America/Santo_Domingo', 'name': 'America/Santo_Domingo'}, {'zone': 'America/Sao_Paulo', 'name': 'America/Sao_Paulo'}, {'zone': 'America/Scoresbysund', 'name': 'America/Scoresbysund'}, {'zone': 'America/Shiprock', 'name': 'America/Shiprock'}, {'zone': 'America/Sitka', 'name': 'America/Sitka'}, {'zone': 'America/St_Barthelemy', 'name': 'America/St_Barthelemy'}, {'zone': 'America/St_Johns', 'name': 'America/St_Johns'}, {'zone': 'America/St_Kitts', 'name': 'America/St_Kitts'}, {'zone': 'America/St_Lucia', 'name': 'America/St_Lucia'}, {'zone': 'America/St_Thomas', 'name': 'America/St_Thomas'}, {'zone': 'America/St_Vincent', 'name': 'America/St_Vincent'}, {'zone': 'America/Swift_Current', 'name': 'America/Swift_Current'}, {'zone': 'America/Tegucigalpa', 'name': 'America/Tegucigalpa'}, {'zone': 'America/Thule', 'name': 'America/Thule'}, {'zone': 'America/Thunder_Bay', 'name': 'America/Thunder_Bay'}, {'zone': 'America/Tijuana', 'name': 'America/Tijuana'}, {'zone': 'America/Toronto', 'name': 'America/Toronto'}, {'zone': 'America/Tortola', 'name': 'America/Tortola'}, {'zone': 'America/Vancouver', 'name': 'America/Vancouver'}, {'zone': 'America/Virgin', 'name': 'America/Virgin'}, {'zone': 'America/Whitehorse', 'name': 'America/Whitehorse'}, {'zone': 'America/Winnipeg', 'name': 'America/Winnipeg'}, {'zone': 'America/Yakutat', 'name': 'America/Yakutat'}, {'zone': 'America/Yellowknife', 'name': 'America/Yellowknife'}, {'zone': 'Antarctica/Casey', 'name': 'Antarctica/Casey'}, {'zone': 'Antarctica/Davis', 'name': 'Antarctica/Davis'}, {'zone': 'Antarctica/DumontDUrville', 'name': 'Antarctica/DumontDUrville'}, {'zone': 'Antarctica/Macquarie', 'name': 'Antarctica/Macquarie'}, {'zone': 'Antarctica/Mawson', 'name': 'Antarctica/Mawson'}, {'zone': 'Antarctica/McMurdo', 'name': 'Antarctica/McMurdo'}, {'zone': 'Antarctica/Palmer', 'name': 'Antarctica/Palmer'}, {'zone': 'Antarctica/Rothera', 'name': 'Antarctica/Rothera'}, {'zone': 'Antarctica/South_Pole', 'name': 'Antarctica/South_Pole'}, {'zone': 'Antarctica/Syowa', 'name': 'Antarctica/Syowa'}, {'zone': 'Antarctica/Troll', 'name': 'Antarctica/Troll'}, {'zone': 'Antarctica/Vostok', 'name': 'Antarctica/Vostok'}, {'zone': 'Arctic/Longyearbyen', 'name': 'Arctic/Longyearbyen'}, {'zone': 'Asia/Aden', 'name': 'Asia/Aden'}, {'zone': 'Asia/Almaty', 'name': 'Asia/Almaty'}, {'zone': 'Asia/Amman', 'name': 'Asia/Amman'}, {'zone': 'Asia/Anadyr', 'name': 'Asia/Anadyr'}, {'zone': 'Asia/Aqtau', 'name': 'Asia/Aqtau'}, {'zone': 'Asia/Aqtobe', 'name': 'Asia/Aqtobe'}, {'zone': 'Asia/Ashgabat', 'name': 'Asia/Ashgabat'}, {'zone': 'Asia/Ashkhabad', 'name': 'Asia/Ashkhabad'}, {'zone': 'Asia/Atyrau', 'name': 'Asia/Atyrau'}, {'zone': 'Asia/Baghdad', 'name': 'Asia/Baghdad'}, {'zone': 'Asia/Bahrain', 'name': 'Asia/Bahrain'}, {'zone': 'Asia/Baku', 'name': 'Asia/Baku'}, {'zone': 'Asia/Bangkok', 'name': 'Asia/Bangkok'}, {'zone': 'Asia/Barnaul', 'name': 'Asia/Barnaul'}, {'zone': 'Asia/Beirut', 'name': 'Asia/Beirut'}, {'zone': 'Asia/Bishkek', 'name': 'Asia/Bishkek'}, {'zone': 'Asia/Brunei', 'name': 'Asia/Brunei'}, {'zone': 'Asia/Calcutta', 'name': 'Asia/Calcutta'}, {'zone': 'Asia/Chita', 'name': 'Asia/Chita'}, {'zone': 'Asia/Choibalsan', 'name': 'Asia/Choibalsan'}, {'zone': 'Asia/Chongqing', 'name': 'Asia/Chongqing'}, {'zone': 'Asia/Chungking', 'name': 'Asia/Chungking'}, {'zone': 'Asia/Colombo', 'name': 'Asia/Colombo'}, {'zone': 'Asia/Dacca', 'name': 'Asia/Dacca'}, {'zone': 'Asia/Damascus', 'name': 'Asia/Damascus'}, {'zone': 'Asia/Dhaka', 'name': 'Asia/Dhaka'}, {'zone': 'Asia/Dili', 'name': 'Asia/Dili'}, {'zone': 'Asia/Dubai', 'name': 'Asia/Dubai'}, {'zone': 'Asia/Dushanbe', 'name': 'Asia/Dushanbe'}, {'zone': 'Asia/Famagusta', 'name': 'Asia/Famagusta'}, {'zone': 'Asia/Gaza', 'name': 'Asia/Gaza'}, {'zone': 'Asia/Harbin', 'name': 'Asia/Harbin'}, {'zone': 'Asia/Hebron', 'name': 'Asia/Hebron'}, {'zone': 'Asia/Ho_Chi_Minh', 'name': 'Asia/Ho_Chi_Minh'}, {'zone': 'Asia/Hong_Kong', 'name': 'Asia/Hong_Kong'}, {'zone': 'Asia/Hovd', 'name': 'Asia/Hovd'}, {'zone': 'Asia/Irkutsk', 'name': 'Asia/Irkutsk'}, {'zone': 'Asia/Istanbul', 'name': 'Asia/Istanbul'}, {'zone': 'Asia/Jakarta', 'name': 'Asia/Jakarta'}, {'zone': 'Asia/Jayapura', 'name': 'Asia/Jayapura'}, {'zone': 'Asia/Jerusalem', 'name': 'Asia/Jerusalem'}, {'zone': 'Asia/Kabul', 'name': 'Asia/Kabul'}, {'zone': 'Asia/Kamchatka', 'name': 'Asia/Kamchatka'}, {'zone': 'Asia/Karachi', 'name': 'Asia/Karachi'}, {'zone': 'Asia/Kashgar', 'name': 'Asia/Kashgar'}, {'zone': 'Asia/Kathmandu', 'name': 'Asia/Kathmandu'}, {'zone': 'Asia/Katmandu', 'name': 'Asia/Katmandu'}, {'zone': 'Asia/Khandyga', 'name': 'Asia/Khandyga'}, {'zone': 'Asia/Kolkata', 'name': 'Asia/Kolkata'}, {'zone': 'Asia/Krasnoyarsk', 'name': 'Asia/Krasnoyarsk'}, {'zone': 'Asia/Kuala_Lumpur', 'name': 'Asia/Kuala_Lumpur'}, {'zone': 'Asia/Kuching', 'name': 'Asia/Kuching'}, {'zone': 'Asia/Kuwait', 'name': 'Asia/Kuwait'}, {'zone': 'Asia/Macao', 'name': 'Asia/Macao'}, {'zone': 'Asia/Macau', 'name': 'Asia/Macau'}, {'zone': 'Asia/Magadan', 'name': 'Asia/Magadan'}, {'zone': 'Asia/Makassar', 'name': 'Asia/Makassar'}, {'zone': 'Asia/Manila', 'name': 'Asia/Manila'}, {'zone': 'Asia/Muscat', 'name': 'Asia/Muscat'}, {'zone': 'Asia/Nicosia', 'name': 'Asia/Nicosia'}, {'zone': 'Asia/Novokuznetsk', 'name': 'Asia/Novokuznetsk'}, {'zone': 'Asia/Novosibirsk', 'name': 'Asia/Novosibirsk'}, {'zone': 'Asia/Omsk', 'name': 'Asia/Omsk'}, {'zone': 'Asia/Oral', 'name': 'Asia/Oral'}, {'zone': 'Asia/Phnom_Penh', 'name': 'Asia/Phnom_Penh'}, {'zone': 'Asia/Pontianak', 'name': 'Asia/Pontianak'}, {'zone': 'Asia/Pyongyang', 'name': 'Asia/Pyongyang'}, {'zone': 'Asia/Qatar', 'name': 'Asia/Qatar'}, {'zone': 'Asia/Qyzylorda', 'name': 'Asia/Qyzylorda'}, {'zone': 'Asia/Rangoon', 'name': 'Asia/Rangoon'}, {'zone': 'Asia/Riyadh', 'name': 'Asia/Riyadh'}, {'zone': 'Asia/Saigon', 'name': 'Asia/Saigon'}, {'zone': 'Asia/Sakhalin', 'name': 'Asia/Sakhalin'}, {'zone': 'Asia/Samarkand', 'name': 'Asia/Samarkand'}, {'zone': 'Asia/Seoul', 'name': 'Asia/Seoul'}, {'zone': 'Asia/Shanghai', 'name': 'Asia/Shanghai'}, {'zone': 'Asia/Singapore', 'name': 'Asia/Singapore'}, {'zone': 'Asia/Srednekolymsk', 'name': 'Asia/Srednekolymsk'}, {'zone': 'Asia/Taipei', 'name': 'Asia/Taipei'}, {'zone': 'Asia/Tashkent', 'name': 'Asia/Tashkent'}, {'zone': 'Asia/Tbilisi', 'name': 'Asia/Tbilisi'}, {'zone': 'Asia/Tehran', 'name': 'Asia/Tehran'}, {'zone': 'Asia/Tel_Aviv', 'name': 'Asia/Tel_Aviv'}, {'zone': 'Asia/Thimbu', 'name': 'Asia/Thimbu'}, {'zone': 'Asia/Thimphu', 'name': 'Asia/Thimphu'}, {'zone': 'Asia/Tokyo', 'name': 'Asia/Tokyo'}, {'zone': 'Asia/Tomsk', 'name': 'Asia/Tomsk'}, {'zone': 'Asia/Ujung_Pandang', 'name': 'Asia/Ujung_Pandang'}, {'zone': 'Asia/Ulaanbaatar', 'name': 'Asia/Ulaanbaatar'}, {'zone': 'Asia/Ulan_Bator', 'name': 'Asia/Ulan_Bator'}, {'zone': 'Asia/Urumqi', 'name': 'Asia/Urumqi'}, {'zone': 'Asia/Ust-Nera', 'name': 'Asia/Ust-Nera'}, {'zone': 'Asia/Vientiane', 'name': 'Asia/Vientiane'}, {'zone': 'Asia/Vladivostok', 'name': 'Asia/Vladivostok'}, {'zone': 'Asia/Yakutsk', 'name': 'Asia/Yakutsk'}, {'zone': 'Asia/Yangon', 'name': 'Asia/Yangon'}, {'zone': 'Asia/Yekaterinburg', 'name': 'Asia/Yekaterinburg'}, {'zone': 'Asia/Yerevan', 'name': 'Asia/Yerevan'}, {'zone': 'Atlantic/Azores', 'name': 'Atlantic/Azores'}, {'zone': 'Atlantic/Bermuda', 'name': 'Atlantic/Bermuda'}, {'zone': 'Atlantic/Canary', 'name': 'Atlantic/Canary'}, {'zone': 'Atlantic/Cape_Verde', 'name': 'Atlantic/Cape_Verde'}, {'zone': 'Atlantic/Faeroe', 'name': 'Atlantic/Faeroe'}, {'zone': 'Atlantic/Faroe', 'name': 'Atlantic/Faroe'}, {'zone': 'Atlantic/Jan_Mayen', 'name': 'Atlantic/Jan_Mayen'}, {'zone': 'Atlantic/Madeira', 'name': 'Atlantic/Madeira'}, {'zone': 'Atlantic/Reykjavik', 'name': 'Atlantic/Reykjavik'}, {'zone': 'Atlantic/South_Georgia', 'name': 'Atlantic/South_Georgia'}, {'zone': 'Atlantic/St_Helena', 'name': 'Atlantic/St_Helena'}, {'zone': 'Atlantic/Stanley', 'name': 'Atlantic/Stanley'}, {'zone': 'Australia/ACT', 'name': 'Australia/ACT'}, {'zone': 'Australia/Adelaide', 'name': 'Australia/Adelaide'}, {'zone': 'Australia/Brisbane', 'name': 'Australia/Brisbane'}, {'zone': 'Australia/Broken_Hill', 'name': 'Australia/Broken_Hill'}, {'zone': 'Australia/Canberra', 'name': 'Australia/Canberra'}, {'zone': 'Australia/Currie', 'name': 'Australia/Currie'}, {'zone': 'Australia/Darwin', 'name': 'Australia/Darwin'}, {'zone': 'Australia/Eucla', 'name': 'Australia/Eucla'}, {'zone': 'Australia/Hobart', 'name': 'Australia/Hobart'}, {'zone': 'Australia/LHI', 'name': 'Australia/LHI'}, {'zone': 'Australia/Lindeman', 'name': 'Australia/Lindeman'}, {'zone': 'Australia/Lord_Howe', 'name': 'Australia/Lord_Howe'}, {'zone': 'Australia/Melbourne', 'name': 'Australia/Melbourne'}, {'zone': 'Australia/NSW', 'name': 'Australia/NSW'}, {'zone': 'Australia/North', 'name': 'Australia/North'}, {'zone': 'Australia/Perth', 'name': 'Australia/Perth'}, {'zone': 'Australia/Queensland', 'name': 'Australia/Queensland'}, {'zone': 'Australia/South', 'name': 'Australia/South'}, {'zone': 'Australia/Sydney', 'name': 'Australia/Sydney'}, {'zone': 'Australia/Tasmania', 'name': 'Australia/Tasmania'}, {'zone': 'Australia/Victoria', 'name': 'Australia/Victoria'}, {'zone': 'Australia/West', 'name': 'Australia/West'}, {'zone': 'Australia/Yancowinna', 'name': 'Australia/Yancowinna'}, {'zone': 'Brazil/Acre', 'name': 'Brazil/Acre'}, {'zone': 'Brazil/DeNoronha', 'name': 'Brazil/DeNoronha'}, {'zone': 'Brazil/East', 'name': 'Brazil/East'}, {'zone': 'Brazil/West', 'name': 'Brazil/West'}, {'zone': 'CET', 'name': 'CET'}, {'zone': 'CST6CDT', 'name': 'CST6CDT'}, {'zone': 'Canada/Atlantic', 'name': 'Canada/Atlantic'}, {'zone': 'Canada/Central', 'name': 'Canada/Central'}, {'zone': 'Canada/Eastern', 'name': 'Canada/Eastern'}, {'zone': 'Canada/Mountain', 'name': 'Canada/Mountain'}, {'zone': 'Canada/Newfoundland', 'name': 'Canada/Newfoundland'}, {'zone': 'Canada/Pacific', 'name': 'Canada/Pacific'}, {'zone': 'Canada/Saskatchewan', 'name': 'Canada/Saskatchewan'}, {'zone': 'Canada/Yukon', 'name': 'Canada/Yukon'}, {'zone': 'Chile/Continental', 'name': 'Chile/Continental'}, {'zone': 'Chile/EasterIsland', 'name': 'Chile/EasterIsland'}, {'zone': 'Cuba', 'name': 'Cuba'}, {'zone': 'EET', 'name': 'EET'}, {'zone': 'EST', 'name': 'EST'}, {'zone': 'EST5EDT', 'name': 'EST5EDT'}, {'zone': 'Egypt', 'name': 'Egypt'}, {'zone': 'Eire', 'name': 'Eire'}, {'zone': 'Etc/GMT', 'name': 'Etc/GMT'}, {'zone': 'Etc/GMT+0', 'name': 'Etc/GMT+0'}, {'zone': 'Etc/GMT+1', 'name': 'Etc/GMT+1'}, {'zone': 'Etc/GMT+10', 'name': 'Etc/GMT+10'}, {'zone': 'Etc/GMT+11', 'name': 'Etc/GMT+11'}, {'zone': 'Etc/GMT+12', 'name': 'Etc/GMT+12'}, {'zone': 'Etc/GMT+2', 'name': 'Etc/GMT+2'}, {'zone': 'Etc/GMT+3', 'name': 'Etc/GMT+3'}, {'zone': 'Etc/GMT+4', 'name': 'Etc/GMT+4'}, {'zone': 'Etc/GMT+5', 'name': 'Etc/GMT+5'}, {'zone': 'Etc/GMT+6', 'name': 'Etc/GMT+6'}, {'zone': 'Etc/GMT+7', 'name': 'Etc/GMT+7'}, {'zone': 'Etc/GMT+8', 'name': 'Etc/GMT+8'}, {'zone': 'Etc/GMT+9', 'name': 'Etc/GMT+9'}, {'zone': 'Etc/GMT-0', 'name': 'Etc/GMT-0'}, {'zone': 'Etc/GMT-1', 'name': 'Etc/GMT-1'}, {'zone': 'Etc/GMT-10', 'name': 'Etc/GMT-10'}, {'zone': 'Etc/GMT-11', 'name': 'Etc/GMT-11'}, {'zone': 'Etc/GMT-12', 'name': 'Etc/GMT-12'}, {'zone': 'Etc/GMT-13', 'name': 'Etc/GMT-13'}, {'zone': 'Etc/GMT-14', 'name': 'Etc/GMT-14'}, {'zone': 'Etc/GMT-2', 'name': 'Etc/GMT-2'}, {'zone': 'Etc/GMT-3', 'name': 'Etc/GMT-3'}, {'zone': 'Etc/GMT-4', 'name': 'Etc/GMT-4'}, {'zone': 'Etc/GMT-5', 'name': 'Etc/GMT-5'}, {'zone': 'Etc/GMT-6', 'name': 'Etc/GMT-6'}, {'zone': 'Etc/GMT-7', 'name': 'Etc/GMT-7'}, {'zone': 'Etc/GMT-8', 'name': 'Etc/GMT-8'}, {'zone': 'Etc/GMT-9', 'name': 'Etc/GMT-9'}, {'zone': 'Etc/GMT0', 'name': 'Etc/GMT0'}, {'zone': 'Etc/Greenwich', 'name': 'Etc/Greenwich'}, {'zone': 'Etc/UCT', 'name': 'Etc/UCT'}, {'zone': 'Etc/UTC', 'name': 'Etc/UTC'}, {'zone': 'Etc/Universal', 'name': 'Etc/Universal'}, {'zone': 'Etc/Zulu', 'name': 'Etc/Zulu'}, {'zone': 'Europe/Amsterdam', 'name': 'Europe/Amsterdam'}, {'zone': 'Europe/Andorra', 'name': 'Europe/Andorra'}, {'zone': 'Europe/Astrakhan', 'name': 'Europe/Astrakhan'}, {'zone': 'Europe/Athens', 'name': 'Europe/Athens'}, {'zone': 'Europe/Belfast', 'name': 'Europe/Belfast'}, {'zone': 'Europe/Belgrade', 'name': 'Europe/Belgrade'}, {'zone': 'Europe/Berlin', 'name': 'Europe/Berlin'}, {'zone': 'Europe/Bratislava', 'name': 'Europe/Bratislava'}, {'zone': 'Europe/Brussels', 'name': 'Europe/Brussels'}, {'zone': 'Europe/Bucharest', 'name': 'Europe/Bucharest'}, {'zone': 'Europe/Budapest', 'name': 'Europe/Budapest'}, {'zone': 'Europe/Busingen', 'name': 'Europe/Busingen'}, {'zone': 'Europe/Chisinau', 'name': 'Europe/Chisinau'}, {'zone': 'Europe/Copenhagen', 'name': 'Europe/Copenhagen'}, {'zone': 'Europe/Dublin', 'name': 'Europe/Dublin'}, {'zone': 'Europe/Gibraltar', 'name': 'Europe/Gibraltar'}, {'zone': 'Europe/Guernsey', 'name': 'Europe/Guernsey'}, {'zone': 'Europe/Helsinki', 'name': 'Europe/Helsinki'}, {'zone': 'Europe/Isle_of_Man', 'name': 'Europe/Isle_of_Man'}, {'zone': 'Europe/Istanbul', 'name': 'Europe/Istanbul'}, {'zone': 'Europe/Jersey', 'name': 'Europe/Jersey'}, {'zone': 'Europe/Kaliningrad', 'name': 'Europe/Kaliningrad'}, {'zone': 'Europe/Kiev', 'name': 'Europe/Kiev'}, {'zone': 'Europe/Kirov', 'name': 'Europe/Kirov'}, {'zone': 'Europe/Lisbon', 'name': 'Europe/Lisbon'}, {'zone': 'Europe/Ljubljana', 'name': 'Europe/Ljubljana'}, {'zone': 'Europe/London', 'name': 'Europe/London'}, {'zone': 'Europe/Luxembourg', 'name': 'Europe/Luxembourg'}, {'zone': 'Europe/Madrid', 'name': 'Europe/Madrid'}, {'zone': 'Europe/Malta', 'name': 'Europe/Malta'}, {'zone': 'Europe/Mariehamn', 'name': 'Europe/Mariehamn'}, {'zone': 'Europe/Minsk', 'name': 'Europe/Minsk'}, {'zone': 'Europe/Monaco', 'name': 'Europe/Monaco'}, {'zone': 'Europe/Moscow', 'name': 'Europe/Moscow'}, {'zone': 'Europe/Nicosia', 'name': 'Europe/Nicosia'}, {'zone': 'Europe/Oslo', 'name': 'Europe/Oslo'}, {'zone': 'Europe/Paris', 'name': 'Europe/Paris'}, {'zone': 'Europe/Podgorica', 'name': 'Europe/Podgorica'}, {'zone': 'Europe/Prague', 'name': 'Europe/Prague'}, {'zone': 'Europe/Riga', 'name': 'Europe/Riga'}, {'zone': 'Europe/Rome', 'name': 'Europe/Rome'}, {'zone': 'Europe/Samara', 'name': 'Europe/Samara'}, {'zone': 'Europe/San_Marino', 'name': 'Europe/San_Marino'}, {'zone': 'Europe/Sarajevo', 'name': 'Europe/Sarajevo'}, {'zone': 'Europe/Saratov', 'name': 'Europe/Saratov'}, {'zone': 'Europe/Simferopol', 'name': 'Europe/Simferopol'}, {'zone': 'Europe/Skopje', 'name': 'Europe/Skopje'}, {'zone': 'Europe/Sofia', 'name': 'Europe/Sofia'}, {'zone': 'Europe/Stockholm', 'name': 'Europe/Stockholm'}, {'zone': 'Europe/Tallinn', 'name': 'Europe/Tallinn'}, {'zone': 'Europe/Tirane', 'name': 'Europe/Tirane'}, {'zone': 'Europe/Tiraspol', 'name': 'Europe/Tiraspol'}, {'zone': 'Europe/Ulyanovsk', 'name': 'Europe/Ulyanovsk'}, {'zone': 'Europe/Uzhgorod', 'name': 'Europe/Uzhgorod'}, {'zone': 'Europe/Vaduz', 'name': 'Europe/Vaduz'}, {'zone': 'Europe/Vatican', 'name': 'Europe/Vatican'}, {'zone': 'Europe/Vienna', 'name': 'Europe/Vienna'}, {'zone': 'Europe/Vilnius', 'name': 'Europe/Vilnius'}, {'zone': 'Europe/Volgograd', 'name': 'Europe/Volgograd'}, {'zone': 'Europe/Warsaw', 'name': 'Europe/Warsaw'}, {'zone': 'Europe/Zagreb', 'name': 'Europe/Zagreb'}, {'zone': 'Europe/Zaporozhye', 'name': 'Europe/Zaporozhye'}, {'zone': 'Europe/Zurich', 'name': 'Europe/Zurich'}, {'zone': 'GB', 'name': 'GB'}, {'zone': 'GB-Eire', 'name': 'GB-Eire'}, {'zone': 'GMT', 'name': 'GMT'}, {'zone': 'GMT+0', 'name': 'GMT+0'}, {'zone': 'GMT-0', 'name': 'GMT-0'}, {'zone': 'GMT0', 'name': 'GMT0'}, {'zone': 'Greenwich', 'name': 'Greenwich'}, {'zone': 'HST', 'name': 'HST'}, {'zone': 'Hongkong', 'name': 'Hongkong'}, {'zone': 'Iceland', 'name': 'Iceland'}, {'zone': 'Indian/Antananarivo', 'name': 'Indian/Antananarivo'}, {'zone': 'Indian/Chagos', 'name': 'Indian/Chagos'}, {'zone': 'Indian/Christmas', 'name': 'Indian/Christmas'}, {'zone': 'Indian/Cocos', 'name': 'Indian/Cocos'}, {'zone': 'Indian/Comoro', 'name': 'Indian/Comoro'}, {'zone': 'Indian/Kerguelen', 'name': 'Indian/Kerguelen'}, {'zone': 'Indian/Mahe', 'name': 'Indian/Mahe'}, {'zone': 'Indian/Maldives', 'name': 'Indian/Maldives'}, {'zone': 'Indian/Mauritius', 'name': 'Indian/Mauritius'}, {'zone': 'Indian/Mayotte', 'name': 'Indian/Mayotte'}, {'zone': 'Indian/Reunion', 'name': 'Indian/Reunion'}, {'zone': 'Iran', 'name': 'Iran'}, {'zone': 'Israel', 'name': 'Israel'}, {'zone': 'Jamaica', 'name': 'Jamaica'}, {'zone': 'Japan', 'name': 'Japan'}, {'zone': 'Kwajalein', 'name': 'Kwajalein'}, {'zone': 'Libya', 'name': 'Libya'}, {'zone': 'MET', 'name': 'MET'}, {'zone': 'MST', 'name': 'MST'}, {'zone': 'MST7MDT', 'name': 'MST7MDT'}, {'zone': 'Mexico/BajaNorte', 'name': 'Mexico/BajaNorte'}, {'zone': 'Mexico/BajaSur', 'name': 'Mexico/BajaSur'}, {'zone': 'Mexico/General', 'name': 'Mexico/General'}, {'zone': 'NZ', 'name': 'NZ'}, {'zone': 'NZ-CHAT', 'name': 'NZ-CHAT'}, {'zone': 'Navajo', 'name': 'Navajo'}, {'zone': 'PRC', 'name': 'PRC'}, {'zone': 'PST8PDT', 'name': 'PST8PDT'}, {'zone': 'Pacific/Apia', 'name': 'Pacific/Apia'}, {'zone': 'Pacific/Auckland', 'name': 'Pacific/Auckland'}, {'zone': 'Pacific/Bougainville', 'name': 'Pacific/Bougainville'}, {'zone': 'Pacific/Chatham', 'name': 'Pacific/Chatham'}, {'zone': 'Pacific/Chuuk', 'name': 'Pacific/Chuuk'}, {'zone': 'Pacific/Easter', 'name': 'Pacific/Easter'}, {'zone': 'Pacific/Efate', 'name': 'Pacific/Efate'}, {'zone': 'Pacific/Enderbury', 'name': 'Pacific/Enderbury'}, {'zone': 'Pacific/Fakaofo', 'name': 'Pacific/Fakaofo'}, {'zone': 'Pacific/Fiji', 'name': 'Pacific/Fiji'}, {'zone': 'Pacific/Funafuti', 'name': 'Pacific/Funafuti'}, {'zone': 'Pacific/Galapagos', 'name': 'Pacific/Galapagos'}, {'zone': 'Pacific/Gambier', 'name': 'Pacific/Gambier'}, {'zone': 'Pacific/Guadalcanal', 'name': 'Pacific/Guadalcanal'}, {'zone': 'Pacific/Guam', 'name': 'Pacific/Guam'}, {'zone': 'Pacific/Honolulu', 'name': 'Pacific/Honolulu'}, {'zone': 'Pacific/Johnston', 'name': 'Pacific/Johnston'}, {'zone': 'Pacific/Kiritimati', 'name': 'Pacific/Kiritimati'}, {'zone': 'Pacific/Kosrae', 'name': 'Pacific/Kosrae'}, {'zone': 'Pacific/Kwajalein', 'name': 'Pacific/Kwajalein'}, {'zone': 'Pacific/Majuro', 'name': 'Pacific/Majuro'}, {'zone': 'Pacific/Marquesas', 'name': 'Pacific/Marquesas'}, {'zone': 'Pacific/Midway', 'name': 'Pacific/Midway'}, {'zone': 'Pacific/Nauru', 'name': 'Pacific/Nauru'}, {'zone': 'Pacific/Niue', 'name': 'Pacific/Niue'}, {'zone': 'Pacific/Norfolk', 'name': 'Pacific/Norfolk'}, {'zone': 'Pacific/Noumea', 'name': 'Pacific/Noumea'}, {'zone': 'Pacific/Pago_Pago', 'name': 'Pacific/Pago_Pago'}, {'zone': 'Pacific/Palau', 'name': 'Pacific/Palau'}, {'zone': 'Pacific/Pitcairn', 'name': 'Pacific/Pitcairn'}, {'zone': 'Pacific/Pohnpei', 'name': 'Pacific/Pohnpei'}, {'zone': 'Pacific/Ponape', 'name': 'Pacific/Ponape'}, {'zone': 'Pacific/Port_Moresby', 'name': 'Pacific/Port_Moresby'}, {'zone': 'Pacific/Rarotonga', 'name': 'Pacific/Rarotonga'}, {'zone': 'Pacific/Saipan', 'name': 'Pacific/Saipan'}, {'zone': 'Pacific/Samoa', 'name': 'Pacific/Samoa'}, {'zone': 'Pacific/Tahiti', 'name': 'Pacific/Tahiti'}, {'zone': 'Pacific/Tarawa', 'name': 'Pacific/Tarawa'}, {'zone': 'Pacific/Tongatapu', 'name': 'Pacific/Tongatapu'}, {'zone': 'Pacific/Truk', 'name': 'Pacific/Truk'}, {'zone': 'Pacific/Wake', 'name': 'Pacific/Wake'}, {'zone': 'Pacific/Wallis', 'name': 'Pacific/Wallis'}, {'zone': 'Pacific/Yap', 'name': 'Pacific/Yap'}, {'zone': 'Poland', 'name': 'Poland'}, {'zone': 'Portugal', 'name': 'Portugal'}, {'zone': 'ROC', 'name': 'ROC'}, {'zone': 'ROK', 'name': 'ROK'}, {'zone': 'Singapore', 'name': 'Singapore'}, {'zone': 'Turkey', 'name': 'Turkey'}, {'zone': 'UCT', 'name': 'UCT'}, {'zone': 'US/Alaska', 'name': 'US/Alaska'}, {'zone': 'US/Aleutian', 'name': 'US/Aleutian'}, {'zone': 'US/Arizona', 'name': 'US/Arizona'}, {'zone': 'US/Central', 'name': 'US/Central'}, {'zone': 'US/East-Indiana', 'name': 'US/East-Indiana'}, {'zone': 'US/Eastern', 'name': 'US/Eastern'}, {'zone': 'US/Hawaii', 'name': 'US/Hawaii'}, {'zone': 'US/Indiana-Starke', 'name': 'US/Indiana-Starke'}, {'zone': 'US/Michigan', 'name': 'US/Michigan'}, {'zone': 'US/Mountain', 'name': 'US/Mountain'}, {'zone': 'US/Pacific', 'name': 'US/Pacific'}, {'zone': 'US/Samoa', 'name': 'US/Samoa'}, {'zone': 'UTC', 'name': 'UTC'}, {'zone': 'Universal', 'name': 'Universal'}, {'zone': 'W-SU', 'name': 'W-SU'}, {'zone': 'WET', 'name': 'WET'},
    {'zone': 'Zulu', 'name': 'Zulu'}]
