from unittest import TestCase, mock

import vpic


fake_db = {
    '5FYD4FS147B031975': {
        'ABS': '',
        'AEB': '',
        'AdaptiveCruiseControl': '',
        'AdaptiveHeadlights': '',
        'AdditionalErrorText': '',
        'AirBagLocCurtain': '',
        'AirBagLocFront': '',
        'AirBagLocKnee': '',
        'AirBagLocSeatCushion': '',
        'AirBagLocSide': '',
        'Artemis': '',
        'AxleConfiguration': '',
        'Axles': '',
        'BasePrice': '',
        'BatteryA': '',
        'BatteryA_to': '',
        'BatteryCells': '',
        'BatteryInfo': '',
        'BatteryKWh': '',
        'BatteryKWh_to': '',
        'BatteryModules': '',
        'BatteryPacks': '',
        'BatteryType': '',
        'BatteryV': '',
        'BatteryV_to': '',
        'BedLengthIN': '',
        'BedType': '',
        'BlindSpotMon': '',
        'BodyCabType': '',
        'BodyClass': 'Bus',
        'BrakeSystemDesc': 'Air With Separate Spring Brake Release '
        '(with Emergency Release Air Tank)',
        'BrakeSystemType': 'Air',
        'BusFloorConfigType': '',
        'BusLength': '',
        'BusType': '',
        'CAFEBodyType': '',
        'CAFEMake': '',
        'CAFEModel': '',
        'CashForClunkers': '',
        'ChargerLevel': '',
        'ChargerPowerKW': '',
        'CoolingType': '',
        'Country': '',
        'CurbWeightLB': '',
        'CustomMotorcycleType': '',
        'DestinationMarket': '',
        'DisplacementCC': '11000',
        'DisplacementCI': '671.2611850420',
        'DisplacementL': '11',
        'Doors': '',
        'DriveType': '',
        'DriverAssist': '',
        'ESC': '',
        'EVDriveUnit': '',
        'ElectrificationLevel': '',
        'EngineConfiguration': 'In-Line',
        'EngineCycles': '4',
        'EngineCylinders': '6',
        'EngineHP': '280',
        'EngineHP_to': '400',
        'EngineKW': '208.7960',
        'EngineManufacturer': 'Cummins',
        'EngineModel': 'M11',
        'EntertainmentSystem': '',
        'EquipmentType': '',
        'ErrorCode': '0 - VIN decoded clean. Check Digit (9th position) is correct',
        'ForwardCollisionWarning': '',
        'FuelInjectionType': '',
        'FuelTypePrimary': 'Diesel',
        'FuelTypeSecondary': '',
        'GVWR': '',
        'LaneDepartureWarning': '',
        'LaneKeepSystem': '',
        'Make': 'NEW FLYER',
        'Manufacturer': 'NEW FLYER',
        'ManufacturerId': '1046',
        'ManufacturerType': '',
        'Model': 'Low Floor',
        'ModelYear': '2007',
        'MotorcycleChassisType': '',
        'MotorcycleSuspensionType': '',
        'NCAPBodyType': '',
        'NCAPMake': '',
        'NCAPModel': '',
        'NCICCode': '',
        'NCSABodyType': '',
        'NCSAMake': '',
        'NCSAModel': '',
        'Note': '40 Foot',
        'OtherBusInfo': '',
        'OtherEngineInfo': 'horsepower: 280, 305, 310, 330, 330/370, 335, 350, 350/400, 370, 400',
        'OtherMotorcycleInfo': '',
        'OtherRestraintSystemInfo': '',
        'OtherTrailerInfo': '',
        'ParkAssist': '',
        'PlantCity': 'St Cloud',
        'PlantCompanyName': 'New Flyer America',
        'PlantCountry': 'United States (USA)',
        'PlantState': 'Minnesota',
        'PossibleValues': '',
        'Pretensioner': '',
        'RearVisibilityCamera': '',
        'SeatBeltsAll': '',
        'SeatRows': '',
        'Seats': '',
        'Series': '',
        'Series2': '',
        'SteeringLocation': '',
        'SuggestedVIN': '',
        'TPMS': '',
        'TopSpeedMPH': '',
        'TrackWidth': '',
        'TractionControl': '',
        'TrailerBodyType': '',
        'TrailerLength': '',
        'TrailerType': '',
        'TransmissionSpeeds': '',
        'TransmissionStyle': '',
        'Trim': '',
        'Trim2': '',
        'Turbo': '',
        'VIN': '5FYD4FS147B031975',
        'ValveTrainDesign': '',
        'VehicleType': 'BUS',
        'WheelBaseLong': '',
        'WheelBaseShort': '',
        'WheelBaseType': '',
        'WheelSizeFront': '',
        'WheelSizeRear': '',
        'Wheels': '',
        'Windows': ''
    },
    '4V4WDBPFSCN735320': {
        'ABS': '',
        'AEB': '',
        'AdaptiveCruiseControl': '',
        'AdaptiveHeadlights': '',
        'AdditionalErrorText': 'The error positions are indicated by ! in Suggested VIN. In the '
        'Possible values section, each pair of parenthesis indicate information about each error '
        'position in VIN . The Numeric value before the : indicates the position in error and the '
        'values after the : indicate the possible values that are allowed in this position\rThe '
        'Model Year decoded for this VIN may be incorrect. If you know the Model year, please '
        'enter it and decode again to get more accurate information.',
        'AirBagLocCurtain': '',
        'AirBagLocFront': '',
        'AirBagLocKnee': '',
        'AirBagLocSeatCushion': '',
        'AirBagLocSide': '',
        'Artemis': '',
        'AxleConfiguration': '',
        'Axles': '',
        'BasePrice': '',
        'BatteryA': '',
        'BatteryA_to': '',
        'BatteryCells': '',
        'BatteryInfo': '',
        'BatteryKWh': '',
        'BatteryKWh_to': '',
        'BatteryModules': '',
        'BatteryPacks': '',
        'BatteryType': '',
        'BatteryV': '',
        'BatteryV_to': '',
        'BedLengthIN': '',
        'BedType': '',
        'BlindSpotMon': '',
        'BodyCabType': 'MDHD: Conventional',
        'BodyClass': '',
        'BrakeSystemDesc': '',
        'BrakeSystemType': '',
        'BusFloorConfigType': '',
        'BusLength': '',
        'BusType': '',
        'CAFEBodyType': '',
        'CAFEMake': '',
        'CAFEModel': '',
        'CashForClunkers': '',
        'ChargerLevel': '',
        'ChargerPowerKW': '',
        'CoolingType': '',
        'Country': '',
        'CurbWeightLB': '',
        'CustomMotorcycleType': '',
        'DestinationMarket': '',
        'DisplacementCC': '',
        'DisplacementCI': '',
        'DisplacementL': '',
        'Doors': '',
        'DriveType': '',
        'DriverAssist': '',
        'ESC': '',
        'EVDriveUnit': '',
        'ElectrificationLevel': '',
        'EngineConfiguration': '',
        'EngineCycles': '',
        'EngineCylinders': '',
        'EngineHP': '325',
        'EngineHP_to': '374',
        'EngineKW': '242.3525',
        'EngineManufacturer': '',
        'EngineModel': '',
        'EntertainmentSystem': '',
        'EquipmentType': '',
        'ErrorCode': '5 - VIN has errors in few positions.',
        'ForwardCollisionWarning': '',
        'FuelInjectionType': '',
        'FuelTypePrimary': '',
        'FuelTypeSecondary': '',
        'GVWR': '',
        'LaneDepartureWarning': '',
        'LaneKeepSystem': '',
        'Make': 'VOLVO TRUCK ',
        'Manufacturer': 'VOLVO GROUP NORTH AMERICA, LLC',
        'ManufacturerId': '1015',
        'ManufacturerType': '',
        'Model': '',
        'ModelYear': '2012',
        'MotorcycleChassisType': '',
        'MotorcycleSuspensionType': '',
        'NCAPBodyType': '',
        'NCAPMake': '',
        'NCAPModel': '',
        'NCICCode': '',
        'NCSABodyType': '',
        'NCSAMake': '',
        'NCSAModel': '',
        'Note': '',
        'OtherBusInfo': '',
        'OtherEngineInfo': '',
        'OtherMotorcycleInfo': '',
        'OtherRestraintSystemInfo': '',
        'OtherTrailerInfo': '',
        'ParkAssist': '',
        'PlantCity': 'New River Valley Dublin',
        'PlantCompanyName': '',
        'PlantCountry': 'United States (USA)',
        'PlantState': 'Virginia',
        'PossibleValues': '(4:KLMNR)(5:139C)(6:9)(7:DEKTUV)',
        'Pretensioner': '',
        'RearVisibilityCamera': '',
        'SeatBeltsAll': '',
        'SeatRows': '',
        'Seats': '',
        'Series': '',
        'Series2': '',
        'SteeringLocation': '',
        'SuggestedVIN': '4V4!!!!FSCN735320',
        'TPMS': '',
        'TopSpeedMPH': '',
        'TrackWidth': '',
        'TractionControl': '',
        'TrailerBodyType': '',
        'TrailerLength': '',
        'TrailerType': '',
        'TransmissionSpeeds': '',
        'TransmissionStyle': '',
        'Trim': '',
        'Trim2': '',
        'Turbo': '',
        'VIN': '4V4WDBPFSCN735320',
        'ValveTrainDesign': '',
        'VehicleType': 'TRUCK ',
        'WheelBaseLong': '',
        'WheelBaseShort': '',
        'WheelBaseType': '',
        'WheelSizeFront': '',
        'WheelSizeRear': '',
        'Wheels': '',
        'Windows': ''
    },
    '1XKWDB9X3TR727776': {
        'ABS': '',
        'AEB': '',
        'AdaptiveCruiseControl': '',
        'AdaptiveHeadlights': '',
        'AdditionalErrorText': '',
        'AirBagLocCurtain': '',
        'AirBagLocFront': '',
        'AirBagLocKnee': '',
        'AirBagLocSeatCushion': '',
        'AirBagLocSide': '',
        'Artemis': '',
        'AxleConfiguration': '',
        'Axles': '',
        'BasePrice': '',
        'BatteryA': '',
        'BatteryA_to': '',
        'BatteryCells': '',
        'BatteryInfo': '',
        'BatteryKWh': '',
        'BatteryKWh_to': '',
        'BatteryModules': '',
        'BatteryPacks': '',
        'BatteryType': '',
        'BatteryV': '',
        'BatteryV_to': '',
        'BedLengthIN': '',
        'BedType': '',
        'BlindSpotMon': '',
        'BodyCabType': 'MDHD: Conventional',
        'BodyClass': 'Truck - Tractor',
        'BrakeSystemDesc': '',
        'BrakeSystemType': 'Air',
        'BusFloorConfigType': '',
        'BusLength': '',
        'BusType': '',
        'CAFEBodyType': '',
        'CAFEMake': '',
        'CAFEModel': '',
        'CashForClunkers': '',
        'ChargerLevel': '',
        'ChargerPowerKW': '',
        'CoolingType': '',
        'Country': '',
        'CurbWeightLB': '',
        'CustomMotorcycleType': '',
        'DestinationMarket': '',
        'DisplacementCC': '',
        'DisplacementCI': '',
        'DisplacementL': '',
        'Doors': '',
        'DriveType': '6x4',
        'DriverAssist': '',
        'ESC': '',
        'EVDriveUnit': '',
        'ElectrificationLevel': '',
        'EngineConfiguration': '',
        'EngineCycles': '',
        'EngineCylinders': '',
        'EngineHP': '',
        'EngineHP_to': '',
        'EngineKW': '',
        'EngineManufacturer': 'Caterpillar ',
        'EngineModel': '3406',
        'EntertainmentSystem': '',
        'EquipmentType': '',
        'ErrorCode': '0 - VIN decoded clean. Check Digit (9th position) is correct',
        'ForwardCollisionWarning': '',
        'FuelInjectionType': '',
        'FuelTypePrimary': '',
        'FuelTypeSecondary': '',
        'GVWR': 'Class 8: 33,001 lb and above (14,969 kg and above)',
        'LaneDepartureWarning': '',
        'LaneKeepSystem': '',
        'Make': 'KENWORTH',
        'Manufacturer': 'KENWORTH TRUCK COMPANY',
        'ManufacturerId': '1032',
        'ManufacturerType': '',
        'Model': 'W900',
        'ModelYear': '1996',
        'MotorcycleChassisType': '',
        'MotorcycleSuspensionType': '',
        'NCAPBodyType': '',
        'NCAPMake': '',
        'NCAPModel': '',
        'NCICCode': '',
        'NCSABodyType': '',
        'NCSAMake': '',
        'NCSAModel': '',
        'Note': '47,001-57,000 lbs.',
        'OtherBusInfo': '',
        'OtherEngineInfo': '',
        'OtherMotorcycleInfo': '',
        'OtherRestraintSystemInfo': '',
        'OtherTrailerInfo': '',
        'ParkAssist': '',
        'PlantCity': 'Renton',
        'PlantCompanyName': '',
        'PlantCountry': 'United States (USA)',
        'PlantState': 'Washington',
        'PossibleValues': '',
        'Pretensioner': '',
        'RearVisibilityCamera': '',
        'SeatBeltsAll': '',
        'SeatRows': '',
        'Seats': '',
        'Series': '',
        'Series2': '',
        'SteeringLocation': '',
        'SuggestedVIN': '',
        'TPMS': '',
        'TopSpeedMPH': '',
        'TrackWidth': '',
        'TractionControl': '',
        'TrailerBodyType': '',
        'TrailerLength': '',
        'TrailerType': '',
        'TransmissionSpeeds': '',
        'TransmissionStyle': '',
        'Trim': '',
        'Trim2': '',
        'Turbo': '',
        'VIN': '1XKWDB9X3TR727776',
        'ValveTrainDesign': '',
        'VehicleType': 'TRUCK ',
        'WheelBaseLong': '',
        'WheelBaseShort': '',
        'WheelBaseType': '',
        'WheelSizeFront': '',
        'WheelSizeRear': '',
        'Wheels': '',
        'Windows': ''
    },
    '1XKAP29XOTR723632': {
        'ABS': '',
        'AEB': '',
        'AdaptiveCruiseControl': '',
        'AdaptiveHeadlights': '',
        'AdditionalErrorText': '',
        'AirBagLocCurtain': '',
        'AirBagLocFront': '',
        'AirBagLocKnee': '',
        'AirBagLocSeatCushion': '',
        'AirBagLocSide': '',
        'Artemis': '',
        'AxleConfiguration': '',
        'Axles': '',
        'BasePrice': '',
        'BatteryA': '',
        'BatteryA_to': '',
        'BatteryCells': '',
        'BatteryInfo': '',
        'BatteryKWh': '',
        'BatteryKWh_to': '',
        'BatteryModules': '',
        'BatteryPacks': '',
        'BatteryType': '',
        'BatteryV': '',
        'BatteryV_to': '',
        'BedLengthIN': '',
        'BedType': '',
        'BlindSpotMon': '',
        'BodyCabType': 'MDHD: Conventional',
        'BodyClass': 'Truck - Tractor',
        'BrakeSystemDesc': '',
        'BrakeSystemType': 'Air',
        'BusFloorConfigType': '',
        'BusLength': '',
        'BusType': '',
        'CAFEBodyType': '',
        'CAFEMake': '',
        'CAFEModel': '',
        'CashForClunkers': '',
        'ChargerLevel': '',
        'ChargerPowerKW': '',
        'CoolingType': '',
        'Country': '',
        'CurbWeightLB': '',
        'CustomMotorcycleType': '',
        'DestinationMarket': '',
        'DisplacementCC': '',
        'DisplacementCI': '',
        'DisplacementL': '',
        'Doors': '',
        'DriveType': 'Other',
        'DriverAssist': '',
        'ESC': '',
        'EVDriveUnit': '',
        'ElectrificationLevel': '',
        'EngineConfiguration': '',
        'EngineCycles': '',
        'EngineCylinders': '',
        'EngineHP': '',
        'EngineHP_to': '',
        'EngineKW': '',
        'EngineManufacturer': 'Cummins ',
        'EngineModel': 'NT',
        'EntertainmentSystem': '',
        'EquipmentType': '',
        'ErrorCode': '1 - VIN decoded clean. Check Digit (9th position) does not calculate '
        'properly.',
        'ForwardCollisionWarning': '',
        'FuelInjectionType': '',
        'FuelTypePrimary': '',
        'FuelTypeSecondary': '',
        'GVWR': 'Class 8: 33,001 lb and above (14,969 kg and above)',
        'LaneDepartureWarning': '',
        'LaneKeepSystem': '',
        'Make': 'KENWORTH',
        'Manufacturer': 'KENWORTH TRUCK COMPANY',
        'ManufacturerId': '1032',
        'ManufacturerType': '',
        'Model': 'T600',
        'ModelYear': '1996',
        'MotorcycleChassisType': '',
        'MotorcycleSuspensionType': '',
        'NCAPBodyType': '',
        'NCAPMake': '',
        'NCAPModel': '',
        'NCICCode': '',
        'NCSABodyType': '',
        'NCSAMake': '',
        'NCSAModel': '',
        'Note': '47,001-57,000 lbs.',
        'OtherBusInfo': '',
        'OtherEngineInfo': '',
        'OtherMotorcycleInfo': '',
        'OtherRestraintSystemInfo': '',
        'OtherTrailerInfo': '',
        'ParkAssist': '',
        'PlantCity': 'Renton',
        'PlantCompanyName': '',
        'PlantCountry': 'United States (USA)',
        'PlantState': 'Washington',
        'PossibleValues': '',
        'Pretensioner': '',
        'RearVisibilityCamera': '',
        'SeatBeltsAll': '',
        'SeatRows': '',
        'Seats': '',
        'Series': '',
        'Series2': '',
        'SteeringLocation': '',
        'SuggestedVIN': '',
        'TPMS': '',
        'TopSpeedMPH': '',
        'TrackWidth': '',
        'TractionControl': '',
        'TrailerBodyType': '',
        'TrailerLength': '',
        'TrailerType': '',
        'TransmissionSpeeds': '',
        'TransmissionStyle': '',
        'Trim': '',
        'Trim2': '',
        'Turbo': '',
        'VIN': '1XKAP29XOTR723632',
        'ValveTrainDesign': '',
        'VehicleType': 'TRUCK ',
        'WheelBaseLong': '',
        'WheelBaseShort': '',
        'WheelBaseType': '',
        'WheelSizeFront': '',
        'WheelSizeRear': '',
        'Wheels': '',
        'Windows': ''
    },
    '1XKADB9X0MJ558312': {
        'ABS': '',
        'AEB': '',
        'AdaptiveCruiseControl': '',
        'AdaptiveHeadlights': '',
        'AdditionalErrorText': '',
        'AirBagLocCurtain': '',
        'AirBagLocFront': '',
        'AirBagLocKnee': '',
        'AirBagLocSeatCushion': '',
        'AirBagLocSide': '',
        'Artemis': '',
        'AxleConfiguration': '',
        'Axles': '',
        'BasePrice': '',
        'BatteryA': '',
        'BatteryA_to': '',
        'BatteryCells': '',
        'BatteryInfo': '',
        'BatteryKWh': '',
        'BatteryKWh_to': '',
        'BatteryModules': '',
        'BatteryPacks': '',
        'BatteryType': '',
        'BatteryV': '',
        'BatteryV_to': '',
        'BedLengthIN': '',
        'BedType': '',
        'BlindSpotMon': '',
        'BodyCabType': 'MDHD: Conventional',
        'BodyClass': 'Truck - Tractor',
        'BrakeSystemDesc': '',
        'BrakeSystemType': 'Air',
        'BusFloorConfigType': '',
        'BusLength': '',
        'BusType': '',
        'CAFEBodyType': '',
        'CAFEMake': '',
        'CAFEModel': '',
        'CashForClunkers': '',
        'ChargerLevel': '',
        'ChargerPowerKW': '',
        'CoolingType': '',
        'Country': '',
        'CurbWeightLB': '',
        'CustomMotorcycleType': '',
        'DestinationMarket': '',
        'DisplacementCC': '',
        'DisplacementCI': '',
        'DisplacementL': '',
        'Doors': '',
        'DriveType': '6x4',
        'DriverAssist': '',
        'ESC': '',
        'EVDriveUnit': '',
        'ElectrificationLevel': '',
        'EngineConfiguration': '',
        'EngineCycles': '',
        'EngineCylinders': '',
        'EngineHP': '',
        'EngineHP_to': '',
        'EngineKW': '',
        'EngineManufacturer': 'Caterpillar ',
        'EngineModel': '3406',
        'EntertainmentSystem': '',
        'EquipmentType': '',
        'ErrorCode': '0 - VIN decoded clean. Check Digit (9th position) is correct',
        'ForwardCollisionWarning': '',
        'FuelInjectionType': '',
        'FuelTypePrimary': '',
        'FuelTypeSecondary': '',
        'GVWR': 'Class 8: 33,001 lb and above (14,969 kg and above)',
        'LaneDepartureWarning': '',
        'LaneKeepSystem': '',
        'Make': 'KENWORTH',
        'Manufacturer': 'KENWORTH TRUCK COMPANY',
        'ManufacturerId': '1032',
        'ManufacturerType': '',
        'Model': 'T600',
        'ModelYear': '1991',
        'MotorcycleChassisType': '',
        'MotorcycleSuspensionType': '',
        'NCAPBodyType': '',
        'NCAPMake': '',
        'NCAPModel': '',
        'NCICCode': '',
        'NCSABodyType': '',
        'NCSAMake': '',
        'NCSAModel': '',
        'Note': '47,001-57,000 lbs.',
        'OtherBusInfo': '',
        'OtherEngineInfo': '',
        'OtherMotorcycleInfo': '',
        'OtherRestraintSystemInfo': '',
        'OtherTrailerInfo': '',
        'ParkAssist': '',
        'PlantCity': 'Chillicothe',
        'PlantCompanyName': '',
        'PlantCountry': 'United States (USA)',
        'PlantState': 'Ohio',
        'PossibleValues': '',
        'Pretensioner': '',
        'RearVisibilityCamera': '',
        'SeatBeltsAll': '',
        'SeatRows': '',
        'Seats': '',
        'Series': '',
        'Series2': '',
        'SteeringLocation': '',
        'SuggestedVIN': '',
        'TPMS': '',
        'TopSpeedMPH': '',
        'TrackWidth': '',
        'TractionControl': '',
        'TrailerBodyType': '',
        'TrailerLength': '',
        'TrailerType': '',
        'TransmissionSpeeds': '',
        'TransmissionStyle': '',
        'Trim': '',
        'Trim2': '',
        'Turbo': '',
        'VIN': '1XKADB9X0MJ558312',
        'ValveTrainDesign': '',
        'VehicleType': 'TRUCK ',
        'WheelBaseLong': '',
        'WheelBaseShort': '',
        'WheelBaseType': '',
        'WheelSizeFront': '',
        'WheelSizeRear': '',
        'Wheels': '',
        'Windows': ''
    },
    '1XKAD29XOVR944280': {
        'ABS': '',
        'AEB': '',
        'AdaptiveCruiseControl': '',
        'AdaptiveHeadlights': '',
        'AdditionalErrorText': '',
        'AirBagLocCurtain': '',
        'AirBagLocFront': '',
        'AirBagLocKnee': '',
        'AirBagLocSeatCushion': '',
        'AirBagLocSide': '',
        'Artemis': '',
        'AxleConfiguration': '',
        'Axles': '',
        'BasePrice': '',
        'BatteryA': '',
        'BatteryA_to': '',
        'BatteryCells': '',
        'BatteryInfo': '',
        'BatteryKWh': '',
        'BatteryKWh_to': '',
        'BatteryModules': '',
        'BatteryPacks': '',
        'BatteryType': '',
        'BatteryV': '',
        'BatteryV_to': '',
        'BedLengthIN': '',
        'BedType': '',
        'BlindSpotMon': '',
        'BodyCabType': '',
        'BodyClass': 'Truck - Tractor',
        'BrakeSystemDesc': '',
        'BrakeSystemType': 'Air',
        'BusFloorConfigType': '',
        'BusLength': '',
        'BusType': '',
        'CAFEBodyType': '',
        'CAFEMake': '',
        'CAFEModel': '',
        'CashForClunkers': '',
        'ChargerLevel': '',
        'ChargerPowerKW': '',
        'CoolingType': '',
        'Country': '',
        'CurbWeightLB': '',
        'CustomMotorcycleType': '',
        'DestinationMarket': '',
        'DisplacementCC': '',
        'DisplacementCI': '',
        'DisplacementL': '',
        'Doors': '',
        'DriveType': '6x4',
        'DriverAssist': '',
        'ESC': '',
        'EVDriveUnit': '',
        'ElectrificationLevel': '',
        'EngineConfiguration': '',
        'EngineCycles': '',
        'EngineCylinders': '',
        'EngineHP': '',
        'EngineHP_to': '',
        'EngineKW': '',
        'EngineManufacturer': 'Cummins ',
        'EngineModel': 'NT',
        'EntertainmentSystem': '',
        'EquipmentType': '',
        'ErrorCode': '1 - VIN decoded clean. Check Digit (9th position) does not calculate '
        'properly.',
        'ForwardCollisionWarning': '',
        'FuelInjectionType': '',
        'FuelTypePrimary': '',
        'FuelTypeSecondary': '',
        'GVWR': 'Class 8: 33,001 lb and above (14,969 kg and above)',
        'LaneDepartureWarning': '',
        'LaneKeepSystem': '',
        'Make': 'KENWORTH',
        'Manufacturer': 'KENWORTH TRUCK COMPANY',
        'ManufacturerId': '1032',
        'ManufacturerType': '',
        'Model': 'T6 Series',
        'ModelYear': '1997',
        'MotorcycleChassisType': '',
        'MotorcycleSuspensionType': '',
        'NCAPBodyType': '',
        'NCAPMake': '',
        'NCAPModel': '',
        'NCICCode': '',
        'NCSABodyType': '',
        'NCSAMake': '',
        'NCSAModel': '',
        'Note': '47,001-57,000 lbs.',
        'OtherBusInfo': '',
        'OtherEngineInfo': '',
        'OtherMotorcycleInfo': '',
        'OtherRestraintSystemInfo': '',
        'OtherTrailerInfo': '',
        'ParkAssist': '',
        'PlantCity': 'Renton',
        'PlantCompanyName': '',
        'PlantCountry': 'United States (USA)',
        'PlantState': 'Washington',
        'PossibleValues': '',
        'Pretensioner': '',
        'RearVisibilityCamera': '',
        'SeatBeltsAll': '',
        'SeatRows': '',
        'Seats': '',
        'Series': '',
        'Series2': '',
        'SteeringLocation': '',
        'SuggestedVIN': '',
        'TPMS': '',
        'TopSpeedMPH': '',
        'TrackWidth': '',
        'TractionControl': '',
        'TrailerBodyType': '',
        'TrailerLength': '',
        'TrailerType': '',
        'TransmissionSpeeds': '',
        'TransmissionStyle': '',
        'Trim': '',
        'Trim2': '',
        'Turbo': '',
        'VIN': '1XKAD29XOVR944280',
        'ValveTrainDesign': '',
        'VehicleType': 'TRUCK ',
        'WheelBaseLong': '',
        'WheelBaseShort': '',
        'WheelBaseType': '',
        'WheelSizeFront': '',
        'WheelSizeRear': '',
        'Wheels': '',
        'Windows': ''
    }
}


