const { test } = require("node:test");
const assert = require("node:assert");
const { add } = require("../app");

test("add positive", () => {
  assert.strictEqual(add(2, 3), 5);
});

test("add zero", () => {
  assert.strictEqual(add(0, 0), 0);
});

test("add negative", () => {
  assert.strictEqual(add(-1, 1), 0);
});
