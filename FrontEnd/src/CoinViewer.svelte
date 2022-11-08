<script>
    import LineChart from "./Components/LineChart.svelte";
    // import Select from "./Components/Select.svelte";

    // Note: If doing the below to switch the websocket connection on the fly, must reassign the .onmessage callback function.
    // let coin = 'btc';
    // let coin_socket = new WebSocket(`wss://stream.binance.com:9443/ws/${coin}usdt@trade`);

    let master_every_other_toggle = true;

    let coins = ['BTC', 'ETH', 'BNB', 'DOGE']
    let coin_socket = new WebSocket(`wss://stream.binance.com:9443/ws/${coins[0].toLocaleLowerCase()}usdt@trade`);
    let coin_socket2 = new WebSocket(`wss://stream.binance.com:9443/ws/${coins[1].toLocaleLowerCase()}usdt@trade`);
    let coin_socket3 = new WebSocket(`wss://stream.binance.com:9443/ws/${coins[2].toLocaleLowerCase()}usdt@trade`);
    let coin_socket4 = new WebSocket(`wss://stream.binance.com:9443/ws/${coins[3].toLocaleLowerCase()}usdt@trade`);

    let coin_x1 = +Infinity;
    let coin_x2 = -Infinity;
    let coin_y1 = +Infinity;
    let coin_y2 = -Infinity;
    let coin_alldata = [];
    let coin_current_price;
    var coin_every_other_toggle = master_every_other_toggle;
    var coin_every_other_tracker = 0;
    var coin_get_nth_msg_to_get = 100;
    coin_socket.onmessage = function (event) {
        if(coin_every_other_toggle){
            if(coin_every_other_tracker%coin_get_nth_msg_to_get==0){
                var coin_data = JSON.parse(event.data);
                let coin_data_dict = {'x':coin_data['E'], 'y':parseFloat(coin_data['p'])}
                // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
                if (coin_data_dict.x>coin_x2) coin_x2 = coin_data_dict.x;
                if (coin_data_dict.x<coin_x1) coin_x1 = coin_data_dict.x;
                if (coin_data_dict.y>coin_y2) coin_y2 = coin_data_dict.y;
                if (coin_data_dict.y<coin_y1) coin_y1 = coin_data_dict.y;
                // if (coin_x2-coin_x1>60000) coin_x1 = coin_x2-60000
                if (coin_x2-coin_x1>86400000) coin_x1 = coin_x2-86400000;
                //store the last price received.
                coin_current_price=coin_data_dict.y;
                coin_alldata.push(coin_data_dict);
                coin_alldata=[...coin_alldata.filter(data => data.x > coin_x1)]
                coin_every_other_tracker+=1;
            }else{
                coin_every_other_tracker+=1;
            }
        }else{
            var coin_data = JSON.parse(event.data);
            let coin_data_dict = {'x':coin_data['E'], 'y':parseFloat(coin_data['p'])}
            // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
            if (coin_data_dict.x>coin_x2) coin_x2 = coin_data_dict.x;
            if (coin_data_dict.x<coin_x1) coin_x1 = coin_data_dict.x;
            if (coin_data_dict.y>coin_y2) coin_y2 = coin_data_dict.y;
            if (coin_data_dict.y<coin_y1) coin_y1 = coin_data_dict.y;
            // if (coin_x2-coin_x1>60000) coin_x1 = coin_x2-60000
            if (coin_x2-coin_x1>86400000) coin_x1 = coin_x2-86400000;
            //store the last price received.
            coin_current_price=coin_data_dict.y;
            coin_alldata.push(coin_data_dict);
            coin_alldata=[...coin_alldata.filter(data => data.x > coin_x1)]
            // console.log(coin_alldata[coin_alldata.length-1]);
        }
    }

    let coin2_x1 = +Infinity;
    let coin2_x2 = -Infinity;
    let coin2_y1 = +Infinity;
    let coin2_y2 = -Infinity;
    let coin2_alldata = [];
    let coin2_current_price;

    var coin2_every_other_toggle = master_every_other_toggle;
    var coin2_every_other_tracker = 0;
    var coin2_get_nth_msg_to_get = 100;
    coin_socket2.onmessage = function (event) {
        if(coin2_every_other_toggle){
            if(coin2_every_other_tracker%coin2_get_nth_msg_to_get==0){
                var coin2_data = JSON.parse(event.data);
                let coin2_data_dict = {'x':coin2_data['E'], 'y':parseFloat(coin2_data['p'])}
                if (coin2_data_dict.x>coin2_x2) coin2_x2 = coin2_data_dict.x;
                if (coin2_data_dict.x<coin2_x1) coin2_x1 = coin2_data_dict.x;
                if (coin2_data_dict.y>coin2_y2) coin2_y2 = coin2_data_dict.y;
                if (coin2_data_dict.y<coin2_y1) coin2_y1 = coin2_data_dict.y;
                // if (coin2_x2-coin2_x1>60000) coin2_x1 = coin2_x2-60000
                if (coin2_x2-coin2_x1>86400000) coin2_x1 = coin2_x2-86400000;
                //store the last price received.
                coin2_current_price=coin2_data_dict.y;
                coin2_alldata.push(coin2_data_dict);
                coin2_alldata=[...coin2_alldata.filter(data => data.x > coin2_x1)]
                coin2_every_other_tracker+=1;
            }else{
                coin2_every_other_tracker+=1;
            }
        }else{
            var coin2_data = JSON.parse(event.data);
            let coin2_data_dict = {'x':coin2_data['E'], 'y':parseFloat(coin2_data['p'])}
            if (coin2_data_dict.x>coin2_x2) coin2_x2 = coin2_data_dict.x;
            if (coin2_data_dict.x<coin2_x1) coin2_x1 = coin2_data_dict.x;
            if (coin2_data_dict.y>coin2_y2) coin2_y2 = coin2_data_dict.y;
            if (coin2_data_dict.y<coin2_y1) coin2_y1 = coin2_data_dict.y;
            // if (coin2_x2-coin2_x1>60000) coin2_x1 = coin2_x2-60000
            if (coin2_x2-coin2_x1>86400000) coin2_x1 = coin2_x2-86400000;
            //store the last price received.
            coin2_current_price=coin2_data_dict.y;
            coin2_alldata.push(coin2_data_dict);
            coin2_alldata=[...coin2_alldata.filter(data => data.x > coin2_x1)]
        }
    }

    let coin3_x1 = +Infinity;
    let coin3_x2 = -Infinity;
    let coin3_y1 = +Infinity;
    let coin3_y2 = -Infinity;
    let coin3_alldata = [];
    let coin3_current_price;
    var coin3_every_other_toggle = master_every_other_toggle;
    var coin3_every_other_tracker = 0;
    var coin3_get_nth_msg_to_get = 100;
    coin_socket3.onmessage = function (event) {
        if(coin3_every_other_toggle){
            if(coin3_every_other_tracker%coin3_get_nth_msg_to_get==0){
                var coin3_data = JSON.parse(event.data);
                let coin3_data_dict = {'x':coin3_data['E'], 'y':parseFloat(coin3_data['p'])}
                if (coin3_data_dict.x>coin3_x2) coin3_x2 = coin3_data_dict.x;
                if (coin3_data_dict.x<coin3_x1) coin3_x1 = coin3_data_dict.x;
                if (coin3_data_dict.y>coin3_y2) coin3_y2 = coin3_data_dict.y;
                if (coin3_data_dict.y<coin3_y1) coin3_y1 = coin3_data_dict.y;
                // if (coin3_x2-coin3_x1>60000) coin3_x1 = coin3_x2-60000
                if (coin3_x2-coin3_x1>86400000) coin3_x1 = coin3_x2-86400000;
                //store the last price received.
                coin3_current_price=coin3_data_dict.y;
                coin3_alldata.push(coin3_data_dict);
                coin3_alldata=[...coin3_alldata.filter(data => data.x > coin3_x1)]
                coin3_every_other_tracker+=1;
            }else{
                coin3_every_other_tracker+=1;
            }
        }else{
            var coin3_data = JSON.parse(event.data);
            let coin3_data_dict = {'x':coin3_data['E'], 'y':parseFloat(coin3_data['p'])}
            if (coin3_data_dict.x>coin3_x2) coin3_x2 = coin3_data_dict.x;
            if (coin3_data_dict.x<coin3_x1) coin3_x1 = coin3_data_dict.x;
            if (coin3_data_dict.y>coin3_y2) coin3_y2 = coin3_data_dict.y;
            if (coin3_data_dict.y<coin3_y1) coin3_y1 = coin3_data_dict.y;
            // if (coin3_x2-coin3_x1>60000) coin3_x1 = coin3_x2-60000
            if (coin3_x2-coin3_x1>86400000) coin3_x1 = coin3_x2-86400000;
            //store the last price received.
            coin3_current_price=coin3_data_dict.y;
            coin3_alldata.push(coin3_data_dict);
            coin3_alldata=[...coin3_alldata.filter(data => data.x > coin3_x1)]
        }
    }

    let coin4_x1 = +Infinity;
    let coin4_x2 = -Infinity;
    let coin4_y1 = +Infinity;
    let coin4_y2 = -Infinity;
    let coin4_alldata = [];
    let coin4_current_price;
    var coin4_every_other_toggle = master_every_other_toggle;
    var coin4_every_other_tracker = 0;
    var coin4_get_nth_msg_to_get = 100;
    coin_socket4.onmessage = function (event) {
        if(coin4_every_other_toggle){
            if(coin4_every_other_tracker%coin4_get_nth_msg_to_get==0){
                var coin4_data = JSON.parse(event.data);
                let coin4_data_dict = {'x':coin4_data['E'], 'y':parseFloat(coin4_data['p'])}
                if (coin4_data_dict.x>coin4_x2) coin4_x2 = coin4_data_dict.x;
                if (coin4_data_dict.x<coin4_x1) coin4_x1 = coin4_data_dict.x;
                if (coin4_data_dict.y>coin4_y2) coin4_y2 = coin4_data_dict.y;
                if (coin4_data_dict.y<coin4_y1) coin4_y1 = coin4_data_dict.y;
                // if (coin4_x2-coin4_x1>60000) coin4_x1 = coin4_x2-60000
                if (coin4_x2-coin4_x1>86400000) coin4_x1 = coin4_x2-86400000;
                //store the last price received.
                coin4_current_price=coin4_data_dict.y;
                coin4_alldata.push(coin4_data_dict);
                coin4_alldata=[...coin4_alldata.filter(data => data.x > coin4_x1)]
                coin4_every_other_tracker+=1;
            }else{
                coin4_every_other_tracker+=1;
            }
        }else{
            var coin4_data = JSON.parse(event.data);
            let coin4_data_dict = {'x':coin4_data['E'], 'y':parseFloat(coin4_data['p'])}
            // let dataDict = {'x':data['E'], 'y':parseFloat(data['c'])}
            if (coin4_data_dict.x>coin4_x2) coin4_x2 = coin4_data_dict.x;
            if (coin4_data_dict.x<coin4_x1) coin4_x1 = coin4_data_dict.x;
            if (coin4_data_dict.y>coin4_y2) coin4_y2 = coin4_data_dict.y;
            if (coin4_data_dict.y<coin4_y1) coin4_y1 = coin4_data_dict.y;
            // if (coin4_x2-coin4_x1>60000) coin4_x1 = coin4_x2-60000
            if (coin4_x2-coin4_x1>86400000) coin4_x1 = coin4_x2-86400000;
            //store the last price received.
            coin4_current_price=coin4_data_dict.y;
            coin4_alldata.push(coin4_data_dict);
            coin4_alldata=[...coin4_alldata.filter(data => data.x > coin4_x1)]
        }
    }

