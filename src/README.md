# File Descriptions
Execute "run.sh" to deploy all servers to edlab machines. Before running the script, please update "username" to your account and make sure that the "targetPath" under each SSH sections are correct.

Please also make sure that port numbers on each edlab machine are available, otherwise the server may not be deployed properly. To update port numbers, please modify config.json.

You can change the number of clients by modifying "client_numbers" in config.json. The client.py will based on the variable to allocate threads for running as different clients. The variable "folder_path" under "log_path" allows you to change the directory path for storing logs. The default location is under "tests/" folder.

To terminate this program, you can use "terminate.sh" to kill all processes run by this program on edlab machines.

Execution:
- run.sh
- terminate.sh

Global config:
- config.json

Frontend tier:
- frontend.py
- define_frontend.json

Backend tier:
- catalog_server.py
- catalog.csv
- order_server.py

Client:
- client.py

Evaluation:
- evaluate.py
