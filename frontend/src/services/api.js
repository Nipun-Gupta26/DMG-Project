const apiUri = 'http://localhost:5000/';

const getTags = async () => {
    const response = await fetch(`${apiUri}colName`);
    return response.json();
}