function deleteTicket(ticketId){
    fetch('/delete-ticket', {
        method: 'POST',
        body: JSON.stringify({ ticketId: ticketId })
    }).then((_res) => {
        window.location.href = "/";
    });
}

function deleteUser(userId){
    fetch('/delete-user', {
        method: 'POST',
        body: JSON.stringify({ userId: userId })
    }).then((_res) => {
        window.location.href = "/users";
    });
}

function createAdmin(userId){
    fetch('/create-admin', {
        method: 'POST',
        body: JSON.stringify({ userId: userId })
    }).then((_res) => {
        window.location.href = "/users";
    });
}   
