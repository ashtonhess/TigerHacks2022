# Live Cryptocurrency Exchange Latencies from All AWS Datacenters Dashboard

## TigerHacks2022

# Purpose
To provide a live, comprehensive view of the latencies between all possible (23) AWS EC2 instance locations and cryptocurrency exchanges. This provides traders with a clear view of what location(s) are best for trading cryptocurrencies with low latency depending on the exchange they are using.

# Back End (24 seperate computers run our website, 23 EC2 instances and a Dell Poweredge Server
### 23 AWS EC2 Instances
1. EC2 Instances at every possible location are constantly pinging multiple different cryptocurrency exchanges across the world. These latencies are then sent to our main server.
2. Our main server listens to messages from all 23 instances. This server handles sending the data to the front end.
### Websockets
3. Websockets are used to communicate between each piece. 
### Dynamic DNS
4. Dynamic DNS is used to access our main server. It is currently using an old domain I had registered for another project, cuppong.hessdevelopments.com. Google DNS is used for this and CRON jobs on my router are being used to constantly update this domain so it can always be accessed.

# Front End
### Language and Framework
1. The front end was done using the framework Svelte. 
2. Languages include: Javascript, HTML, and CSS
### Charting Library
3. Pancake library was used. This is a highly customizable and very barebones charting library. 
4. Using SVG lines, live data is easily mapped in and updated in real time on the screen.
### Live Cryptocurrency Data
5. Using free websockets provided by Binance, the top of our page includes 4 graphs showing prices of popular cryptocurrencies at the granularity of each trade. This is not a common form of granularity accessible to the public.


# To run:
For the time being, this is not finished and not available to the public. Future plans include hosting this project for the public. 
### Front end
1. install npm
2. cd to FrontEnd folder
3. run 'npm install'
4. run 'npm run dev'

