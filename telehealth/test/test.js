const assert = require('assert');
const http = require('http');
const createServer = require('../server');

const server = createServer();
server.listen(0, () => {
  const { port } = server.address();
  http.get({ port, path: '/' }, res => {
    try {
      assert.strictEqual(res.statusCode, 200);
      console.log('Test passed');
      server.close();
    } catch (err) {
      console.error('Test failed');
      server.close();
      process.exitCode = 1;
    }
  }).on('error', err => {
    console.error('Request error', err);
    server.close();
    process.exitCode = 1;
  });
});
