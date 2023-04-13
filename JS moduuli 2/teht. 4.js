let nums = [];
while (true) {
    num = parseInt(prompt("Enter number: "));
    if (num === 0) break;
    nums.push(num);
}
nums.sort((a, b) => b - a);
console.log(nums);