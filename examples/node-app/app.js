function add(a, b) {
  return a + b;
}

function main() {
  console.log(`Sum of 2 and 3 is ${add(2, 3)}`);
}

module.exports = { add, main };

if (require.main === module) {
  main();
}
