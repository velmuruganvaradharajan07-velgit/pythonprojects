import win32serviceutil
import win32service
import psutil
import time
import wmi
import pandas

def get_service_status(service_name):
    try:
        status = win32serviceutil.QueryServiceStatus(service_name)[1]
        status_map = {
            win32service.SERVICE_STOPPED: "Stopped",
            win32service.SERVICE_START_PENDING: "Start Pending",
            win32service.SERVICE_STOP_PENDING: "Stop Pending",
            win32service.SERVICE_RUNNING: "Running",
            win32service.SERVICE_CONTINUE_PENDING: "Continue Pending",
            win32service.SERVICE_PAUSE_PENDING: "Pause Pending",
            win32service.SERVICE_PAUSED: "Paused"
        }
        return status_map.get(status, "Unknown")
    except Exception as e:
        return f"Error: {e}"

def get_service_pid(service_name):
    try:
        c = wmi.WMI()
        for service in c.Win32_Service(Name=service_name):
            return service.ProcessId
    except Exception as e:
        print(f"Failed to get PID for service '{service_name}': {e}")
        return None

def monitor_multiple_services(service_names, interval=5):
    print(f"Monitoring CPU and memory usage for services: {', '.join(service_names)}")
    while True:
        for service_name in service_names:
            print(f"\n--- {service_name} ---")
            status = get_service_status(service_name)
            pid = get_service_pid(service_name)

            print(f"Service Status: {status}")

            if pid and pid != 0:
                try:
                    proc = psutil.Process(pid)
                    cpu_usage = proc.cpu_percent(interval=0.1)  # faster response
                    mem_info = proc.memory_info()
                    mem_usage_mb = mem_info.rss / (1024 * 1024)
                    print(f"PID: {pid}, CPU Usage: {cpu_usage:.2f}%, Memory Usage: {mem_usage_mb:.2f} MB")
                except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                    print(f"Could not access process with PID {pid}: {e}")
            else:
                print(f"Service '{service_name}' is not running or PID not found.")
        print("=" * 60)
        time.sleep(interval)

# Example usage
services_to_monitor = ["MIMSMonitoringService", "AbilityMACHConnectService", "AbilityMACHEventConnectService"]
monitor_multiple_services(services_to_monitor, interval=5)


# import psutil
#
# import time
#
# from datetime import datetime
#
# from openpyxl import Workbook, load_workbook
#
# import os
#
# # Define process names (adjust as needed)
#
# process_names = {
#
#     "Vtrin Service": "Vtrin Server",
#
#     "DTMP API": "DTMPAPI",
#
#     "Vtrin DB": "Vtrin.exe",         # Replace with actual DB process name
#
#     "pgAdmin": "postgres.exe"
#
# }
#
# excel_file = "detailed_service_metrics.xlsx"
#
# def get_process_metrics(proc_name):
#
#     cpu = 0.0
#
#     mem = 0.0
#
#     for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_info']):
#
#         try:
#
#             if proc.info['name'].lower() == proc_name.lower():
#
#                 cpu += proc.cpu_percent(interval=0.1)
#
#                 mem += proc.info['memory_info'].rss / (1024 * 1024)  # MB
#
#         except (psutil.NoSuchProcess, psutil.AccessDenied):
#
#             continue
#
#     return cpu, mem
#
# def write_to_excel(timestamp, metrics):
#
#     if not os.path.exists(excel_file):
#
#         wb = Workbook()
#
#         ws = wb.active
#
#         ws.title = "Service Metrics"
#
#         headers = ["Timestamp"]
#
#         for service in process_names:
#
#             headers.extend([f"{service} CPU (%)", f"{service} Memory (MB)"])
#
#         ws.append(headers)
#
#     else:
#
#         wb = load_workbook(excel_file)
#
#         ws = wb["Service Metrics"]
#
#     row = [timestamp]
#
#     for service in process_names:
#
#         cpu, mem = metrics.get(service, (0.0, 0.0))
#
#         row.extend([round(cpu, 2), round(mem, 2)])
#
#     ws.append(row)
#
#     wb.save(excel_file)
#
# if __name__ == "__main__":
#
#     while True:
#
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#         metrics = {}
#
#         for label, proc_name in process_names.items():
#
#             cpu, mem = get_process_metrics(proc_name)
#
#             metrics[label] = (cpu, mem)
#
#         write_to_excel(timestamp, metrics)
#
#         time.sleep(1)
#
#
