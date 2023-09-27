#!/usr/bin/node
/*
 * Write a script that computes the number of tasks completed by user id.
 */

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const listUsers = JSON.parse(body);
  const listId = [];
  for (let i = 0; i < listUsers.length; i++) {
    listId.push(listUsers[i].userId);
  }
  const setId = [...new Set(listId)];
  const dictUsers = {};
  for (let i = 0; i < setId.length; i++) {
    dictUsers[setId[i]] = 0;
    for (let j = 0; j < listUsers.length; j++) {
      if (listUsers[j].userId === setId[i]) {
        dictUsers[setId[i]] += 1;
      }
    }
  }
  console.log(dictUsers);
});
