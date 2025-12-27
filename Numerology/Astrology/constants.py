METALS_DICT = {
    "gold": {"value": 96},
    "silver": {"value": 81},
}

DAYS_DICT = {
    "sunday": {"value": 40},
    "monday": {"value": 50},
    "tuesday": {"value": 57},
    "wednesday": {"value": 72},
    "thursday": {"value": 65},
    "friday": {"value": 24},
    "saturday": {"value": 14},
}

RAASHI_LIST = [
    "mesh", "vrishabh", "mithun", "karka", "simha", "kanya",
    "tula", "vrishchik", "dhanu", "makara", "kumbha", "meena"
]

RAASHI_DICT_1 = {
    "aries": {"value": 37},        # Mesh
    "taurus": {"value": 84},       # Vrishabh
    "gemini": {"value": 66},       # Mithun
    "cancer": {"value": 109},       # Karka
    "leo": {"value": 125},          # Simha
    "virgo": {"value": 102},        # Kanya
    "libra": {"value": 140},        # Tula
    "scorpio": {"value": 144},      # Vrishchik
    "sagittarius": {"value": 144},  # Dhanu
    "capricorn": {"value": 198},    # Makara
    "aquarius": {"value": 190},     # Kumbha
    "pisces": {"value": 180},       # Meena
}

RAASHI_DICT_2 = {
    "mesh": {"value": 37},        # Aries
    "vrishabh": {"value": 84},    # Taurus
    "mithun": {"value": 66},      # Gemini
    "karka": {"value": 109},       # Cancer
    "simha": {"value": 125},       # Leo
    "kanya": {"value": 102},       # Virgo
    "tula": {"value": 140},        # Libra
    "vrishchik": {"value": 144},   # Scorpio
    "dhanu": {"value": 144},       # Sagittarius
    "makara": {"value": 198},      # Capricorn
    "kumbha": {"value": 190},      # Aquarius
    "meena": {"value": 180},       # Pisces
}


# 27 nakshatras: indices 0..26
NAKSHATRA_NAMES = [
    "ashwini", "bharani", "krittika", "rohini", "mrigashira", "ardra", 
    "punarvasu", "pushya", "ashlesha", "magha", "purva_phalguni", 
    "uttara_phalguni", "hasta", "chitra", "swati", "vishakha", "anuradha", 
    "jyeshtha", "mula", "purva_ashadha", "uttara_ashadha", "shravana", 
    "dhanishtha", "shatabhisha", "purva_bhadrapada", "uttara_bhadrapada", "revati"
]

NAKSHATRA_DICT = {
    "ashwini": {"value": 10},
    "bharani": {"value": 10},
    "krittika": {"value": 96},
    "rohini": {"value": 56},
    "mrigashira": {"value": 20},
    "ardra": {"value": 86},
    "punarvasu": {"value": 21},
    "pushya": {"value": 64},
    "ashlesha": {"value": 135},
    "magha": {"value": 150},
    "purva_phalguni": {"value": 220},
    "uttara_phalguni": {"value": 72},
    "hasta": {"value": 334},
    "chitra": {"value": 21},
    "swati": {"value": 210},
    "vishakha": {"value": 320},
    "anuradha": {"value": 493},
    "jyeshtha": {"value": 559},
    "mula": {"value": 552},
    "purva_ashadha": {"value": 142},
    "uttara_ashadha": {"value": 420},
    "shravana": {"value": 550},
    "dhanishtha": {"value": 736},
    "shatabhisha": {"value": 576},
    "purva_bhadrapada": {"value": 275},
    "uttara_bhadrapada": {"value": 126},
    "revati": {"value": 256},
}

TITHI_NAMES = [
    "pratipada", "dvitiya", "tritiya", "chaturthi", "panchami", 
    "shashthi", "saptami", "ashtami", "navami", "dashami", 
    "ekadashi", "dwadashi", "trayodashi", "chaturdashi", 
    "purnima",
    "pratipada", "dvitiya", "tritiya", "chaturthi", "panchami", 
    "shashthi", "saptami", "ashtami", "navami", "dashami", 
    "ekadashi", "dwadashi", "trayodashi", "chaturdashi",
    "amavasya"
]
TITHI_DICT = {
    # Shukla Paksha (Waxing Moon)
    "pratipada_shukla": {"value": 18},
    "dvitiya_shukla": {"value": 20},
    "tritiya_shukla": {"value": 22},
    "chaturthi_shukla": {"value": 24},
    "panchami_shukla": {"value": 26},
    "shashthi_shukla": {"value": 25},
    "saptami_shukla": {"value": 23},
    "ashtami_shukla": {"value": 21},
    "navami_shukla": {"value": 19},
    "dashami_shukla": {"value": 17},
    "ekadashi_shukla": {"value": 15},
    "dwadashi_shukla": {"value": 13},
    "trayodashi_shukla": {"value": 11},
    "chaturdashi_shukla": {"value": 6},
    "purnima": {"value": 16},

    # Krishna Paksha (Waning Moon)
    "pratipada_krishna": {"value": 18},
    "dvitiya_krishna": {"value": 20},
    "tritiya_krishna": {"value": 22},
    "chaturthi_krishna": {"value": 24},
    "panchami_krishna": {"value": 26},
    "shashthi_krishna": {"value": 25},
    "saptami_krishna": {"value": 23},
    "ashtami_krishna": {"value": 21},
    "navami_krishna": {"value": 19},
    "dashami_krishna": {"value": 17},
    "ekadashi_krishna": {"value": 15},
    "dwadashi_krishna": {"value": 13},
    "trayodashi_krishna": {"value": 11},
    "chaturdashi_krishna": {"value": 6},
    "amavasya": {"value": 7},
}

LOCATION_DATA = {
    "DELHI":  {"lat": 28.6139, "lon": 77.2090, "tz_offset": 5.5}, 
    "MUMBAI": {"lat": 19.0760, "lon": 72.8777, "tz_offset": 5.5},
    "UJJAIN": {"lat": 23.15, "lon": 75.77, "tz_offset": 5.5},
}