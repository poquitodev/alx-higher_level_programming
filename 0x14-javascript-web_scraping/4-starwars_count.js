#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let times = 0;

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let k = 0; k < body.length; ++k) {
    const characters = body[k].characters;

    for (let i = 0; i < characters.length; ++i) {
      const character = characters[i];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }

  console.log(times);
});
