let disasterChart;
let programChart;
let pieChart; 

function initializeData() {
    loadStatesSelector();
    loadYearsSelector();
    loadIncidentTypesSelector();
    numDisastersPerYear();
    pieChartDisaster();
    numProgramsPerYear();
}
function get_url(selectors, selector_keys, url) {
    let a = 0;
    let variableTracker = 0;
    for (let i = 0; i < selectors.length; i++) {
        let selector = document.getElementById(selectors[i]);
        console.log("get_url")
        if (!selector.value.includes("choose") || !selector.value == null) {
            if (variableTracker == 0) {
                url += "?"
                variableTracker += 1
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
function numDisastersPerYear() {

    let url = getAPIBaseURL() + '/disasters_year';
    let selectors = ['state_selectors', 'start_year_selector', 'end_year_selector', 'incident_type'];
    let selector_key = ['state', 'start_year', 'end_year', 'incident_type']
    url = get_url(selectors, selector_key, url);

    if (url == "http://127.0.0.1:5000/api/disasters_year?state=&start_year=&end_year=&incident_type=") {
        url = "http://127.0.0.1:5000/api/disasters_year"
    }

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

            disastersPerYear(years, numOccurences, barColors);

        })
        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);
        });
}
function numProgramsPerYear() {

    let url = getAPIBaseURL() + '/programs_year';
    let selectors = ['state_selectors', 'start_year_selector', 'end_year_selector', 'incident_type'];
    let selector_key = ['state', 'start_year', 'end_year', 'incident_type']
    url = get_url(selectors, selector_key, url);

    if (url == "http://127.0.0.1:5000/api/programs_year?state=&start_year=&end_year=&incident_type=") {
        url = "http://127.0.0.1:5000/api/programs_year"
    }

    fetch(url, { method: 'get' })

        // When the results come back, transform them from a JSON string into
        // a Javascript object (in this case, a list of author dictionaries).
        .then((response) => response.json())
        // Once you have your list of author dictionaries, use it to build
        // an HTML table displaying the author names and lifespan.
        .then(function (yearData) {
            // Add the <option> elements to the <select> element
            years = yearData[0]
            numPrograms = yearData[1]
            barColors = yearData[2]

            programsChart(years, numPrograms, barColors);

        })
        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);
        });
}
function disastersPerYear(years, numOccurences, barColors) {
    if (disasterChart) {
        disasterChart.destroy();
    }
    disasterChart = new Chart("numDis", {
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
                display: true
            },
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Years'
                    }
                }],
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: '# Disasters'
                    }
                }]
            }
        }
    });
}

function pieChartDisaster() {

    let url = getAPIBaseURL() + '/pie_chart';
    let selectors = ['state_selectors', 'start_year_selector', 'end_year_selector', 'incident_type'];
    let selector_key = ['state', 'start_year', 'end_year', 'incident_type']
    url = get_url(selectors, selector_key, url);

    if (url == "http://127.0.0.1:5000/api/pie_chart?state=&start_year=&end_year=&incident_type=") {
        url = "http://127.0.0.1:5000/api/pie_chart"
    }

    fetch(url, { method: 'get' })

        // When the results come back, transform them from a JSON string into
        // a Javascript object (in this case, a list of author dictionaries).
        .then((response) => response.json())
        // Once you have your list of author dictionaries, use it to build
        // an HTML table displaying the author names and lifespan.
        .then(function (incident_data) {
            // Add the <option> elements to the <select> element
            incidents = incident_data[0];
            numOccurences = incident_data[1];
            colors = incident_data[2];

            pie_chart_helper(incidents, numOccurences, colors);

        })
        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);
        });
    }
function pie_chart_helper(incident_types, numOccurences, colors) {
    if (pieChart){
        pieChart.destroy();
    }
    pieChart = new Chart("typesOfDisasters", {
        type: "pie",
        data: {
            labels: incident_types,
            datasets: [{
                backgroundColor: colors,
                data: numOccurences
            }]
        },
        options: {
            title: {
                display: true,
            }
        }
    });
}


function programsChart(years, numPrograms, barColors) {

    if (programChart) {
        programChart.destroy();
    }

    programChart = new Chart("numPerYear", {
        type: "bar",
        data: {
            labels: years,
            datasets: [{
                backgroundColor: barColors,
                data: numPrograms
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true
            }
        }
    });
}