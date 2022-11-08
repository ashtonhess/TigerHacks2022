<script>

    import * as Pancake from '@sveltejs/pancake'

    export let header = '';
    export let header2 = '';

    export let x1=+Infinity;
    export let x2=-Infinity;
    export let y1=+Infinity;
    export let y2=-Infinity;

    export let data = [];

    export let current_price = "(No live data.)";

    let closest;

</script>

<div class='chart'>
    <div class='headerdiv'>
        <h3 class='header'>{header} {header2}: {current_price.toLocaleString()} seconds</h3>
        <!-- <h3 class='header'>{header}</h3> -->
        <!-- <h3 class='header2'>${data[data.length-1]}</h3> -->
    </div>
    <Pancake.Chart {x1} {x2} {y1} {y2}>
        <Pancake.Grid horizontal count = {4} let:value>
            <!-- <div class='grid-line horizontal'><span>${value.toLocaleString()}</span></div> -->
            <div class='grid-line horizontal'><span>{value}</span></div>

        </Pancake.Grid>
        <Pancake.Grid vertical count = {4} let:value>
            <span class = 'x-label'>{String(new Date(value).toLocaleTimeString())}</span>
        </Pancake.Grid>
        <Pancake.Svg>
            <Pancake.SvgLine data={data} let:d>
                <path class='data' {d}></path>
            </Pancake.SvgLine>
        </Pancake.Svg>

        {#if closest}
        <Pancake.Point x={closest.x} y={closest.y}>
            <span class="annotation-point"></span>
            <div class="annotation" style="transform: translate(-{100 * ((closest.x - x1) / (x2 - x1))}%,0)">
                <strong class='closestY'>{closest.y.toLocaleString()} seconds</strong>
                <!-- <span>{closest.x}: {closest.y}</span> -->
                <span class='closestDate'>{String(new Date(closest.x).toLocaleTimeString())}</span>
            </div>
        </Pancake.Point>
        {/if}

        <Pancake.Quadtree data={data} bind:closest/>

    </Pancake.Chart>
</div>


<style>
    .header{
        left: 0em;
        /* left: -3em; */
        /* position: relative; */
        /* display: block; */
        font-size:smaller;
        font-weight: bolder;
        /* color:rgb(0, 0, 0) */
        color: black;
    }

    .chart{
        height: 90%;
        width: 90%;
        padding: 0em 2em 2em 2em;
        margin: 0 0 30px 0;
        padding-left: 1em;
        /* padding-right: 4em; */
    }
    .grid-line{
        position: relative;
        display: block;
    }
    .grid-line.horizontal{
        width: calc(100% + 4em);
        /* left: -4em; */
        left: -4em;
        border-bottom: 1px dashed #ccc;
    }
    .grid-line span{
        position: absolute;
        left: 0em;
        bottom: 2px;
        font-family: sans-serif;
        font-size: 14px;
        /* color: rgb(71, 71, 71); */
        color: black;
        font-weight: bolder;
    }
    .x-label{
        position: absolute;
        width: 4em;
        left: -2em;
        bottom: -2.4em;
        font-family: sans-serif;
        font-size: 12px;
        font-weight: bold;
        /* color: rgb(71, 71, 71); */
        color: black;
        text-align: center;
    }
    path.data{
        stroke: rgba(33, 226, 62, 0.8);
        stroke-linejoin: round;
        stroke-linecap: round;
        stroke-width: 2px;
        fill: none;
    }

    .annotation {
		position: absolute;
		white-space: nowrap;
		bottom: 1em;
		line-height: 1.2;
		/* background-color: rgba(255,255,255,0.3); */
        background-color: rgb(255, 255, 255,.3);
		padding: 0.2em 0.4em;
		border-radius: 2px;
	}
	.annotation-point {
		position: absolute;
		width: 5px;
		height: 5px;
		/* background-color: #000000; */
        background-color: black;
		border-radius: 50%;
		transform: translate(-50%,-50%);
	}
	.annotation strong {
		display: block;
		font-size: 14px;
	}
	.annotation span {
		display: block;
		font-size: 10px;
	}
    .closestY{
        color: black;
    }
    .closestDate{
        color: black;
    }
</style>
