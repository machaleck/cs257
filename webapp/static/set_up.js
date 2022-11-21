/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 */

window.onload = initialize;

function initialize() {
    //Loads dropdowns
    loadStatesSelector();
    loadYearsSelector();
    loadIncidentTypesSelector();

    //Hides tables
    x = document.getElementById("hidden")
    x.style.display = "none"
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
//Function that hides the home page and replaces it with the table of data. 
function hide() {  
    var hide = document.getElementsByClassName("hide_me")
    var show = document.getElementById("hidden")
    for (let i = 0; i < hide.length; i++){
        console.log(hide[i])
        hide[i].style.display = "none"
    }
    show.style.display= "block"
}
//fetches data from the server and loads it into our datatable. 
function loadTableData() {
    let url = getAPIBaseURL() + '/natural_disasters?';
    selectors = { 'state' : 'state_selectors', 
    'start_year' : 'start_year_selector',
    'end_year' : 'end_year_selector',
    'incident_type' : 'incident_type'
    };
    let a = 0;
    for (let key in selectors){
        let selector = document.getElementById(selectors[key]);
        if (!selector.value.includes("choose")) {
            let selector_value = selector.value;
            console.log(selector_value);
            if (a!=0 && a<Object.keys(selectors).length){
                url += '&'
            }
            url += key + '=' + selector_value;
            a+=1
        }
    }
    // Send the request to our URL.
    fetch(url, { method: 'get' })

        // When the results come back, transform them from a JSON string into
        // a Javascript object (in this case, a list of author dictionaries).
        .then((response) => response.json())
        // Once you have your list of author dictionaries, use it to build
        // an HTML table displaying the author names and lifespan.
        .then(function(disasters) {
            // Add the <option> elements to the <select> element
            let selectorBody = [];
            id = 1
            for (let k = 0; k < disasters.length; k++) {
                let disaster = disasters[k];
                selectorBody.push([disaster['state'], disaster['declaration_title'],disaster['incident_type'],disaster['programs'],disaster['year']])
            }
            // let selector = document.getElementById('example');
            // console.log("yo I'm running")
            // if (selector) {
            //     selector.innerHTML = selectorBody;
            // }
            var table = $('#example').DataTable();
            table.clear();
            table.rows.add(selectorBody).draw(); 
        })
        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);    
        });
}
//loads the state dropdown
function loadStatesSelector() {
    let url = getAPIBaseURL() + '/states/';

    // Send the request to the books API /authors/ endpoint
    fetch(url, { method: 'get' })

        // When the results come back, transform them from a JSON string into
        // a Javascript object (in this case, a list of author dictionaries).
        .then((response) => response.json())

        // Once you have your list of author dictionaries, use it to build
        // an HTML table displaying the author names and lifespan.
        .then(function (states) {
            // Add the <option> elements to the <select> element
            let selectorBody = '<option selected>choose a state...</option>\n';
            id = 1
            for (let k = 0; k < states.length; k++) {
                let state = states[k];
                selectorBody += '<option value="' + state['name'] + '">'
                    + state['name']
                    + '</option>\n';
                id += 1
            }

            let selector = document.getElementById('state_selectors');
            if (selector) {
                selector.innerHTML = selectorBody;
            }
        })

        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);
        });
}
//loads the year dropdown
function loadYearsSelector() {
    let url = getAPIBaseURL() + '/years/';

    // Send the request to the books API /authors/ endpoint
    fetch(url, { method: 'get' })

        // When the results come back, transform them from a JSON string into
        // a Javascript object (in this case, a list of author dictionaries).
        .then((response) => response.json())

        // Once you have your list of author dictionaries, use it to build
        // an HTML table displaying the author names and lifespan.
        .then(function (years) {
            // Add the <option> elements to the <select> element
            let selectorBody = '<option selected>choose a year...</option>\n';
            for (let k = 0; k < years.length; k++) {
                let year = years[k];
                selectorBody += '<option value="' + year['year'] + '">'
                    + year['year']
                    + '</option>\n';
            }

            let selectors = document.getElementsByClassName('year_selector');
            selector = selectors[0]
            selector2 = selectors[1]
            if (selector) {
                selector.innerHTML = selectorBody;
            }
            if (selector2) {
                selector2.innerHTML = selectorBody;
            }
        }
        )

        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);
        });
}
//loads the incident type dropdown
function loadIncidentTypesSelector() {
    let url = getAPIBaseURL() + '/incidents/';

    // Send the request to the books API /authors/ endpoint
    fetch(url, { method: 'get' })

        // When the results come back, transform them from a JSON string into
        // a Javascript object (in this case, a list of author dictionaries).
        .then((response) => response.json())

        // Once you have your list of author dictionaries, use it to build
        // an HTML table displaying the author names and lifespan.
        .then(function (incidents) {
            console.log(incidents);
            // Add the <option> elements to the <select> element
            let selectorBody = '<option selected>choose an incident...</option>\n';

            for (let k = 0; k < incidents.length; k++) {
                let incident_type = incidents[k];
                console.log(incident_type)
                selectorBody += '<option value="' + incident_type["incident_type"] + '">'
                    + incident_type["incident_type"]
                    + '</option>\n';

            }

            let selector = document.getElementById('incident_type');
            if (selector) {
                selector.innerHTML = selectorBody;
            }
        })

        // Log the error if anything went wrong during the fetch.
        .catch(function (error) {
            console.log(error);
        });
}