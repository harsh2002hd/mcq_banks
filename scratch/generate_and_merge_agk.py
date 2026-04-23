import json
import random

# Batch 1: 50 Questions (Hydraulics, Pneumatics, Landing Gear)
questions_batch_1 = [
    {
        "questionText": "In a basic hydraulic system, the purpose of an accumulator is to:",
        "options": [
            "store fluid under pressure and dampen pressure surges.",
            "increase the flow rate of the hydraulic pump.",
            "cool the hydraulic fluid before it returns to the reservoir.",
            "filter out contaminants from the hydraulic lines."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The hydraulic fluid used in most modern transport aircraft is typically:",
        "options": [
            "Mineral-based (MIL-H-5606).",
            "Phosphate ester-based (e.g., Skydrol).",
            "Vegetable-based fluid.",
            "Water-glycol mixture."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'priority valve' in a hydraulic system ensures that:",
        "options": [
            "the reservoir is always filled first.",
            "the landing gear always retracts before the flaps.",
            "essential services receive pressure before non-essential services.",
            "the pump does not exceed its maximum RPM."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a pneumatic system, 'bleed air' is typically taken from:",
        "options": [
            "the exhaust section of the engine.",
            "the compressor section of the engine.",
            "the bypass air of the fan.",
            "the intake manifold."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The purpose of a shimmy damper on a nose landing gear is to:",
        "options": [
            "prevent oscillations during high-speed taxi and takeoff.",
            "absorb the initial shock of landing.",
            "center the nose wheel after retraction.",
            "lock the nose wheel in the straight-ahead position."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the primary function of a fusible plug in an aircraft tire?",
        "options": [
            "To allow for manual deflation during maintenance.",
            "To prevent the tire from exploding due to excessive heat from braking.",
            "To provide a backup seal in case of valve failure.",
            "To indicate when the tire pressure is too low."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In an aircraft braking system, 'anti-skid' works by:",
        "options": [
            "increasing brake pressure when a skid is detected.",
            "releasing brake pressure when a wheel lock-up is imminent.",
            "automatically applying the emergency brake.",
            "reversing the rotation of the wheels."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Air Cycle Machine' (ACM) in a pneumatic system is used for:",
        "options": [
            "filtering the cabin air.",
            "cooling the bleed air for the air conditioning system.",
            "generating electrical power from bleed air.",
            "pressurizing the hydraulic reservoirs."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A check valve (non-return valve) in a hydraulic system allows fluid to flow:",
        "options": [
            "in both directions at all times.",
            "only when the pressure exceeds a certain limit.",
            "in one direction only.",
            "only during emergency operations."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The purpose of a hydraulic 'fuse' is to:",
        "options": [
            "prevent electrical shorts in the pump motor.",
            "shut off the flow if a downstream line ruptures or leaks excessively.",
            "regulate the system pressure to a constant value.",
            "mix fluid from two different systems."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What component in a landing gear system prevents the gear from retracting while the aircraft is on the ground?",
        "options": [
            "The up-lock mechanism.",
            "The ground safety switch (squat switch).",
            "The hydraulic selector valve.",
            "The emergency extension handle."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The term 'Pascal's Law' is the fundamental principle behind:",
        "options": [
            "aerodynamics.",
            "thermodynamics.",
            "hydraulics.",
            "pneumatics."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a multi-engine aircraft, a 'cross-feed' valve in the fuel system is used to:",
        "options": [
            "feed fuel from any tank to any engine.",
            "jettison fuel in an emergency.",
            "transfer fuel between wing tanks to balance the load.",
            "mix fuel with additives during flight."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The primary disadvantage of Skydrol hydraulic fluid is:",
        "options": [
            "it is highly flammable.",
            "it is chemically aggressive and can irritate skin and damage paint.",
            "it has a very low boiling point.",
            "it becomes extremely thick at low temperatures."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'brake wear indicator' on a large aircraft is typically:",
        "options": [
            "a light on the flight deck.",
            "a pin that protrudes from the brake assembly.",
            "a gauge in the wheel well.",
            "a sensor that measures brake temperature."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The function of a 'water separator' in an air conditioning system is to:",
        "options": [
            "remove moisture from the cooled air before it enters the cabin.",
            "provide drinking water for the crew.",
            "cool the air using evaporation.",
            "prevent ice from forming on the wings."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Which type of landing gear arrangement has two main wheels and a nose wheel?",
        "options": [
            "Conventional (Taildragger).",
            "Tricycle.",
            "Tandem.",
            "Bogie."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a hydraulic system, the 'relief valve' is designed to:",
        "options": [
            "increase system pressure during takeoff.",
            "protect the system from over-pressurization.",
            "allow the fluid to bypass the filter.",
            "indicate when the reservoir is low."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'boot' on a de-icing system is typically inflated by:",
        "options": [
            "hydraulic fluid.",
            "electrical motors.",
            "pneumatic air.",
            "exhaust gas."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'thermal relief valve' is used to:",
        "options": [
            "cool the hydraulic fluid.",
            "prevent damage caused by fluid expansion due to temperature increases.",
            "shut down the engine if it overheats.",
            "activate the fire extinguishers."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'snubber' in a landing gear system is used to:",
        "options": [
            "stop the wheels from spinning after retraction.",
            "lock the gear in the down position.",
            "provide steering on the ground.",
            "cushion the gear during extension."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Most aircraft pneumatic systems include a 'desiccant' or 'dryer' to:",
        "options": [
            "add humidity to the cabin air.",
            "remove moisture to prevent freezing and corrosion.",
            "cool the air before it reaches the actuators.",
            "increase the oxygen content of the air."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'variable displacement' hydraulic pump:",
        "options": [
            "changes its speed to match demand.",
            "automatically adjusts its fluid output to maintain a constant pressure.",
            "requires a separate regulator to control pressure.",
            "can only operate at one specific pressure."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The purpose of a 'selector valve' in a hydraulic system is to:",
        "options": [
            "select which pump is active.",
            "direct the flow of fluid to the desired actuator.",
            "choose between different types of hydraulic fluid.",
            "bypass the filter during cold starts."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a landing gear assembly, the 'oleo strut' uses:",
        "options": [
            "compressed air and springs.",
            "hydraulic fluid and compressed nitrogen.",
            "solid rubber blocks.",
            "magnetic levitation."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the function of the 'torque links' on a landing gear?",
        "options": [
            "To allow the gear to retract.",
            "To keep the upper and lower halves of the shock strut aligned.",
            "To transmit braking torque to the fuselage.",
            "To lock the gear in the down position."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'bootstrap reservoir' in a hydraulic system is pressurized by:",
        "options": [
            "engine bleed air.",
            "a separate electric pump.",
            "system pressure acting on a small piston.",
            "atmospheric pressure."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'dump valve' in a cabin pressurization system is used to:",
        "options": [
            "release all cabin pressure rapidly in an emergency.",
            "jettison excess fuel.",
            "remove water from the air conditioning lines.",
            "refill the oxygen tanks."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Which component prevents 'shimmy' by providing a damping force?",
        "options": [
            "Hydraulic fuse.",
            "Shimmy damper.",
            "Priority valve.",
            "Check valve."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'inflow valve' in a pressurization system controls:",
        "options": [
            "the rate at which air enters the cabin.",
            "the rate at which air leaves the cabin.",
            "the temperature of the incoming air.",
            "the humidity of the cabin."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a hydraulic system, 'cavitation' is usually caused by:",
        "options": [
            "excessive pressure.",
            "air or vapor bubbles forming in the fluid due to low pressure at the pump inlet.",
            "using the wrong type of fluid.",
            "overheating of the pump."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What does a 'brake temperature indicator' help the pilot avoid?",
        "options": [
            "Ice on the runway.",
            "Brake fade or fire after heavy use.",
            "Low hydraulic pressure.",
            "Tire wear."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'outflow valve' in a pressurization system maintains cabin altitude by:",
        "options": [
            "regulating the amount of air escaping from the cabin.",
            "changing the speed of the engine compressor.",
            "adjusting the mix of bleed air and outside air.",
            "opening the emergency exits slightly."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'tandem' landing gear configuration is most commonly found on:",
        "options": [
            "light general aviation aircraft.",
            "modern transport jets.",
            "some high-wing cargo or glider aircraft.",
            "carrier-based fighters."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The purpose of a 'shuttle valve' is to:",
        "options": [
            "allow two different power sources to operate a single component.",
            "reverse the direction of a hydraulic motor.",
            "shut down the system if a leak is detected.",
            "cool the hydraulic fluid."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the primary benefit of a multi-disc brake system?",
        "options": [
            "It is lighter than a single disc system.",
            "It provides a larger surface area for heat dissipation and friction.",
            "It is easier to maintain.",
            "It does not require hydraulic fluid."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'emergency extension' of landing gear on many aircraft is achieved by:",
        "options": [
            "reversing the hydraulic pump.",
            "gravity and aerodynamic loads (free-fall).",
            "using a hand crank connected to a gearbox.",
            "increasing the engine RPM."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a pneumatic system, the 'pressure regulator' ensures that:",
        "options": [
            "the system pressure remains at a constant, safe level.",
            "the air is always at the same temperature.",
            "the air is filtered properly.",
            "the pump does not overheat."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'bogie' landing gear refers to:",
        "options": [
            "a single wheel on a strut.",
            "a pair or more of wheels attached to a single shock strut.",
            "a retractable tail wheel.",
            "a gear that rotates 90 degrees during retraction."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The color of MIL-H-5606 hydraulic fluid is:",
        "options": [
            "Purple.",
            "Red.",
            "Green.",
            "Straw-yellow."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The color of Skydrol (phosphate ester) hydraulic fluid is typically:",
        "options": [
            "Red.",
            "Purple or Amber.",
            "Blue.",
            "Clear."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a 'constant pressure' hydraulic system, the pump is typically:",
        "options": [
            "fixed displacement with a pressure regulator.",
            "variable displacement.",
            "a simple gear pump.",
            "hand-operated."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'scissor link' on a landing gear shock strut is another name for:",
        "options": [
            "the drag brace.",
            "the torque link.",
            "the side stay.",
            "the up-lock."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Which component in a landing gear system absorbs the vertical energy of a landing?",
        "options": [
            "The tires.",
            "The shock strut (oleo).",
            "The torque links.",
            "The retraction actuator."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'ground-lock' pins are used to:",
        "options": [
            "lock the brakes when parked.",
            "prevent accidental gear retraction while the aircraft is on the ground.",
            "secure the aircraft to the hangar floor.",
            "lock the flight controls."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the purpose of 'venting' a fuel tank?",
        "options": [
            "To allow air to enter as fuel is consumed, preventing a vacuum.",
            "To let excess fuel vapor escape to prevent over-pressurization.",
            "Both A and B are correct.",
            "Neither A nor B is correct."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'primary' purpose of the landing gear is to:",
        "options": [
            "provide a means of steering the aircraft.",
            "support the aircraft on the ground and during takeoff/landing.",
            "act as a speed brake.",
            "protect the fuselage from damage."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'retractable' landing gear is primarily used to:",
        "options": [
            "save space in the hangar.",
            "reduce aerodynamic drag in flight.",
            "increase the weight of the aircraft.",
            "make the aircraft look more modern."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'nose wheel steering' system is typically powered by:",
        "options": [
            "the pilot's leg muscles.",
            "the electrical system.",
            "the hydraulic system.",
            "the pneumatic system."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What happens if the 'anti-skid' system fails?",
        "options": [
            "The brakes will not work at all.",
            "Normal braking is still available, but without skid protection.",
            "The landing gear will not retract.",
            "The aircraft will automatically veer off the runway."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    }
]

# Batch 2: 50 Questions (Engines, Electrics)
questions_batch_2 = [
    {
        "questionText": "In a four-stroke piston engine, the sequence of strokes is:",
        "options": [
            "Intake, Compression, Power, Exhaust.",
            "Intake, Power, Compression, Exhaust.",
            "Compression, Intake, Power, Exhaust.",
            "Intake, Compression, Exhaust, Power."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'compression ratio' of a piston engine is the ratio of:",
        "options": [
            "intake pressure to exhaust pressure.",
            "cylinder volume at BDC to cylinder volume at TDC.",
            "fuel to air in the mixture.",
            "engine speed to propeller speed."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The purpose of a 'turbocharger' in a piston engine is to:",
        "options": [
            "cool the engine oil.",
            "increase the density of the intake air, especially at high altitudes.",
            "reduce the noise of the exhaust.",
            "generate electrical power."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a gas turbine engine, the 'Brayton cycle' consists of which four processes?",
        "options": [
            "Intake, Compression, Combustion, Expansion.",
            "Induction, Compression, Ignition, Exhaust.",
            "Compression, Heating, Expansion, Cooling.",
            "Suction, Squeeze, Bang, Blow."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'N1' gauge in a turbofan engine typically indicates:",
        "options": [
            "the rotational speed of the high-pressure compressor.",
            "the rotational speed of the low-pressure compressor/fan.",
            "the exhaust gas temperature.",
            "the fuel flow rate."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'N2' or 'N3' gauge indicates:",
        "options": [
            "the speed of the intermediate or high-pressure compressor core.",
            "the speed of the propeller.",
            "the oil pressure.",
            "the cabin altitude."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'turboprop' engine is essentially a gas turbine that:",
        "options": [
            "drives a propeller through a reduction gearbox.",
            "uses a fan to produce most of its thrust.",
            "has no compressor section.",
            "only operates at low altitudes."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The purpose of a 'stator' blade in a compressor is to:",
        "options": [
            "increase the velocity of the air.",
            "convert kinetic energy into pressure energy and direct air to the next rotor stage.",
            "ignite the fuel-air mixture.",
            "cool the turbine blades."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Which component in a gas turbine engine is most likely to suffer from 'creep'?",
        "options": [
            "The compressor blades.",
            "The turbine blades.",
            "The intake cowling.",
            "The accessory gearbox."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'bypass ratio' in a turbofan engine is the ratio of:",
        "options": [
            "fuel flow to air flow.",
            "air that passes around the core to air that passes through the core.",
            "thrust produced by the fan to thrust produced by the core.",
            "intake area to exhaust area."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'igniters' in a jet engine are typically used:",
        "options": [
            "continuously throughout the flight.",
            "only during starting and in certain conditions like heavy rain or icing.",
            "only when the engine is at full throttle.",
            "to pre-heat the fuel."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the function of a 'FADEC' system?",
        "options": [
            "To control the flight surfaces.",
            "To provide full authority digital control over all aspects of engine performance.",
            "To manage the cabin entertainment system.",
            "To monitor the landing gear position."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'EGT' (Exhaust Gas Temperature) is a critical parameter because it indicates:",
        "options": [
            "the efficiency of the propeller.",
            "the thermal stress on the turbine section.",
            "the amount of thrust being produced.",
            "the altitude of the aircraft."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "An 'Inverter' in an aircraft electrical system converts:",
        "options": [
            "AC to DC.",
            "DC to AC.",
            "High voltage to low voltage.",
            "Mechanical energy to electrical energy."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Transformer Rectifier Unit' (TRU) converts:",
        "options": [
            "DC to AC.",
            "AC to DC.",
            "Low frequency to high frequency.",
            "Fuel energy to electrical energy."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Most large transport aircraft use an electrical system with a frequency of:",
        "options": [
            "50 Hz.",
            "60 Hz.",
            "400 Hz.",
            "1000 Hz."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The standard DC voltage on many light and medium aircraft is:",
        "options": [
            "12V.",
            "24V or 28V.",
            "115V.",
            "230V."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Constant Speed Drive' (CSD) or 'Integrated Drive Generator' (IDG) is used to:",
        "options": [
            "keep the propeller at a constant RPM.",
            "ensure the generator produces a constant AC frequency regardless of engine speed.",
            "regulate the battery charging rate.",
            "control the speed of the cooling fans."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Circuit Breaker' is designed to:",
        "options": [
            "store electrical energy for later use.",
            "protect the electrical circuit from over-current or short circuits.",
            "increase the voltage of the system.",
            "switch between different power sources."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Bus Bar' in an electrical system acts as:",
        "options": [
            "a cooling fin for the generator.",
            "a central distribution point for electrical power to various circuits.",
            "a backup battery.",
            "a sensor for measuring current."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the purpose of an 'APU' (Auxiliary Power Unit)?",
        "options": [
            "To provide extra thrust during takeoff.",
            "To provide electrical power and bleed air when the main engines are not running.",
            "To act as a backup for the flight controls.",
            "To stabilize the aircraft in turbulence."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'RAT' (Ram Air Turbine) is an emergency device that provides:",
        "options": [
            "extra fuel to the engines.",
            "limited hydraulic or electrical power using the aircraft's airspeed.",
            "oxygen to the passengers.",
            "braking force on the runway."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Nickel-Cadmium' (NiCd) battery is common in aviation because:",
        "options": [
            "it is very cheap.",
            "it can provide high discharge rates and has a flat discharge curve.",
            "it is extremely light.",
            "it never requires maintenance."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Thermal Runaway' is a dangerous condition associated with:",
        "options": [
            "jet engines at high power.",
            "Nickel-Cadmium batteries.",
            "hydraulic fluid overheating.",
            "glass cockpits."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Exciter' in a generator system is used to:",
        "options": [
            "start the engine.",
            "provide the initial magnetic field for the main generator.",
            "cool the generator windings.",
            "regulate the frequency."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a 'split-bus' electrical system:",
        "options": [
            "the left and right generators normally operate independently.",
            "all power sources are always connected in parallel.",
            "the battery is the only source of power.",
            "half of the instruments are turned off to save power."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The purpose of a 'Galley Shed' function in an electrical system is to:",
        "options": [
            "increase power to the kitchen ovens.",
            "automatically disconnect non-essential loads (like the galley) during power shortages.",
            "store food for the crew.",
            "protect the galley from fire."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What does a 'Voltmeter' measure in an aircraft?",
        "options": [
            "Current flow (Amps).",
            "Electrical potential difference (Volts).",
            "Resistance (Ohms).",
            "Power (Watts)."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What does an 'Ammeter' measure?",
        "options": [
            "Voltage.",
            "Current flow in Amperes.",
            "Magnetic field strength.",
            "Battery temperature."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Master Switch' in a light aircraft:",
        "options": [
            "starts the engine.",
            "connects the battery to the main electrical bus.",
            "activates the autopilot.",
            "jettisons the fuel."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Magneto' in a piston engine provides:",
        "options": [
            "electrical power for the cabin lights.",
            "an independent high-voltage source for the spark plugs.",
            "magnetic force to hold the propeller.",
            "timing for the valves."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Dual ignition systems in piston engines provide:",
        "options": [
            "better fuel economy.",
            "redundancy and more efficient combustion.",
            "higher top speed.",
            "easier starting in cold weather."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'impulse coupling' on a magneto is used to:",
        "options": [
            "speed up the magneto rotation during engine start for a hotter spark.",
            "disconnect the magneto in flight.",
            "synchronize two magnetos.",
            "cool the magneto."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Solid State' power controller is:",
        "options": [
            "a heavy mechanical switch.",
            "a modern, electronic equivalent to a circuit breaker or relay.",
            "a type of battery.",
            "a fuel regulator."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Neutral' or 'Ground' point in an aircraft electrical system is usually:",
        "options": [
            "a separate wire returning to the battery.",
            "the metal structure (airframe) of the aircraft.",
            "the engine block only.",
            "connected to a copper rod trailing behind the plane."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is 'Load Shedding'?",
        "options": [
            "Dropping cargo in an emergency.",
            "The intentional reduction of electrical demand by turning off non-essential systems.",
            "Reducing the aircraft's weight for landing.",
            "Emptying the waste tanks."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Brushless' generator is preferred in aviation because:",
        "options": [
            "it is much heavier.",
            "it reduces maintenance and eliminates the risk of sparking at high altitudes.",
            "it produces DC power directly.",
            "it is more colorful."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'GCU' (Generator Control Unit) manages:",
        "options": [
            "engine thrust.",
            "voltage regulation, protection, and bus connection for the generator.",
            "the speed of the APU.",
            "the brightness of the cockpit lights."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Which electrical component allows current to flow in one direction only?",
        "options": [
            "Resistor.",
            "Capacitor.",
            "Diode.",
            "Inductor."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Static Wick' is used to:",
        "options": [
            "light the engine burners.",
            "dissipate static electricity buildup from the airframe into the atmosphere.",
            "measure the humidity.",
            "protect against lightning strikes."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Primary' source of DC power in a large aircraft with an AC system is:",
        "options": [
            "the batteries.",
            "the Transformer Rectifier Units (TRUs).",
            "the static inverters.",
            "the APU generator."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Hot Battery Bus' is one that is:",
        "options": [
            "overheated and dangerous.",
            "always connected to the battery, regardless of the master switch position.",
            "used only for the cabin heater.",
            "activated only when the engines are hot."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Essential Bus' provides power to:",
        "options": [
            "the coffee maker and ovens.",
            "systems critical for the safe continuation of the flight.",
            "the landing lights only.",
            "the passenger reading lights."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What does a 'Zener Diode' typically do in a circuit?",
        "options": [
            "Acts as a voltage regulator.",
            "Stores large amounts of charge.",
            "Amplifies signals.",
            "Converts AC to DC."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a parallel AC system, the 'Real Load' (Watts) is shared by:",
        "options": [
            "adjusting the voltage of the generators.",
            "adjusting the torque (phase angle) of the drives.",
            "changing the size of the wires.",
            "turning off the lights."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a parallel AC system, the 'Reactive Load' (VARs) is shared by:",
        "options": [
            "adjusting the engine RPM.",
            "adjusting the generator field excitation (voltage).",
            "using capacitors.",
            "disconnecting the battery."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the function of a 'Bonding Jumper'?",
        "options": [
            "To connect the pilot's harness.",
            "To ensure all parts of the aircraft have the same electrical potential.",
            "To jump-start the engine.",
            "To attach the wings to the fuselage."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Standby' power system usually consists of:",
        "options": [
            "a second APU.",
            "a battery and a static inverter.",
            "a hand-cranked generator.",
            "extra fuel for the engines."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Relay' is essentially:",
        "options": [
            "a type of battery.",
            "an electrically operated switch.",
            "a variable resistor.",
            "a fuse that resets itself."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Frequency' of an AC generator depends on:",
        "options": [
            "the voltage output.",
            "the speed of rotation and the number of poles.",
            "the ambient temperature.",
            "the load connected to it."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    }
]

# Batch 3: 50 Questions (Fire, Fuel, Ice, Misc)
questions_batch_3 = [
    {
        "questionText": "A 'Kidde' or 'Fenwal' system is used for:",
        "options": [
            "fire detection.",
            "fuel measurement.",
            "cabin altitude control.",
            "landing gear positioning."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'continuous loop' fire detector works on the principle of:",
        "options": [
            "measuring the brightness of the fire.",
            "detecting a change in resistance or capacitance due to temperature.",
            "the melting of a fuse link.",
            "the pilot seeing smoke."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In an engine fire extinguishing system, 'Halon' is used because:",
        "options": [
            "it is very cold and freezes the fire.",
            "it chemically interrupts the combustion process and is non-conductive.",
            "it provides a thick blanket of foam.",
            "it is highly flammable and burns off the oxygen."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'red disk' on the side of the fuselage indicates:",
        "options": [
            "the aircraft is ready for flight.",
            "the fire extinguisher has been discharged due to over-pressurization (thermal discharge).",
            "the oxygen system is full.",
            "the fuel is contaminated."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'smoke detector' in a cargo compartment often uses:",
        "options": [
            "a thermal switch.",
            "an optical (light scattering) or ionization sensor.",
            "a microphone to hear the crackling.",
            "a moisture sensor."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The purpose of 'scavenge pumps' in a fuel system is to:",
        "options": [
            "increase fuel pressure to the engine.",
            "ensure all fuel is moved from the bottom of the tanks to the main pump intake.",
            "clean the fuel of impurities.",
            "jettison fuel in an emergency."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'dripstick' or 'magnetic level indicator' is used to:",
        "options": [
            "check the oil level in the engine.",
            "manually measure fuel quantity from under the wing.",
            "detect leaks in the hydraulic system.",
            "measure the tire pressure."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is 'Fuel Jettisoning' used for?",
        "options": [
            "To increase the weight for a smoother landing.",
            "To reduce aircraft weight to the maximum landing weight in an emergency.",
            "To clean the fuel tanks.",
            "To create a smoke screen."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Expansion Space' in a fuel tank is required to:",
        "options": [
            "allow for fuel to increase in volume due to temperature changes.",
            "store extra fuel for long flights.",
            "collect water at the bottom.",
            "provide a place for the pumps."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "An 'Anti-Icing' system is designed to:",
        "options": [
            "remove ice after it has already formed.",
            "prevent ice from forming in the first place.",
            "detect ice on the wings.",
            "cool the engines."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'De-Icing' system is designed to:",
        "options": [
            "prevent ice from forming.",
            "remove ice that has already accumulated.",
            "increase the lift of the wing.",
            "prevent the fuel from freezing."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Wing 'thermal anti-ice' systems typically use:",
        "options": [
            "electrical heating elements.",
            "hot bleed air from the engines.",
            "hot engine oil circulated through the skin.",
            "chemical sprays."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Pitot Probe' is heated to:",
        "options": [
            "keep the air inside warm.",
            "prevent ice from blocking the pressure port.",
            "increase the accuracy of the altimeter.",
            "prevent the probe from breaking off."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the purpose of a 'Weeping Wing' system (TKS)?",
        "options": [
            "To wash the wings during flight.",
            "To release an anti-icing fluid through porous panels on the leading edge.",
            "To allow fuel to leak out in an emergency.",
            "To signal a structural failure."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Which part of a propeller is most likely to be heated for ice protection?",
        "options": [
            "The tips.",
            "The leading edges near the root.",
            "The trailing edges.",
            "The spinner only."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The purpose of a 'fuel-oil heat exchanger' is to:",
        "options": [
            "cool the fuel using the oil.",
            "cool the engine oil while pre-warming the fuel.",
            "heat the cabin using engine oil.",
            "cool the exhaust gases."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'baffle' in a fuel tank is used to:",
        "options": [
            "prevent fuel from sloshing and causing center of gravity shifts.",
            "filter the fuel.",
            "measure the fuel level.",
            "heat the fuel."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a fuel system, 'sump' is the point where:",
        "options": [
            "the fuel is pumped to the engine.",
            "water and contaminants collect and can be drained.",
            "the fuel is pressurized.",
            "the cross-feed valve is located."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'specific gravity' of jet fuel is approximately:",
        "options": [
            "0.72.",
            "0.80.",
            "1.00.",
            "1.25."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Which type of fuel is commonly used in modern jet transport aircraft?",
        "options": [
            "AVGAS 100LL.",
            "JET A-1.",
            "MOGAS.",
            "Kerosene-free biofuel."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The primary danger of 'ice accumulation' on a wing is:",
        "options": [
            "it makes the plane too heavy to fly.",
            "it changes the aerodynamic shape, reducing lift and increasing stall speed.",
            "it blocks the pilot's view.",
            "it causes the engines to stop."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "An 'Oxygen Candle' (chemical oxygen generator) produces oxygen by:",
        "options": [
            "burning a chemical mixture (e.g., sodium chlorate).",
            "filtering nitrogen from the air.",
            "compressing outside air.",
            "electrolysis of water."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'diluter-demand' oxygen regulator provides:",
        "options": [
            "100% oxygen at all times.",
            "a mixture of air and oxygen based on altitude, or 100% oxygen if selected.",
            "oxygen only when the pilot inhales.",
            "oxygen at a constant flow rate."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "In a 'pressure-demand' oxygen system:",
        "options": [
            "oxygen is forced into the pilot's lungs under pressure at high altitudes.",
            "the pilot must pump the oxygen manually.",
            "the oxygen is stored at extremely high pressure.",
            "the mask is tightened automatically."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The purpose of a 'Mach Trim' system is to:",
        "options": [
            "speed up the aircraft.",
            "automatically adjust the pitch to prevent 'Mach Tuck' at high speeds.",
            "trim the aircraft for takeoff.",
            "limit the maximum speed."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Yaw Damper' is used to:",
        "options": [
            "stop the aircraft from turning.",
            "prevent or dampen 'Dutch Roll' oscillations.",
            "assist the pilot in steep turns.",
            "lock the rudder on the ground."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Fly-by-Wire' system replaces mechanical linkages with:",
        "options": [
            "hydraulic lines only.",
            "electrical signals and computers.",
            "radio waves.",
            "pulleys and cables."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "An 'Autothrottle' (or Autotrust) system:",
        "options": [
            "controls the aircraft's altitude.",
            "automatically adjusts the engine power to maintain a set speed or thrust.",
            "steers the aircraft on the ground.",
            "starts the engines automatically."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Stick Shaker' is a device that:",
        "options": [
            "indicates the engine is running roughly.",
            "provides a tactile warning to the pilot that a stall is imminent.",
            "helps the pilot move the controls.",
            "signals that the autopilot has disconnected."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Stick Pusher' system:",
        "options": [
            "assists the pilot in pulling up.",
            "automatically moves the control column forward to prevent a deep stall.",
            "locks the controls on the ground.",
            "is used for aerobatics."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'EICAS' or 'ECAM' system provides:",
        "options": [
            "entertainment for the passengers.",
            "integrated monitoring of engine and system parameters and alerts.",
            "weather radar information.",
            "navigation instructions."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the function of a 'Vortex Generator'?",
        "options": [
            "To create electricity.",
            "To delay airflow separation at high angles of attack or high speeds.",
            "To cool the wings.",
            "To make the aircraft quieter."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Spoiler' on a wing can be used for:",
        "options": [
            "roll control (as asymmetric spoilers).",
            "descending rapidly (as speed brakes).",
            "dumping lift on landing (as ground spoilers).",
            "All of the above."
        ],
        "correctAnswerIndex": 3,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Which type of flap extends rearward and downward, increasing both wing area and camber?",
        "options": [
            "Plain flap.",
            "Split flap.",
            "Fowler flap.",
            "Slotted flap."
        ],
        "correctAnswerIndex": 2,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Slotted' flap allows high-pressure air from the lower surface to:",
        "options": [
            "escape into the atmosphere.",
            "flow over the upper surface to delay airflow separation.",
            "cool the brakes.",
            "enter the cabin."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Slat' is a leading-edge device that:",
        "options": [
            "increases drag for landing.",
            "creates a slot to allow air to flow over the wing at high angles of attack.",
            "protects the wing from bird strikes.",
            "is only used on supersonic planes."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Stabilator' is a flight control surface that combines the functions of:",
        "options": [
            "the rudder and elevator.",
            "the horizontal stabilizer and the elevator.",
            "the aileron and the flap.",
            "the wing and the fuselage."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'V-tail' (Butterfly tail) arrangement uses 'Ruddervators' to control:",
        "options": [
            "roll and pitch.",
            "pitch and yaw.",
            "roll and yaw.",
            "pitch only."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Servo Tab' is used to:",
        "options": [
            "trim the aircraft.",
            "assist the pilot in moving a large or heavy control surface.",
            "lock the controls.",
            "measure the airspeed."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "An 'Anti-Servo Tab' on a stabilator moves in:",
        "options": [
            "the opposite direction to the surface, making it easier to move.",
            "the same direction as the surface, increasing the aerodynamic feel and stability.",
            "only one direction.",
            "a random pattern."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Balance Tab' moves in:",
        "options": [
            "the same direction as the control surface.",
            "the opposite direction to the control surface, reducing the force required by the pilot.",
            "a fixed position.",
            "response to the autopilot only."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "Which instrument provides the pilot with an artificial horizon?",
        "options": [
            "Altimeter.",
            "Attitude Indicator (Gyro Horizon).",
            "Vertical Speed Indicator.",
            "Heading Indicator."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Turn Coordinator' provides information about:",
        "options": [
            "the angle of bank only.",
            "the rate of turn and the coordination (slip/skid).",
            "the aircraft's heading.",
            "the altitude."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Pitot-Static' system is used by which instruments?",
        "options": [
            "Altimeter, Airspeed Indicator, and VSI.",
            "Attitude Indicator and Heading Indicator.",
            "Magnetic Compass and Turn Coordinator.",
            "Engine Tachometer."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Radio Altimeter' measures altitude based on:",
        "options": [
            "barometric pressure.",
            "the time taken for a radio signal to reflect off the ground.",
            "GPS signals.",
            "the distance to the nearest mountain."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'GPWS' (Ground Proximity Warning System) warns the pilot of:",
        "options": [
            "other aircraft in the area.",
            "imminent impact with the ground or terrain.",
            "engine failure.",
            "low fuel."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'TCAS' (Traffic Alert and Collision Avoidance System) is used to:",
        "options": [
            "detect terrain.",
            "detect and provide resolution advisories for other aircraft.",
            "guide the aircraft to the runway.",
            "monitor the weather."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "A 'Magnetic Compass' is subject to errors such as:",
        "options": [
            "Variation and Deviation.",
            "Parallax and Refraction.",
            "Friction and Lag.",
            "All of the above."
        ],
        "correctAnswerIndex": 0,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "What is the purpose of 'Compass Swing'?",
        "options": [
            "To make the compass look better.",
            "To calibrate the compass and determine its deviation on various headings.",
            "To clean the compass liquid.",
            "To check if the compass points North."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    },
    {
        "questionText": "The 'Glass Cockpit' refers to a flight deck that uses:",
        "options": [
            "mostly glass windows.",
            "electronic flight instrument system (EFIS) displays instead of traditional dials.",
            "touchscreen controls only.",
            "transparent wings."
        ],
        "correctAnswerIndex": 1,
        "hasDetectedAnswer": False
    }
]

all_new_questions = questions_batch_1 + questions_batch_2 + questions_batch_3

def interleave_questions():
    file_path = r'c:\Users\91635\Documents\programmes\assignment\aviation website\src\data\questions.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    subjects = data.get('subjects', [])
    agk_subject = None
    for s in subjects:
        if s['id'] == 'agk-pdf':
            agk_subject = s
            break
            
    if not agk_subject:
        print("AGK subject not found!")
        return

    existing_questions = agk_subject['questions']
    new_questions_formatted = []
    
    # Format new questions (assign temporary IDs and set defaults)
    for i, q in enumerate(all_new_questions):
        q_copy = q.copy()
        q_copy['id'] = f"agk-new-{i+1}"
        new_questions_formatted.append(q_copy)
    
    # Interleave logic
    # We want to insert 150 questions into 802.
    # Gap between insertions = 802 / 150 ≈ 5.34
    
    merged_questions = []
    total_new = len(new_questions_formatted)
    total_existing = len(existing_questions)
    
    new_idx = 0
    for i in range(total_existing):
        merged_questions.append(existing_questions[i])
        # Insert a new question roughly every 5.34 steps
        if new_idx < total_new and (i + 1) * total_new // total_existing > new_idx:
            merged_questions.append(new_questions_formatted[new_idx])
            new_idx += 1
            
    # Add any remaining new questions
    while new_idx < total_new:
        merged_questions.append(new_questions_formatted[new_idx])
        new_idx += 1
        
    # Re-index all questions
    for i, q in enumerate(merged_questions):
        q['id'] = f"agk-pdf-{i+1}"
        
    agk_subject['questions'] = merged_questions
    
    # Update count if it exists in metadata (though not seen in snippet)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully merged. Total AGK questions: {len(merged_questions)}")

if __name__ == "__main__":
    interleave_questions()
