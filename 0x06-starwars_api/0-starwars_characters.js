#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};
let people = [];
const names = [];

const requestCharacters = async () => {
  try {
    const response = await new Promise((resolve, reject) => {
      request(filmUrl, (err, response, body) => {
        if (err || response.statusCode !== 200) {
          reject(err);
        } else {
          resolve(body);
        }
      });
    });
    const filmData = JSON.parse(response);
    people = filmData.characters;
  } catch (error) {
    console.error('Error fetching characters:', error);
  }
};

const requestNames = async () => {
  if (people.length > 0) {
    try {
      for (const p of people) {
        const response = await new Promise((resolve, reject) => {
          request(p, (err, response, body) => {
            if (err || response.statusCode !== 200) {
              reject(err);
            } else {
              resolve(body);
            }
          });
        });
        const characterData = JSON.parse(response);
        names.push(characterData.name);
      }
    } catch (error) {
      if (error.response && error.response.statusCode === 404) {
        console.error('Error: Movie not found');
      } else {
        console.error('Error fetching data:', error);
      }
    }
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

getCharNames();
