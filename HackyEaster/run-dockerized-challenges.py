import os
import subprocess
import time
def run_docker_compose_up(root_dir):
    processes = []
    count = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file == 'docker-compose.yaml':
                compose_file = os.path.join(root, file)
                print(f"Found docker-compose file: {compose_file}")
                cmd = f"docker-compose -f {compose_file} up"
                print(f"Running command: {cmd}")
                p = subprocess.Popen(cmd, shell=True)
                processes.append(p)
                print(f"Started process with PID: {p.pid}")
                count += 1

    print(f"Triggered {count} docker-compose commands.")
    print("All docker-compose commands started. Waiting for them to complete...")
     # Wait for all processes to complete
    for p in processes:
        p.wait()
    print("All docker-compose commands completed.")

if __name__ == '__main__':
    root_dir = '/workspaces/CTFd/HackyEaster/2021/'   # replace with the path to the folder you want to search in
    start_time = time.time()
    run_docker_compose_up(root_dir)
    end_time = time.time()
    print(f"Script completed in {end_time - start_time:.2f} seconds")