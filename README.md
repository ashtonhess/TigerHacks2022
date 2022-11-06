# Live Cryptocurrency Exchange Latencies from All AWS Datacenters Dashboard 
## Powered by 23 AWS EC2 Instances + Dell Poweredge to create 142 informative, real-time graphs.
### TigerHacks2022

# Purpose
To provide a live, comprehensive view of the latencies between all possible (23) AWS EC2 instance locations and cryptocurrency exchanges. This provides traders with a clear view of what location(s) are best for trading cryptocurrencies with low latency depending on the exchange they are using.

# Back End (24 seperate computers run the website, 23 EC2 instances and a Dell Poweredge Server)
### 23 AWS EC2 Instances
1. EC2 Instances at every possible location are constantly pinging multiple different cryptocurrency exchanges across the world. These latencies are then sent to our main server.
2. Our main server listens to messages from all 23 instances. This server handles sending the data to the front end.
3. Each instance is running Ubuntu release 22.04.
### Websockets
4. Websockets are used to communicate between each component.
### Dynamic DNS
5. Dynamic DNS is used to access our main server. It is currently using an old domain I had registered for another project, cuppong.hessdevelopments.com. Google DNS is used for this and CRON jobs on my router are being used to constantly update this domain so it can always be accessed.

# Front End
### Language and Framework
1. The front end was done using the framework Svelte. 
2. Languages include: Javascript, HTML, and CSS.
### Charting Library
3. Pancake library was used. This is a highly customizable and very barebones charting library. 
4. Using SVG lines, live data is easily mapped in and updated in real time on the screen.
### Live Cryptocurrency Data
5. Using free websockets provided by Binance, the top of our page includes 4 graphs showing prices of popular cryptocurrencies at the granularity of each trade. This is not a common form of granularity accessible to the public.


# To run:
For the time being, this is not a final product and not available to the public. Future plans include hosting this project for public use.
### Front end
1. install npm
2. cd to FrontEnd folder
3. run 'npm install'
4. run 'npm run dev'
### Back end
For each AWS Server:
1. install python3.10
2. pip install ccxt
3. pip install websockets
4. run 'python3 main.py'
For the Main Server:
1. install python 3.9
2. pip install websockets
3. run 'python3.9 MainServer.py'
