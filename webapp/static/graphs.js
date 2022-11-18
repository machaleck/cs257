function initializeData() {
    loadStatesSelector();
    loadYearsSelector();
    loadIncidentTypesSelector();
    numDisastersPerYear('numDis');
    typesOfDisasters('typesOfDisasters');
    numProgramsPerYear('numPerYear');
}

function get_url(selectors, selector_keys, url) {
    let a = 0;
    let baseURL = url;
    let variableTracker = 0;
    for (let i = 0; i < selectors.length; i++) {
        let selector = document.getElementById(selectors[i]);
        console.log("get_url")
        if (!selector.value.includes("choose") ) {
            if (variableTracker==0){
                url += "?"
                variableTracker +=1
            }
            
            let selector_value = selector.value;
            console.log(selector_value);
            if (a != 0 && a < selectors.length) {
                url += '&';
            }
            url += selector_keys[i] + '=' + selector_value;
            a += 1
        }
    }
    return url;
}

function getAPIBaseURL() {
    let baseURL = window.location.protocol
        + '//' + window.location.hostname
        + ':' + window.location.port
        + '/api';
    return baseURL;
}

function numDisastersPerYear(chartId) {

    let url = getAPIBaseURL() + '/disasters_year';
    selectors = ['state_selectors','start_year_selector','end_year_selector', 'incident_type'];
    selector_key = ['state', 'start_year', 'end_year', 'incident_type']
    url = get_url(selectors, selector_key, url);
    console.log(url);
    

    fetch(url, { method: 'get' })

        // When the results come back, transform them from a JSON string into
        // a Javascript object (in this case, a list of author dictionaries).
        .then((response) => response.json())
        // Once you have your list of author dictionaries, use it to build
        // an HTML table displaying the author names and lifespan.
        .then(function (yearData) {
            // Add the <option> elements to the <select> element
            years = yearData[0]
            numOccurences = yearData[1]
            barColors = yearData[2]
            console.log(years, numOccurences, barColors)

            disastersPerYear(years, numOccurences, barColors).destroy();
            disastersPerYear(years,numOccurences,barColors)
        })
        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);
        });
}


function disastersPerYear(years, numOccurences, barColors){
    new Chart("numDis", {
        type: "bar",
        data: {
            labels: years,
            datasets: [{
                backgroundColor: barColors,
                data: numOccurences
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: "Disasters Per Year"
            },
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display:true, 
                        labelString: 'Years'
                    }
                }],
                yAxes: [{
                    scaleLabel: {
                        display:true, 
                        labelString: '# Disasters'
                    }
                }]
            }
        }
    });
}

function typesOfDisasters(chartId) {
    var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
    var yValues = [55, 49, 44, 24, 15];
    var barColors = [
        "#b91d47",
        "#00aba9",
        "#2b5797",
        "#e8c3b9",
        "#1e7145"
    ];

    new Chart(chartId, {
        type: "pie",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: yValues
            }]
        },
        options: {
            title: {
                display: true,
                text: "World Wide Wine Production 2018"
            }
        }
    });
}

function numProgramsPerYear(chartId) {
    var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
    var yValues = [55, 49, 44, 24, 15];
    var barColors = ["red", "green", "blue", "orange", "brown"];

    new Chart(chartId, {
        type: "bar",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: yValues
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: "World Wine Production 2018"
            }
        }
    });
}