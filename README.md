# 677 Lab 2

This is the Git repo for 677 Lab 2. See https://marcoserafini.github.io/teaching/distributed-os/spring20/labs/lab2.html for a description of the lab. The lab is due on Apr 6th, 11:59 pm. Prior to submitting your project, replace this README file with the one that explains how to setup and run your code. Be sure to provide enough details fo us to run it in order to grade it.
---
### Setup
Please make sure below settings are correct:
- In "src/run.sh", update "username" to your account and make sure that the "targetPath" under each SSH sections are correct.
- In "src/config.json", make sure that port numbers on each edlab machine are available. Otherwise, those servers may not be deployed. By default, the frontend server, the catalog server, the order server and the client are deploy on elnux1, elnux2, elnux7 and elnux3 respectively. Please change "addr" and "port" under "ip" as you need.
- (Optional) You can change the number of clients by modifying "client_numbers" in config.json. The client.py will based on the variable to allocate threads for running as different clients. The variable "folder_path" under "log_path" allows you to change the directory path for storing logs. The default location is under "tests/" folder.

### Execution
If above settings are set correctly, simply execute "run.sh" to deploy all servers to edlab machines.

To terminate this program and all servers, use "terminate.sh" to kill all processes run by this program on edlab machines.