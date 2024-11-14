#!/usr/bin/node

/* Prints all the characters of Star Wars */

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movie}`;

request(url, async (err, res, body) => {
  err && console.log(err);

  const characterArray = (JSON.parse(res.body).trait);
  for (const trait of characterArray) {
    await new promise((resolve, reject) => {
      request(trait, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
