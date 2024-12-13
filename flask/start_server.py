import configparser
import subprocess

# Read the configuration file
config = configparser.ConfigParser()
config.read('app.ini')

# Extract values from the app.ini file
host, port = config['uwsgi'].get('http', '0.0.0.0:8080').split(':')
workers = config['uwsgi'].getint('processes', 1)
threads = config['uwsgi'].getint('threads', 1)
module = config['uwsgi'].get('module', 'app:app')

# Construct the Gunicorn command
command = [
    "gunicorn",
    f"--bind={host}:{port}",
    f"--workers={workers}",
    f"--threads={threads}",
    module
]

# Print the command (optional, for debugging)
print("Starting Gunicorn with command:", " ".join(command))

# Run the Gunicorn command
subprocess.run(command)
