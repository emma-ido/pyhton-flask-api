# Project Prompt
Develop and deploy a web application using docker. The web application must provide the following APIs:

1. `/permissions?code=<number>`
This API method accepts a code given by number and returns a JSON object specifying the permissions represented for owner, group and other. E.g.,

        The request /permissions?code=744 

        should return:

        {owner: [read, write, execute], group [read], other:[read]}

</br>
 

2. `/parity?b1=<bits>&b2=<bits>&b3=<bits>&b4=<bits>` This API method accepts the bits on corresponding disk blocks of a RAID-4 and returns the parity bits. Assume that each block has two bits. E.g., 

        The request /parity?b1=00&b2=10&b3=11&b4=10 

        should return:

        11

 

</br>

# Set up instructions
  **Assuming you already have Docker installed**

i.   Open the command line in the path of this project's folder

ii.  Run the command: 
	`docker-compose up`</br>
	**MOVE to step (iii) when an output similar to the following is shown:**
	
    Running on http://172.18.0.2:5000/ (Press CTRL+C to quit)
		Restarting with stat
		Debugger is active!
		Debugger PIN: xxx-xxx-xxx

iii. Go to `http://localhost:5000/permissions?code=<number>`
	OR `http://localhost:5000//parity?b1=00&b2=10&b3=11&b4=10` and use the various api methods.