</script>

    <!-- <Select options={[{"text":"btc"},{"text":"eth"},{"text":"ada"}]}
				display_func={o => o.text}
				bind:value={coin}/> -->

    <!-- Live charts at top of page. -->
    <div class = 'chart-grid oneXfour'>
        <LineChart bind:data={coin_alldata} bind:x1={coin_x1} bind:x2={coin_x2} bind:y1={coin_y1} bind:y2={coin_y2} bind:header={coins[0]} bind:current_price={coin_current_price}/>
        <LineChart bind:data={coin2_alldata} bind:x1={coin2_x1} bind:x2={coin2_x2} bind:y1={coin2_y1} bind:y2={coin2_y2} bind:header={coins[1]} bind:current_price={coin2_current_price}/>
        <LineChart bind:data={coin3_alldata} bind:x1={coin3_x1} bind:x2={coin3_x2} bind:y1={coin3_y1} bind:y2={coin3_y2} bind:header={coins[2]} bind:current_price={coin3_current_price}/>
        <LineChart bind:data={coin4_alldata} bind:x1={coin4_x1} bind:x2={coin4_x2} bind:y1={coin4_y1} bind:y2={coin4_y2} bind:header={coins[3]} bind:current_price={coin4_current_price}/>
    </div>


<style>
    .chart-grid.oneXfour { 
        display: grid;
        grid-template-rows: repeat(1, 1fr);  
        grid-template-columns: repeat(4, 1fr); 
        grid-column-gap: 5em;
        grid-row-gap: 75px; 
        padding-left: 4vw;
    }
    /* .chartDiv{
        display:block;
        width: 22.5vw;
        height: 33vh;
        padding-left: 5vw;
    } */
</style>