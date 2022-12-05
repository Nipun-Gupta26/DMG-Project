const apiUri = 'http://localhost:5000/';

function getTags() {
    const response = fetch(`${apiUri}colName`);
    return response;
}

export default {
    getTags
}