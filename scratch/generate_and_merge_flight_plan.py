import json

# 58 new Flight Planning questions
new_questions = [
    {
        "questionText": "According to ICAO/EASA regulations, the 'Final Reserve Fuel' for a jet aircraft during an IFR flight is based on:",
        "options": [
            "30 minutes of holding at 1,500 ft above destination or alternate.",
            "45 minutes of holding at 1,500 ft above destination.",
            "15 minutes of cruise fuel.",
            "2 hours of holding at any altitude."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In an ICAO Flight Plan (FPL), item 15 'Route' should begin with:",
        "options": [
            "the first waypoint on the airway.",
            "the SID or the first point of the route.",
            "the cruise speed and level.",
            "the destination airport code."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the primary purpose of a 'Point of Equal Time' (PET)?",
        "options": [
            "To calculate the maximum range of the aircraft.",
            "To determine the point where it takes the same time to continue to destination or return to departure.",
            "To find the point of lowest fuel consumption.",
            "To synchronize the aircraft's clocks."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "If the TAS is 450 kts and there is a 50 kts headwind, the groundspeed (GS) is:",
        "options": [
            "500 kts.",
            "400 kts.",
            "450 kts.",
            "425 kts."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The term 'Point of Safe Return' (PSR) defines:",
        "options": [
            "the point beyond which the aircraft cannot return to the departure airfield with the required fuel reserves.",
            "the point where the engines must be checked.",
            "the point where the pilot must decide on the alternate.",
            "the halfway point of the flight."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "ICAO Flight Plan Item 10 'Equipment' - the letter 'S' stands for:",
        "options": [
            "Standard (VHF RTF, VOR, and ILS).",
            "Secondary Surveillance Radar.",
            "Satellite Navigation.",
            "Short-range capability."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Which type of fuel is used for holding, approach, and landing at the destination?",
        "options": [
            "Trip fuel.",
            "Contingency fuel.",
            "Final reserve fuel.",
            "Alternate fuel."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "If a flight is planned at FL350, the altimeter should be set to:",
        "options": [
            "Local QNH.",
            "Local QFE.",
            "Standard pressure (1013.25 hPa / 29.92 inHg).",
            "The destination airport pressure."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'step climb' is typically used in long-haul flight planning to:",
        "options": [
            "avoid other aircraft.",
            "improve fuel efficiency as the aircraft weight decreases.",
            "follow the curvature of the earth.",
            "cool the engines."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In an ICAO FPL, Item 18 'Other Information' - the prefix 'PBN/' is used to indicate:",
        "options": [
            "Passenger boarding numbers.",
            "Performance Based Navigation capabilities.",
            "Primary beacon nodes.",
            "Pilot's basic notes."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Contingency fuel is typically calculated as:",
        "options": [
            "5% of the trip fuel or a minimum amount (e.g., 5 mins of holding).",
            "a fixed 2,000 kg for all flights.",
            "the fuel needed to fly to the alternate.",
            "the fuel needed for taxiing."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the 'Decision Point' in Reduced Contingency Fuel (RCF) procedure?",
        "options": [
            "The point where the pilot chooses the meal.",
            "A point on the route where the flight can continue to destination or divert to an en-route alternate.",
            "The point of rotation during takeoff.",
            "The point where the landing gear is extended."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "If GS = 240 kts, how long does it take to fly 80 NM?",
        "options": [
            "20 minutes.",
            "30 minutes.",
            "15 minutes.",
            "25 minutes."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Mach Number' is the ratio of:",
        "options": [
            "TAS to the local speed of sound.",
            "IAS to Groundspeed.",
            "TAS to 100.",
            "Engine RPM to 1000."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In flight planning, 'Still Air' means:",
        "options": [
            "the aircraft is not moving.",
            "the wind component is zero.",
            "the engines are off.",
            "there is no turbulence."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Minimum Sector Altitude' (MSA) provides how much clearance over all obstacles in a sector?",
        "options": [
            "500 ft.",
            "1,000 ft.",
            "2,000 ft.",
            "100 ft."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the standard ICAO symbol for a 'compulsory reporting point'?",
        "options": [
            "An open triangle.",
            "A solid (filled) triangle.",
            "A circle.",
            "A square."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The flight time from PET to Destination is calculated using:",
        "options": [
            "TAS.",
            "Groundspeed Out.",
            "Groundspeed Home.",
            "Groundspeed On (Continuing)."
        ],
        "correctAnswerIndex": 3,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In Item 19 of the FPL, 'R/' indicates:",
        "options": [
            "Registration of the aircraft.",
            "Radio frequencies available.",
            "Rescue equipment available.",
            "Route alternatives."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is 'Fuel Bias' or 'Fuel Degradation Factor'?",
        "options": [
            "The price of fuel.",
            "A multiplier applied to performance data to account for an aging/less efficient aircraft.",
            "The weight of the fuel.",
            "The rate of fuel flow."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Transition Altitude' (TA) is the altitude:",
        "options": [
            "above which the aircraft is always in a climb.",
            "at or below which the vertical position of an aircraft is controlled by reference to altitudes (QNH).",
            "where the landing gear must be retracted.",
            "where the pilot changes frequency."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "If the QNH is 1000 hPa and the aircraft is at 3,000 ft, what is its Pressure Altitude? (Standard = 1013 hPa, 1 hPa = 27 ft)",
        "options": [
            "3,351 ft.",
            "2,649 ft.",
            "3,000 ft.",
            "3,130 ft."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In an ICAO FPL, Item 15 'Level' - 'F330' means:",
        "options": [
            "33,000 meters.",
            "Flight Level 330.",
            "Altitude 3,300 ft.",
            "Speed 330 kts."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What does 'EET' stand for in a flight plan?",
        "options": [
            "Estimated Entry Time.",
            "Estimated Elapsed Time.",
            "Extra Engine Thrust.",
            "Emergency Exit Toggle."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Take-off Alternate' is required if:",
        "options": [
            "it's raining at the departure airport.",
            "weather conditions at the departure airport are below the landing minima.",
            "the destination is too far away.",
            "the aircraft is very heavy."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Fuel density is important for flight planning because:",
        "options": [
            "it changes the color of the fuel.",
            "jet fuel is measured by volume but its energy and mass (weight) vary with temperature.",
            "it affects the engine RPM.",
            "it makes the fuel pump work harder."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is 'Tankering'?",
        "options": [
            "Cleaning the fuel tanks.",
            "Carrying more fuel than required for the flight because it is cheaper at the departure airport.",
            "Refueling while the engines are running.",
            "Emptying the tanks before a long stay."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a TAF, 'BECMG 1214' means the weather will change:",
        "options": [
            "at exactly 1214 UTC.",
            "gradually between 1200 and 1400 UTC.",
            "at 12:14 AM.",
            "suddenly at 12:00 UTC."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The symbol 'CAVOK' implies:",
        "options": [
            "Clouds and Visibility OK.",
            "Clear Air and Velocity OK.",
            "Cabin Air Ventilation OK.",
            "Cool Air and Vapor OK."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Under EASA rules, the 'Final Reserve' for a piston-engine aircraft is:",
        "options": [
            "30 minutes.",
            "45 minutes.",
            "15 minutes.",
            "60 minutes."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Lowest Usable Flight Level' is determined by:",
        "options": [
            "the pilot's preference.",
            "the local QNH and the transition altitude.",
            "the engine power.",
            "the distance to destination."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Great Circle' route is:",
        "options": [
            "the longest possible route.",
            "the shortest distance between two points on a sphere.",
            "a route that follows a constant heading (Rhumb line).",
            "a route that stays inside one country."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In Item 10 of an ICAO FPL, the letter 'Y' indicates:",
        "options": [
            "Yellow color aircraft.",
            "8.33 kHz spacing radio equipment.",
            "Yaw damper installed.",
            "Year of manufacture."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the code for 'Emergency' on a transponder?",
        "options": [
            "7500.",
            "7600.",
            "7700.",
            "1200."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the code for 'Unlawful Interference' (Hijack) on a transponder?",
        "options": [
            "7500.",
            "7600.",
            "7700.",
            "7000."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "If Fuel Flow = 2,400 kg/h, how much fuel is burned in 15 minutes?",
        "options": [
            "600 kg.",
            "400 kg.",
            "1,200 kg.",
            "800 kg."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Specific Air Range' (SAR) is defined as:",
        "options": [
            "TAS / Fuel Flow.",
            "Groundspeed / Fuel Flow.",
            "Weight / Fuel Flow.",
            "Altitude / Fuel Flow."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Specific Ground Range' (SGR) is defined as:",
        "options": [
            "TAS / Fuel Flow.",
            "Groundspeed / Fuel Flow.",
            "Weight / Fuel Flow.",
            "Distance / Fuel Flow."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is 'VNAV'?",
        "options": [
            "Very Nice Aviation Video.",
            "Vertical Navigation (automation for climbs, descents, and levels).",
            "Variable Navigation.",
            "Visual Navigation."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Cost Index' (CI) of zero in a Flight Management System (FMS) results in:",
        "options": [
            "maximum speed.",
            "maximum range speed (minimum fuel burn).",
            "minimum time flight.",
            "the aircraft not moving."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Estimated Off Block Time' (EOBT) is the time when:",
        "options": [
            "the aircraft takes off.",
            "the aircraft first moves for the purpose of taking off.",
            "the pilot arrives at the plane.",
            "the passengers start boarding."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the 'Top of Descent' (TOD)?",
        "options": [
            "The highest point in the sky.",
            "The calculated point where the transition from cruise to descent begins.",
            "The point where the landing gear is lowered.",
            "The destination airport."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Grid MORA' provides obstacle clearance within a grid defined by:",
        "options": [
            "magnetic headings.",
            "latitude and longitude lines.",
            "political borders.",
            "airways."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is 'RVSM'?",
        "options": [
            "Reduced Vertical Separation Minimum (1,000 ft between FL290 and FL410).",
            "Radio Velocity Speed Monitor.",
            "Rapid Vertical Speed Management.",
            "Revised Visual Standard Minimum."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "If TAS = 200 kts and wind is a 20 kts direct crosswind, the groundspeed is approximately:",
        "options": [
            "200 kts.",
            "199 kts.",
            "180 kts.",
            "220 kts."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'En-route Alternate' is used if:",
        "options": [
            "the destination is closed.",
            "a technical failure occurs during the cruise portion of the flight.",
            "the pilot is tired.",
            "there is too much traffic."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is 'Contingency Fuel' for?",
        "options": [
            "Unforeseen factors like wind changes, deviations from track, or holding.",
            "Flying to the alternate.",
            "Taxiing at the destination.",
            "A gift for the ground crew."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a METAR, 'SKC' stands for:",
        "options": [
            "Sky Clear.",
            "Smoke and Clouds.",
            "Scattered Clouds.",
            "Small Kansas City."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a METAR, 'FEW' means the sky coverage is:",
        "options": [
            "0 oktas.",
            "1 to 2 oktas.",
            "3 to 4 oktas.",
            "8 oktas."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a METAR, 'BKN' (Broken) means the sky coverage is:",
        "options": [
            "1 to 2 oktas.",
            "3 to 4 oktas.",
            "5 to 7 oktas.",
            "8 oktas."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a METAR, 'OVC' (Overcast) means the sky coverage is:",
        "options": [
            "5 to 7 oktas.",
            "8 oktas.",
            "10 oktas.",
            "No clouds."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What does 'SFC' stand for on a weather chart?",
        "options": [
            "Safe Flight Conditions.",
            "Surface.",
            "Special Flight Code.",
            "Sector Flight Center."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'SIGMET' is a weather advisory for:",
        "options": [
            "routine weather updates.",
            "significant meteorological phenomena which may affect the safety of aircraft operations.",
            "sunsets and sunrises.",
            "temperature changes at the airport."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Standard Rate' turn is:",
        "options": [
            "1 degree per second.",
            "3 degrees per second (Two minutes for 360 degrees).",
            "5 degrees per second.",
            "10 degrees per second."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "If the destination has only one runway, what is usually required for IFR planning?",
        "options": [
            "Two alternates.",
            "One alternate.",
            "Extra fuel for 2 hours.",
            "No alternate is needed."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the minimum visibility required for a 'Visual Approach'?",
        "options": [
            "1,500 m.",
            "5 km (or as specified by the state).",
            "800 m.",
            "No minimum."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Rhumb Line' is a track that:",
        "options": [
            "crosses all meridians at the same angle.",
            "is the shortest path.",
            "follows a circle of latitude.",
            "always points North."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Magnetic Variation' is the angle between:",
        "options": [
            "True North and Magnetic North.",
            "Magnetic North and Compass North.",
            "The aircraft heading and the wind.",
            "The ground and the flight path."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    }
]

def interleave_questions():
    file_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\src\data\questions.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    subjects = data.get('subjects', [])
    target_subject = None
    for s in subjects:
        if s['id'] == 'fligh-plan':
            target_subject = s
            break
            
    if not target_subject:
        print("Flight Planning subject not found!")
        return

    existing_questions = target_subject['questions']
    new_questions_formatted = []
    
    # Format new questions
    for i, q in enumerate(new_questions):
        q_copy = q.copy()
        q_copy['id'] = f"fligh-plan-new-{i+1}"
        new_questions_formatted.append(q_copy)
    
    merged_questions = []
    total_new = len(new_questions_formatted)
    total_existing = len(existing_questions)
    
    new_idx = 0
    for i in range(total_existing):
        merged_questions.append(existing_questions[i])
        if new_idx < total_new and (i + 1) * total_new // total_existing > new_idx:
            merged_questions.append(new_questions_formatted[new_idx])
            new_idx += 1
            
    while new_idx < total_new:
        merged_questions.append(new_questions_formatted[new_idx])
        new_idx += 1
        
    # Re-index
    for i, q in enumerate(merged_questions):
        q['id'] = f"fligh-plan-{i+1}"
        
    target_subject['questions'] = merged_questions
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully merged. Total Flight Planning questions: {len(merged_questions)}")

if __name__ == "__main__":
    interleave_questions()
