#!/usr/bin/node
const req = require('request');

req(process.argv[2], undefined, (err, res) => {
  if (err) {
    console.log(err);
    return;
  }

  const completed = {};
  const todos = JSON.parse(res.body);

  todos.forEach((todo) => {
    if (todo.completed) {
      completed[todo.userId] = completed[todo.userId]
        ? completed[todo.userId] + 1
        : 1;
    }
  });

  console.log(completed);
});
