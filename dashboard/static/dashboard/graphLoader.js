// Get the Sidebar
var mySidebar = document.getElementById("mySidebar");
const moistureValueDisp = document.getElementById('sMoistureValue');

// var i = 0;

// Get the DIV with overlay effect
var overlayBg = document.getElementById("myOverlay");

// Toggle between showing and hiding the sidebar, and add overlay effect
function w3_open() {
    if (mySidebar.style.display === 'block') {
        mySidebar.style.display = 'none';
        overlayBg.style.display = "none";
    } else {
        mySidebar.style.display = 'block';
        overlayBg.style.display = "block";
    }
}

// Close the sidebar with the close button
function w3_close() {
    mySidebar.style.display = "none";
    overlayBg.style.display = "none";
}


/// Our stuff starts here

function getSoilNow() {
    var moisture = Math.floor((Math.random() * 100) + 1);
    moistureValueDisp.innerHTML = moisture + "%";
}

function startTime() {
    // document.getElementById('ftr').innerHTML = "Hello "+i;
    // i = i + 1;
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
        h + ":" + m + ":" + s;
    // getSoilNow();
    var t = setTimeout(startTime, 500);
}

function checkTime(i) {
    if (i < 10) {
        i = "0" + i
    }; // add zero in front of numbers < 10
    return i;
}


// console.log("Script is loaded successfully");
// var r = [];
// var i = 0;
// var plantStats = [];

console.log("Graph Script has been loaded");
// updateChart();

google.charts.load('current', {
    'packages': ['line']
});
google.charts.setOnLoadCallback(mainFun);

function sleep(miliseconds) {
   var currentTime = new Date().getTime();

   while (currentTime + miliseconds >= new Date().getTime()) {
   }
}

function getRows() {
    var gog = (Math.random() * 100) + 1;
    // var avenge = (Math.random() * 100) + 1;
    // var trf = (Math.random() * 100) + 1;

    r[i] = [(i + 1), gog]; // avenge, trf];
    i = i + 1;

    return r;
}

function drawTempChart(rows) {

    const drawMaterial = 'tempGraph';

    var data = new google.visualization.DataTable();
    data.addColumn('date', 'Timestamp');
    data.addColumn('number', 'Temperature');
    data.addRows(rows);
    // data.addColumn('number', 'The Avengers');
    // data.addColumn('number', 'Transformers: Age of Extinction');

    // data.addRows([
    //     [1, 37.8, 80.8, 41.8],
    //     [2, 30.9, 69.5, 32.4],
    //     [3, 25.4, 57, 25.7],
    //     [4, 11.7, 18.8, 10.5],
    //     [5, 11.9, 17.6, 10.4],
    //     [6, 8.8, 13.6, 7.7],
    //     [7, 7.6, 12.3, 9.6],
    //     [8, 12.3, 29.2, 10.6],
    //     [9, 16.9, 42.9, 14.8],
    //     [10, 12.8, 30.9, 11.6],
    //     [11, 5.3, 7.9, 4.7],
    //     [12, 6.6, 8.4, 5.2],
    //     [13, 4.8, 6.3, 3.6],
    //     [14, 4.2, 6.2, 3.4]
    // ]);

    // rows = getRows();

    // data.addRows(rows);
    // var dt = new Date();
    // data.addRows([
    //     [new Date(2018, 11, 24, 10, 33, 30, 0), 44],
    //     [dt, 12]
    // ]);


    // rows = getRows();
    // var data = new google.visualization.DataTable({
    //     cols: [{
    //             id: 'timeStmp',
    //             label: 'Time Stamp',
    //             type: 'string'
    //         },
    //         {
    //             id: 'temperature',
    //             label: 'Temperature',
    //             type: 'number'
    //         }
    //     ],
    //     rows: rows
    // }, 0.6);

    var options = {
        chart: {
            title: 'Temperature Recorded in your plant',
            subtitle: 'in Celsius'
        },
        width: 900,
        height: 500
    };

    var chart = new google.charts.Line(document.getElementById(drawMaterial));

    chart.draw(data, google.charts.Line.convertOptions(options));

    // mainFun();
    // mainFun2();

    // drawHumChart();
    //
    // setTimeout(drawTempChart, 10000);

}

function drawHumChart(rows) {

    const drawMaterial = 'humGraph';

    var data = new google.visualization.DataTable();
    data.addColumn('date', 'Timestamp');
    data.addColumn('number', 'Temperature');
    // data.addColumn('number', 'The Avengers');
    // data.addColumn('number', 'Transformers: Age of Extinction');

    // data.addRows([
    //     [1, 37.8, 80.8, 41.8],
    //     [2, 30.9, 69.5, 32.4],
    //     [3, 25.4, 57, 25.7],
    //     [4, 11.7, 18.8, 10.5],
    //     [5, 11.9, 17.6, 10.4],
    //     [6, 8.8, 13.6, 7.7],
    //     [7, 7.6, 12.3, 9.6],
    //     [8, 12.3, 29.2, 10.6],
    //     [9, 16.9, 42.9, 14.8],
    //     [10, 12.8, 30.9, 11.6],
    //     [11, 5.3, 7.9, 4.7],
    //     [12, 6.6, 8.4, 5.2],
    //     [13, 4.8, 6.3, 3.6],
    //     [14, 4.2, 6.2, 3.4]
    // ]);

    // rows = getRows();

    data.addRows(rows);

    var options = {
        chart: {
            title: 'Humidity Recorded in your plant',
            subtitle: 'In %'
        },
        width: 900,
        height: 500
    };

    var chart = new google.charts.Line(document.getElementById(drawMaterial));

    chart.draw(data, google.charts.Line.convertOptions(options));

    // mainFun();
    // mainFun2();

    // setTimeout(drawTempChart, 10000);

}

