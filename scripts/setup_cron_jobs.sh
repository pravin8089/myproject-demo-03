#!/bin/bash

# Remove existing cron jobs for the scripts
crontab -l | grep -v "/usr/bin/python3 /home/$USER/artifacts_python/scripts/script_every_minute.py" | crontab -
crontab -l | grep -v "/usr/bin/python3 /home/$USER/artifacts_python/scripts/script_every_five_minutes.py" | crontab -

# Schedule a cron job to run the specified script every minute
(crontab -l ; echo "* * * * * /usr/bin/python3 /home/$USER/artifacts_python/scripts/script_every_minute.py >> /home/$USER/artifacts_python/logs/script_every_minute.log 2>&1") | crontab -

# Schedule a cron job to run the specified script every 5 minutes
(crontab -l ; echo "*/5 * * * * /usr/bin/python3 /home/$USER/artifacts_python/scripts/script_every_five_minutes.py >> /home/$USER/artifacts_python/logs/script_every_five_minutes.log 2>&1") | crontab -

echo "Cron jobs have been set up."
