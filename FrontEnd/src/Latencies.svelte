<script>
    import LineChart2 from "./Components/LineChart2.svelte";


   // <!-- let coinbase1_socket = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade'); -->
 
    let coins = ['']

    let coinbase1_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    let coinbase1_x1 = +Infinity;
    let coinbase1_x2 = -Infinity;
    let coinbase1_y1 = +Infinity;
    let coinbase1_y2 = -Infinity;
    let coinbase1_alldata = [];
    let coinbase1_current_price;

    var coinbase1_every_other_toggle = false;
    var coinbase1_every_other_tracker = 0;
    var coinbase1_get_nth_msg_to_get = 100;
    coinbase1_socket.onmessage = function (event) {
        console.log("MESSAGE")
        console.log(event.data)
        if(coinbase1_every_other_toggle){
            if(coinbase1_every_other_tracker%coinbase1_get_nth_msg_to_get==0){
                var coinbase1_data = JSON.parse(event.data);
                console.log(coinbase1_data)
                let coinbase1_data_dict = {'x':coinbase1_data['current_time'], 'y':parseFloat(coinbase1_data['coinbase'])}
                // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
                if (coinbase1_data_dict.x>coinbase1_x2) coinbase1_x2 = coinbase1_data_dict.x;
                if (coinbase1_data_dict.x<coinbase1_x1) coinbase1_x1 = coinbase1_data_dict.x;
                if (coinbase1_data_dict.y>coinbase1_y2) coinbase1_y2 = coinbase1_data_dict.y;
                if (coinbase1_data_dict.y<coinbase1_y1) coinbase1_y1 = coinbase1_data_dict.y;
                // if (coinbase1_x2-coinbase1_x1>60000) coinbase1_x1 = coinbase1_x2-60000
                if (coinbase1_x2-coinbase1_x1>86400000) coinbase1_x1 = coinbase1_x2-86400000;
                
                //store the last price received.
                coinbase1_current_price=coinbase1_data_dict.y;

                coinbase1_alldata.push(coinbase1_data_dict);
                coinbase1_alldata=[...coinbase1_alldata.filter(data => data.x > coinbase1_x1)]
                coinbase1_every_other_tracker+=1;
            }else{
                coinbase1_every_other_tracker+=1;
            }
        }else{
            var coinbase1_data = JSON.parse(event.data);
            console.log(coinbase1_data)
            // coinbase1_data = coinbase1_data['data'];
            let coinbase1_data_dict = {'x':coinbase1_data['current_time'], 'y':parseFloat(coinbase1_data['coinbase'])}
            // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
            if (coinbase1_data_dict.x>coinbase1_x2) coinbase1_x2 = coinbase1_data_dict.x;
            if (coinbase1_data_dict.x<coinbase1_x1) coinbase1_x1 = coinbase1_data_dict.x;
            if (coinbase1_data_dict.y>coinbase1_y2) coinbase1_y2 = coinbase1_data_dict.y;
            if (coinbase1_data_dict.y<coinbase1_y1) coinbase1_y1 = coinbase1_data_dict.y;
            // if (coinbase1_x2-coinbase1_x1>60000) coinbase1_x1 = coinbase1_x2-60000
            if (coinbase1_x2-coinbase1_x1>86400000) coinbase1_x1 = coinbase1_x2-86400000;
            //store the last price received.
            coinbase1_current_price=coinbase1_data_dict.y;
            coinbase1_alldata.push(coinbase1_data_dict);
            coinbase1_alldata=[...coinbase1_alldata.filter(data => data.x > coinbase1_x1)]
            // console.log(coinbase1_alldata[coinbase1_alldata.length-1]);
        }
        
    }

    
    
</script>

<div class="chart-grid oneXfour">
    <LineChart2 bind:data={coinbase1_alldata} bind:x1={coinbase1_x1} bind:x2={coinbase1_x2} bind:y1={coinbase1_y1} bind:y2={coinbase1_y2} bind:header={coins[0]} bind:current_price={coinbase1_current_price}/>
    <!-- <LineChart2 bind:data={coinbase2_alldata} bind:x1={coinbase2_x1} bind:x2={coinbase2_x2} bind:y1={coinbase2_y1} bind:y2={coinbase2_y2} bind:header={coins[0]} bind:current_price={coinbase2_current_price}/>
    <LineChart2 bind:data={coinbase3_alldata} bind:x1={coinbase3_x1} bind:x2={coinbase3_x2} bind:y1={coinbase3_y1} bind:y2={coinbase3_y2} bind:header={coins[0]} bind:current_price={coinbase3_current_price}/>
    <LineChart2 bind:data={coinbase4_alldata} bind:x1={coinbase4_x1} bind:x2={coinbase4_x2} bind:y1={coinbase4_y1} bind:y2={coinbase4_y2} bind:header={coins[0]} bind:current_price={coinbase4_current_price}/>
    <LineChart2 bind:data={coinbase5_alldata} bind:x1={coinbase5_x1} bind:x2={coinbase5_x2} bind:y1={coinbase5_y1} bind:y2={coinbase5_y2} bind:header={coins[0]} bind:current_price={coinbase5_current_price}/>
    <LineChart2 bind:data={coinbase6_alldata} bind:x1={coinbase6_x1} bind:x2={coinbase6_x2} bind:y1={coinbase6_y1} bind:y2={coinbase6_y2} bind:header={coins[0]} bind:current_price={coinbase6_current_price}/> -->


</div>


<style>
.chart-grid.oneXfour { 
        display: grid;
        grid-template-rows: repeat(35, 1fr);  
        grid-template-columns: repeat(4, 1fr); 
        grid-column-gap: 5em;
        grid-row-gap: 75px; 
        padding-left: 4vw;
        padding-top: 10vh;
        
    }
</style>