// function updatePlantStats(ctxt) {
//     // plantStats = ctxt;
//     // console.log(plantStats);
//     plantStats = JSON.parse(ctxt);
//     // console.log(plantStats);
//     // console.log(plantStats.length);
// }

function makeDataForTempGraph(plantStats) {
    // console.log('In Make Data');
    var tmpData = new Array();
    var n = plantStats.length;
    var ts, tmp, i = 0;
    var j = 0;

    // console.log('done with initials, n = '+n);

    // while(i < plantStats.length){
    //     console.log(i);
    //     i = i + 1;
    // }

    i = 0;

    while (i < plantStats.length) {
        // console.log('In loop');
        // console.log(i);
        ts = plantStats[i]["timestamp"];
        tmp = plantStats[i]["temperature"];

        // console.log(ts);
        // console.log(tmp);
        tmpData[j] = [new Date(ts), tmp];
        j = j + 1;
        // console.log(tmpData[tmpData.length - 1]);
        i = i + 1;

    }

    // console.log('Final: '+tmpData);

    drawTempChart(tmpData);

    // return tmpData;
}

function makeDataForHumGraph(plantStats) {
    // console.log('In Make Data');
    var tmpData = new Array();
    var n = plantStats.length;
    var ts, tmp, i = 0;
    var j = 0;

    // console.log('done with initials, n = '+n);

    // while(i < plantStats.length){
    //     console.log(i);
    //     i = i + 1;
    // }

    i = 0;

    while (i < plantStats.length) {
        // console.log('In loop');
        // console.log(i);
        ts = plantStats[i]["timestamp"];
        hum = plantStats[i]["humidity"];

        // console.log(ts);
        // console.log(tmp);
        tmpData[j] = [new Date(ts), hum];
        j = j + 1;
        // console.log(tmpData[tmpData.length - 1]);
        i = i + 1;

    }

    // console.log('Final: '+tmpData);

    drawHumChart(tmpData);

    // return tmpData;
}

function drawGraphs() {
    //Type -> Temperature, Hunidity, All

    let url = '/conditions/plant';
    var request = new XMLHttpRequest();

    var data


    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // var jsonObj = JSON.parse(request.responseText);
            var jsonObj = JSON.parse(request.responseText);

            data = jsonObj;

            makeDataForTempGraph(data);
            makeDataForHumGraph(data);
            // updatePlantStats(jsonObj);
            // console.log(jsonObj);

            // console.log('In inner function: '+data);
        }
    };

    request.open("GET", url, true);
    request.send();

    // console.log('In Outer function: '+data);

    // return request.data;
}

function updateBlocks() {

    const tVal = document.getElementById('temperatureVal');
    const hVal = document.getElementById('humidityVal');
    const disVal = document.getElementById('diseaseVal');
    const sVal = document.getElementById('sMoistureValue');
    // console.log('sVal');

    let url = '/conditions/infocus/1';
    var request = new XMLHttpRequest();

    var data


    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // var jsonObj = JSON.parse(request.responseText);
            var jsonObj = JSON.parse(request.responseText);

            tVal.innerHTML = jsonObj["temperature"] + "°C";
            hVal.innerHTML = jsonObj["humidity"] + "%";
            sVal.innerHTML = jsonObj["soilMoisture"] + "%";

            if (!(jsonObj["diseased"])) {
                disVal.innerHTML = "No";
            } else {
                disVal.innerHTML = "Yes";
            }


            // data = jsonObj;

            // makeDataForTempGraph(data);
            // makeDataForHumGraph(data);
            // updatePlantStats(jsonObj);
            // console.log(jsonObj);

            // console.log('In inner function: '+data);
        }
    };

    request.open("GET", url, true);
    request.send();

    // console.log('In Outer function: '+data);

    // return request.data;
}

function actuate(component, act) {

    console.log(component + " " + act);
    var dat = {
        "modType": component,
        "value": act
    };
    var dat = JSON.stringify(dat);

    // console.log(dat);

    var url = "/conditions/actuate/1";
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            // console.log("POST successful");
        }
    };

    xhr.send(dat);

}

function runFunc() {
    var d = new Date();
    var m = d.getMinutes();
    // console.log("Howdy!");
    updateBlocks();

    if ((m % 10 == 0)) {
        console.log('Graph drawn at ' + (new Date()));
        drawGraphs();

        sleep(65000)
    }

    setTimeout(runFunc, 300);
}

function mainFun() {
    drawGraphs();
    runFunc();
}
