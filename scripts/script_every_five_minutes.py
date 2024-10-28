import datetime

def main():
    # Get the current date and time
    now = datetime.datetime.now()

    # Log the current date and time to a file
    log_file = '/home/ec2-user/artifacts_python/logs/script_five_minutes.log'
    with open(log_file, 'a') as f:
        f.write(f"[{now}] script_every_five_minutes.py ran successfully.\n")

if __name__ == "__main__":
    main()
