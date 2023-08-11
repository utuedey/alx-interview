#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${baseUrl}/films/${process.argv[2]}/`, (error, _, body) => {
    if (error) {
      console.log(error);
    }
    const charactersUrl = JSON.parse(body).characters;
    const charactersName = charactersUrl.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseError, _, RequestBody) => {
        if (promiseError) {
	  reject(promiseError);
	}
	  resolve(JSON.parse(RequestBody).name);
	});
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join("\n")))
      .catch(errors => console.log(errors));
    });
}
