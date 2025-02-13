import subprocess
import time

def start_service(file_name, port):
    """
    Starts a Python service in a new subprocess.
    """
    print(f"Starting {file_name} on port {port}...")
    return subprocess.Popen(["python", file_name])

def main():
    print("Initializing Recommendation Microservices...")
    
    # Define services with file names and their ports
    services = [
        ("user_service.py", 5001),
        ("item_service.py", 5002),
        ("rating_service.py", 5003),
        ("recommondation_model_service.py", 5004),
        ("recommend_to_user_service.py", 5005),
    ]
    
    # Start all services
    processes = [start_service(service[0], service[1]) for service in services]
    
    print("All services started successfully.")
    
    # Keep the main process running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down services...")
        for process in processes:
            process.terminate()
            process.wait()
        print("All services stopped.")

if __name__ == "__main__":
    main()
