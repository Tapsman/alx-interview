#!/usr/bin/node

/* Prints all the characters of Star Wars */

const request = require('request');

const movieId = process.argv[2];

const urlfilm = 'https://swapi-api.hbtn.io/api/films/' + movieId;

let persons = [];
const names = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(urlfilm, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      persons = jsonBody.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (persons.length > 0) {
    for (const p of persons) {
      await new Promise(resolve => request(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const n of names) {
    if (n === names[names.length - 1]) {
      process.stdout.write(n);
    } else {
      process.stdout.write(n + '\n');
    }
  }
};

getCharNames;
