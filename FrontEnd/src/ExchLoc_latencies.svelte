<script>
    import LineChart2 from "./Components/LineChart2.svelte";


   // <!-- let coinbase1_socket = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade'); -->
 
    let coins = ['']
    let exchange_count = 6;
    let exchanges = ['coinbase', 'coinbasepro', 'binance', 'binanceus', 'gemini', 'kraken']
    let locations_count = 23;
    let aws_locations = ['US East (N. Virginia): us-east-1', 'US East (Ohio): us-east-2', 'US West (N. California): us-west-1', 'US West (Oregon): us-west-2']
    let aws_location_category = ['US East', 'US East', 'US West', 'US West', 'Africa', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Asia Pacific', 'Canada', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Middle East', 'Middle East', 'South America']
    let aws_location_names = ['N. Virginia', 'Ohio', 'N. California', 'Oregon', 'Cape Town', 'Hong Kong', 'Jakarta', 'Mumbai', 'Osaka', 'Seoul', 'Singapore', 'Sydney', 'Tokyo', 'Central', 'Frankfurt', 'Ireland', 'London', 'Milan', 'Paris', 'Stockholm', 'Bahrain', 'UAE', 'Sao Paulo']
    let aws_location_code = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'af-south-1', 'ap-east-1', 'ap-southeast-1', 'ap-south-1', 'ap-northeast-3', 'ap-northeast-2','ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1','ca-central-1','eu-central-1', 'eu-west-1','eu-west-2','eu-south-1','eu-west-3','eu-north-1','me-south-1','me-central-1','sa-east-1']
    
    
    let socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');

    let all_x1 = []
    let x1_counter = 0;
    for(let i = 0; i < exchange_count; i++){
        for(let i = 0; i < locations_count; i++){
            all_x1[x1_counter] = +Infinity;
            x1_counter+=1;
        }
    }
    let all_x2 = []
    let x2_counter = 0;
    for(let i = 0; i < exchange_count; i++){
        for(let i = 0; i < locations_count; i++){
            all_x2[x2_counter] = -Infinity;
            x2_counter+=1;
        }
    }
    let all_y1 = []
    let y1_counter = 0;
    for(let i = 0; i < exchange_count; i++){
        for(let i = 0; i < locations_count; i++){
            all_y1[y1_counter] = +Infinity;
            y1_counter+=1;
        }
    }
    let all_y2 = []
    let y2_counter = 0;
    for(let i = 0; i < exchange_count; i++){
        for(let i = 0; i < locations_count; i++){
            all_y2[y2_counter] = -Infinity;
            y2_counter+=1;
        }
    }

    let all_data = [];
    let all_data_counter = 0;
    for(let i = 0; i < exchange_count; i++){
        for(let i = 0; i < locations_count; i++){
            all_data[all_data_counter] = []
            all_data_counter+=1;
        }
    }

    let coinbase1_x1 = +Infinity;
    let coinbase1_x2 = -Infinity;
    // let coinbase1_y1 = +Infinity;
    let coinbase1_y1 = 0;
    let coinbase1_y2 = -Infinity;
    let coinbase1_alldata = [];
    let coinbase1_current_price;

    var coinbase1_every_other_toggle = false;
    var coinbase1_every_other_tracker = 0;
    var coinbase1_get_nth_msg_to_get = 100;
    socket.onmessage = function (event) {
        console.log("MESSAGE RECEIVED:")
        console.log(event.data)
        var message = JSON.parse(event.data);
        console.log("From AWS Server: ")
        console.log(message)
        //all_data[location][exchange]


        // let data_dict = {'x':message['current_time'], 'y':parseFloat(message['coinbase'])}
        var coinbase1_data = JSON.parse(event.data);

        // console.log(coinbase1_data)
        // coinbase1_data = coinbase1_data['data'];
        let coinbase1_data_dict = {'x':coinbase1_data['current_time'], 'y':parseFloat(coinbase1_data['coinbase'])}
        // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
        if (coinbase1_data_dict.x>coinbase1_x2) coinbase1_x2 = coinbase1_data_dict.x;
        if (coinbase1_data_dict.x<coinbase1_x1) coinbase1_x1 = coinbase1_data_dict.x;
        if (coinbase1_data_dict.y>coinbase1_y2) coinbase1_y2 = coinbase1_data_dict.y;
        // Comment out next line for disabling lower Y bound. Setting to 0 seconds. This makes more sense for these charts.
        // if (coinbase1_data_dict.y<coinbase1_y1) coinbase1_y1 = coinbase1_data_dict.y;


        // if (coinbase1_x2-coinbase1_x1>60000) coinbase1_x1 = coinbase1_x2-60000
        if (coinbase1_x2-coinbase1_x1>86400000) coinbase1_x1 = coinbase1_x2-86400000;
        //store the last price received.
        coinbase1_current_price=coinbase1_data_dict.y;
        coinbase1_alldata.push(coinbase1_data_dict);
        coinbase1_alldata=[...coinbase1_alldata.filter(data => data.x > coinbase1_x1)]


        // if(coinbase1_every_other_toggle){
        //     if(coinbase1_every_other_tracker%coinbase1_get_nth_msg_to_get==0){
        //         var coinbase1_data = JSON.parse(event.data);
        //         console.log(coinbase1_data)
        //         let coinbase1_data_dict = {'x':coinbase1_data['current_time'], 'y':parseFloat(coinbase1_data['coinbase'])}
        //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
        //         if (coinbase1_data_dict.x>coinbase1_x2) coinbase1_x2 = coinbase1_data_dict.x;
        //         if (coinbase1_data_dict.x<coinbase1_x1) coinbase1_x1 = coinbase1_data_dict.x;
        //         if (coinbase1_data_dict.y>coinbase1_y2) coinbase1_y2 = coinbase1_data_dict.y;
        //         // Comment out next line for disabling lower Y bound. Setting to 0 seconds. This makes more sense for these charts.
        //         // if (coinbase1_data_dict.y<coinbase1_y1) coinbase1_y1 = coinbase1_data_dict.y;
                

        //         // if (coinbase1_x2-coinbase1_x1>60000) coinbase1_x1 = coinbase1_x2-60000
        //         if (coinbase1_x2-coinbase1_x1>86400000) coinbase1_x1 = coinbase1_x2-86400000;
                
        //         //store the last price received.
        //         coinbase1_current_price=coinbase1_data_dict.y;

        //         coinbase1_alldata.push(coinbase1_data_dict);
        //         coinbase1_alldata=[...coinbase1_alldata.filter(data => data.x > coinbase1_x1)]
        //         coinbase1_every_other_tracker+=1;
        //     }else{
        //         coinbase1_every_other_tracker+=1;
        //     }
        // }else{
        //     var coinbase1_data = JSON.parse(event.data);
        //     console.log(coinbase1_data)
        //     // coinbase1_data = coinbase1_data['data'];
        //     let coinbase1_data_dict = {'x':coinbase1_data['current_time'], 'y':parseFloat(coinbase1_data['coinbase'])}
        //     // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
        //     if (coinbase1_data_dict.x>coinbase1_x2) coinbase1_x2 = coinbase1_data_dict.x;
        //     if (coinbase1_data_dict.x<coinbase1_x1) coinbase1_x1 = coinbase1_data_dict.x;
        //     if (coinbase1_data_dict.y>coinbase1_y2) coinbase1_y2 = coinbase1_data_dict.y;
        //     // Comment out next line for disabling lower Y bound. Setting to 0 seconds. This makes more sense for these charts.
        //     // if (coinbase1_data_dict.y<coinbase1_y1) coinbase1_y1 = coinbase1_data_dict.y;


        //     // if (coinbase1_x2-coinbase1_x1>60000) coinbase1_x1 = coinbase1_x2-60000
        //     if (coinbase1_x2-coinbase1_x1>86400000) coinbase1_x1 = coinbase1_x2-86400000;
        //     //store the last price received.
        //     coinbase1_current_price=coinbase1_data_dict.y;
        //     coinbase1_alldata.push(coinbase1_data_dict);
        //     coinbase1_alldata=[...coinbase1_alldata.filter(data => data.x > coinbase1_x1)]
        //     // console.log(coinbase1_alldata[coinbase1_alldata.length-1]);
        // }
        
    }

    
    
