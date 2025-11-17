import win32serviceutil
import win32service
def MIMS_restart():
    service_name = "MIMS API"
    try:
        #service_name="MIMS API"
        win32serviceutil.RestartService(service_name)
        print(f"Service '{service_name}' restarted successfully.")
    except Exception as e:
        print(f"Error restarting service '{service_name}': {e}")


def DTMP_restart():
    try:
        service_name="DTMP API"
        win32serviceutil.RestartService(service_name)
        print(f"Service '{service_name}' restarted successfully.")
    except Exception as e:
        print(f"Error restarting service '{service_name}': {e}")
def VTrin_restart():
    try:
        service_name="Vtrin Server"
        win32serviceutil.RestartService(service_name)
        print(f"Service '{service_name}' restarted successfully.")
    except Exception as e:
        print(f"Error restarting service '{service_name}': {e}")

def Postgres_restart():
    try:
        service_name="Postgres"
        win32serviceutil.RestartService(service_name)
        print(f"Service '{service_name}' restarted successfully.")
    except Exception as e:
        print(f"Error restarting service '{service_name}': {e}")

def RTDB_Service_1_restart():
    try:
        service_name="RTDB C:\RTDBData"
        win32serviceutil.RestartService(service_name)
        print(f"Service '{service_name}' restarted successfully.")
    except Exception as e:
        print(f"Error restarting service '{service_name}': {e}")
def  RTDB_Service_2_restart():
    try:
        service_name="RTDB CalcService C RTDBData"
        win32serviceutil.RestartService(service_name)
        print(f"Service '{service_name}' restarted successfully.")
    except Exception as e:
        print(f"Error restarting service '{service_name}': {e}")
def  RTDB_Service_3_restart():
    try:
        service_name="RTDB-CVMCServer C:\RTDBData"
        win32serviceutil.RestartService(service_name)
        print(f"Service '{service_name}' restarted successfully.")
    except Exception as e:
        print(f"Error restarting service '{service_name}': {e}")

def  RTDB_Service_4_restart():
    try:
        service_name="RTDB-EcPerfMon C:\RTDBData"
        win32serviceutil.RestartService(service_name)
        print(f"Service '{service_name}' restarted successfully.")
    except Exception as e:
        print(f"Error restarting service '{service_name}': {e}")


def check_service_status(service_name):
    try:
        # Query the service status.
        # It returns a tuple, where the second element is the state.
        status_tuple = win32serviceutil.QueryServiceStatus(service_name)

        # The second element of the tuple corresponds to the service's state.
        # We can compare it with predefined constants.
        service_state = status_tuple[1]

        if service_state == win32service.SERVICE_RUNNING:
            print( "running")
        elif service_state == win32service.SERVICE_STOPPED:
            return "stopped"
        elif service_state == win32service.SERVICE_START_PENDING:
            return "start pending"
        elif service_state == win32service.SERVICE_STOP_PENDING:
            return "stop pending"
        else:
            return "unknown"

    except Exception as e:l
        print(f"Error checking service status: {e}")
        return "error"




print(check_service_status("MIMS API"))
MIMS_restart()
DTMP_restart()
VTrin_restart()
Postgres_restart()
RTDB_Service_1_restart()
RTDB_Service_2_restart()
RTDB_Service_3_restart()
RTDB_Service_4_restart()



a= f""" DO $$
DECLARE fixed_instance UUID := {c};
DECLARE fixed_equipmentname TEXT := {d};
DECLARE fixed_equipmenttype TEXT := {e};
BEGIN
   INSERT INTO transformersignal ("SignalName", "EquipmentName", "EquipmentType" ,"InstanceId", "ParameterId")
   VALUES 
   -- Input Signals
   ('HotspotFibreObticTemperature1', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 96),
    ('HotspotFibreObticTemperature2', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 97),
    ('HotspotFibreObticTemperature3', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 98),
 
   ('HotspotFibreObticTemperature1_Flag', fixed_equipmentname, fixed_equipmenttype,  fixed_instance,  99),
   ('HotspotFibreObticTemperature2_Flag', fixed_equipmentname, fixed_equipmenttype,  fixed_instance,  100),
   ('HotspotFibreObticTemperature3_Flag', fixed_equipmentname, fixed_equipmenttype,  fixed_instance,  101),
 
  ('TransformerCharged', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 102),
   -- Output Signals
   ('state.x', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 103),
   ('state.y', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 104),
   ('Condition', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 109),
   ('firstPhase.condition', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 106),
   ('secondPhase.condition', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 107),
   ('thirdPhase.condition', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 108),
   ('DeviatingPhases', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 105);
 
END $$;"""



































DO $$
DECLARE fixed_instance UUID := 'c22c8e5b-ef2b-418f-8a1b-f7238b605165';
DECLARE fixed_equipmentname TEXT := 'TransformerGroup_1000_TapChangerTemperatureSupervision';
DECLARE fixed_equipmenttype TEXT := 'TapChangerTemperatureSupervision';
BEGIN
   INSERT INTO transformersignal ("SignalName", "EquipmentName", "EquipmentType" ,"InstanceId", "ParameterId")
   VALUES
   -- Input Signals
   ('TopOilTemperature1', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 96),
   ('TapChangerTemperature1', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 97),
   ('TopOilTemperature2', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 98),
   ('TapChangerTemperature2', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 97),
   ('TopOilTemperature3', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 97),
   ('TapChangerTemperature3', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 97),
   ('TopOilTemperature1_Flag', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 96),
   ('TapChangerTemperature1_Flag', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 97),
   ('TopOilTemperature2_Flag', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 98),
   ('TapChangerTemperature2_Flag', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 97),
   ('TopOilTemperature3_Flag', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 97),
   ('TapChangerTemperature3_Flag', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 97),
   ('TransformerCharged', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 102),
   -- Output Signals
   ('state.x', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 103),
   ('state.y', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 104),
   ('Condition', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 109),
   ('DeviatingPhases', fixed_equipmentname, fixed_equipmenttype,  fixed_instance, 105);

END $$;