<!-- // // let coinbase2_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbase2_x1 = +Infinity;
    // let coinbase2_x2 = -Infinity;
    // let coinbase2_y1 = +Infinity;
    // let coinbase2_y2 = -Infinity;
    // let coinbase2_alldata = [];
    // let coinbase2_current_price;

    // var coinbase2_every_other_toggle = true;
    // var coinbase2_every_other_tracker = 0;
    // var coinbase2_get_nth_msg_to_get = 100;
    // coinbase2_socket.onmessage = function (event) {
    //     if(coinbase2_every_other_toggle){
    //         if(coinbase2_every_other_tracker%coinbase2_get_nth_msg_to_get==0){
    //             var coinbase2_data = JSON.parse(event.data);
    //             let coinbase2_data_dict = {'x':coinbase2_data['E'], 'y':parseFloat(coinbase2_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbase2_data_dict.x>coinbase2_x2) coinbase2_x2 = coinbase2_data_dict.x;
    //             if (coinbase2_data_dict.x<coinbase2_x1) coinbase2_x1 = coinbase2_data_dict.x;
    //             if (coinbase2_data_dict.y>coinbase2_y2) coinbase2_y2 = coinbase2_data_dict.y;
    //             if (coinbase2_data_dict.y<coinbase2_y1) coinbase2_y1 = coinbase2_data_dict.y;
    //             // if (coinbase2_x2-coinbase2_x1>60000) coinbase2_x1 = coinbase2_x2-60000
    //             if (coinbase2_x2-coinbase2_x1>86400000) coinbase2_x1 = coinbase2_x2-86400000;
                
    //             //store the last price received.
    //             coinbase2_current_price=coinbase2_data_dict.y;

    //             coinbase2_alldata.push(coinbase2_data_dict);
    //             coinbase2_alldata=[...coinbase2_alldata.filter(data => data.x > coinbase2_x1)]
    //             coinbase2_every_other_tracker+=1;
    //         }else{
    //             coinbase2_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbase2_data = JSON.parse(event.data);
    //         let coinbase2_data_dict = {'x':coinbase2_data['current_price'], 'y':parseFloat(coinbase2_data['coinbase'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbase2_data_dict.x>coinbase2_x2) coinbase2_x2 = coinbase2_data_dict.x;
    //         if (coinbase2_data_dict.x<coinbase2_x1) coinbase2_x1 = coinbase2_data_dict.x;
    //         if (coinbase2_data_dict.y>coinbase2_y2) coinbase2_y2 = coinbase2_data_dict.y;
    //         if (coinbase2_data_dict.y<coinbase2_y1) coinbase2_y1 = coinbase2_data_dict.y;
    //         // if (coinbase2_x2-coinbase2_x1>60000) coinbase2_x1 = coinbase2_x2-60000
    //         if (coinbase2_x2-coinbase2_x1>86400000) coinbase2_x1 = coinbase2_x2-86400000;
    //         //store the last price received.
    //         coinbase2_current_price=coinbase2_data_dict.x;
    //         coinbase2_alldata.push(coinbase2_data_dict);
    //         coinbase2_alldata=[...coinbase2_alldata.filter(data => data.x > coinbase2_x1)]
    //         // console.log(coinbase2_alldata[coinbase2_alldata.length-1]);
    //     }
        
    // }

    // // let coinbase3_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbase3_x1 = +Infinity;
    // let coinbase3_x2 = -Infinity;
    // let coinbase3_y1 = +Infinity;
    // let coinbase3_y2 = -Infinity;
    // let coinbase3_alldata = [];
    // let coinbase3_current_price;

    // var coinbase3_every_other_toggle = true;
    // var coinbase3_every_other_tracker = 0;
    // var coinbase3_get_nth_msg_to_get = 100;
    // coinbase3_socket.onmessage = function (event) {
    //     if(coinbase3_every_other_toggle){
    //         if(coinbase3_every_other_tracker%coinbase3_get_nth_msg_to_get==0){
    //             var coinbase3_data = JSON.parse(event.data);
    //             let coinbase3_data_dict = {'x':coinbase3_data['current_time'], 'y':parseFloat(coinbase3_data['coinbase'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbase3_data_dict.x>coinbase3_x2) coinbase3_x2 = coinbase3_data_dict.x;
    //             if (coinbase3_data_dict.x<coinbase3_x1) coinbase3_x1 = coinbase3_data_dict.x;
    //             if (coinbase3_data_dict.y>coinbase3_y2) coinbase3_y2 = coinbase3_data_dict.y;
    //             if (coinbase3_data_dict.y<coinbase3_y1) coinbase3_y1 = coinbase3_data_dict.y;
    //             // if (coinbase3_x2-coinbase3_x1>60000) coinbase3_x1 = coinbase3_x2-60000
    //             if (coinbase3_x2-coinbase3_x1>86400000) coinbase3_x1 = coinbase3_x2-86400000;
                
    //             //store the last price received.
    //             coinbase3_current_price=coinbase3_data_dict.y;

    //             coinbase3_alldata.push(coinbase3_data_dict);
    //             coinbase3_alldata=[...coinbase3_alldata.filter(data => data.x > coinbase3_x1)]
    //             coinbase3_every_other_tracker+=1;
    //         }else{
    //             coinbase3_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbase3_data = JSON.parse(event.data);
    //         let coinbase3_data_dict = {'x':coinbase3_data['current_time'], 'y':parseFloat(coinbase3_data['coinbase'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbase3_data_dict.x>coinbase3_x2) coinbase3_x2 = coinbase3_data_dict.x;
    //         if (coinbase3_data_dict.x<coinbase3_x1) coinbase3_x1 = coinbase3_data_dict.x;
    //         if (coinbase3_data_dict.y>coinbase3_y2) coinbase3_y2 = coinbase3_data_dict.y;
    //         if (coinbase3_data_dict.y<coinbase3_y1) coinbase3_y1 = coinbase3_data_dict.y;
    //         // if (coinbase3_x2-coinbase3_x1>60000) coinbase3_x1 = coinbase3_x2-60000
    //         if (coinbase3_x2-coinbase3_x1>86400000) coinbase3_x1 = coinbase3_x2-86400000;
    //         //store the last price received.
    //         coinbase3_current_price=coinbase3_data_dict.x;
    //         coinbase3_alldata.push(coinbase3_data_dict);
    //         coinbase3_alldata=[...coinbase3_alldata.filter(data => data.x > coinbase3_x1)]
    //         // console.log(coinbase3_alldata[coinbase3_alldata.length-1]);
    //     }
        
    // }

    // // let coinbase4_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbase4_x1 = +Infinity;
    // let coinbase4_x2 = -Infinity;
    // let coinbase4_y1 = +Infinity;
    // let coinbase4_y2 = -Infinity;
    // let coinbase4_alldata = [];
    // let coinbase4_current_price;

    // var coinbase4_every_other_toggle = true;
    // var coinbase4_every_other_tracker = 0;
    // var coinbase4_get_nth_msg_to_get = 100;
    // coinbase4_socket.onmessage = function (event) {
    //     if(coinbase4_every_other_toggle){
    //         if(coinbase4_every_other_tracker%coinbase4_get_nth_msg_to_get==0){
    //             var coinbase4_data = JSON.parse(event.data);
    //             let coinbase4_data_dict = {'x':coinbase4_data['current_time'], 'y':parseFloat(coinbase4_data['coinbase'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbase4_data_dict.x>coinbase4_x2) coinbase4_x2 = coinbase4_data_dict.x;
    //             if (coinbase4_data_dict.x<coinbase4_x1) coinbase4_x1 = coinbase4_data_dict.x;
    //             if (coinbase4_data_dict.y>coinbase4_y2) coinbase4_y2 = coinbase4_data_dict.y;
    //             if (coinbase4_data_dict.y<coinbase4_y1) coinbase4_y1 = coinbase4_data_dict.y;
    //             // if (coinbase4_x2-coinbase4_x1>60000) coinbase4_x1 = coinbase4_x2-60000
    //             if (coinbase4_x2-coinbase4_x1>86400000) coinbase4_x1 = coinbase4_x2-86400000;
                
    //             //store the last price received.
    //             coinbase4_current_price=coinbase4_data_dict.y;

    //             coinbase4_alldata.push(coinbase4_data_dict);
    //             coinbase4_alldata=[...coinbase4_alldata.filter(data => data.x > coinbase4_x1)]
    //             coinbase4_every_other_tracker+=1;
    //         }else{
    //             coinbase4_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbase4_data = JSON.parse(event.data);
    //         let coinbase4_data_dict = {'x':coinbase4_data['current_time'], 'y':parseFloat(coinbase4_data['coinbase'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbase4_data_dict.x>coinbase4_x2) coinbase4_x2 = coinbase4_data_dict.x;
    //         if (coinbase4_data_dict.x<coinbase4_x1) coinbase4_x1 = coinbase4_data_dict.x;
    //         if (coinbase4_data_dict.y>coinbase4_y2) coinbase4_y2 = coinbase4_data_dict.y;
    //         if (coinbase4_data_dict.y<coinbase4_y1) coinbase4_y1 = coinbase4_data_dict.y;
    //         // if (coinbase4_x2-coinbase4_x1>60000) coinbase4_x1 = coinbase4_x2-60000
    //         if (coinbase4_x2-coinbase4_x1>86400000) coinbase4_x1 = coinbase4_x2-86400000;
    //         //store the last price received.
    //         coinbase4_current_price=coinbase4_data_dict.x;
    //         coinbase4_alldata.push(coinbase4_data_dict);
    //         coinbase4_alldata=[...coinbase4_alldata.filter(data => data.x > coinbase4_x1)]
    //         // console.log(coinbase4_alldata[coinbase4_alldata.length-1]);
    //     }
        
    // }

    // // let coinbase5_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbase5_x1 = +Infinity;
    // let coinbase5_x2 = -Infinity;
    // let coinbase5_y1 = +Infinity;
    // let coinbase5_y2 = -Infinity;
    // let coinbase5_alldata = [];
    // let coinbase5_current_price;

    // var coinbase5_every_other_toggle = true;
    // var coinbase5_every_other_tracker = 0;
    // var coinbase5_get_nth_msg_to_get = 100;
    // coinbase5_socket.onmessage = function (event) {
    //     if(coinbase5_every_other_toggle){
    //         if(coinbase5_every_other_tracker%coinbase5_get_nth_msg_to_get==0){
    //             var coinbase5_data = JSON.parse(event.data);
    //             let coinbase5_data_dict = {'x':coinbase5_data['current_time'], 'y':parseFloat(coinbase5_data['coinbase'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbase5_data_dict.x>coinbase5_x2) coinbase5_x2 = coinbase5_data_dict.x;
    //             if (coinbase5_data_dict.x<coinbase5_x1) coinbase5_x1 = coinbase5_data_dict.x;
    //             if (coinbase5_data_dict.y>coinbase5_y2) coinbase5_y2 = coinbase5_data_dict.y;
    //             if (coinbase5_data_dict.y<coinbase5_y1) coinbase5_y1 = coinbase5_data_dict.y;
    //             // if (coinbase5_x2-coinbase5_x1>60000) coinbase5_x1 = coinbase5_x2-60000
    //             if (coinbase5_x2-coinbase5_x1>86400000) coinbase5_x1 = coinbase5_x2-86400000;
                
    //             //store the last price received.
    //             coinbase5_current_price=coinbase5_data_dict.y;

    //             coinbase5_alldata.push(coinbase5_data_dict);
    //             coinbase5_alldata=[...coinbase5_alldata.filter(data => data.x > coinbase5_x1)]
    //             coinbase5_every_other_tracker+=1;
    //         }else{
    //             coinbase5_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbase5_data = JSON.parse(event.data);
    //         let coinbase5_data_dict = {'x':coinbase5_data['current_time'], 'y':parseFloat(coinbase5_data['coinbase'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbase5_data_dict.x>coinbase5_x2) coinbase5_x2 = coinbase5_data_dict.x;
    //         if (coinbase5_data_dict.x<coinbase5_x1) coinbase5_x1 = coinbase5_data_dict.x;
    //         if (coinbase5_data_dict.y>coinbase5_y2) coinbase5_y2 = coinbase5_data_dict.y;
    //         if (coinbase5_data_dict.y<coinbase5_y1) coinbase5_y1 = coinbase5_data_dict.y;
    //         // if (coinbase5_x2-coinbase5_x1>60000) coinbase5_x1 = coinbase5_x2-60000
    //         if (coinbase5_x2-coinbase5_x1>86400000) coinbase5_x1 = coinbase5_x2-86400000;
    //         //store the last price received.
    //         coinbase5_current_price=coinbase5_data_dict.x;
    //         coinbase5_alldata.push(coinbase5_data_dict);
    //         coinbase5_alldata=[...coinbase5_alldata.filter(data => data.x > coinbase5_x1)]
    //         // console.log(coinbase5_alldata[coinbase5_alldata.length-1]);
    //     }
        
    // }

    // // let coinbase6_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbase6_x1 = +Infinity;
    // let coinbase6_x2 = -Infinity;
    // let coinbase6_y1 = +Infinity;
    // let coinbase6_y2 = -Infinity;
    // let coinbase6_alldata = [];
    // let coinbase6_current_price;

    // var coinbase6_every_other_toggle = true;
    // var coinbase6_every_other_tracker = 0;
    // var coinbase6_get_nth_msg_to_get = 100;
    // coinbase6_socket.onmessage = function (event) {
    //     if(coinbase6_every_other_toggle){
    //         if(coinbase6_every_other_tracker%coinbase6_get_nth_msg_to_get==0){
    //             var coinbase6_data = JSON.parse(event.data);
    //             let coinbase6_data_dict = {'x':coinbase6_data['current_time'], 'y':parseFloat(coinbase6_data['coinbase'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbase6_data_dict.x>coinbase6_x2) coinbase6_x2 = coinbase6_data_dict.x;
    //             if (coinbase6_data_dict.x<coinbase6_x1) coinbase6_x1 = coinbase6_data_dict.x;
    //             if (coinbase6_data_dict.y>coinbase6_y2) coinbase6_y2 = coinbase6_data_dict.y;
    //             if (coinbase6_data_dict.y<coinbase6_y1) coinbase6_y1 = coinbase6_data_dict.y;
    //             // if (coinbase6_x2-coinbase6_x1>60000) coinbase6_x1 = coinbase6_x2-60000
    //             if (coinbase6_x2-coinbase6_x1>86400000) coinbase6_x1 = coinbase6_x2-86400000;
                
    //             //store the last price received.
    //             coinbase6_current_price=coinbase6_data_dict.y;

    //             coinbase6_alldata.push(coinbase6_data_dict);
    //             coinbase6_alldata=[...coinbase6_alldata.filter(data => data.x > coinbase6_x1)]
    //             coinbase6_every_other_tracker+=1;
    //         }else{
    //             coinbase6_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbase6_data = JSON.parse(event.data);
    //         let coinbase6_data_dict = {'x':coinbase6_data['current_time'], 'y':parseFloat(coinbase6_data['coinbase'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbase6_data_dict.x>coinbase6_x2) coinbase6_x2 = coinbase6_data_dict.x;
    //         if (coinbase6_data_dict.x<coinbase6_x1) coinbase6_x1 = coinbase6_data_dict.x;
    //         if (coinbase6_data_dict.y>coinbase6_y2) coinbase6_y2 = coinbase6_data_dict.y;
    //         if (coinbase6_data_dict.y<coinbase6_y1) coinbase6_y1 = coinbase6_data_dict.y;
    //         // if (coinbase6_x2-coinbase6_x1>60000) coinbase6_x1 = coinbase6_x2-60000
    //         if (coinbase6_x2-coinbase6_x1>86400000) coinbase6_x1 = coinbase6_x2-86400000;
    //         //store the last price received.
    //         coinbase6_current_price=coinbase6_data_dict.x;
    //         coinbase6_alldata.push(coinbase6_data_dict);
    //         coinbase6_alldata=[...coinbase6_alldata.filter(data => data.x > coinbase6_x1)]
    //         // console.log(coinbase6_alldata[coinbase6_alldata.length-1]);
    //     }
        
    // }







    // // let kraken1_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let kraken1_x1 = +Infinity;
    // let kraken1_x2 = -Infinity;
    // let kraken1_y1 = +Infinity;
    // let kraken1_y2 = -Infinity;
    // let kraken1_alldata = [];
    // let kraken1_current_price;

    // var kraken1_every_other_toggle = true;
    // var kraken1_every_other_tracker = 0;
    // var kraken1_get_nth_msg_to_get = 100;
    // kraken1_socket.onmessage = function (event) {
    //     if(kraken1_every_other_toggle){
    //         if(kraken1_every_other_tracker%kraken1_get_nth_msg_to_get==0){
    //             var kraken1_data = JSON.parse(event.data);
    //             let kraken1_data_dict = {'x':kraken1_data['current_time'], 'y':parseFloat(kraken1_data['kraken'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (kraken1_data_dict.x>kraken1_x2) kraken1_x2 = kraken1_data_dict.x;
    //             if (kraken1_data_dict.x<kraken1_x1) kraken1_x1 = kraken1_data_dict.x;
    //             if (kraken1_data_dict.y>kraken1_y2) kraken1_y2 = kraken1_data_dict.y;
    //             if (kraken1_data_dict.y<kraken1_y1) kraken1_y1 = kraken1_data_dict.y;
    //             // if (kraken1_x2-kraken1_x1>60000) kraken1_x1 = kraken1_x2-60000
    //             if (kraken1_x2-kraken1_x1>86400000) kraken1_x1 = kraken1_x2-86400000;
                
    //             //store the last price received.
    //             kraken1_current_price=kraken1_data_dict.y;

    //             kraken1_alldata.push(kraken1_data_dict);
    //             kraken1_alldata=[...kraken1_alldata.filter(data => data.x > kraken1_x1)]
    //             kraken1_every_other_tracker+=1;
    //         }else{
    //             kraken1_every_other_tracker+=1;
    //         }
    //     }else{
    //         var kraken1_data = JSON.parse(event.data);
    //         let kraken1_data_dict = {'x':kraken1_data['current_time'], 'y':parseFloat(kraken1_data['kraken'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (kraken1_data_dict.x>kraken1_x2) kraken1_x2 = kraken1_data_dict.x;
    //         if (kraken1_data_dict.x<kraken1_x1) kraken1_x1 = kraken1_data_dict.x;
    //         if (kraken1_data_dict.y>kraken1_y2) kraken1_y2 = kraken1_data_dict.y;
    //         if (kraken1_data_dict.y<kraken1_y1) kraken1_y1 = kraken1_data_dict.y;
    //         // if (kraken1_x2-kraken1_x1>60000) kraken1_x1 = kraken1_x2-60000
    //         if (kraken1_x2-kraken1_x1>86400000) kraken1_x1 = kraken1_x2-86400000;
    //         //store the last price received.
    //         kraken1_current_price=kraken1_data_dict.x;
    //         kraken1_alldata.push(kraken1_data_dict);
    //         kraken1_alldata=[...kraken1_alldata.filter(data => data.x > kraken1_x1)]
    //         // console.log(kraken1_alldata[kraken1_alldata.length-1]);
    //     }
        
    // }

    // // let kraken2_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let kraken2_x1 = +Infinity;
    // let kraken2_x2 = -Infinity;
    // let kraken2_y1 = +Infinity;
    // let kraken2_y2 = -Infinity;
    // let kraken2_alldata = [];
    // let kraken2_current_price;

    // var kraken2_every_other_toggle = true;
    // var kraken2_every_other_tracker = 0;
    // var kraken2_get_nth_msg_to_get = 100;
    // kraken2_socket.onmessage = function (event) {
    //     if(kraken2_every_other_toggle){
    //         if(kraken2_every_other_tracker%kraken2_get_nth_msg_to_get==0){
    //             var kraken2_data = JSON.parse(event.data);
    //             let kraken2_data_dict = {'x':kraken2_data['current_time'], 'y':parseFloat(kraken2_data['kraken'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (kraken2_data_dict.x>kraken2_x2) kraken2_x2 = kraken2_data_dict.x;
    //             if (kraken2_data_dict.x<kraken2_x1) kraken2_x1 = kraken2_data_dict.x;
    //             if (kraken2_data_dict.y>kraken2_y2) kraken2_y2 = kraken2_data_dict.y;
    //             if (kraken2_data_dict.y<kraken2_y1) kraken2_y1 = kraken2_data_dict.y;
    //             // if (kraken2_x2-kraken2_x1>60000) kraken2_x1 = kraken2_x2-60000
    //             if (kraken2_x2-kraken2_x1>86400000) kraken2_x1 = kraken2_x2-86400000;
                
    //             //store the last price received.
    //             kraken2_current_price=kraken2_data_dict.y;

    //             kraken2_alldata.push(kraken2_data_dict);
    //             kraken2_alldata=[...kraken2_alldata.filter(data => data.x > kraken2_x1)]
    //             kraken2_every_other_tracker+=1;
    //         }else{
    //             kraken2_every_other_tracker+=1;
    //         }
    //     }else{
    //         var kraken2_data = JSON.parse(event.data);
    //         let kraken2_data_dict = {'x':kraken2_data['current_time'], 'y':parseFloat(kraken2_data['kraken'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (kraken2_data_dict.x>kraken2_x2) kraken2_x2 = kraken2_data_dict.x;
    //         if (kraken2_data_dict.x<kraken2_x1) kraken2_x1 = kraken2_data_dict.x;
    //         if (kraken2_data_dict.y>kraken2_y2) kraken2_y2 = kraken2_data_dict.y;
    //         if (kraken2_data_dict.y<kraken2_y1) kraken2_y1 = kraken2_data_dict.y;
    //         // if (kraken2_x2-kraken2_x1>60000) kraken2_x1 = kraken2_x2-60000
    //         if (kraken2_x2-kraken2_x1>86400000) kraken2_x1 = kraken2_x2-86400000;
    //         //store the last price received.
    //         kraken2_current_price=kraken2_data_dict.x;
    //         kraken2_alldata.push(kraken2_data_dict);
    //         kraken2_alldata=[...kraken2_alldata.filter(data => data.x > kraken2_x1)]
    //         // console.log(kraken2_alldata[kraken2_alldata.length-1]);
    //     }
        
    // }

    // // let kraken3_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let kraken3_x1 = +Infinity;
    // let kraken3_x2 = -Infinity;
    // let kraken3_y1 = +Infinity;
    // let kraken3_y2 = -Infinity;
    // let kraken3_alldata = [];
    // let kraken3_current_price;

    // var kraken3_every_other_toggle = true;
    // var kraken3_every_other_tracker = 0;
    // var kraken3_get_nth_msg_to_get = 100;
    // kraken3_socket.onmessage = function (event) {
    //     if(kraken3_every_other_toggle){
    //         if(kraken3_every_other_tracker%kraken3_get_nth_msg_to_get==0){
    //             var kraken3_data = JSON.parse(event.data);
    //             let kraken3_data_dict = {'x':kraken3_data['E'], 'y':parseFloat(kraken3_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (kraken3_data_dict.x>kraken3_x2) kraken3_x2 = kraken3_data_dict.x;
    //             if (kraken3_data_dict.x<kraken3_x1) kraken3_x1 = kraken3_data_dict.x;
    //             if (kraken3_data_dict.y>kraken3_y2) kraken3_y2 = kraken3_data_dict.y;
    //             if (kraken3_data_dict.y<kraken3_y1) kraken3_y1 = kraken3_data_dict.y;
    //             // if (kraken3_x2-kraken3_x1>60000) kraken3_x1 = kraken3_x2-60000
    //             if (kraken3_x2-kraken3_x1>86400000) kraken3_x1 = kraken3_x2-86400000;
                
    //             //store the last price received.
    //             kraken3_current_price=kraken3_data_dict.y;

    //             kraken3_alldata.push(kraken3_data_dict);
    //             kraken3_alldata=[...kraken3_alldata.filter(data => data.x > kraken3_x1)]
    //             kraken3_every_other_tracker+=1;
    //         }else{
    //             kraken3_every_other_tracker+=1;
    //         }
    //     }else{
    //         var kraken3_data = JSON.parse(event.data);
    //         let kraken3_data_dict = {'x':kraken3_data['E'], 'y':parseFloat(kraken3_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (kraken3_data_dict.x>kraken3_x2) kraken3_x2 = kraken3_data_dict.x;
    //         if (kraken3_data_dict.x<kraken3_x1) kraken3_x1 = kraken3_data_dict.x;
    //         if (kraken3_data_dict.y>kraken3_y2) kraken3_y2 = kraken3_data_dict.y;
    //         if (kraken3_data_dict.y<kraken3_y1) kraken3_y1 = kraken3_data_dict.y;
    //         // if (kraken3_x2-kraken3_x1>60000) kraken3_x1 = kraken3_x2-60000
    //         if (kraken3_x2-kraken3_x1>86400000) kraken3_x1 = kraken3_x2-86400000;
    //         //store the last price received.
    //         kraken3_current_price=kraken3_data_dict.x;
    //         kraken3_alldata.push(kraken3_data_dict);
    //         kraken3_alldata=[...kraken3_alldata.filter(data => data.x > kraken3_x1)]
    //         // console.log(kraken3_alldata[kraken3_alldata.length-1]);
    //     }
        
    // }

    // // let kraken4_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let kraken4_x1 = +Infinity;
    // let kraken4_x2 = -Infinity;
    // let kraken4_y1 = +Infinity;
    // let kraken4_y2 = -Infinity;
    // let kraken4_alldata = [];
    // let kraken4_current_price;

    // var kraken4_every_other_toggle = true;
    // var kraken4_every_other_tracker = 0;
    // var kraken4_get_nth_msg_to_get = 100;
    // kraken4_socket.onmessage = function (event) {
    //     if(kraken4_every_other_toggle){
    //         if(kraken4_every_other_tracker%kraken4_get_nth_msg_to_get==0){
    //             var kraken4_data = JSON.parse(event.data);
    //             let kraken4_data_dict = {'x':kraken4_data['E'], 'y':parseFloat(kraken4_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (kraken4_data_dict.x>kraken4_x2) kraken4_x2 = kraken4_data_dict.x;
    //             if (kraken4_data_dict.x<kraken4_x1) kraken4_x1 = kraken4_data_dict.x;
    //             if (kraken4_data_dict.y>kraken4_y2) kraken4_y2 = kraken4_data_dict.y;
    //             if (kraken4_data_dict.y<kraken4_y1) kraken4_y1 = kraken4_data_dict.y;
    //             // if (kraken4_x2-kraken4_x1>60000) kraken4_x1 = kraken4_x2-60000
    //             if (kraken4_x2-kraken4_x1>86400000) kraken4_x1 = kraken4_x2-86400000;
                
    //             //store the last price received.
    //             kraken4_current_price=kraken4_data_dict.y;

    //             kraken4_alldata.push(kraken4_data_dict);
    //             kraken4_alldata=[...kraken4_alldata.filter(data => data.x > kraken4_x1)]
    //             kraken4_every_other_tracker+=1;
    //         }else{
    //             kraken4_every_other_tracker+=1;
    //         }
    //     }else{
    //         var kraken4_data = JSON.parse(event.data);
    //         let kraken4_data_dict = {'x':kraken4_data['E'], 'y':parseFloat(kraken4_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (kraken4_data_dict.x>kraken4_x2) kraken4_x2 = kraken4_data_dict.x;
    //         if (kraken4_data_dict.x<kraken4_x1) kraken4_x1 = kraken4_data_dict.x;
    //         if (kraken4_data_dict.y>kraken4_y2) kraken4_y2 = kraken4_data_dict.y;
    //         if (kraken4_data_dict.y<kraken4_y1) kraken4_y1 = kraken4_data_dict.y;
    //         // if (kraken4_x2-kraken4_x1>60000) kraken4_x1 = kraken4_x2-60000
    //         if (kraken4_x2-kraken4_x1>86400000) kraken4_x1 = kraken4_x2-86400000;
    //         //store the last price received.
    //         kraken4_current_price=kraken4_data_dict.x;
    //         kraken4_alldata.push(kraken4_data_dict);
    //         kraken4_alldata=[...kraken4_alldata.filter(data => data.x > kraken4_x1)]
    //         // console.log(kraken4_alldata[kraken4_alldata.length-1]);
    //     }
        
    // }

    // // let kraken5_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let kraken5_x1 = +Infinity;
    // let kraken5_x2 = -Infinity;
    // let kraken5_y1 = +Infinity;
    // let kraken5_y2 = -Infinity;
    // let kraken5_alldata = [];
    // let kraken5_current_price;

    // var kraken5_every_other_toggle = true;
    // var kraken5_every_other_tracker = 0;
    // var kraken5_get_nth_msg_to_get = 100;
    // kraken5_socket.onmessage = function (event) {
    //     if(kraken5_every_other_toggle){
    //         if(kraken5_every_other_tracker%kraken5_get_nth_msg_to_get==0){
    //             var kraken5_data = JSON.parse(event.data);
    //             let kraken5_data_dict = {'x':kraken5_data['E'], 'y':parseFloat(kraken5_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (kraken5_data_dict.x>kraken5_x2) kraken5_x2 = kraken5_data_dict.x;
    //             if (kraken5_data_dict.x<kraken5_x1) kraken5_x1 = kraken5_data_dict.x;
    //             if (kraken5_data_dict.y>kraken5_y2) kraken5_y2 = kraken5_data_dict.y;
    //             if (kraken5_data_dict.y<kraken5_y1) kraken5_y1 = kraken5_data_dict.y;
    //             // if (kraken5_x2-kraken5_x1>60000) kraken5_x1 = kraken5_x2-60000
    //             if (kraken5_x2-kraken5_x1>86400000) kraken5_x1 = kraken5_x2-86400000;
                
    //             //store the last price received.
    //             kraken5_current_price=kraken5_data_dict.y;

    //             kraken5_alldata.push(kraken5_data_dict);
    //             kraken5_alldata=[...kraken5_alldata.filter(data => data.x > kraken5_x1)]
    //             kraken5_every_other_tracker+=1;
    //         }else{
    //             kraken5_every_other_tracker+=1;
    //         }
    //     }else{
    //         var kraken5_data = JSON.parse(event.data);
    //         let kraken5_data_dict = {'x':kraken5_data['E'], 'y':parseFloat(kraken5_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (kraken5_data_dict.x>kraken5_x2) kraken5_x2 = kraken5_data_dict.x;
    //         if (kraken5_data_dict.x<kraken5_x1) kraken5_x1 = kraken5_data_dict.x;
    //         if (kraken5_data_dict.y>kraken5_y2) kraken5_y2 = kraken5_data_dict.y;
    //         if (kraken5_data_dict.y<kraken5_y1) kraken5_y1 = kraken5_data_dict.y;
    //         // if (kraken5_x2-kraken5_x1>60000) kraken5_x1 = kraken5_x2-60000
    //         if (kraken5_x2-kraken5_x1>86400000) kraken5_x1 = kraken5_x2-86400000;
    //         //store the last price received.
    //         kraken5_current_price=kraken5_data_dict.x;
    //         kraken5_alldata.push(kraken5_data_dict);
    //         kraken5_alldata=[...kraken5_alldata.filter(data => data.x > kraken5_x1)]
    //         // console.log(kraken5_alldata[kraken5_alldata.length-1]);
    //     }
        
    // }

    // // let kraken6_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let kraken6_x1 = +Infinity;
    // let kraken6_x2 = -Infinity;
    // let kraken6_y1 = +Infinity;
    // let kraken6_y2 = -Infinity;
    // let kraken6_alldata = [];
    // let kraken6_current_price;

    // var kraken6_every_other_toggle = true;
    // var kraken6_every_other_tracker = 0;
    // var kraken6_get_nth_msg_to_get = 100;
    // kraken6_socket.onmessage = function (event) {
    //     if(kraken6_every_other_toggle){
    //         if(kraken6_every_other_tracker%kraken6_get_nth_msg_to_get==0){
    //             var kraken6_data = JSON.parse(event.data);
    //             let kraken6_data_dict = {'x':kraken6_data['E'], 'y':parseFloat(kraken6_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (kraken6_data_dict.x>kraken6_x2) kraken6_x2 = kraken6_data_dict.x;
    //             if (kraken6_data_dict.x<kraken6_x1) kraken6_x1 = kraken6_data_dict.x;
    //             if (kraken6_data_dict.y>kraken6_y2) kraken6_y2 = kraken6_data_dict.y;
    //             if (kraken6_data_dict.y<kraken6_y1) kraken6_y1 = kraken6_data_dict.y;
    //             // if (kraken6_x2-kraken6_x1>60000) kraken6_x1 = kraken6_x2-60000
    //             if (kraken6_x2-kraken6_x1>86400000) kraken6_x1 = kraken6_x2-86400000;
                
    //             //store the last price received.
    //             kraken6_current_price=kraken6_data_dict.y;

    //             kraken6_alldata.push(kraken6_data_dict);
    //             kraken6_alldata=[...kraken6_alldata.filter(data => data.x > kraken6_x1)]
    //             kraken6_every_other_tracker+=1;
    //         }else{
    //             kraken6_every_other_tracker+=1;
    //         }
    //     }else{
    //         var kraken6_data = JSON.parse(event.data);
    //         let kraken6_data_dict = {'x':kraken6_data['E'], 'y':parseFloat(kraken6_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (kraken6_data_dict.x>kraken6_x2) kraken6_x2 = kraken6_data_dict.x;
    //         if (kraken6_data_dict.x<kraken6_x1) kraken6_x1 = kraken6_data_dict.x;
    //         if (kraken6_data_dict.y>kraken6_y2) kraken6_y2 = kraken6_data_dict.y;
    //         if (kraken6_data_dict.y<kraken6_y1) kraken6_y1 = kraken6_data_dict.y;
    //         // if (kraken6_x2-kraken6_x1>60000) kraken6_x1 = kraken6_x2-60000
    //         if (kraken6_x2-kraken6_x1>86400000) kraken6_x1 = kraken6_x2-86400000;
    //         //store the last price received.
    //         kraken6_current_price=kraken6_data_dict.x;
    //         kraken6_alldata.push(kraken6_data_dict);
    //         kraken6_alldata=[...kraken6_alldata.filter(data => data.x > kraken6_x1)]
    //         // console.log(kraken6_alldata[kraken6_alldata.length-1]);
    //     }
        
    // }


    // // let gemini1_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let gemini1_x1 = +Infinity;
    // let gemini1_x2 = -Infinity;
    // let gemini1_y1 = +Infinity;
    // let gemini1_y2 = -Infinity;
    // let gemini1_alldata = [];
    // let gemini1_current_price;

    // var gemini1_every_other_toggle = true;
    // var gemini1_every_other_tracker = 0;
    // var gemini1_get_nth_msg_to_get = 100;
    // gemini1_socket.onmessage = function (event) {
    //     if(gemini1_every_other_toggle){
    //         if(gemini1_every_other_tracker%gemini1_get_nth_msg_to_get==0){
    //             var gemini1_data = JSON.parse(event.data);
    //             let gemini1_data_dict = {'x':gemini1_data['E'], 'y':parseFloat(gemini1_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (gemini1_data_dict.x>gemini1_x2) gemini1_x2 = gemini1_data_dict.x;
    //             if (gemini1_data_dict.x<gemini1_x1) gemini1_x1 = gemini1_data_dict.x;
    //             if (gemini1_data_dict.y>gemini1_y2) gemini1_y2 = gemini1_data_dict.y;
    //             if (gemini1_data_dict.y<gemini1_y1) gemini1_y1 = gemini1_data_dict.y;
    //             // if (gemini1_x2-gemini1_x1>60000) gemini1_x1 = gemini1_x2-60000
    //             if (gemini1_x2-gemini1_x1>86400000) gemini1_x1 = gemini1_x2-86400000;
                
    //             //store the last price received.
    //             gemini1_current_price=gemini1_data_dict.y;

    //             gemini1_alldata.push(gemini1_data_dict);
    //             gemini1_alldata=[...gemini1_alldata.filter(data => data.x > gemini1_x1)]
    //             gemini1_every_other_tracker+=1;
    //         }else{
    //             gemini1_every_other_tracker+=1;
    //         }
    //     }else{
    //         var gemini1_data = JSON.parse(event.data);
    //         let gemini1_data_dict = {'x':gemini1_data['E'], 'y':parseFloat(gemini1_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (gemini1_data_dict.x>gemini1_x2) gemini1_x2 = gemini1_data_dict.x;
    //         if (gemini1_data_dict.x<gemini1_x1) gemini1_x1 = gemini1_data_dict.x;
    //         if (gemini1_data_dict.y>gemini1_y2) gemini1_y2 = gemini1_data_dict.y;
    //         if (gemini1_data_dict.y<gemini1_y1) gemini1_y1 = gemini1_data_dict.y;
    //         // if (gemini1_x2-gemini1_x1>60000) gemini1_x1 = gemini1_x2-60000
    //         if (gemini1_x2-gemini1_x1>86400000) gemini1_x1 = gemini1_x2-86400000;
    //         //store the last price received.
    //         gemini1_current_price=gemini1_data_dict.x;
    //         gemini1_alldata.push(gemini1_data_dict);
    //         gemini1_alldata=[...gemini1_alldata.filter(data => data.x > gemini1_x1)]
    //         // console.log(gemini1_alldata[gemini1_alldata.length-1]);
    //     }
        
    // }

    // // let gemini2_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let gemini2_x1 = +Infinity;
    // let gemini2_x2 = -Infinity;
    // let gemini2_y1 = +Infinity;
    // let gemini2_y2 = -Infinity;
    // let gemini2_alldata = [];
    // let gemini2_current_price;

    // var gemini2_every_other_toggle = true;
    // var gemini2_every_other_tracker = 0;
    // var gemini2_get_nth_msg_to_get = 100;
    // gemini2_socket.onmessage = function (event) {
    //     if(gemini2_every_other_toggle){
    //         if(gemini2_every_other_tracker%gemini2_get_nth_msg_to_get==0){
    //             var gemini2_data = JSON.parse(event.data);
    //             let gemini2_data_dict = {'x':gemini2_data['E'], 'y':parseFloat(gemini2_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (gemini2_data_dict.x>gemini2_x2) gemini2_x2 = gemini2_data_dict.x;
    //             if (gemini2_data_dict.x<gemini2_x1) gemini2_x1 = gemini2_data_dict.x;
    //             if (gemini2_data_dict.y>gemini2_y2) gemini2_y2 = gemini2_data_dict.y;
    //             if (gemini2_data_dict.y<gemini2_y1) gemini2_y1 = gemini2_data_dict.y;
    //             // if (gemini2_x2-gemini2_x1>60000) gemini2_x1 = gemini2_x2-60000
    //             if (gemini2_x2-gemini2_x1>86400000) gemini2_x1 = gemini2_x2-86400000;
                
    //             //store the last price received.
    //             gemini2_current_price=gemini2_data_dict.y;

    //             gemini2_alldata.push(gemini2_data_dict);
    //             gemini2_alldata=[...gemini2_alldata.filter(data => data.x > gemini2_x1)]
    //             gemini2_every_other_tracker+=1;
    //         }else{
    //             gemini2_every_other_tracker+=1;
    //         }
    //     }else{
    //         var gemini2_data = JSON.parse(event.data);
    //         let gemini2_data_dict = {'x':gemini2_data['E'], 'y':parseFloat(gemini2_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (gemini2_data_dict.x>gemini2_x2) gemini2_x2 = gemini2_data_dict.x;
    //         if (gemini2_data_dict.x<gemini2_x1) gemini2_x1 = gemini2_data_dict.x;
    //         if (gemini2_data_dict.y>gemini2_y2) gemini2_y2 = gemini2_data_dict.y;
    //         if (gemini2_data_dict.y<gemini2_y1) gemini2_y1 = gemini2_data_dict.y;
    //         // if (gemini2_x2-gemini2_x1>60000) gemini2_x1 = gemini2_x2-60000
    //         if (gemini2_x2-gemini2_x1>86400000) gemini2_x1 = gemini2_x2-86400000;
    //         //store the last price received.
    //         gemini2_current_price=gemini2_data_dict.x;
    //         gemini2_alldata.push(gemini2_data_dict);
    //         gemini2_alldata=[...gemini2_alldata.filter(data => data.x > gemini2_x1)]
    //         // console.log(gemini2_alldata[gemini2_alldata.length-1]);
    //     }
        
    // }

    // // let gemini3_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let gemini3_x1 = +Infinity;
    // let gemini3_x2 = -Infinity;
    // let gemini3_y1 = +Infinity;
    // let gemini3_y2 = -Infinity;
    // let gemini3_alldata = [];
    // let gemini3_current_price;

    // var gemini3_every_other_toggle = true;
    // var gemini3_every_other_tracker = 0;
    // var gemini3_get_nth_msg_to_get = 100;
    // gemini3_socket.onmessage = function (event) {
    //     if(gemini3_every_other_toggle){
    //         if(gemini3_every_other_tracker%gemini3_get_nth_msg_to_get==0){
    //             var gemini3_data = JSON.parse(event.data);
    //             let gemini3_data_dict = {'x':gemini3_data['E'], 'y':parseFloat(gemini3_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (gemini3_data_dict.x>gemini3_x2) gemini3_x2 = gemini3_data_dict.x;
    //             if (gemini3_data_dict.x<gemini3_x1) gemini3_x1 = gemini3_data_dict.x;
    //             if (gemini3_data_dict.y>gemini3_y2) gemini3_y2 = gemini3_data_dict.y;
    //             if (gemini3_data_dict.y<gemini3_y1) gemini3_y1 = gemini3_data_dict.y;
    //             // if (gemini3_x2-gemini3_x1>60000) gemini3_x1 = gemini3_x2-60000
    //             if (gemini3_x2-gemini3_x1>86400000) gemini3_x1 = gemini3_x2-86400000;
                
    //             //store the last price received.
    //             gemini3_current_price=gemini3_data_dict.y;

    //             gemini3_alldata.push(gemini3_data_dict);
    //             gemini3_alldata=[...gemini3_alldata.filter(data => data.x > gemini3_x1)]
    //             gemini3_every_other_tracker+=1;
    //         }else{
    //             gemini3_every_other_tracker+=1;
    //         }
    //     }else{
    //         var gemini3_data = JSON.parse(event.data);
    //         let gemini3_data_dict = {'x':gemini3_data['E'], 'y':parseFloat(gemini3_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (gemini3_data_dict.x>gemini3_x2) gemini3_x2 = gemini3_data_dict.x;
    //         if (gemini3_data_dict.x<gemini3_x1) gemini3_x1 = gemini3_data_dict.x;
    //         if (gemini3_data_dict.y>gemini3_y2) gemini3_y2 = gemini3_data_dict.y;
    //         if (gemini3_data_dict.y<gemini3_y1) gemini3_y1 = gemini3_data_dict.y;
    //         // if (gemini3_x2-gemini3_x1>60000) gemini3_x1 = gemini3_x2-60000
    //         if (gemini3_x2-gemini3_x1>86400000) gemini3_x1 = gemini3_x2-86400000;
    //         //store the last price received.
    //         gemini3_current_price=gemini3_data_dict.x;
    //         gemini3_alldata.push(gemini3_data_dict);
    //         gemini3_alldata=[...gemini3_alldata.filter(data => data.x > gemini3_x1)]
    //         // console.log(gemini3_alldata[gemini3_alldata.length-1]);
    //     }
        
    // }

    // // let gemini4_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let gemini4_x1 = +Infinity;
    // let gemini4_x2 = -Infinity;
    // let gemini4_y1 = +Infinity;
    // let gemini4_y2 = -Infinity;
    // let gemini4_alldata = [];
    // let gemini4_current_price;

    // var gemini4_every_other_toggle = true;
    // var gemini4_every_other_tracker = 0;
    // var gemini4_get_nth_msg_to_get = 100;
    // gemini4_socket.onmessage = function (event) {
    //     if(gemini4_every_other_toggle){
    //         if(gemini4_every_other_tracker%gemini4_get_nth_msg_to_get==0){
    //             var gemini4_data = JSON.parse(event.data);
    //             let gemini4_data_dict = {'x':gemini4_data['E'], 'y':parseFloat(gemini4_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (gemini4_data_dict.x>gemini4_x2) gemini4_x2 = gemini4_data_dict.x;
    //             if (gemini4_data_dict.x<gemini4_x1) gemini4_x1 = gemini4_data_dict.x;
    //             if (gemini4_data_dict.y>gemini4_y2) gemini4_y2 = gemini4_data_dict.y;
    //             if (gemini4_data_dict.y<gemini4_y1) gemini4_y1 = gemini4_data_dict.y;
    //             // if (gemini4_x2-gemini4_x1>60000) gemini4_x1 = gemini4_x2-60000
    //             if (gemini4_x2-gemini4_x1>86400000) gemini4_x1 = gemini4_x2-86400000;
                
    //             //store the last price received.
    //             gemini4_current_price=gemini4_data_dict.y;

    //             gemini4_alldata.push(gemini4_data_dict);
    //             gemini4_alldata=[...gemini4_alldata.filter(data => data.x > gemini4_x1)]
    //             gemini4_every_other_tracker+=1;
    //         }else{
    //             gemini4_every_other_tracker+=1;
    //         }
    //     }else{
    //         var gemini4_data = JSON.parse(event.data);
    //         let gemini4_data_dict = {'x':gemini4_data['E'], 'y':parseFloat(gemini4_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (gemini4_data_dict.x>gemini4_x2) gemini4_x2 = gemini4_data_dict.x;
    //         if (gemini4_data_dict.x<gemini4_x1) gemini4_x1 = gemini4_data_dict.x;
    //         if (gemini4_data_dict.y>gemini4_y2) gemini4_y2 = gemini4_data_dict.y;
    //         if (gemini4_data_dict.y<gemini4_y1) gemini4_y1 = gemini4_data_dict.y;
    //         // if (gemini4_x2-gemini4_x1>60000) gemini4_x1 = gemini4_x2-60000
    //         if (gemini4_x2-gemini4_x1>86400000) gemini4_x1 = gemini4_x2-86400000;
    //         //store the last price received.
    //         gemini4_current_price=gemini4_data_dict.x;
    //         gemini4_alldata.push(gemini4_data_dict);
    //         gemini4_alldata=[...gemini4_alldata.filter(data => data.x > gemini4_x1)]
    //         // console.log(gemini4_alldata[gemini4_alldata.length-1]);
    //     }
        
    // }

    // // let gemini5_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let gemini5_x1 = +Infinity;
    // let gemini5_x2 = -Infinity;
    // let gemini5_y1 = +Infinity;
    // let gemini5_y2 = -Infinity;
    // let gemini5_alldata = [];
    // let gemini5_current_price;

    // var gemini5_every_other_toggle = true;
    // var gemini5_every_other_tracker = 0;
    // var gemini5_get_nth_msg_to_get = 100;
    // gemini5_socket.onmessage = function (event) {
    //     if(gemini5_every_other_toggle){
    //         if(gemini5_every_other_tracker%gemini5_get_nth_msg_to_get==0){
    //             var gemini5_data = JSON.parse(event.data);
    //             let gemini5_data_dict = {'x':gemini5_data['E'], 'y':parseFloat(gemini5_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (gemini5_data_dict.x>gemini5_x2) gemini5_x2 = gemini5_data_dict.x;
    //             if (gemini5_data_dict.x<gemini5_x1) gemini5_x1 = gemini5_data_dict.x;
    //             if (gemini5_data_dict.y>gemini5_y2) gemini5_y2 = gemini5_data_dict.y;
    //             if (gemini5_data_dict.y<gemini5_y1) gemini5_y1 = gemini5_data_dict.y;
    //             // if (gemini5_x2-gemini5_x1>60000) gemini5_x1 = gemini5_x2-60000
    //             if (gemini5_x2-gemini5_x1>86400000) gemini5_x1 = gemini5_x2-86400000;
                
    //             //store the last price received.
    //             gemini5_current_price=gemini5_data_dict.y;

    //             gemini5_alldata.push(gemini5_data_dict);
    //             gemini5_alldata=[...gemini5_alldata.filter(data => data.x > gemini5_x1)]
    //             gemini5_every_other_tracker+=1;
    //         }else{
    //             gemini5_every_other_tracker+=1;
    //         }
    //     }else{
    //         var gemini5_data = JSON.parse(event.data);
    //         let gemini5_data_dict = {'x':gemini5_data['E'], 'y':parseFloat(gemini5_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (gemini5_data_dict.x>gemini5_x2) gemini5_x2 = gemini5_data_dict.x;
    //         if (gemini5_data_dict.x<gemini5_x1) gemini5_x1 = gemini5_data_dict.x;
    //         if (gemini5_data_dict.y>gemini5_y2) gemini5_y2 = gemini5_data_dict.y;
    //         if (gemini5_data_dict.y<gemini5_y1) gemini5_y1 = gemini5_data_dict.y;
    //         // if (gemini5_x2-gemini5_x1>60000) gemini5_x1 = gemini5_x2-60000
    //         if (gemini5_x2-gemini5_x1>86400000) gemini5_x1 = gemini5_x2-86400000;
    //         //store the last price received.
    //         gemini5_current_price=gemini5_data_dict.x;
    //         gemini5_alldata.push(gemini5_data_dict);
    //         gemini5_alldata=[...gemini5_alldata.filter(data => data.x > gemini5_x1)]
    //         // console.log(gemini5_alldata[gemini5_alldata.length-1]);
    //     }
        
    // }

    // // let gemini6_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let gemini6_x1 = +Infinity;
    // let gemini6_x2 = -Infinity;
    // let gemini6_y1 = +Infinity;
    // let gemini6_y2 = -Infinity;
    // let gemini6_alldata = [];
    // let gemini6_current_price;

    // var gemini6_every_other_toggle = true;
    // var gemini6_every_other_tracker = 0;
    // var gemini6_get_nth_msg_to_get = 100;
    // gemini6_socket.onmessage = function (event) {
    //     if(gemini6_every_other_toggle){
    //         if(gemini6_every_other_tracker%gemini6_get_nth_msg_to_get==0){
    //             var gemini6_data = JSON.parse(event.data);
    //             let gemini6_data_dict = {'x':gemini6_data['E'], 'y':parseFloat(gemini6_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (gemini6_data_dict.x>gemini6_x2) gemini6_x2 = gemini6_data_dict.x;
    //             if (gemini6_data_dict.x<gemini6_x1) gemini6_x1 = gemini6_data_dict.x;
    //             if (gemini6_data_dict.y>gemini6_y2) gemini6_y2 = gemini6_data_dict.y;
    //             if (gemini6_data_dict.y<gemini6_y1) gemini6_y1 = gemini6_data_dict.y;
    //             // if (gemini6_x2-gemini6_x1>60000) gemini6_x1 = gemini6_x2-60000
    //             if (gemini6_x2-gemini6_x1>86400000) gemini6_x1 = gemini6_x2-86400000;
                
    //             //store the last price received.
    //             gemini6_current_price=gemini6_data_dict.y;

    //             gemini6_alldata.push(gemini6_data_dict);
    //             gemini6_alldata=[...gemini6_alldata.filter(data => data.x > gemini6_x1)]
    //             gemini6_every_other_tracker+=1;
    //         }else{
    //             gemini6_every_other_tracker+=1;
    //         }
    //     }else{
    //         var gemini6_data = JSON.parse(event.data);
    //         let gemini6_data_dict = {'x':gemini6_data['E'], 'y':parseFloat(gemini6_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (gemini6_data_dict.x>gemini6_x2) gemini6_x2 = gemini6_data_dict.x;
    //         if (gemini6_data_dict.x<gemini6_x1) gemini6_x1 = gemini6_data_dict.x;
    //         if (gemini6_data_dict.y>gemini6_y2) gemini6_y2 = gemini6_data_dict.y;
    //         if (gemini6_data_dict.y<gemini6_y1) gemini6_y1 = gemini6_data_dict.y;
    //         // if (gemini6_x2-gemini6_x1>60000) gemini6_x1 = gemini6_x2-60000
    //         if (gemini6_x2-gemini6_x1>86400000) gemini6_x1 = gemini6_x2-86400000;
    //         //store the last price received.
    //         gemini6_current_price=gemini6_data_dict.x;
    //         gemini6_alldata.push(gemini6_data_dict);
    //         gemini6_alldata=[...gemini6_alldata.filter(data => data.x > gemini6_x1)]
    //         // console.log(gemini6_alldata[gemini6_alldata.length-1]);
    //     }
        
    // }

    // // let binanceus1_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binanceus1_x1 = +Infinity;
    // let binanceus1_x2 = -Infinity;
    // let binanceus1_y1 = +Infinity;
    // let binanceus1_y2 = -Infinity;
    // let binanceus1_alldata = [];
    // let binanceus1_current_price;

    // var binanceus1_every_other_toggle = true;
    // var binanceus1_every_other_tracker = 0;
    // var binanceus1_get_nth_msg_to_get = 100;
    // binanceus1_socket.onmessage = function (event) {
    //     if(binanceus1_every_other_toggle){
    //         if(binanceus1_every_other_tracker%binanceus1_get_nth_msg_to_get==0){
    //             var binanceus1_data = JSON.parse(event.data);
    //             let binanceus1_data_dict = {'x':binanceus1_data['E'], 'y':parseFloat(binanceus1_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binanceus1_data_dict.x>binanceus1_x2) binanceus1_x2 = binanceus1_data_dict.x;
    //             if (binanceus1_data_dict.x<binanceus1_x1) binanceus1_x1 = binanceus1_data_dict.x;
    //             if (binanceus1_data_dict.y>binanceus1_y2) binanceus1_y2 = binanceus1_data_dict.y;
    //             if (binanceus1_data_dict.y<binanceus1_y1) binanceus1_y1 = binanceus1_data_dict.y;
    //             // if (binanceus1_x2-binanceus1_x1>60000) binanceus1_x1 = binanceus1_x2-60000
    //             if (binanceus1_x2-binanceus1_x1>86400000) binanceus1_x1 = binanceus1_x2-86400000;
                
    //             //store the last price received.
    //             binanceus1_current_price=binanceus1_data_dict.y;

    //             binanceus1_alldata.push(binanceus1_data_dict);
    //             binanceus1_alldata=[...binanceus1_alldata.filter(data => data.x > binanceus1_x1)]
    //             binanceus1_every_other_tracker+=1;
    //         }else{
    //             binanceus1_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binanceus1_data = JSON.parse(event.data);
    //         let binanceus1_data_dict = {'x':binanceus1_data['E'], 'y':parseFloat(binanceus1_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binanceus1_data_dict.x>binanceus1_x2) binanceus1_x2 = binanceus1_data_dict.x;
    //         if (binanceus1_data_dict.x<binanceus1_x1) binanceus1_x1 = binanceus1_data_dict.x;
    //         if (binanceus1_data_dict.y>binanceus1_y2) binanceus1_y2 = binanceus1_data_dict.y;
    //         if (binanceus1_data_dict.y<binanceus1_y1) binanceus1_y1 = binanceus1_data_dict.y;
    //         // if (binanceus1_x2-binanceus1_x1>60000) binanceus1_x1 = binanceus1_x2-60000
    //         if (binanceus1_x2-binanceus1_x1>86400000) binanceus1_x1 = binanceus1_x2-86400000;
    //         //store the last price received.
    //         binanceus1_current_price=binanceus1_data_dict.x;
    //         binanceus1_alldata.push(binanceus1_data_dict);
    //         binanceus1_alldata=[...binanceus1_alldata.filter(data => data.x > binanceus1_x1)]
    //         // console.log(binanceus1_alldata[binanceus1_alldata.length-1]);
    //     }
        
    // }

    // let binanceus2_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binanceus2_x1 = +Infinity;
    // let binanceus2_x2 = -Infinity;
    // let binanceus2_y1 = +Infinity;
    // let binanceus2_y2 = -Infinity;
    // let binanceus2_alldata = [];
    // let binanceus2_current_price;

    // var binanceus2_every_other_toggle = true;
    // var binanceus2_every_other_tracker = 0;
    // var binanceus2_get_nth_msg_to_get = 100;
    // binanceus2_socket.onmessage = function (event) {
    //     if(binanceus2_every_other_toggle){
    //         if(binanceus2_every_other_tracker%binanceus2_get_nth_msg_to_get==0){
    //             var binanceus2_data = JSON.parse(event.data);
    //             let binanceus2_data_dict = {'x':binanceus2_data['E'], 'y':parseFloat(binanceus2_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binanceus2_data_dict.x>binanceus2_x2) binanceus2_x2 = binanceus2_data_dict.x;
    //             if (binanceus2_data_dict.x<binanceus2_x1) binanceus2_x1 = binanceus2_data_dict.x;
    //             if (binanceus2_data_dict.y>binanceus2_y2) binanceus2_y2 = binanceus2_data_dict.y;
    //             if (binanceus2_data_dict.y<binanceus2_y1) binanceus2_y1 = binanceus2_data_dict.y;
    //             // if (binanceus2_x2-binanceus2_x1>60000) binanceus2_x1 = binanceus2_x2-60000
    //             if (binanceus2_x2-binanceus2_x1>86400000) binanceus2_x1 = binanceus2_x2-86400000;
                
    //             //store the last price received.
    //             binanceus2_current_price=binanceus2_data_dict.y;

    //             binanceus2_alldata.push(binanceus2_data_dict);
    //             binanceus2_alldata=[...binanceus2_alldata.filter(data => data.x > binanceus2_x1)]
    //             binanceus2_every_other_tracker+=1;
    //         }else{
    //             binanceus2_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binanceus2_data = JSON.parse(event.data);
    //         let binanceus2_data_dict = {'x':binanceus2_data['E'], 'y':parseFloat(binanceus2_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binanceus2_data_dict.x>binanceus2_x2) binanceus2_x2 = binanceus2_data_dict.x;
    //         if (binanceus2_data_dict.x<binanceus2_x1) binanceus2_x1 = binanceus2_data_dict.x;
    //         if (binanceus2_data_dict.y>binanceus2_y2) binanceus2_y2 = binanceus2_data_dict.y;
    //         if (binanceus2_data_dict.y<binanceus2_y1) binanceus2_y1 = binanceus2_data_dict.y;
    //         // if (binanceus2_x2-binanceus2_x1>60000) binanceus2_x1 = binanceus2_x2-60000
    //         if (binanceus2_x2-binanceus2_x1>86400000) binanceus2_x1 = binanceus2_x2-86400000;
    //         //store the last price received.
    //         binanceus2_current_price=binanceus2_data_dict.x;
    //         binanceus2_alldata.push(binanceus2_data_dict);
    //         binanceus2_alldata=[...binanceus2_alldata.filter(data => data.x > binanceus2_x1)]
    //         // console.log(binanceus2_alldata[binanceus2_alldata.length-1]);
    //     }
        
    // }

    // let binanceus3_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binanceus3_x1 = +Infinity;
    // let binanceus3_x2 = -Infinity;
    // let binanceus3_y1 = +Infinity;
    // let binanceus3_y2 = -Infinity;
    // let binanceus3_alldata = [];
    // let binanceus3_current_price;

    // var binanceus3_every_other_toggle = true;
    // var binanceus3_every_other_tracker = 0;
    // var binanceus3_get_nth_msg_to_get = 100;
    // binanceus3_socket.onmessage = function (event) {
    //     if(binanceus3_every_other_toggle){
    //         if(binanceus3_every_other_tracker%binanceus3_get_nth_msg_to_get==0){
    //             var binanceus3_data = JSON.parse(event.data);
    //             let binanceus3_data_dict = {'x':binanceus3_data['E'], 'y':parseFloat(binanceus3_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binanceus3_data_dict.x>binanceus3_x2) binanceus3_x2 = binanceus3_data_dict.x;
    //             if (binanceus3_data_dict.x<binanceus3_x1) binanceus3_x1 = binanceus3_data_dict.x;
    //             if (binanceus3_data_dict.y>binanceus3_y2) binanceus3_y2 = binanceus3_data_dict.y;
    //             if (binanceus3_data_dict.y<binanceus3_y1) binanceus3_y1 = binanceus3_data_dict.y;
    //             // if (binanceus3_x2-binanceus3_x1>60000) binanceus3_x1 = binanceus3_x2-60000
    //             if (binanceus3_x2-binanceus3_x1>86400000) binanceus3_x1 = binanceus3_x2-86400000;
                
    //             //store the last price received.
    //             binanceus3_current_price=binanceus3_data_dict.y;

    //             binanceus3_alldata.push(binanceus3_data_dict);
    //             binanceus3_alldata=[...binanceus3_alldata.filter(data => data.x > binanceus3_x1)]
    //             binanceus3_every_other_tracker+=1;
    //         }else{
    //             binanceus3_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binanceus3_data = JSON.parse(event.data);
    //         let binanceus3_data_dict = {'x':binanceus3_data['E'], 'y':parseFloat(binanceus3_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binanceus3_data_dict.x>binanceus3_x2) binanceus3_x2 = binanceus3_data_dict.x;
    //         if (binanceus3_data_dict.x<binanceus3_x1) binanceus3_x1 = binanceus3_data_dict.x;
    //         if (binanceus3_data_dict.y>binanceus3_y2) binanceus3_y2 = binanceus3_data_dict.y;
    //         if (binanceus3_data_dict.y<binanceus3_y1) binanceus3_y1 = binanceus3_data_dict.y;
    //         // if (binanceus3_x2-binanceus3_x1>60000) binanceus3_x1 = binanceus3_x2-60000
    //         if (binanceus3_x2-binanceus3_x1>86400000) binanceus3_x1 = binanceus3_x2-86400000;
    //         //store the last price received.
    //         binanceus3_current_price=binanceus3_data_dict.x;
    //         binanceus3_alldata.push(binanceus3_data_dict);
    //         binanceus3_alldata=[...binanceus3_alldata.filter(data => data.x > binanceus3_x1)]
    //         // console.log(binanceus3_alldata[binanceus3_alldata.length-1]);
    //     }
        
    // }

    // let binanceus4_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binanceus4_x1 = +Infinity;
    // let binanceus4_x2 = -Infinity;
    // let binanceus4_y1 = +Infinity;
    // let binanceus4_y2 = -Infinity;
    // let binanceus4_alldata = [];
    // let binanceus4_current_price;

    // var binanceus4_every_other_toggle = true;
    // var binanceus4_every_other_tracker = 0;
    // var binanceus4_get_nth_msg_to_get = 100;
    // binanceus4_socket.onmessage = function (event) {
    //     if(binanceus4_every_other_toggle){
    //         if(binanceus4_every_other_tracker%binanceus4_get_nth_msg_to_get==0){
    //             var binanceus4_data = JSON.parse(event.data);
    //             let binanceus4_data_dict = {'x':binanceus4_data['E'], 'y':parseFloat(binanceus4_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binanceus4_data_dict.x>binanceus4_x2) binanceus4_x2 = binanceus4_data_dict.x;
    //             if (binanceus4_data_dict.x<binanceus4_x1) binanceus4_x1 = binanceus4_data_dict.x;
    //             if (binanceus4_data_dict.y>binanceus4_y2) binanceus4_y2 = binanceus4_data_dict.y;
    //             if (binanceus4_data_dict.y<binanceus4_y1) binanceus4_y1 = binanceus4_data_dict.y;
    //             // if (binanceus4_x2-binanceus4_x1>60000) binanceus4_x1 = binanceus4_x2-60000
    //             if (binanceus4_x2-binanceus4_x1>86400000) binanceus4_x1 = binanceus4_x2-86400000;
                
    //             //store the last price received.
    //             binanceus4_current_price=binanceus4_data_dict.y;

    //             binanceus4_alldata.push(binanceus4_data_dict);
    //             binanceus4_alldata=[...binanceus4_alldata.filter(data => data.x > binanceus4_x1)]
    //             binanceus4_every_other_tracker+=1;
    //         }else{
    //             binanceus4_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binanceus4_data = JSON.parse(event.data);
    //         let binanceus4_data_dict = {'x':binanceus4_data['E'], 'y':parseFloat(binanceus4_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binanceus4_data_dict.x>binanceus4_x2) binanceus4_x2 = binanceus4_data_dict.x;
    //         if (binanceus4_data_dict.x<binanceus4_x1) binanceus4_x1 = binanceus4_data_dict.x;
    //         if (binanceus4_data_dict.y>binanceus4_y2) binanceus4_y2 = binanceus4_data_dict.y;
    //         if (binanceus4_data_dict.y<binanceus4_y1) binanceus4_y1 = binanceus4_data_dict.y;
    //         // if (binanceus4_x2-binanceus4_x1>60000) binanceus4_x1 = binanceus4_x2-60000
    //         if (binanceus4_x2-binanceus4_x1>86400000) binanceus4_x1 = binanceus4_x2-86400000;
    //         //store the last price received.
    //         binanceus4_current_price=binanceus4_data_dict.x;
    //         binanceus4_alldata.push(binanceus4_data_dict);
    //         binanceus4_alldata=[...binanceus4_alldata.filter(data => data.x > binanceus4_x1)]
    //         // console.log(binanceus4_alldata[binanceus4_alldata.length-1]);
    //     }
        
    // }

    // let binanceus5_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binanceus5_x1 = +Infinity;
    // let binanceus5_x2 = -Infinity;
    // let binanceus5_y1 = +Infinity;
    // let binanceus5_y2 = -Infinity;
    // let binanceus5_alldata = [];
    // let binanceus5_current_price;

    // var binanceus5_every_other_toggle = true;
    // var binanceus5_every_other_tracker = 0;
    // var binanceus5_get_nth_msg_to_get = 100;
    // binanceus5_socket.onmessage = function (event) {
    //     if(binanceus5_every_other_toggle){
    //         if(binanceus5_every_other_tracker%binanceus5_get_nth_msg_to_get==0){
    //             var binanceus5_data = JSON.parse(event.data);
    //             let binanceus5_data_dict = {'x':binanceus5_data['E'], 'y':parseFloat(binanceus5_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binanceus5_data_dict.x>binanceus5_x2) binanceus5_x2 = binanceus5_data_dict.x;
    //             if (binanceus5_data_dict.x<binanceus5_x1) binanceus5_x1 = binanceus5_data_dict.x;
    //             if (binanceus5_data_dict.y>binanceus5_y2) binanceus5_y2 = binanceus5_data_dict.y;
    //             if (binanceus5_data_dict.y<binanceus5_y1) binanceus5_y1 = binanceus5_data_dict.y;
    //             // if (binanceus5_x2-binanceus5_x1>60000) binanceus5_x1 = binanceus5_x2-60000
    //             if (binanceus5_x2-binanceus5_x1>86400000) binanceus5_x1 = binanceus5_x2-86400000;
                
    //             //store the last price received.
    //             binanceus5_current_price=binanceus5_data_dict.y;

    //             binanceus5_alldata.push(binanceus5_data_dict);
    //             binanceus5_alldata=[...binanceus5_alldata.filter(data => data.x > binanceus5_x1)]
    //             binanceus5_every_other_tracker+=1;
    //         }else{
    //             binanceus5_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binanceus5_data = JSON.parse(event.data);
    //         let binanceus5_data_dict = {'x':binanceus5_data['E'], 'y':parseFloat(binanceus5_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binanceus5_data_dict.x>binanceus5_x2) binanceus5_x2 = binanceus5_data_dict.x;
    //         if (binanceus5_data_dict.x<binanceus5_x1) binanceus5_x1 = binanceus5_data_dict.x;
    //         if (binanceus5_data_dict.y>binanceus5_y2) binanceus5_y2 = binanceus5_data_dict.y;
    //         if (binanceus5_data_dict.y<binanceus5_y1) binanceus5_y1 = binanceus5_data_dict.y;
    //         // if (binanceus5_x2-binanceus5_x1>60000) binanceus5_x1 = binanceus5_x2-60000
    //         if (binanceus5_x2-binanceus5_x1>86400000) binanceus5_x1 = binanceus5_x2-86400000;
    //         //store the last price received.
    //         binanceus5_current_price=binanceus5_data_dict.x;
    //         binanceus5_alldata.push(binanceus5_data_dict);
    //         binanceus5_alldata=[...binanceus5_alldata.filter(data => data.x > binanceus5_x1)]
    //         // console.log(binanceus5_alldata[binanceus5_alldata.length-1]);
    //     }
        
    // }

    // let binanceus6_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binanceus6_x1 = +Infinity;
    // let binanceus6_x2 = -Infinity;
    // let binanceus6_y1 = +Infinity;
    // let binanceus6_y2 = -Infinity;
    // let binanceus6_alldata = [];
    // let binanceus6_current_price;

    // var binanceus6_every_other_toggle = true;
    // var binanceus6_every_other_tracker = 0;
    // var binanceus6_get_nth_msg_to_get = 100;
    // binanceus6_socket.onmessage = function (event) {
    //     if(binanceus6_every_other_toggle){
    //         if(binanceus6_every_other_tracker%binanceus6_get_nth_msg_to_get==0){
    //             var binanceus6_data = JSON.parse(event.data);
    //             let binanceus6_data_dict = {'x':binanceus6_data['E'], 'y':parseFloat(binanceus6_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binanceus6_data_dict.x>binanceus6_x2) binanceus6_x2 = binanceus6_data_dict.x;
    //             if (binanceus6_data_dict.x<binanceus6_x1) binanceus6_x1 = binanceus6_data_dict.x;
    //             if (binanceus6_data_dict.y>binanceus6_y2) binanceus6_y2 = binanceus6_data_dict.y;
    //             if (binanceus6_data_dict.y<binanceus6_y1) binanceus6_y1 = binanceus6_data_dict.y;
    //             // if (binanceus6_x2-binanceus6_x1>60000) binanceus6_x1 = binanceus6_x2-60000
    //             if (binanceus6_x2-binanceus6_x1>86400000) binanceus6_x1 = binanceus6_x2-86400000;
                
    //             //store the last price received.
    //             binanceus6_current_price=binanceus6_data_dict.y;

    //             binanceus6_alldata.push(binanceus6_data_dict);
    //             binanceus6_alldata=[...binanceus6_alldata.filter(data => data.x > binanceus6_x1)]
    //             binanceus6_every_other_tracker+=1;
    //         }else{
    //             binanceus6_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binanceus6_data = JSON.parse(event.data);
    //         let binanceus6_data_dict = {'x':binanceus6_data['E'], 'y':parseFloat(binanceus6_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binanceus6_data_dict.x>binanceus6_x2) binanceus6_x2 = binanceus6_data_dict.x;
    //         if (binanceus6_data_dict.x<binanceus6_x1) binanceus6_x1 = binanceus6_data_dict.x;
    //         if (binanceus6_data_dict.y>binanceus6_y2) binanceus6_y2 = binanceus6_data_dict.y;
    //         if (binanceus6_data_dict.y<binanceus6_y1) binanceus6_y1 = binanceus6_data_dict.y;
    //         // if (binanceus6_x2-binanceus6_x1>60000) binanceus6_x1 = binanceus6_x2-60000
    //         if (binanceus6_x2-binanceus6_x1>86400000) binanceus6_x1 = binanceus6_x2-86400000;
    //         //store the last price received.
    //         binanceus6_current_price=binanceus6_data_dict.x;
    //         binanceus6_alldata.push(binanceus6_data_dict);
    //         binanceus6_alldata=[...binanceus6_alldata.filter(data => data.x > binanceus6_x1)]
    //         // console.log(binanceus6_alldata[binanceus6_alldata.length-1]);
    //     }
        
    // }

    // let binance1_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binance1_x1 = +Infinity;
    // let binance1_x2 = -Infinity;
    // let binance1_y1 = +Infinity;
    // let binance1_y2 = -Infinity;
    // let binance1_alldata = [];
    // let binance1_current_price;

    // var binance1_every_other_toggle = true;
    // var binance1_every_other_tracker = 0;
    // var binance1_get_nth_msg_to_get = 100;
    // binance1_socket.onmessage = function (event) {
    //     if(binance1_every_other_toggle){
    //         if(binance1_every_other_tracker%binance1_get_nth_msg_to_get==0){
    //             var binance1_data = JSON.parse(event.data);
    //             let binance1_data_dict = {'x':binance1_data['E'], 'y':parseFloat(binance1_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binance1_data_dict.x>binance1_x2) binance1_x2 = binance1_data_dict.x;
    //             if (binance1_data_dict.x<binance1_x1) binance1_x1 = binance1_data_dict.x;
    //             if (binance1_data_dict.y>binance1_y2) binance1_y2 = binance1_data_dict.y;
    //             if (binance1_data_dict.y<binance1_y1) binance1_y1 = binance1_data_dict.y;
    //             // if (binance1_x2-binance1_x1>60000) binance1_x1 = binance1_x2-60000
    //             if (binance1_x2-binance1_x1>86400000) binance1_x1 = binance1_x2-86400000;
                
    //             //store the last price received.
    //             binance1_current_price=binance1_data_dict.y;

    //             binance1_alldata.push(binance1_data_dict);
    //             binance1_alldata=[...binance1_alldata.filter(data => data.x > binance1_x1)]
    //             binance1_every_other_tracker+=1;
    //         }else{
    //             binance1_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binance1_data = JSON.parse(event.data);
    //         let binance1_data_dict = {'x':binance1_data['E'], 'y':parseFloat(binance1_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binance1_data_dict.x>binance1_x2) binance1_x2 = binance1_data_dict.x;
    //         if (binance1_data_dict.x<binance1_x1) binance1_x1 = binance1_data_dict.x;
    //         if (binance1_data_dict.y>binance1_y2) binance1_y2 = binance1_data_dict.y;
    //         if (binance1_data_dict.y<binance1_y1) binance1_y1 = binance1_data_dict.y;
    //         // if (binance1_x2-binance1_x1>60000) binance1_x1 = binance1_x2-60000
    //         if (binance1_x2-binance1_x1>86400000) binance1_x1 = binance1_x2-86400000;
    //         //store the last price received.
    //         binance1_current_price=binance1_data_dict.x;
    //         binance1_alldata.push(binance1_data_dict);
    //         binance1_alldata=[...binance1_alldata.filter(data => data.x > binance1_x1)]
    //         // console.log(binance1_alldata[binance1_alldata.length-1]);
    //     }
        
    // }

    // let binance2_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binance2_x1 = +Infinity;
    // let binance2_x2 = -Infinity;
    // let binance2_y1 = +Infinity;
    // let binance2_y2 = -Infinity;
    // let binance2_alldata = [];
    // let binance2_current_price;

    // var binance2_every_other_toggle = true;
    // var binance2_every_other_tracker = 0;
    // var binance2_get_nth_msg_to_get = 100;
    // binance2_socket.onmessage = function (event) {
    //     if(binance2_every_other_toggle){
    //         if(binance2_every_other_tracker%binance2_get_nth_msg_to_get==0){
    //             var binance2_data = JSON.parse(event.data);
    //             let binance2_data_dict = {'x':binance2_data['E'], 'y':parseFloat(binance2_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binance2_data_dict.x>binance2_x2) binance2_x2 = binance2_data_dict.x;
    //             if (binance2_data_dict.x<binance2_x1) binance2_x1 = binance2_data_dict.x;
    //             if (binance2_data_dict.y>binance2_y2) binance2_y2 = binance2_data_dict.y;
    //             if (binance2_data_dict.y<binance2_y1) binance2_y1 = binance2_data_dict.y;
    //             // if (binance2_x2-binance2_x1>60000) binance2_x1 = binance2_x2-60000
    //             if (binance2_x2-binance2_x1>86400000) binance2_x1 = binance2_x2-86400000;
                
    //             //store the last price received.
    //             binance2_current_price=binance2_data_dict.y;

    //             binance2_alldata.push(binance2_data_dict);
    //             binance2_alldata=[...binance2_alldata.filter(data => data.x > binance2_x1)]
    //             binance2_every_other_tracker+=1;
    //         }else{
    //             binance2_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binance2_data = JSON.parse(event.data);
    //         let binance2_data_dict = {'x':binance2_data['E'], 'y':parseFloat(binance2_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binance2_data_dict.x>binance2_x2) binance2_x2 = binance2_data_dict.x;
    //         if (binance2_data_dict.x<binance2_x1) binance2_x1 = binance2_data_dict.x;
    //         if (binance2_data_dict.y>binance2_y2) binance2_y2 = binance2_data_dict.y;
    //         if (binance2_data_dict.y<binance2_y1) binance2_y1 = binance2_data_dict.y;
    //         // if (binance2_x2-binance2_x1>60000) binance2_x1 = binance2_x2-60000
    //         if (binance2_x2-binance2_x1>86400000) binance2_x1 = binance2_x2-86400000;
    //         //store the last price received.
    //         binance2_current_price=binance2_data_dict.x;
    //         binance2_alldata.push(binance2_data_dict);
    //         binance2_alldata=[...binance2_alldata.filter(data => data.x > binance2_x1)]
    //         // console.log(binance2_alldata[binance2_alldata.length-1]);
    //     }
        
    // }

    // let binance3_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binance3_x1 = +Infinity;
    // let binance3_x2 = -Infinity;
    // let binance3_y1 = +Infinity;
    // let binance3_y2 = -Infinity;
    // let binance3_alldata = [];
    // let binance3_current_price;

    // var binance3_every_other_toggle = true;
    // var binance3_every_other_tracker = 0;
    // var binance3_get_nth_msg_to_get = 100;
    // binance3_socket.onmessage = function (event) {
    //     if(binance3_every_other_toggle){
    //         if(binance3_every_other_tracker%binance3_get_nth_msg_to_get==0){
    //             var binance3_data = JSON.parse(event.data);
    //             let binance3_data_dict = {'x':binance3_data['E'], 'y':parseFloat(binance3_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binance3_data_dict.x>binance3_x2) binance3_x2 = binance3_data_dict.x;
    //             if (binance3_data_dict.x<binance3_x1) binance3_x1 = binance3_data_dict.x;
    //             if (binance3_data_dict.y>binance3_y2) binance3_y2 = binance3_data_dict.y;
    //             if (binance3_data_dict.y<binance3_y1) binance3_y1 = binance3_data_dict.y;
    //             // if (binance3_x2-binance3_x1>60000) binance3_x1 = binance3_x2-60000
    //             if (binance3_x2-binance3_x1>86400000) binance3_x1 = binance3_x2-86400000;
                
    //             //store the last price received.
    //             binance3_current_price=binance3_data_dict.y;

    //             binance3_alldata.push(binance3_data_dict);
    //             binance3_alldata=[...binance3_alldata.filter(data => data.x > binance3_x1)]
    //             binance3_every_other_tracker+=1;
    //         }else{
    //             binance3_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binance3_data = JSON.parse(event.data);
    //         let binance3_data_dict = {'x':binance3_data['E'], 'y':parseFloat(binance3_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binance3_data_dict.x>binance3_x2) binance3_x2 = binance3_data_dict.x;
    //         if (binance3_data_dict.x<binance3_x1) binance3_x1 = binance3_data_dict.x;
    //         if (binance3_data_dict.y>binance3_y2) binance3_y2 = binance3_data_dict.y;
    //         if (binance3_data_dict.y<binance3_y1) binance3_y1 = binance3_data_dict.y;
    //         // if (binance3_x2-binance3_x1>60000) binance3_x1 = binance3_x2-60000
    //         if (binance3_x2-binance3_x1>86400000) binance3_x1 = binance3_x2-86400000;
    //         //store the last price received.
    //         binance3_current_price=binance3_data_dict.x;
    //         binance3_alldata.push(binance3_data_dict);
    //         binance3_alldata=[...binance3_alldata.filter(data => data.x > binance3_x1)]
    //         // console.log(binance3_alldata[binance3_alldata.length-1]);
    //     }
        
    // }

    // let binance4_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binance4_x1 = +Infinity;
    // let binance4_x2 = -Infinity;
    // let binance4_y1 = +Infinity;
    // let binance4_y2 = -Infinity;
    // let binance4_alldata = [];
    // let binance4_current_price;

    // var binance4_every_other_toggle = true;
    // var binance4_every_other_tracker = 0;
    // var binance4_get_nth_msg_to_get = 100;
    // binance4_socket.onmessage = function (event) {
    //     if(binance4_every_other_toggle){
    //         if(binance4_every_other_tracker%binance4_get_nth_msg_to_get==0){
    //             var binance4_data = JSON.parse(event.data);
    //             let binance4_data_dict = {'x':binance4_data['E'], 'y':parseFloat(binance4_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binance4_data_dict.x>binance4_x2) binance4_x2 = binance4_data_dict.x;
    //             if (binance4_data_dict.x<binance4_x1) binance4_x1 = binance4_data_dict.x;
    //             if (binance4_data_dict.y>binance4_y2) binance4_y2 = binance4_data_dict.y;
    //             if (binance4_data_dict.y<binance4_y1) binance4_y1 = binance4_data_dict.y;
    //             // if (binance4_x2-binance4_x1>60000) binance4_x1 = binance4_x2-60000
    //             if (binance4_x2-binance4_x1>86400000) binance4_x1 = binance4_x2-86400000;
                
    //             //store the last price received.
    //             binance4_current_price=binance4_data_dict.y;

    //             binance4_alldata.push(binance4_data_dict);
    //             binance4_alldata=[...binance4_alldata.filter(data => data.x > binance4_x1)]
    //             binance4_every_other_tracker+=1;
    //         }else{
    //             binance4_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binance4_data = JSON.parse(event.data);
    //         let binance4_data_dict = {'x':binance4_data['E'], 'y':parseFloat(binance4_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binance4_data_dict.x>binance4_x2) binance4_x2 = binance4_data_dict.x;
    //         if (binance4_data_dict.x<binance4_x1) binance4_x1 = binance4_data_dict.x;
    //         if (binance4_data_dict.y>binance4_y2) binance4_y2 = binance4_data_dict.y;
    //         if (binance4_data_dict.y<binance4_y1) binance4_y1 = binance4_data_dict.y;
    //         // if (binance4_x2-binance4_x1>60000) binance4_x1 = binance4_x2-60000
    //         if (binance4_x2-binance4_x1>86400000) binance4_x1 = binance4_x2-86400000;
    //         //store the last price received.
    //         binance4_current_price=binance4_data_dict.x;
    //         binance4_alldata.push(binance4_data_dict);
    //         binance4_alldata=[...binance4_alldata.filter(data => data.x > binance4_x1)]
    //         // console.log(binance4_alldata[binance4_alldata.length-1]);
    //     }
        
    // }

    // let binance5_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binance5_x1 = +Infinity;
    // let binance5_x2 = -Infinity;
    // let binance5_y1 = +Infinity;
    // let binance5_y2 = -Infinity;
    // let binance5_alldata = [];
    // let binance5_current_price;

    // var binance5_every_other_toggle = true;
    // var binance5_every_other_tracker = 0;
    // var binance5_get_nth_msg_to_get = 100;
    // binance5_socket.onmessage = function (event) {
    //     if(binance5_every_other_toggle){
    //         if(binance5_every_other_tracker%binance5_get_nth_msg_to_get==0){
    //             var binance5_data = JSON.parse(event.data);
    //             let binance5_data_dict = {'x':binance5_data['E'], 'y':parseFloat(binance5_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binance5_data_dict.x>binance5_x2) binance5_x2 = binance5_data_dict.x;
    //             if (binance5_data_dict.x<binance5_x1) binance5_x1 = binance5_data_dict.x;
    //             if (binance5_data_dict.y>binance5_y2) binance5_y2 = binance5_data_dict.y;
    //             if (binance5_data_dict.y<binance5_y1) binance5_y1 = binance5_data_dict.y;
    //             // if (binance5_x2-binance5_x1>60000) binance5_x1 = binance5_x2-60000
    //             if (binance5_x2-binance5_x1>86400000) binance5_x1 = binance5_x2-86400000;
                
    //             //store the last price received.
    //             binance5_current_price=binance5_data_dict.y;

    //             binance5_alldata.push(binance5_data_dict);
    //             binance5_alldata=[...binance5_alldata.filter(data => data.x > binance5_x1)]
    //             binance5_every_other_tracker+=1;
    //         }else{
    //             binance5_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binance5_data = JSON.parse(event.data);
    //         let binance5_data_dict = {'x':binance5_data['E'], 'y':parseFloat(binance5_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binance5_data_dict.x>binance5_x2) binance5_x2 = binance5_data_dict.x;
    //         if (binance5_data_dict.x<binance5_x1) binance5_x1 = binance5_data_dict.x;
    //         if (binance5_data_dict.y>binance5_y2) binance5_y2 = binance5_data_dict.y;
    //         if (binance5_data_dict.y<binance5_y1) binance5_y1 = binance5_data_dict.y;
    //         // if (binance5_x2-binance5_x1>60000) binance5_x1 = binance5_x2-60000
    //         if (binance5_x2-binance5_x1>86400000) binance5_x1 = binance5_x2-86400000;
    //         //store the last price received.
    //         binance5_current_price=binance5_data_dict.x;
    //         binance5_alldata.push(binance5_data_dict);
    //         binance5_alldata=[...binance5_alldata.filter(data => data.x > binance5_x1)]
    //         // console.log(binance5_alldata[binance5_alldata.length-1]);
    //     }
        
    // }

    // let binance6_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let binance6_x1 = +Infinity;
    // let binance6_x2 = -Infinity;
    // let binance6_y1 = +Infinity;
    // let binance6_y2 = -Infinity;
    // let binance6_alldata = [];
    // let binance6_current_price;

    // var binance6_every_other_toggle = true;
    // var binance6_every_other_tracker = 0;
    // var binance6_get_nth_msg_to_get = 100;
    // binance6_socket.onmessage = function (event) {
    //     if(binance6_every_other_toggle){
    //         if(binance6_every_other_tracker%binance6_get_nth_msg_to_get==0){
    //             var binance6_data = JSON.parse(event.data);
    //             let binance6_data_dict = {'x':binance6_data['E'], 'y':parseFloat(binance6_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (binance6_data_dict.x>binance6_x2) binance6_x2 = binance6_data_dict.x;
    //             if (binance6_data_dict.x<binance6_x1) binance6_x1 = binance6_data_dict.x;
    //             if (binance6_data_dict.y>binance6_y2) binance6_y2 = binance6_data_dict.y;
    //             if (binance6_data_dict.y<binance6_y1) binance6_y1 = binance6_data_dict.y;
    //             // if (binance6_x2-binance6_x1>60000) binance6_x1 = binance6_x2-60000
    //             if (binance6_x2-binance6_x1>86400000) binance6_x1 = binance6_x2-86400000;
                
    //             //store the last price received.
    //             binance6_current_price=binance6_data_dict.y;

    //             binance6_alldata.push(binance6_data_dict);
    //             binance6_alldata=[...binance6_alldata.filter(data => data.x > binance6_x1)]
    //             binance6_every_other_tracker+=1;
    //         }else{
    //             binance6_every_other_tracker+=1;
    //         }
    //     }else{
    //         var binance6_data = JSON.parse(event.data);
    //         let binance6_data_dict = {'x':binance6_data['E'], 'y':parseFloat(binance6_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (binance6_data_dict.x>binance6_x2) binance6_x2 = binance6_data_dict.x;
    //         if (binance6_data_dict.x<binance6_x1) binance6_x1 = binance6_data_dict.x;
    //         if (binance6_data_dict.y>binance6_y2) binance6_y2 = binance6_data_dict.y;
    //         if (binance6_data_dict.y<binance6_y1) binance6_y1 = binance6_data_dict.y;
    //         // if (binance6_x2-binance6_x1>60000) binance6_x1 = binance6_x2-60000
    //         if (binance6_x2-binance6_x1>86400000) binance6_x1 = binance6_x2-86400000;
    //         //store the last price received.
    //         binance6_current_price=binance6_data_dict.x;
    //         binance6_alldata.push(binance6_data_dict);
    //         binance6_alldata=[...binance6_alldata.filter(data => data.x > binance6_x1)]
    //         // console.log(binance6_alldata[binance6_alldata.length-1]);
    //     }
        
    // }

    // let coinbasepro1_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbasepro1_x1 = +Infinity;
    // let coinbasepro1_x2 = -Infinity;
    // let coinbasepro1_y1 = +Infinity;
    // let coinbasepro1_y2 = -Infinity;
    // let coinbasepro1_alldata = [];
    // let coinbasepro1_current_price;

    // var coinbasepro1_every_other_toggle = true;
    // var coinbasepro1_every_other_tracker = 0;
    // var coinbasepro1_get_nth_msg_to_get = 100;
    // coinbasepro1_socket.onmessage = function (event) {
    //     if(coinbasepro1_every_other_toggle){
    //         if(coinbasepro1_every_other_tracker%coinbasepro1_get_nth_msg_to_get==0){
    //             var coinbasepro1_data = JSON.parse(event.data);
    //             let coinbasepro1_data_dict = {'x':coinbasepro1_data['E'], 'y':parseFloat(coinbasepro1_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbasepro1_data_dict.x>coinbasepro1_x2) coinbasepro1_x2 = coinbasepro1_data_dict.x;
    //             if (coinbasepro1_data_dict.x<coinbasepro1_x1) coinbasepro1_x1 = coinbasepro1_data_dict.x;
    //             if (coinbasepro1_data_dict.y>coinbasepro1_y2) coinbasepro1_y2 = coinbasepro1_data_dict.y;
    //             if (coinbasepro1_data_dict.y<coinbasepro1_y1) coinbasepro1_y1 = coinbasepro1_data_dict.y;
    //             // if (coinbasepro1_x2-coinbasepro1_x1>60000) coinbasepro1_x1 = coinbasepro1_x2-60000
    //             if (coinbasepro1_x2-coinbasepro1_x1>86400000) coinbasepro1_x1 = coinbasepro1_x2-86400000;
                
    //             //store the last price received.
    //             coinbasepro1_current_price=coinbasepro1_data_dict.y;

    //             coinbasepro1_alldata.push(coinbasepro1_data_dict);
    //             coinbasepro1_alldata=[...coinbasepro1_alldata.filter(data => data.x > coinbasepro1_x1)]
    //             coinbasepro1_every_other_tracker+=1;
    //         }else{
    //             coinbasepro1_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbasepro1_data = JSON.parse(event.data);
    //         let coinbasepro1_data_dict = {'x':coinbasepro1_data['E'], 'y':parseFloat(coinbasepro1_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbasepro1_data_dict.x>coinbasepro1_x2) coinbasepro1_x2 = coinbasepro1_data_dict.x;
    //         if (coinbasepro1_data_dict.x<coinbasepro1_x1) coinbasepro1_x1 = coinbasepro1_data_dict.x;
    //         if (coinbasepro1_data_dict.y>coinbasepro1_y2) coinbasepro1_y2 = coinbasepro1_data_dict.y;
    //         if (coinbasepro1_data_dict.y<coinbasepro1_y1) coinbasepro1_y1 = coinbasepro1_data_dict.y;
    //         // if (coinbasepro1_x2-coinbasepro1_x1>60000) coinbasepro1_x1 = coinbasepro1_x2-60000
    //         if (coinbasepro1_x2-coinbasepro1_x1>86400000) coinbasepro1_x1 = coinbasepro1_x2-86400000;
    //         //store the last price received.
    //         coinbasepro1_current_price=coinbasepro1_data_dict.x;
    //         coinbasepro1_alldata.push(coinbasepro1_data_dict);
    //         coinbasepro1_alldata=[...coinbasepro1_alldata.filter(data => data.x > coinbasepro1_x1)]
    //         // console.log(coinbasepro1_alldata[coinbasepro1_alldata.length-1]);
    //     }
        
    // }

    // let coinbasepro2_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbasepro2_x1 = +Infinity;
    // let coinbasepro2_x2 = -Infinity;
    // let coinbasepro2_y1 = +Infinity;
    // let coinbasepro2_y2 = -Infinity;
    // let coinbasepro2_alldata = [];
    // let coinbasepro2_current_price;

    // var coinbasepro2_every_other_toggle = true;
    // var coinbasepro2_every_other_tracker = 0;
    // var coinbasepro2_get_nth_msg_to_get = 100;
    // coinbasepro2_socket.onmessage = function (event) {
    //     if(coinbasepro2_every_other_toggle){
    //         if(coinbasepro2_every_other_tracker%coinbasepro2_get_nth_msg_to_get==0){
    //             var coinbasepro2_data = JSON.parse(event.data);
    //             let coinbasepro2_data_dict = {'x':coinbasepro2_data['E'], 'y':parseFloat(coinbasepro2_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbasepro2_data_dict.x>coinbasepro2_x2) coinbasepro2_x2 = coinbasepro2_data_dict.x;
    //             if (coinbasepro2_data_dict.x<coinbasepro2_x1) coinbasepro2_x1 = coinbasepro2_data_dict.x;
    //             if (coinbasepro2_data_dict.y>coinbasepro2_y2) coinbasepro2_y2 = coinbasepro2_data_dict.y;
    //             if (coinbasepro2_data_dict.y<coinbasepro2_y1) coinbasepro2_y1 = coinbasepro2_data_dict.y;
    //             // if (coinbasepro2_x2-coinbasepro2_x1>60000) coinbasepro2_x1 = coinbasepro2_x2-60000
    //             if (coinbasepro2_x2-coinbasepro2_x1>86400000) coinbasepro2_x1 = coinbasepro2_x2-86400000;
                
    //             //store the last price received.
    //             coinbasepro2_current_price=coinbasepro2_data_dict.y;

    //             coinbasepro2_alldata.push(coinbasepro2_data_dict);
    //             coinbasepro2_alldata=[...coinbasepro2_alldata.filter(data => data.x > coinbasepro2_x1)]
    //             coinbasepro2_every_other_tracker+=1;
    //         }else{
    //             coinbasepro2_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbasepro2_data = JSON.parse(event.data);
    //         let coinbasepro2_data_dict = {'x':coinbasepro2_data['E'], 'y':parseFloat(coinbasepro2_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbasepro2_data_dict.x>coinbasepro2_x2) coinbasepro2_x2 = coinbasepro2_data_dict.x;
    //         if (coinbasepro2_data_dict.x<coinbasepro2_x1) coinbasepro2_x1 = coinbasepro2_data_dict.x;
    //         if (coinbasepro2_data_dict.y>coinbasepro2_y2) coinbasepro2_y2 = coinbasepro2_data_dict.y;
    //         if (coinbasepro2_data_dict.y<coinbasepro2_y1) coinbasepro2_y1 = coinbasepro2_data_dict.y;
    //         // if (coinbasepro2_x2-coinbasepro2_x1>60000) coinbasepro2_x1 = coinbasepro2_x2-60000
    //         if (coinbasepro2_x2-coinbasepro2_x1>86400000) coinbasepro2_x1 = coinbasepro2_x2-86400000;
    //         //store the last price received.
    //         coinbasepro2_current_price=coinbasepro2_data_dict.x;
    //         coinbasepro2_alldata.push(coinbasepro2_data_dict);
    //         coinbasepro2_alldata=[...coinbasepro2_alldata.filter(data => data.x > coinbasepro2_x1)]
    //         // console.log(coinbasepro2_alldata[coinbasepro2_alldata.length-1]);
    //     }
        
    // }

    // let coinbasepro3_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbasepro3_x1 = +Infinity;
    // let coinbasepro3_x2 = -Infinity;
    // let coinbasepro3_y1 = +Infinity;
    // let coinbasepro3_y2 = -Infinity;
    // let coinbasepro3_alldata = [];
    // let coinbasepro3_current_price;

    // var coinbasepro3_every_other_toggle = true;
    // var coinbasepro3_every_other_tracker = 0;
    // var coinbasepro3_get_nth_msg_to_get = 100;
    // coinbasepro3_socket.onmessage = function (event) {
    //     if(coinbasepro3_every_other_toggle){
    //         if(coinbasepro3_every_other_tracker%coinbasepro3_get_nth_msg_to_get==0){
    //             var coinbasepro3_data = JSON.parse(event.data);
    //             let coinbasepro3_data_dict = {'x':coinbasepro3_data['E'], 'y':parseFloat(coinbasepro3_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbasepro3_data_dict.x>coinbasepro3_x2) coinbasepro3_x2 = coinbasepro3_data_dict.x;
    //             if (coinbasepro3_data_dict.x<coinbasepro3_x1) coinbasepro3_x1 = coinbasepro3_data_dict.x;
    //             if (coinbasepro3_data_dict.y>coinbasepro3_y2) coinbasepro3_y2 = coinbasepro3_data_dict.y;
    //             if (coinbasepro3_data_dict.y<coinbasepro3_y1) coinbasepro3_y1 = coinbasepro3_data_dict.y;
    //             // if (coinbasepro3_x2-coinbasepro3_x1>60000) coinbasepro3_x1 = coinbasepro3_x2-60000
    //             if (coinbasepro3_x2-coinbasepro3_x1>86400000) coinbasepro3_x1 = coinbasepro3_x2-86400000;
                
    //             //store the last price received.
    //             coinbasepro3_current_price=coinbasepro3_data_dict.y;

    //             coinbasepro3_alldata.push(coinbasepro3_data_dict);
    //             coinbasepro3_alldata=[...coinbasepro3_alldata.filter(data => data.x > coinbasepro3_x1)]
    //             coinbasepro3_every_other_tracker+=1;
    //         }else{
    //             coinbasepro3_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbasepro3_data = JSON.parse(event.data);
    //         let coinbasepro3_data_dict = {'x':coinbasepro3_data['E'], 'y':parseFloat(coinbasepro3_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbasepro3_data_dict.x>coinbasepro3_x2) coinbasepro3_x2 = coinbasepro3_data_dict.x;
    //         if (coinbasepro3_data_dict.x<coinbasepro3_x1) coinbasepro3_x1 = coinbasepro3_data_dict.x;
    //         if (coinbasepro3_data_dict.y>coinbasepro3_y2) coinbasepro3_y2 = coinbasepro3_data_dict.y;
    //         if (coinbasepro3_data_dict.y<coinbasepro3_y1) coinbasepro3_y1 = coinbasepro3_data_dict.y;
    //         // if (coinbasepro3_x2-coinbasepro3_x1>60000) coinbasepro3_x1 = coinbasepro3_x2-60000
    //         if (coinbasepro3_x2-coinbasepro3_x1>86400000) coinbasepro3_x1 = coinbasepro3_x2-86400000;
    //         //store the last price received.
    //         coinbasepro3_current_price=coinbasepro3_data_dict.x;
    //         coinbasepro3_alldata.push(coinbasepro3_data_dict);
    //         coinbasepro3_alldata=[...coinbasepro3_alldata.filter(data => data.x > coinbasepro3_x1)]
    //         // console.log(coinbasepro3_alldata[coinbasepro3_alldata.length-1]);
    //     }
        
    // }

    // let coinbasepro4_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbasepro4_x1 = +Infinity;
    // let coinbasepro4_x2 = -Infinity;
    // let coinbasepro4_y1 = +Infinity;
    // let coinbasepro4_y2 = -Infinity;
    // let coinbasepro4_alldata = [];
    // let coinbasepro4_current_price;

    // var coinbasepro4_every_other_toggle = true;
    // var coinbasepro4_every_other_tracker = 0;
    // var coinbasepro4_get_nth_msg_to_get = 100;
    // coinbasepro4_socket.onmessage = function (event) {
    //     if(coinbasepro4_every_other_toggle){
    //         if(coinbasepro4_every_other_tracker%coinbasepro4_get_nth_msg_to_get==0){
    //             var coinbasepro4_data = JSON.parse(event.data);
    //             let coinbasepro4_data_dict = {'x':coinbasepro4_data['E'], 'y':parseFloat(coinbasepro4_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbasepro4_data_dict.x>coinbasepro4_x2) coinbasepro4_x2 = coinbasepro4_data_dict.x;
    //             if (coinbasepro4_data_dict.x<coinbasepro4_x1) coinbasepro4_x1 = coinbasepro4_data_dict.x;
    //             if (coinbasepro4_data_dict.y>coinbasepro4_y2) coinbasepro4_y2 = coinbasepro4_data_dict.y;
    //             if (coinbasepro4_data_dict.y<coinbasepro4_y1) coinbasepro4_y1 = coinbasepro4_data_dict.y;
    //             // if (coinbasepro4_x2-coinbasepro4_x1>60000) coinbasepro4_x1 = coinbasepro4_x2-60000
    //             if (coinbasepro4_x2-coinbasepro4_x1>86400000) coinbasepro4_x1 = coinbasepro4_x2-86400000;
                
    //             //store the last price received.
    //             coinbasepro4_current_price=coinbasepro4_data_dict.y;

    //             coinbasepro4_alldata.push(coinbasepro4_data_dict);
    //             coinbasepro4_alldata=[...coinbasepro4_alldata.filter(data => data.x > coinbasepro4_x1)]
    //             coinbasepro4_every_other_tracker+=1;
    //         }else{
    //             coinbasepro4_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbasepro4_data = JSON.parse(event.data);
    //         let coinbasepro4_data_dict = {'x':coinbasepro4_data['E'], 'y':parseFloat(coinbasepro4_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbasepro4_data_dict.x>coinbasepro4_x2) coinbasepro4_x2 = coinbasepro4_data_dict.x;
    //         if (coinbasepro4_data_dict.x<coinbasepro4_x1) coinbasepro4_x1 = coinbasepro4_data_dict.x;
    //         if (coinbasepro4_data_dict.y>coinbasepro4_y2) coinbasepro4_y2 = coinbasepro4_data_dict.y;
    //         if (coinbasepro4_data_dict.y<coinbasepro4_y1) coinbasepro4_y1 = coinbasepro4_data_dict.y;
    //         // if (coinbasepro4_x2-coinbasepro4_x1>60000) coinbasepro4_x1 = coinbasepro4_x2-60000
    //         if (coinbasepro4_x2-coinbasepro4_x1>86400000) coinbasepro4_x1 = coinbasepro4_x2-86400000;
    //         //store the last price received.
    //         coinbasepro4_current_price=coinbasepro4_data_dict.x;
    //         coinbasepro4_alldata.push(coinbasepro4_data_dict);
    //         coinbasepro4_alldata=[...coinbasepro4_alldata.filter(data => data.x > coinbasepro4_x1)]
    //         // console.log(coinbasepro4_alldata[coinbasepro4_alldata.length-1]);
    //     }
        
    // }

    // let coinbasepro5_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbasepro5_x1 = +Infinity;
    // let coinbasepro5_x2 = -Infinity;
    // let coinbasepro5_y1 = +Infinity;
    // let coinbasepro5_y2 = -Infinity;
    // let coinbasepro5_alldata = [];
    // let coinbasepro5_current_price;

    // var coinbasepro5_every_other_toggle = true;
    // var coinbasepro5_every_other_tracker = 0;
    // var coinbasepro5_get_nth_msg_to_get = 100;
    // coinbasepro5_socket.onmessage = function (event) {
    //     if(coinbasepro5_every_other_toggle){
    //         if(coinbasepro5_every_other_tracker%coinbasepro5_get_nth_msg_to_get==0){
    //             var coinbasepro5_data = JSON.parse(event.data);
    //             let coinbasepro5_data_dict = {'x':coinbasepro5_data['E'], 'y':parseFloat(coinbasepro5_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbasepro5_data_dict.x>coinbasepro5_x2) coinbasepro5_x2 = coinbasepro5_data_dict.x;
    //             if (coinbasepro5_data_dict.x<coinbasepro5_x1) coinbasepro5_x1 = coinbasepro5_data_dict.x;
    //             if (coinbasepro5_data_dict.y>coinbasepro5_y2) coinbasepro5_y2 = coinbasepro5_data_dict.y;
    //             if (coinbasepro5_data_dict.y<coinbasepro5_y1) coinbasepro5_y1 = coinbasepro5_data_dict.y;
    //             // if (coinbasepro5_x2-coinbasepro5_x1>60000) coinbasepro5_x1 = coinbasepro5_x2-60000
    //             if (coinbasepro5_x2-coinbasepro5_x1>86400000) coinbasepro5_x1 = coinbasepro5_x2-86400000;
                
    //             //store the last price received.
    //             coinbasepro5_current_price=coinbasepro5_data_dict.y;

    //             coinbasepro5_alldata.push(coinbasepro5_data_dict);
    //             coinbasepro5_alldata=[...coinbasepro5_alldata.filter(data => data.x > coinbasepro5_x1)]
    //             coinbasepro5_every_other_tracker+=1;
    //         }else{
    //             coinbasepro5_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbasepro5_data = JSON.parse(event.data);
    //         let coinbasepro5_data_dict = {'x':coinbasepro5_data['E'], 'y':parseFloat(coinbasepro5_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbasepro5_data_dict.x>coinbasepro5_x2) coinbasepro5_x2 = coinbasepro5_data_dict.x;
    //         if (coinbasepro5_data_dict.x<coinbasepro5_x1) coinbasepro5_x1 = coinbasepro5_data_dict.x;
    //         if (coinbasepro5_data_dict.y>coinbasepro5_y2) coinbasepro5_y2 = coinbasepro5_data_dict.y;
    //         if (coinbasepro5_data_dict.y<coinbasepro5_y1) coinbasepro5_y1 = coinbasepro5_data_dict.y;
    //         // if (coinbasepro5_x2-coinbasepro5_x1>60000) coinbasepro5_x1 = coinbasepro5_x2-60000
    //         if (coinbasepro5_x2-coinbasepro5_x1>86400000) coinbasepro5_x1 = coinbasepro5_x2-86400000;
    //         //store the last price received.
    //         coinbasepro5_current_price=coinbasepro5_data_dict.x;
    //         coinbasepro5_alldata.push(coinbasepro5_data_dict);
    //         coinbasepro5_alldata=[...coinbasepro5_alldata.filter(data => data.x > coinbasepro5_x1)]
    //         // console.log(coinbasepro5_alldata[coinbasepro5_alldata.length-1]);
    //     }
        
    // }

    // let coinbasepro6_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbasepro6_x1 = +Infinity;
    // let coinbasepro6_x2 = -Infinity;
    // let coinbasepro6_y1 = +Infinity;
    // let coinbasepro6_y2 = -Infinity;
    // let coinbasepro6_alldata = [];
    // let coinbasepro6_current_price;

    // var coinbasepro6_every_other_toggle = true;
    // var coinbasepro6_every_other_tracker = 0;
    // var coinbasepro6_get_nth_msg_to_get = 100;
    // coinbasepro6_socket.onmessage = function (event) {
    //     if(coinbasepro6_every_other_toggle){
    //         if(coinbasepro6_every_other_tracker%coinbasepro6_get_nth_msg_to_get==0){
    //             var coinbasepro6_data = JSON.parse(event.data);
    //             let coinbasepro6_data_dict = {'x':coinbasepro6_data['E'], 'y':parseFloat(coinbasepro6_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbasepro6_data_dict.x>coinbasepro6_x2) coinbasepro6_x2 = coinbasepro6_data_dict.x;
    //             if (coinbasepro6_data_dict.x<coinbasepro6_x1) coinbasepro6_x1 = coinbasepro6_data_dict.x;
    //             if (coinbasepro6_data_dict.y>coinbasepro6_y2) coinbasepro6_y2 = coinbasepro6_data_dict.y;
    //             if (coinbasepro6_data_dict.y<coinbasepro6_y1) coinbasepro6_y1 = coinbasepro6_data_dict.y;
    //             // if (coinbasepro6_x2-coinbasepro6_x1>60000) coinbasepro6_x1 = coinbasepro6_x2-60000
    //             if (coinbasepro6_x2-coinbasepro6_x1>86400000) coinbasepro6_x1 = coinbasepro6_x2-86400000;
                
    //             //store the last price received.
    //             coinbasepro6_current_price=coinbasepro6_data_dict.y;

    //             coinbasepro6_alldata.push(coinbasepro6_data_dict);
    //             coinbasepro6_alldata=[...coinbasepro6_alldata.filter(data => data.x > coinbasepro6_x1)]
    //             coinbasepro6_every_other_tracker+=1;
    //         }else{
    //             coinbasepro6_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbasepro6_data = JSON.parse(event.data);
    //         let coinbasepro6_data_dict = {'x':coinbasepro6_data['E'], 'y':parseFloat(coinbasepro6_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbasepro6_data_dict.x>coinbasepro6_x2) coinbasepro6_x2 = coinbasepro6_data_dict.x;
    //         if (coinbasepro6_data_dict.x<coinbasepro6_x1) coinbasepro6_x1 = coinbasepro6_data_dict.x;
    //         if (coinbasepro6_data_dict.y>coinbasepro6_y2) coinbasepro6_y2 = coinbasepro6_data_dict.y;
    //         if (coinbasepro6_data_dict.y<coinbasepro6_y1) coinbasepro6_y1 = coinbasepro6_data_dict.y;
    //         // if (coinbasepro6_x2-coinbasepro6_x1>60000) coinbasepro6_x1 = coinbasepro6_x2-60000
    //         if (coinbasepro6_x2-coinbasepro6_x1>86400000) coinbasepro6_x1 = coinbasepro6_x2-86400000;
    //         //store the last price received.
    //         coinbasepro6_current_price=coinbasepro6_data_dict.x;
    //         coinbasepro6_alldata.push(coinbasepro6_data_dict);
    //         coinbasepro6_alldata=[...coinbasepro6_alldata.filter(data => data.x > coinbasepro6_x1)]
    //         // console.log(coinbasepro6_alldata[coinbasepro6_alldata.length-1]);
    //     }
        
    // }

    // let coinbase1_socket = new WebSocket('ws://cuppong.hessdevelopments.com:11328/subscribe');
    // let coinbase1_x1 = +Infinity;
    // let coinbase1_x2 = -Infinity;
    // let coinbase1_y1 = +Infinity;
    // let coinbase1_y2 = -Infinity;
    // let coinbase1_alldata = [];
    // let coinbase1_current_price;

    // var coinbase1_every_other_toggle = true;
    // var coinbase1_every_other_tracker = 0;
    // var coinbase1_get_nth_msg_to_get = 100;
    // coinbase1_socket.onmessage = function (event) {
    //     if(coinbase1_every_other_toggle){
    //         if(coinbase1_every_other_tracker%coinbase1_get_nth_msg_to_get==0){
    //             var coinbase1_data = JSON.parse(event.data);
    //             let coinbase1_data_dict = {'x':coinbase1_data['E'], 'y':parseFloat(coinbase1_data['p'])}
    //             // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //             if (coinbase1_data_dict.x>coinbase1_x2) coinbase1_x2 = coinbase1_data_dict.x;
    //             if (coinbase1_data_dict.x<coinbase1_x1) coinbase1_x1 = coinbase1_data_dict.x;
    //             if (coinbase1_data_dict.y>coinbase1_y2) coinbase1_y2 = coinbase1_data_dict.y;
    //             if (coinbase1_data_dict.y<coinbase1_y1) coinbase1_y1 = coinbase1_data_dict.y;
    //             // if (coinbase1_x2-coinbase1_x1>60000) coinbase1_x1 = coinbase1_x2-60000
    //             if (coinbase1_x2-coinbase1_x1>86400000) coinbase1_x1 = coinbase1_x2-86400000;
                
    //             //store the last price received.
    //             coinbase1_current_price=coinbase1_data_dict.y;

    //             coinbase1_alldata.push(coinbase1_data_dict);
    //             coinbase1_alldata=[...coinbase1_alldata.filter(data => data.x > coinbase1_x1)]
    //             coinbase1_every_other_tracker+=1;
    //         }else{
    //             coinbase1_every_other_tracker+=1;
    //         }
    //     }else{
    //         var coinbase1_data = JSON.parse(event.data);
    //         let coinbase1_data_dict = {'x':coinbase1_data['E'], 'y':parseFloat(coinbase1_data['p'])}
    //         // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
    //         if (coinbase1_data_dict.x>coinbase1_x2) coinbase1_x2 = coinbase1_data_dict.x;
    //         if (coinbase1_data_dict.x<coinbase1_x1) coinbase1_x1 = coinbase1_data_dict.x;
    //         if (coinbase1_data_dict.y>coinbase1_y2) coinbase1_y2 = coinbase1_data_dict.y;
    //         if (coinbase1_data_dict.y<coinbase1_y1) coinbase1_y1 = coinbase1_data_dict.y;
    //         // if (coinbase1_x2-coinbase1_x1>60000) coinbase1_x1 = coinbase1_x2-60000
    //         if (coinbase1_x2-coinbase1_x1>86400000) coinbase1_x1 = coinbase1_x2-86400000;
    //         //store the last price received.
    //         coinbase1_current_price=coinbase1_data_dict.x;
    //         coinbase1_alldata.push(coinbase1_data_dict);
    //         coinbase1_alldata=[...coinbase1_alldata.filter(data => data.x > coinbase1_x1)]
    //         // console.log(coinbase1_alldata[coinbase1_alldata.length-1]);
    //     }
        
    // } -->
