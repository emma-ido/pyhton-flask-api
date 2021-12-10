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

 

**Notes:**

* You may use any programming language for this. Python seems like a good option however.
* Zip the project folder and submit on the appropriate slot on Canvas.
* The root of the project folder should contain a README with instructions on how to run your dockerized application. Your instructions can assume we already have docker installed.
* The root of the project folder should contain a folder called tests with screenshots showing calls to your APIs as well as the results returned. You could make the calls on the command-line using curl or using a tool like Postman or even the browser. The screenshot must show clearly what the request was and the response.

</br>

# Instructions
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
