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
//Gets the desired URL. 
function get_url(selectors, selector_keys, url) {
    let a = 0;
    let variableTracker = 0;
    baseURL = url
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
    if (url == baseURL + "state=&start_year=&end_year=&incident_type=") {
        url = baseURL
    }
    return url;
}
// Returns the base URL of the API, onto which endpoint
// components can be appended.
function getAPIBaseURL() {
    let baseURL = window.location.protocol
        + '//' + window.location.hostname
        + ':' + window.location.port
        + '/api';
    return baseURL;
}
//fetches data from the server and then creates the graph. 
function numDisastersPerYear() {

    let url = getAPIBaseURL() + '/disasters_year';
    let selectors = ['state_selectors', 'start_year_selector', 'end_year_selector', 'incident_type'];
    let selector_key = ['state', 'start_year', 'end_year', 'incident_type']
    url = get_url(selectors, selector_key, url);

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

            disastersPerYearHelper(years, numOccurences, barColors);

        })
        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);
        });
}
//Creates the graph in numDisastersPerYear
function disastersPerYearHelper(years, numOccurences, barColors) {
    
    //Destroys the previous version of the graph it was already created.
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
//fetches data from the server and then creates the graph. 
function numProgramsPerYear() {

    let url = getAPIBaseURL() + '/programs_year';
    let selectors = ['state_selectors', 'start_year_selector', 'end_year_selector', 'incident_type'];
    let selector_key = ['state', 'start_year', 'end_year', 'incident_type']
    url = get_url(selectors, selector_key, url);


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

            programsHelper(years, numPrograms, barColors);

        })
        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);
        });
}
//Creates the graph in numProgramsPerYear
function programsHelper(years, numPrograms, barColors) {

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
//fetches data from the server and then creates the graph. 
function pieChartDisaster() {

    let url = getAPIBaseURL() + '/pie_chart';
    let selectors = ['state_selectors', 'start_year_selector', 'end_year_selector', 'incident_type'];
    let selector_key = ['state', 'start_year', 'end_year', 'incident_type']
    url = get_url(selectors, selector_key, url);

    fetch(url, { method: 'get' })

        // When the results come back, transform them from a JSON string into
        // a Javascript object (in this case, a list of author dictionaries).
        .then((response) => response.json())
        // Once you have your list of author dictionaries, use it to build
        // an HTML table displaying the author names and lifespan.
        .then(function (incident_data) {

            incidents = incident_data[0];
            numOccurences = incident_data[1];
            colors = incident_data[2];

            pieChartHelper(incidents, numOccurences, colors);

        })
        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);
        });
}
//Creates the graph in pieChartDisaster
function pieChartHelper(incident_types, numOccurences, colors) {
    //Destroys the previous version of the graph it was already created.
    if (pieChart) {
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
