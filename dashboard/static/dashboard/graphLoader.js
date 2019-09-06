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
r = [];
i = 0;
console.log("Graph Script has been loaded");
// updateChart();

function getRows() {
    var gog = (Math.random() * 100) + 1;
    // var avenge = (Math.random() * 100) + 1;
    // var trf = (Math.random() * 100) + 1;

    r[i] = [(i + 1), gog]; // avenge, trf];
    i = i + 1;

    return r;
}

google.charts.load('current', {
    'packages': ['line']
});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

    const drawMaterial = 'tempGraph';

    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Timestamp');
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

    rows = getRows();

    data.addRows(rows);

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

    setTimeout(drawChart, 10000);

}

function mainFun(plantID){
    console.log('Plant that you\'ve requested is '+plantID);
}

function mainFun2(){
    console.log('Howdy!');
}
