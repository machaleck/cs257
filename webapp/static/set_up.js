/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 */

window.onload = initialize;

function initialize() {
    loadAuthorsSelector();

    let element = document.getElementById('state_selector');
    // if (element) {
    //     element.onchange = onAuthorsSelectionChanged;
    // }
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

function loadAuthorsSelector() {
    let url = getAPIBaseURL() + '/states/';

    // Send the request to the books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(states) {
        // Add the <option> elements to the <select> element
        let selectorBody = '<option selected>choose a state...</option>\n';
        id = 1
        for (let k = 0; k < states.length; k++) {
            let state = states[k];
            selectorBody += '<option value="' + id + '">'
                                + state['name']
                                + '</option>\n';
            id +=1
        }

        let selector = document.getElementById('state_selector');
        if (selector) {
            selector.innerHTML = selectorBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

// function onAuthorsSelectionChanged() {
//     let element = document.getElementById('state_selector');
//     if (!element) {
//         return;
//     }
//     let authorID = element.value; 

//     let url = getAPIBaseURL() + '/books/author/' + authorID;

//     fetch(url, {method: 'get'})

//     .then((response) => response.json())

//     .then(function(books) {
//         let tableBody = '';
//         for (let k = 0; k < books.length; k++) {
//             let book = books[k];
//             tableBody += '<tr>'
//                             + '<td>' + book['title'] + '</td>'
//                             + '<td>' + book['publication_year'] + '</td>'
//                             + '</tr>\n';
//         }

//         // Put the table body we just built inside the table that's already on the page.
//         let booksTable = document.getElementById('books_table');
//         if (booksTable) {
//             booksTable.innerHTML = tableBody;
//         }
//     })

//     .catch(function(error) {
//         console.log(error);
//     });
// }