</script>

<div class="chart-grid thirtyfiveXfour">
    <!-- {#each exchanges as exchange, e}
        <h1>{exchanges[e]}</h1>
    {/each} -->
    {#each aws_location_code as location, l}
    
        <!-- <h1>{exchanges[e]}</h1> -->
        {#each exchanges as exchange, e}
            <LineChart2 bind:data={coinbase1_alldata} bind:x1={coinbase1_x1} bind:x2={coinbase1_x2} bind:y1={coinbase1_y1} bind:y2={coinbase1_y2} bind:header={location} bind:header2={exchange} bind:current_price={coinbase1_current_price}/>
        {/each}
    {/each}
    <!-- <LineChart2 bind:data={coinbase2_alldata} bind:x1={coinbase2_x1} bind:x2={coinbase2_x2} bind:y1={coinbase2_y1} bind:y2={coinbase2_y2} bind:header={coins[0]} bind:current_price={coinbase2_current_price}/>
    <LineChart2 bind:data={coinbase3_alldata} bind:x1={coinbase3_x1} bind:x2={coinbase3_x2} bind:y1={coinbase3_y1} bind:y2={coinbase3_y2} bind:header={coins[0]} bind:current_price={coinbase3_current_price}/>
    <LineChart2 bind:data={coinbase4_alldata} bind:x1={coinbase4_x1} bind:x2={coinbase4_x2} bind:y1={coinbase4_y1} bind:y2={coinbase4_y2} bind:header={coins[0]} bind:current_price={coinbase4_current_price}/>
    <LineChart2 bind:data={coinbase5_alldata} bind:x1={coinbase5_x1} bind:x2={coinbase5_x2} bind:y1={coinbase5_y1} bind:y2={coinbase5_y2} bind:header={coins[0]} bind:current_price={coinbase5_current_price}/>
    <LineChart2 bind:data={coinbase6_alldata} bind:x1={coinbase6_x1} bind:x2={coinbase6_x2} bind:y1={coinbase6_y1} bind:y2={coinbase6_y2} bind:header={coins[0]} bind:current_price={coinbase6_current_price}/> -->


</div>


<style>
.chart-grid.thirtyfiveXfour { 
        display: grid;
        grid-template-rows: repeat(35, 1fr);  
        grid-template-columns: repeat(6, 1fr); 
        grid-column-gap: 5em;
        grid-row-gap: 75px; 
        padding-left: 4vw;
        padding-top: 10vh;
        
    }
</style>