class FakeResponse(object):

    def __init__(self, status_code=200, results=None, exception=None):
        self.status_code = status_code
        self.results = results or []
        self.exception = exception

    def raise_for_status(self):
        if self.exception:
            raise self.exception()

    def json(self):
        return {
            'Count': len(self.results),
            'Message': 'Results returned successfully',
            'SearchCriteria': '',
            'Results': list(self.results),
        }


class VPicSingleTests(TestCase):

    @mock.patch('vpic.requests.post')
    def test_vin_lookup(self, mock_post):
        vin = '5FYD4FS147B031975'
        raw_data = fake_db[vin]
        mock_post.return_value = FakeResponse(results=[raw_data])
        v = vpic.vpic.lookup_vin(vin)
        self.assertIsInstance(v, vpic.models.Vehicle)
        self.assertEqual(v.make, raw_data['Make'])
        self.assertEqual(v.model, raw_data['Model'])
        self.assertEqual(v.model_year, raw_data['ModelYear'])
        mock_post.assert_called_once_with(vpic.VPicAPI.url, data={'DATA': vin, 'format': 'JSON'})


class VPicBulkTests(TestCase):

    @mock.patch('vpic.requests.post')
    def test_bulk_vin_lookup(self, mock_post):
        vins = list(fake_db.keys())
        mock_post.return_value = FakeResponse(results=[fake_db[k] for k in vins])
        vehicles = vpic.vpic.lookup_vins([{'vin': v} for v in vins])
        self.assertIsInstance(vehicles, list)
        self.assertEqual(len(vehicles), len(fake_db))
        mock_post.assert_called_once_with(
            vpic.VPicAPI.url, data={'DATA': ';'.join(vins), 'format': 'JSON'}
        )
        for v in vehicles:
            self.assertIsInstance(v, vpic.models.Vehicle)
            raw_data = fake_db[v.vin]
            self.assertEqual(v.make, raw_data['Make'].strip())
            self.assertEqual(v.model, raw_data['Model'].strip())
            self.assertEqual(v.model_year, raw_data['ModelYear'].strip())
