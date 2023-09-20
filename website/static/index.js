// This function is called when the user clicks a delete ticket button
function deleteTicket(ticketId){
    // It sends a POST request to the server with the ticketId
    fetch('/delete-ticket', {
        method: 'POST',
        body: JSON.stringify({ ticketId: ticketId })
    }).then((_res) => {
        // it responds with a redirect to the home page
        window.location.href = "/";
    });
}


// This function is called when the user clicks a delete user button
function deleteUser(userId){
    // It sends a POST request to the server with the UserId
    fetch('/delete-user', {
        method: 'POST',
        body: JSON.stringify({ userId: userId })
    }).then((_res) => {
        // it responds with a redirect to the users page
        window.location.href = "/users";
    });
}

// This function is called when the user clicks a create admin button
function createAdmin(userId){
    // It sends a POST request to the server with the UserId
    fetch('/create-admin', {
        method: 'POST',
        body: JSON.stringify({ userId: userId })
    }).then((_res) => {
        // it responds with a redirect to the users page
        window.location.href = "/users";
    });
}   
